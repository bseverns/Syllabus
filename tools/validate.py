#!/usr/bin/env python3
"""Validate course front matter and build catalog."""
import os, sys, json, re
from pathlib import Path

SCHEMA_PATH = Path('catalog/schema.json')
INDEX_PATH = Path('catalog/index.json')
REQUIRED_SECTIONS = [
    "Description",
    "Outcomes",
    "Weekly arc",
    "Major assignments",
    "Assessment",
    "Access/UDL",
    "Policies",
    "Documentation expectations",
]


def load_schema():
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def parse_simple_yaml(text):
    data = {}
    current = None
    for line in text.splitlines():
        if not line.strip():
            continue
        if line.startswith('-') and current:
            data[current].append(line.split('-',1)[1].strip().strip('"'))
            continue
        if ':' in line:
            key, val = line.split(':',1)
            key = key.strip()
            val = val.strip()
            if val.startswith('[') and val.endswith(']'):
                items = [i.strip().strip('"') for i in val[1:-1].split(',') if i.strip()]
                data[key] = items
            elif val == '' or val is None:
                data[key] = []
                current = key
            else:
                data[key] = val.strip('"')
                current = key
    return data


def load_front_matter(path):
    text = Path(path).read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---', text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: missing front matter")
    data = parse_simple_yaml(m.group(1))
    return data, text


def validate(data, schema, path):
    errors = []
    for key in schema.get('required', []):
        if key not in data:
            errors.append(f"{path}: missing {key}")
    props = schema.get('properties', {})
    for key, spec in props.items():
        if key in data:
            typ = spec.get('type')
            if typ == 'array' and not isinstance(data[key], list):
                errors.append(f"{path}: {key} should be list")
            if typ == 'string' and not isinstance(data[key], str):
                errors.append(f"{path}: {key} should be string")
    return errors


def check_syllabus(path):
    warnings = []
    text = Path(path).read_text(encoding='utf-8')
    for h in REQUIRED_SECTIONS:
        if re.search(r'^## +'+re.escape(h)+r'\b', text, re.MULTILINE) is None:
            warnings.append(f"{path}: missing section '{h}'")
    if 'process-log' not in text:
        warnings.append(f"{path}: link to process-log missing")
    if 'assumption-ledger' not in text:
        warnings.append(f"{path}: link to assumption-ledger missing")
    return warnings


def main():
    schema = load_schema()
    records = []
    errors = []
    warnings = []

    for d in sorted(Path('.').iterdir()):
        if d.is_dir() and (d / 'brief.md').exists():
            data, _ = load_front_matter(d / 'brief.md')
            errors.extend(validate(data, schema, str(d / 'brief.md')))
            records.append({k: data[k] for k in ['course_id','title','level','delivery','updated']})
            syl = d / 'syllabus.md'
            if syl.exists():
                warnings.extend(check_syllabus(syl))

    for md in Path('course-briefs').glob('*.md'):
        data, _ = load_front_matter(md)
        errors.extend(validate(data, schema, str(md)))
        records.append({k: data[k] for k in ['course_id','title','level','delivery','updated']})

    records.sort(key=lambda r: r['title'])
    INDEX_PATH.write_text(json.dumps(records, indent=2) + '\n', encoding='utf-8')

    for w in warnings:
        print('WARN:', w, file=sys.stderr)
    if errors:
        for e in errors:
            print('ERROR:', e, file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
