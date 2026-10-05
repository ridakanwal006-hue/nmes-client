#!/usr/bin/env bash
# Installs everything checklist-reel-edit needs. Safe to re-run (skips what is already there).
# Models come from the sherpa-onnx GitHub releases (Hugging Face was blocked in this environment).
set -e
MODEL_DIR="${MODEL_DIR:-$HOME/.cache/reel-edit}"
REL=https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models
need=""
command -v ffmpeg >/dev/null || need="$need ffmpeg"
fc-list | grep -qi "InterDisplay-ExtraBold" || need="$need fonts-inter"
if [ -n "$need" ]; then apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y -qq $need >/dev/null; fi
python3 -c "import sherpa_onnx, PIL, numpy" 2>/dev/null || pip install -q sherpa-onnx pillow numpy
mkdir -p "$MODEL_DIR"
get() {  # $1 = model folder name, $2 = file that proves it is complete
  if [ ! -f "$MODEL_DIR/$1/$2" ]; then
    curl -sSfL -o "$MODEL_DIR/m.tar.bz2" "$REL/$1.tar.bz2"
    tar xjf "$MODEL_DIR/m.tar.bz2" -C "$MODEL_DIR" && rm "$MODEL_DIR/m.tar.bz2"
  fi
}
get sherpa-onnx-nemo-parakeet-tdt-0.6b-v2-int8 encoder.int8.onnx   # word timestamps (~480 MB)
get sherpa-onnx-whisper-medium.en medium.en-encoder.int8.onnx       # second opinion (~1.9 GB)
rm -f "$MODEL_DIR/sherpa-onnx-whisper-medium.en/medium.en-encoder.onnx" "$MODEL_DIR/sherpa-onnx-whisper-medium.en/medium.en-decoder.onnx"
python3 "$(dirname "$0")/sfx.py" "$MODEL_DIR/sfx" >/dev/null
echo "checklist-reel-edit ready: models + sound effects in $MODEL_DIR"
