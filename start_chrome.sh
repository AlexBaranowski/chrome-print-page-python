#!/usr/bin/env bash



# Args taken from https://github.com/thecodingmachine/gotenberg/blob/f9f0fc1d67d15d3fc1cc978b2de3c88dd8f16f7b/internal/pkg/chrome/chrome.go
BASIC_ARGS="--no-sandbox --headless --disable-dev-shm-usage --font-render-hinting=none --remote-debugging-port=9222 --disable-gpu --disable-translate --disable-extensions --disable-background-networking --safebrowsing-disable-auto-update --disable-sync --disable-default-apps --hide-scrollbars --metrics-recording-only --mute-audio --no-first-run"

google-chrome $BASIC_ARGS 

