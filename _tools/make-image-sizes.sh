#!/bin/sh
# Britannia IoT Solutions — responsive derivatives for the platform photographs.
#
#     sh _tools/make-image-sizes.sh
#
# The photographs arrive at 1080px but display in a column around 630px wide on
# a desktop and 360px on a phone, so a phone was downloading roughly three times
# the pixels it could show. This emits 480px and 768px variants in both formats,
# plus a WebP of the original, and the pages choose between them with srcset.
#
# Any derivative that does not come out smaller than the original is deleted
# again: re-encoding an already-compressed JPEG can easily make it bigger, and
# shipping a "smaller" file that is larger would be worse than doing nothing.
#
# The original .jpg filenames are deliberately left untouched — the structured
# data and the social cards point at them, and those URLs must not move.
#
# Needs sips (macOS) and cwebp (brew install webp).
set -e
cd "$(dirname "$0")/.."
DIR=assets/img/platform

for src in $DIR/*.jpg; do
  case "$src" in *-480.jpg|*-768.jpg) continue;; esac
  base="${src%.jpg}"
  full=$(sips -g pixelWidth "$src" | awk '/pixelWidth/{print $2}')
  orig=$(wc -c < "$src")

  for w in 480 768; do
    [ "$w" -ge "$full" ] && continue
    sips -Z "$w" -s formatOptions 68 "$src" --out "$base-$w.jpg" >/dev/null
    cwebp -quiet -q 78 -resize "$w" 0 "$src" -o "$base-$w.webp"
  done
  # The full-size WebP has to beat the JPEG to be worth having. A noisy
  # photograph can lose that contest at q78, so drop the quality once and try
  # again before giving up on it.
  cwebp -quiet -q 78 "$src" -o "$base.webp"
  if [ "$(wc -c < "$base.webp")" -ge "$orig" ]; then
    cwebp -quiet -q 68 "$src" -o "$base.webp"
  fi

  for f in "$base-480.jpg" "$base-768.jpg" "$base-480.webp" "$base-768.webp" "$base.webp"; do
    [ -f "$f" ] || continue
    if [ "$(wc -c < "$f")" -ge "$orig" ]; then
      echo "  dropping $(basename "$f") — not smaller than the original"
      rm "$f"
    fi
  done
done

echo "--- platform images ---"
ls -S $DIR | while read f; do printf '  %-36s %6s\n' "$f" "$(du -h $DIR/$f | cut -f1)"; done
