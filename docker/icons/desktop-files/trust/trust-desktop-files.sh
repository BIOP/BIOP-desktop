#!/bin/bash
set -e
for f in "$HOME"/Desktop/*.desktop; do
    [ -e "$f" ] || continue
    chmod +x "$f"
    sum=$(sha256sum "$f" | awk '{print $1}')
    gio set -t string "$f" metadata::xfce-exe-checksum "$sum" || true
    gio set -t string "$f" metadata::trusted true || true
done