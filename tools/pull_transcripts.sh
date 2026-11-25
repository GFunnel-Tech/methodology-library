#!/usr/bin/env bash
# Pull English captions for Eric Deeran's long-form videos and the free course.
# Run on YOUR computer (YouTube blocks cloud servers). Needs: yt-dlp (pip install yt-dlp).
# Output: transcripts/<video id>.en.vtt and transcripts/<id>.txt (plain text).
# Transcripts are research notes: they stay out of git (see .gitignore).
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p transcripts
SRC=(
  "https://www.youtube.com/playlist?list=PLfs3ASv4Xy7REIx_g0dRx8fVhdQReNxuC"  # free course first
  "https://www.youtube.com/@EricDeeran/videos"                               # 206 long-form
)
for u in "${SRC[@]}"; do
  yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en.*,en" --sub-format vtt \
    --sleep-requests 1 --sleep-subtitles 2 --download-archive transcripts/.done \
    -o "transcripts/%(id)s.%(ext)s" "$u" || true
done
# VTT -> plain text, deduplicating the rolling caption lines
for f in transcripts/*.vtt; do
  [ -e "$f" ] || continue
  id=$(basename "$f" | cut -d. -f1)
  grep -v -E '^(WEBVTT|Kind:|Language:|[0-9:.]+ -->|$)' "$f" | sed 's/<[^>]*>//g' | awk '!seen[$0]++' > "transcripts/$id.txt"
done
echo "Done: $(ls transcripts/*.txt 2>/dev/null | wc -l) transcripts in ./transcripts"
