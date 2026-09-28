#!/bin/bash
# Installs the reel-edit video tools (ffmpeg, Montserrat, Whisper model) in web sessions.
set -euo pipefail
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi
bash "$CLAUDE_PROJECT_DIR/.claude/skills/reel-edit/scripts/setup.sh"
