---
course_id: "local-ai-archives-and-small-tools"
title: "Local AI, Archives & Small Tools"
level: "Undergrad"
hours: "3 credits; 14-week semester"
delivery: "Studio-Seminar"
keywords: ["local ai", "archives", "retrieval", "annotation", "small tools", "provenance", "interfaces"]
outcomes:
  - "work with local or constrained AI systems as specific tools rather than universal platforms"
  - "prepare and structure document sets, archives, or corpora for meaningful retrieval and annotation"
  - "design small interfaces or workflows that keep provenance and trust visible"
  - "evaluate ethical boundaries around consent, leakage, labor, and false confidence"
access_notes: "Can run with mixed local and cloud-constrained workflows, but should foreground local-first, small-model, and low-cost toolchains where possible. Supports humanities, art, education, and archive-centered use cases."
artifacts: ["document set audit", "retrieval / annotation workflow", "small tool prototype", "trust and provenance guide", "final demo and postmortem"]
lineage: ["diy-local-ai-workshop", "ai-story-society", "digital-storytelling-data-viz", "critical-making-civic-media"]
version: "v0.1"
updated: "2026-04-09"
suggested_path: "POST_SECONDARY/local-ai-archives-and-small-tools"
---

## Snapshot
**Working title:** Local AI, Archives & Small Tools  
**Intended level:** POST_SECONDARY  
**Estimated hours:** 3 credits / 14-week semester  
**Suggested future path:** `POST_SECONDARY/local-ai-archives-and-small-tools`

**Learning outcomes:**
- Build local or constrained AI workflows that remain legible, bounded, and inspectable.
- Structure document sets and archives for retrieval, summarization, tagging, or guided writing tasks.
- Design small interfaces that expose sources, uncertainty, and provenance.
- Resist platform fantasy by making tools with narrow scope and clear accountability.

**What’s missing:**
- [ ] Full reading list
- [ ] Semester schedule
- [ ] Assignment ladder
- [ ] Session plans
- [ ] Local tooling notes by OS / hardware tier
- [ ] Rubric for provenance, legibility, and bounded tool design

## Why
This course would turn several live threads in the repo into a formal post-secondary studio: local AI, archive use, careful prompting, small tools, and the politics of who gets to automate what. It would be especially useful for artists, educators, librarians, organizers, and small institutions that need help from machines without surrendering judgment to them.

## Core idea
Students do not build “AI products” in the startup sense. They build **small tools**:
- archive search helpers
- annotated retrieval systems
- summarizers for constrained document sets
- tagging or clustering assistants
- writing supports with visible citations
- local-first study or planning aids

The course should make the model feel like one component in a larger workflow, not the whole story.

## Suggested arc
### Phase 1 - What kind of tool is this?
- define narrow use cases
- distinguish model, corpus, interface, and user task
- audit document sets for mess, gaps, and permissions

### Phase 2 - Retrieval, annotation, and trust
- chunking, metadata, citation visibility
- where summaries go wrong
- provenance as interface, not backend trivia

### Phase 3 - Small tool studio
- build a bounded helper
- prototype input/output patterns
- keep sources, uncertainty, and failure modes visible

### Phase 4 - Postmortem and deployment realism
- document hardware / software assumptions
- test with actual users
- write a handoff guide and clear “what this tool is / is not” statement

## Assessment mix
- document set audit
- retrieval / annotation exercise
- small interface prototype
- trust / provenance memo
- final tool demo with documentation bundle

## Materials / access notes
Possible toolchains:
- local LLM runners
- notebook or CLI-based workflows
- lightweight web UIs
- embeddings / retrieval libraries
- markdown corpora
- exported PDFs, notes, transcripts, code docs, or archival materials

Low-resource version:
- use smaller local models
- reduce corpus size
- emphasize workflow and interface logic over benchmark performance

## Artifacts
- corpus audit and permissions notes
- metadata or chunking strategy doc
- prototype tool or workflow
- “how to trust / not trust this” guide
- final demo and postmortem

## Teacher notes
This should not become a generic prompt-engineering class. Keep it grounded in:
- real document sets
- real users
- real failure modes
- clear provenance
- small, useful scope

The strongest projects will help a particular person do a particular task more clearly, not impress a room with artificial fluency.

## Repo fit
This brief would grow naturally from:
- `SECONDARY/diy-local-ai-workshop`
- `in-progress/ai-story-society`
- `in-progress/digital-storytelling-data-viz`
- `POST_SECONDARY/critical-making-civic-media`
