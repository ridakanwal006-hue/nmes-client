#!/bin/bash
# Installs the video tools for the reel-edit and checklist-reel-edit skills in web sessions.
set -euo pipefail
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi
bash "$CLAUDE_PROJECT_DIR/.claude/skills/reel-edit/scripts/setup.sh"
bash "$CLAUDE_PROJECT_DIR/.claude/skills/checklist-reel-edit/scripts/setup.sh"
