#!/bin/bash
set -euo pipefail

# Only run on fresh session start, not resume/clear/compact
INPUT=$(cat)
SOURCE=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('source',''))" 2>/dev/null || echo "")
if [ "$SOURCE" != "startup" ]; then
  exit 0
fi

ANALYSIS_FILE="${CLAUDE_PROJECT_DIR:-$(pwd)}/latest_analysis.md"

if [ ! -f "$ANALYSIS_FILE" ]; then
  exit 0
fi

# Only surface it if the workflow updated it in the last 48 hours
LAST_UPDATE=$(git log -1 --format="%ct" -- latest_analysis.md 2>/dev/null)
LAST_UPDATE=${LAST_UPDATE:-0}  # git log returns empty string (not error) if file never committed
NOW=$(date +%s)
AGE=$((NOW - LAST_UPDATE))

if [ "$AGE" -lt "172800" ]; then
  echo "New Nate Herk analysis is ready:"
  echo ""
  cat "$ANALYSIS_FILE"
fi
