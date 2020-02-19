#!/usr/bin/env bash
RESAMPLED="$1-sampled.wav"
if [ ! -f "$RESAMPLED" ]
then
  sox "$1.wav" -r 16000 "$1-sampled.wav"
fi
deepspeech --model deepspeech-0.6.1-models/output_graph.pbmm --lm deepspeech-0.6.1-models/lm.binary --trie deepspeech-0.6.1-models/trie --audio "$RESAMPLED" --json > "$1-out.json"