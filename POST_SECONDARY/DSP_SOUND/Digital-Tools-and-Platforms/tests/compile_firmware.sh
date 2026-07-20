#!/usr/bin/env bash
set -euo pipefail

course_dir="$(cd "$(dirname "$0")/.." && pwd)"
board_id="${BOARD_ID:-uno}"

find "$course_dir/firmware" -mindepth 2 -maxdepth 2 -name '*.ino' -print \
  | sort \
  | while IFS= read -r sketch; do
      echo "Compiling $sketch for $board_id"
      pio ci "$sketch" --board "$board_id"
    done
