#!/usr/bin/env bash
# Installs everything the reel-edit skill needs. Safe to re-run.
# Hugging Face is blocked in this environment, so the Whisper model comes from
# the sherpa-onnx GitHub release instead of faster-whisper's default download.
set -e
MODEL_DIR="${MODEL_DIR:-$HOME/.cache/reel-edit}"
command -v ffmpeg >/dev/null || { apt-get update -qq && apt-get install -y -qq ffmpeg; }
fc-list | grep -qi "Montserrat-ExtraBold" || apt-get install -y -qq fonts-montserrat
python3 -c "import sherpa_onnx, PIL, numpy" 2>/dev/null || pip install -q sherpa-onnx pillow numpy
if [ ! -f "$MODEL_DIR/sherpa-onnx-whisper-medium.en/medium.en-encoder.int8.onnx" ]; then
  mkdir -p "$MODEL_DIR" && cd "$MODEL_DIR"
  curl -sSfL -o m.tar.bz2 https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-medium.en.tar.bz2
  tar xjf m.tar.bz2 && rm m.tar.bz2
  # keep only the int8 model to save disk
  rm -f sherpa-onnx-whisper-medium.en/medium.en-encoder.onnx sherpa-onnx-whisper-medium.en/medium.en-decoder.onnx
fi
echo "reel-edit ready: model in $MODEL_DIR"
