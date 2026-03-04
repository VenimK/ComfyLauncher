# ComfyLauncher Optimization Guide

This guide explains how to optimize ComfyLauncher for better performance and lower resource usage.

## Resource Usage Overview

### Typical Resource Usage

**Idle State:**
- Memory: 150-250 MB
- CPU: <5%
- Threads: 8-12

**Active State (ComfyUI running):**
- Memory: 200-400 MB
- CPU: 5-15%
- Threads: 10-15

**High Usage Indicators:**
- Memory >500 MB: Check console buffer, browser cache
- CPU >20%: Check polling intervals, background tasks
- Threads >20: Possible resource leak

## Performance Settings

### Configuration File

Edit `user_config.json` to add performance settings:

```json
{
  "performance": {
    "console_buffer_lines": 1000,
    "console_max_line_length": 1000,
    "server_check_interval": 1.0,
    "enable_splash_video": true,
    "low_memory_mode": false,
    "log_resource_usage": false
  }
}
```

### Setting Explanations

#### `console_buffer_lines` (default: 1000)
Number of console output lines to keep in memory.

**Recommendations:**
- **Low memory systems:** 500
- **Normal systems:** 1000 (default)
- **High memory systems:** 2000
- **Debugging:** 5000

**Impact:**
- Lower = Less memory, lose older logs
- Higher = More memory, keep full history

#### `console_max_line_length` (default: 1000)
Maximum characters per console line.

**Recommendations:**
- **Low memory:** 500
- **Normal:** 1000 (default)
- **Unlimited:** 10000

**Impact:**
- Prevents memory bloat from extremely long log lines
- Truncates lines with "..." suffix

#### `server_check_interval` (default: 1.0)
Seconds between ComfyUI server status checks.

**Recommendations:**
- **Low CPU systems:** 2.0-5.0
- **Normal systems:** 1.0 (default)
- **Fast response needed:** 0.5

**Impact:**
- Higher = Less CPU, slower detection
- Lower = More CPU, faster detection

#### `enable_splash_video` (default: true)
Show animated splash screen on startup.

**Recommendations:**
- **Low memory/CPU:** false
- **Normal:** true

**Impact:**
- Disabled = Faster startup, less memory
- Enabled = Better UX, slight overhead

#### `low_memory_mode` (default: false)
Enable aggressive memory optimizations.

**Recommendations:**
- **Systems with <4GB RAM:** true
- **Normal systems:** false

**Impact:**
- Reduces buffer sizes
- Disables non-essential features
- May affect user experience

#### `log_resource_usage` (default: false)
Log memory/CPU usage periodically.

**Recommendations:**
- **Debugging performance:** true
- **Normal use:** false

**Impact:**
- Helps identify resource issues
- Slight overhead from monitoring

## Optimization Strategies

### 1. Reduce Memory Usage

#### A. Use "Show CMD" Mode
```json
{
  "show_cmd": true
}
```

**Benefit:** Reduces memory by 50-100MB
- No internal console buffering
- Output goes to external terminal
- Launcher acts as thin client

#### B. Reduce Console Buffer
```json
{
  "performance": {
    "console_buffer_lines": 500,
    "console_max_line_length": 500
  }
}
```

**Benefit:** Reduces memory by 20-50MB

#### C. Clear Browser Cache
```bash
# macOS
rm -rf ~/Library/Application\ Support/ComfyLauncher/webview2

# Windows
rmdir /s %LOCALAPPDATA%\ComfyLauncher\webview2

# Linux
rm -rf ~/.local/share/ComfyLauncher/webview2
```

**Benefit:** Reduces disk usage, may improve performance

#### D. Use Remote Mode
```json
{
  "remote_server": {
    "enabled": true,
    "host": "192.168.1.100",
    "port": 8188
  }
}
```

**Benefit:** Minimal memory usage (~150MB)
- No local ComfyUI process
- Launcher is just a browser wrapper

### 2. Reduce CPU Usage

#### A. Increase Check Interval
```json
{
  "performance": {
    "server_check_interval": 2.0
  }
}
```

**Benefit:** Reduces CPU by 50%

#### B. Disable Splash Video
```json
{
  "performance": {
    "enable_splash_video": false
  }
}
```

**Benefit:** Faster startup, less CPU during launch

#### C. Close Unused Builds
Remove builds you don't use from `user_config.json`:

```json
{
  "builds": [
    // Keep only active builds
  ]
}
```

### 3. Optimize for Different Scenarios

#### Scenario 1: Low-End System (<4GB RAM)

```json
{
  "show_cmd": true,
  "performance": {
    "console_buffer_lines": 500,
    "console_max_line_length": 500,
    "server_check_interval": 2.0,
    "enable_splash_video": false,
    "low_memory_mode": true
  }
}
```

**Expected Usage:** 100-150MB RAM, <3% CPU

#### Scenario 2: Remote Client Only

```json
{
  "remote_server": {
    "enabled": true,
    "host": "YOUR_SERVER",
    "port": 8188
  },
  "performance": {
    "console_buffer_lines": 500,
    "server_check_interval": 2.0
  }
}
```

**Expected Usage:** 150-200MB RAM, <5% CPU

#### Scenario 3: High-Performance System

```json
{
  "show_cmd": false,
  "performance": {
    "console_buffer_lines": 2000,
    "console_max_line_length": 2000,
    "server_check_interval": 0.5,
    "enable_splash_video": true,
    "low_memory_mode": false,
    "log_resource_usage": true
  }
}
```

**Expected Usage:** 300-400MB RAM, 5-10% CPU

#### Scenario 4: Battery-Powered (Laptop)

```json
{
  "performance": {
    "server_check_interval": 3.0,
    "enable_splash_video": false,
    "low_memory_mode": true
  }
}
```

**Expected Usage:** Optimized for battery life

## Monitoring Resource Usage

### Enable Resource Logging

```json
{
  "performance": {
    "log_resource_usage": true
  }
}
```

Check logs for resource usage:
```bash
# macOS
tail -f ~/Library/Logs/ComfyLauncher/logs/launcher.log | grep "📊"

# Windows
type %APPDATA%\ComfyLauncher\logs\launcher.log | findstr "📊"
```

### Manual Monitoring

**macOS:**
```bash
# Find ComfyLauncher process
ps aux | grep ComfyLauncher

# Monitor with Activity Monitor
open -a "Activity Monitor"
```

**Windows:**
```cmd
# Task Manager
taskmgr

# Find Python process running main.py
tasklist | findstr python
```

**Linux:**
```bash
# htop
htop

# top
top -p $(pgrep -f ComfyLauncher)
```

## Troubleshooting Performance Issues

### High Memory Usage

**Symptoms:** >500MB RAM usage

**Diagnosis:**
1. Check console buffer size
2. Check browser cache size
3. Check for memory leaks

**Solutions:**
```json
{
  "show_cmd": true,
  "performance": {
    "console_buffer_lines": 500,
    "low_memory_mode": true
  }
}
```

### High CPU Usage

**Symptoms:** >20% CPU when idle

**Diagnosis:**
1. Check server polling interval
2. Check for background tasks
3. Check browser activity

**Solutions:**
```json
{
  "performance": {
    "server_check_interval": 3.0
  }
}
```

### Slow Startup

**Symptoms:** Takes >5 seconds to launch

**Solutions:**
1. Disable splash video
2. Clear browser cache
3. Use SSD for installation
4. Reduce number of builds

```json
{
  "performance": {
    "enable_splash_video": false
  }
}
```

### Memory Leaks

**Symptoms:** Memory grows over time

**Diagnosis:**
1. Enable resource logging
2. Monitor over extended period
3. Check console buffer growth

**Solutions:**
1. Restart launcher periodically
2. Reduce console buffer
3. Report issue on GitHub

## Platform-Specific Optimizations

### macOS

**Use Native Python:**
```bash
# Avoid Rosetta 2 on Apple Silicon
arch -arm64 python3 main.py
```

**Reduce Energy Impact:**
```bash
# Check energy impact
pmset -g assertions

# Reduce polling
# Edit user_config.json: "server_check_interval": 2.0
```

### Windows

**Disable Windows Defender Scanning:**
Add ComfyLauncher directory to exclusions:
```
Settings → Windows Security → Virus & threat protection → Exclusions
```

**Use Hardware Acceleration:**
Ensure GPU acceleration is enabled in browser settings.

### Linux

**Use Lightweight Desktop:**
- XFCE, LXQt instead of GNOME/KDE
- Reduces overall system overhead

**Compile Python with Optimizations:**
```bash
CFLAGS="-O3" python3 -m pip install --force-reinstall pyqt6
```

## Best Practices

### 1. Regular Maintenance

- Clear browser cache monthly
- Restart launcher after extended use
- Update to latest version
- Monitor resource usage periodically

### 2. Configuration Management

- Keep backup of `user_config.json`
- Document custom settings
- Test changes incrementally
- Revert if issues occur

### 3. System Requirements

**Minimum:**
- 2GB RAM
- Dual-core CPU
- 500MB disk space

**Recommended:**
- 4GB RAM
- Quad-core CPU
- 2GB disk space (with cache)

**Optimal:**
- 8GB+ RAM
- 6+ core CPU
- SSD storage

## Performance Benchmarks

### Startup Time

- **Cold start:** 2-4 seconds
- **Warm start:** 1-2 seconds
- **With splash video:** +0.5 seconds
- **Remote mode:** 1-2 seconds

### Memory Usage by Mode

| Mode | Idle | Active | Peak |
|------|------|--------|------|
| Local (Show CMD) | 100MB | 150MB | 200MB |
| Local (Internal Console) | 200MB | 300MB | 400MB |
| Remote | 150MB | 200MB | 250MB |
| Low Memory Mode | 80MB | 120MB | 150MB |

### CPU Usage by Activity

| Activity | CPU % |
|----------|-------|
| Idle | <5% |
| Starting ComfyUI | 10-20% |
| ComfyUI Running | <5% |
| Image Generation | <5% (ComfyUI uses CPU) |
| Browser Rendering | 5-15% |

## Advanced Optimizations

### 1. Custom Python Flags

```bash
# Optimize Python interpreter
python3 -O main.py  # Enable optimizations
python3 -OO main.py # Remove docstrings too
```

### 2. Reduce Qt Overhead

```bash
# Disable Qt debug output
export QT_LOGGING_RULES="*.debug=false"
```

### 3. Profile Performance

```bash
# Profile with cProfile
python3 -m cProfile -o profile.stats main.py

# Analyze results
python3 -m pstats profile.stats
```

## Getting Help

If you experience performance issues:

1. **Enable resource logging**
2. **Collect system information**
3. **Document the issue**
4. **Report on GitHub** with:
   - OS and version
   - Python version
   - Resource usage logs
   - Configuration file
   - Steps to reproduce

---

**Last Updated:** March 2026  
**Version:** 1.6.0+
