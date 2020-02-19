#!/usr/bin/env bash
youtube-dl -x --audio-format wav -o "%(id)s.wav" "$1"