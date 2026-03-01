# Troubleshooting Guide

## Common Issues

### Issue: "Port 8188 already in use" or Launcher won't start

**Symptoms:**
- ComfyUI shows: `To see the GUI go to: http://0.0.0.0:8188/`
- Launcher fails to detect running server
- Multiple ComfyUI instances trying to start

**Cause:**
ComfyUI is binding to `0.0.0.0:8188` (all network interfaces) instead of `127.0.0.1:8188` (localhost only). This can happen with certain ComfyUI configurations or command-line arguments.

**Solution:**

1. **Stop all ComfyUI instances:**
   
   **Windows:**
   ```cmd
   taskkill /F /IM python.exe
   ```
   
   **macOS/Linux:**
   ```bash
   lsof -ti:8188 | xargs kill -9
   ```

2. **Check ComfyUI launch arguments:**
   - Look for `--listen 0.0.0.0` in your startup scripts
   - Remove or change to `--listen 127.0.0.1`

3. **Update ComfyLauncher:**
   - Latest version (1.6.0+) automatically detects servers on any interface
   - The launcher will now work regardless of binding address

4. **If you need ComfyUI accessible from network:**
   - Keep `--listen 0.0.0.0` in ComfyUI
   - ComfyLauncher will detect and connect via localhost automatically
   - External devices can still access via your machine's IP

### Issue: Blank browser window

**Symptoms:**
- Launcher opens but shows white/blank screen
- No ComfyUI interface visible

**Solutions:**

1. **Check if ComfyUI server is running:**
   - Look for console output: "To see the GUI go to: http://..."
   - Check logs in ComfyLauncher settings

2. **Verify port is accessible:**
   
   **Windows:**
   ```cmd
   netstat -an | findstr :8188
   ```
   
   **macOS/Linux:**
   ```bash
   lsof -i :8188
   ```

3. **Try manual browser test:**
   - Open regular browser
   - Go to `http://127.0.0.1:8188`
   - If this works, it's a launcher browser issue

4. **Clear browser cache (WebEngine):**
   
   **Windows:**
   ```
   %LOCALAPPDATA%\ComfyLauncher\webview2
   ```
   
   **macOS:**
   ```
   ~/Library/Application Support/ComfyLauncher/webview2
   ```
   
   Delete this folder and restart launcher.

### Issue: "Permission Denied" (macOS/Linux)

**Symptoms:**
- Cannot run startup scripts
- "Permission denied" errors

**Solution:**
```bash
chmod +x setup_macos.sh run_macos.sh
chmod +x /path/to/ComfyUI/*.sh
```

### Issue: Multiple ComfyUI windows opening

**Symptoms:**
- Each launcher start creates new ComfyUI instance
- Multiple CMD/Terminal windows

**Cause:**
Port detection not working properly.

**Solution:**

1. **Update to latest launcher** (includes improved port detection)

2. **Manually stop all instances:**
   ```bash
   # Find all Python processes running ComfyUI
   ps aux | grep comfyui
   # Kill them
   kill -9 <PID>
   ```

3. **Check firewall settings:**
   - Ensure localhost (127.0.0.1) is not blocked
   - Allow Python through firewall

### Issue: "No module named PyQt6" (macOS)

**Symptoms:**
- ImportError when running launcher
- Missing dependencies

**Solution:**

1. **Create virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Or use setup script:**
   ```bash
   ./setup_macos.sh
   ```

3. **Always activate venv before running:**
   ```bash
   source venv/bin/activate
   python main.py
   ```

### Issue: High memory usage

**Symptoms:**
- Launcher uses excessive RAM
- System slowdown

**Solutions:**

1. **Close unused builds:**
   - Only keep one ComfyUI instance running
   - Use launcher's Stop button

2. **Reduce browser cache:**
   - Settings → Clear cache
   - Restart launcher

3. **Use "Show CMD" mode:**
   - Settings → Show CMD window
   - Reduces internal console buffer

### Issue: ComfyUI won't stop

**Symptoms:**
- Stop button doesn't work
- Process remains after closing launcher

**Solution:**

1. **Force stop via launcher:**
   - Settings → Application Logs
   - Look for process PID
   - Use system task manager

2. **Manual process kill:**
   
   **Windows:**
   ```cmd
   tasklist | findstr python
   taskkill /F /PID <PID>
   ```
   
   **macOS/Linux:**
   ```bash
   ps aux | grep comfyui
   kill -9 <PID>
   ```

### Issue: Startup script not found

**Symptoms:**
- "run_cpu.bat not found" (Windows)
- "run_cpu.sh not found" (macOS/Linux)

**Cause:**
ComfyUI portable build doesn't include startup scripts.

**Solution:**

Launcher will automatically fall back to Python mode. This is normal and works fine.

**Optional:** Create startup scripts manually:

**Windows (run_cpu.bat):**
```batch
@echo off
cd /d "%~dp0"
.\python_embeded\python.exe -s ComfyUI\main.py --cpu
pause
```

**macOS/Linux (run_cpu.sh):**
```bash
#!/bin/bash
cd "$(dirname "$0")"
python3 main.py --cpu
```

## Getting Help

### Collect diagnostic information:

1. **Launcher logs:**
   - Windows: `%APPDATA%\ComfyLauncher\logs\launcher.log`
   - macOS: `~/Library/Logs/ComfyLauncher/logs/launcher.log`
   - Linux: `~/.local/state/ComfyLauncher/logs/launcher.log`

2. **System info:**
   - OS version
   - Python version: `python --version`
   - ComfyUI version
   - Launcher version (see About dialog)

3. **Port status:**
   ```bash
   # Windows
   netstat -an | findstr :8188
   
   # macOS/Linux
   lsof -i :8188
   ```

### Report issues:

- GitHub Issues: https://github.com/nondeletable/ComfyLauncher/issues
- Discord: https://discord.com/invite/6nvXwXp78u
- Include logs and system info above

## Advanced Troubleshooting

### Enable debug logging:

Add to `user_config.json`:
```json
{
  "debug_mode": true,
  "verbose_logging": true
}
```

### Test port detection manually:

```python
import psutil

for conn in psutil.net_connections(kind='inet'):
    if conn.laddr and conn.laddr.port == 8188:
        print(f"Port 8188: {conn.laddr.ip}:{conn.laddr.port} - {conn.status}")
```

### Reset launcher configuration:

**Backup first!**

**Windows:**
```cmd
del %LOCALAPPDATA%\ComfyLauncher\user_config.json
```

**macOS:**
```bash
rm ~/Library/Application\ Support/ComfyLauncher/user_config.json
```

This will reset all settings to defaults.
