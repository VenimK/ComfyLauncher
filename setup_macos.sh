#!/bin/bash
# ComfyLauncher macOS Setup Script

set -e

echo "🚀 ComfyLauncher macOS Setup"
echo "=============================="
echo ""

# Check Python version
echo "📋 Checking Python version..."
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "   Install it with: brew install python@3.11"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✅ Found Python $PYTHON_VERSION"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
if [ -d "venv" ]; then
    echo "⚠️  Virtual environment already exists. Removing old one..."
    rm -rf venv
fi

python3 -m venv venv
echo "✅ Virtual environment created"

# Activate and install dependencies
echo ""
echo "📥 Installing dependencies..."
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo ""
echo "✅ Setup complete!"
echo ""
echo "To run ComfyLauncher:"
echo "  source venv/bin/activate"
echo "  python main.py"
echo ""
echo "Or directly:"
echo "  venv/bin/python main.py"
