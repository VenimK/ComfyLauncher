# Cross-Platform Implementation Notes

## Architecture Overview

ComfyLauncher now supports **Windows, macOS, and Linux** through platform abstraction layers.

## Platform Detection

All platform-specific code uses `utils/platform_utils.py`:

```python
from utils.platform_utils import is_windows, is_macos, is_linux
```

## Key Differences by Platform

### Browser Widget

| Platform | Widget | Backend |
|----------|--------|---------|
| Windows | WebView2Widget | Microsoft Edge WebView2 |
| macOS | WebEngineWidget | Qt WebEngine (Chromium) |
| Linux | WebEngineWidget | Qt WebEngine (Chromium) |

**Fallback**: Windows can use WebEngineWidget if WebView2 is unavailable.

### File Manager

| Platform | Command | Function |
|----------|---------|----------|
| Windows | `os.startfile()` | Opens Explorer |
| macOS | `open` | Opens Finder |
| Linux | `xdg-open` | Opens default file manager |

### Startup Scripts

| Platform | Extension | Shell |
|----------|-----------|-------|
| Windows | `.bat` | cmd.exe |
| macOS | `.sh` | bash |
| Linux | `.sh` | bash |

### Python Executable Paths

**Windows**:
- `python_embeded/python.exe`
- `python_embedded/python.exe`

**macOS/Linux**:
- `python_embeded/bin/python3`
- `python_embedded/bin/python3`
- `venv/bin/python3`
- `.venv/bin/python3`

### Process Creation Flags

**Windows**:
- `CREATE_NEW_CONSOLE` - Show terminal
- `CREATE_NO_WINDOW` - Hide terminal

**macOS/Linux**:
- No flags needed for hidden mode
- Uses `osascript` (macOS) or terminal emulator for visible mode

### User Data Directories

| Platform | Location |
|----------|----------|
| Windows | `%LOCALAPPDATA%\ComfyLauncher` |
| macOS | `~/Library/Application Support/ComfyLauncher` |
| Linux | `~/.local/share/ComfyLauncher` |

### Log Directories

| Platform | Location |
|----------|----------|
| Windows | `%APPDATA%\ComfyLauncher\logs` |
| macOS | `~/Library/Logs/ComfyLauncher/logs` |
| Linux | `~/.local/state/ComfyLauncher/logs` |

## Code Patterns

### Opening Files/Folders

**Before** (Windows-only):
```python
os.startfile(path)
```

**After** (Cross-platform):
```python
from utils.platform_utils import open_file_manager
open_file_manager(path)
```

### Process Creation

**Before** (Windows-only):
```python
subprocess.Popen(
    ["cmd.exe", "/k", "script.bat"],
    creationflags=subprocess.CREATE_NEW_CONSOLE
)
```

**After** (Cross-platform):
```python
from utils.platform_utils import get_shell_command, get_new_console_flag

if is_windows():
    subprocess.Popen(
        ["cmd.exe", "/k", script_file],
        creationflags=get_new_console_flag()
    )
else:
    subprocess.Popen(
        ["bash", script_file],
        cwd=base_dir
    )
```

### Python Paths

**Before** (Windows-only):
```python
python_exe = os.path.join(base_dir, "python_embeded", "python.exe")
```

**After** (Cross-platform):
```python
from utils.platform_utils import get_embedded_python_paths

candidates = get_embedded_python_paths(base_dir)
for python_exe in candidates:
    if os.path.exists(python_exe):
        break
```

## Testing Checklist

### Windows
- [ ] WebView2 browser loads ComfyUI
- [ ] .bat files execute correctly
- [ ] CMD window shows/hides based on settings
- [ ] File Explorer opens for folders
- [ ] Process tree termination works

### macOS
- [ ] Qt WebEngine browser loads ComfyUI
- [ ] .sh files execute correctly
- [ ] Terminal.app integration works
- [ ] Finder opens for folders
- [ ] Process tree termination works
- [ ] High DPI displays render correctly

### Linux
- [ ] Qt WebEngine browser loads ComfyUI
- [ ] .sh files execute correctly
- [ ] File manager opens (xdg-open)
- [ ] Process tree termination works
- [ ] Various desktop environments (GNOME, KDE, etc.)

## Known Issues

### macOS
1. **Terminal visibility**: Cannot fully hide terminal like Windows CMD
2. **GPU detection**: CUDA detection may not work (most Macs use Metal)
3. **Notarization**: Standalone app requires Apple Developer signing

### Linux
1. **WebEngine dependencies**: May require additional system packages
2. **File manager**: `xdg-open` behavior varies by desktop environment
3. **Terminal emulators**: Different distros use different terminals

## Future Improvements

1. **Native macOS WebKit**: Use PyObjC for native WebKit instead of Qt WebEngine
2. **Metal GPU Support**: Detect and use Metal on macOS
3. **Wayland Support**: Better Linux compatibility with Wayland
4. **ARM Builds**: Native Apple Silicon and ARM Linux support
5. **Flatpak/Snap**: Linux distribution packaging
