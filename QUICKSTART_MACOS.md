# Quick Start Guide - macOS

## First Time Setup (One-Time)

```bash
# 1. Make setup script executable and run it
chmod +x setup_macos.sh
./setup_macos.sh
```

This will:
- Create a Python virtual environment
- Install all required dependencies (PyQt6, WebEngine, etc.)
- Set up the project for macOS

## Running ComfyLauncher

### Option 1: Using the run script (Recommended)
```bash
./run_macos.sh
```

### Option 2: Manual activation
```bash
source venv/bin/activate
python main.py
```

### Option 3: Direct execution
```bash
venv/bin/python main.py
```

## What to Expect

1. **First Launch**: You'll see a setup window asking for your ComfyUI path
2. **Build Manager**: Select which ComfyUI build to launch
3. **Main Window**: Browser-based interface to ComfyUI

## Setting Up ComfyUI for macOS

### If you don't have ComfyUI yet:

```bash
# Clone ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install torch torchvision torchaudio
pip install -r requirements.txt

# Test run
python main.py
```

### Point ComfyLauncher to your ComfyUI:
- When prompted, select the folder containing ComfyUI's `main.py`
- Example: `/Users/yourname/ComfyUI`

## Troubleshooting

### "Permission Denied" when running scripts
```bash
chmod +x setup_macos.sh run_macos.sh
```

### "No module named PyQt6"
You forgot to activate the virtual environment:
```bash
source venv/bin/activate
```

### Port 8188 already in use
ComfyUI is already running. Either:
- Use the existing instance
- Stop it: `lsof -i :8188` then `kill -9 <PID>`

### Blank browser window
1. Check if ComfyUI server is actually running (look for "To see the GUI go to: http://127.0.0.1:8188")
2. Try refreshing the browser (Cmd+R)
3. Check logs in `~/Library/Logs/ComfyLauncher/logs/launcher.log`

## Features on macOS

✅ **Cross-platform browser** - Uses Qt WebEngine (Chromium-based)  
✅ **File manager integration** - Opens Finder with Cmd+Click  
✅ **Process management** - Clean start/stop/restart  
✅ **Console output** - Built-in terminal viewer  
✅ **Multiple builds** - Manage different ComfyUI installations  

## System Requirements

- macOS 10.15 (Catalina) or later
- Python 3.11 - 3.13 (3.14 also works)
- 4GB RAM minimum (8GB recommended)
- 2GB free disk space

## Performance

- **Startup**: ~2-3 seconds
- **Memory**: ~200MB (launcher only)
- **CPU**: <5% idle

Enjoy using ComfyLauncher on macOS! 🚀
