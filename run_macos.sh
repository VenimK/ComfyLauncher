#!/bin/bash
# ComfyLauncher macOS Runner Script

cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "   Run ./setup_macos.sh first"
    exit 1
fi

source venv/bin/activate
python main.py
