#!/usr/bin/env bash
youtube-dl -x --audio-format "wav" -o "%(id)s.%(ext)s" -a urls.txt