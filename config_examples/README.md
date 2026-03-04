# Configuration Examples

This directory contains example configuration files for different use cases.

## How to Use

1. **Choose the configuration that matches your setup**
2. **Copy it to your config location:**

   **macOS:**
   ```bash
   cp config_examples/YOUR_CHOICE.json ~/Library/Application\ Support/ComfyLauncher/user_config.json
   # or for local config:
   cp config_examples/YOUR_CHOICE.json /path/to/ComfyLauncher/user_config.json
   ```

   **Windows:**
   ```cmd
   copy config_examples\YOUR_CHOICE.json %LOCALAPPDATA%\ComfyLauncher\user_config.json
   ```

   **Linux:**
   ```bash
   cp config_examples/YOUR_CHOICE.json ~/.local/share/ComfyLauncher/user_config.json
   ```

3. **Edit the config to match your paths/IPs**
4. **Launch ComfyLauncher**

## Available Configurations

### `local_only.json`
**For:** Single machine with local ComfyUI installation

**Features:**
- One local ComfyUI build
- Launcher manages start/stop
- Works offline
- Full process control

**Edit:** Change `/path/to/ComfyUI` to your actual path

---

### `remote_only.json`
**For:** Connecting to a remote ComfyUI server (Proxmox, dedicated server, etc.)

**Features:**
- No local ComfyUI needed
- Lightweight client
- Connect to existing server
- Skip setup dialog

**Edit:** 
- Change `192.168.1.100` to your server IP
- Change port if not using 8188

**Requirements:**
- Remote ComfyUI must be running with `--listen 0.0.0.0`

---

### `proxmox_lxc.json`
**For:** Connecting to ComfyUI running in Proxmox LXC container

**Features:**
- Optimized for Proxmox LXC setup
- Pre-configured for container networking
- Skip local setup

**Edit:**
- Change `192.168.1.61` to your LXC container IP
- Verify port matches your LXC ComfyUI port

**Setup Guide:** See `REMOTE_SERVER_GUIDE.md`

---

### `hybrid_setup.json`
**For:** Users with both local and remote ComfyUI instances

**Features:**
- Multiple local builds (dev, stable)
- Remote server option
- Switch between environments
- Maximum flexibility

**Edit:**
- Update local paths
- Update remote IP
- Toggle `remote_server.enabled` as needed

**Usage:**
- Set `"enabled": false` to use local builds
- Set `"enabled": true` to use remote server
- Switch via build manager

---

## Quick Setup Commands

### Local Only Setup
```bash
# macOS
cp config_examples/local_only.json user_config.json
nano user_config.json  # Edit path
./run_macos.sh

# Windows
copy config_examples\local_only.json user_config.json
notepad user_config.json
python main.py
```

### Remote Only Setup
```bash
# macOS
cp config_examples/remote_only.json user_config.json
nano user_config.json  # Edit IP
./run_macos.sh

# Windows
copy config_examples\remote_only.json user_config.json
notepad user_config.json
python main.py
```

### Proxmox LXC Setup
```bash
# macOS
cp config_examples/proxmox_lxc.json user_config.json
nano user_config.json  # Edit LXC IP
./run_macos.sh
```

## Configuration Fields Explained

```json
{
  // Exit behavior
  "ask_on_exit": true,              // Prompt before closing
  "exit_mode": "always_stop",       // Stop ComfyUI on exit
  
  // Build definitions
  "builds": [
    {
      "id": "unique-id",            // Unique identifier
      "name": "Display Name",       // Shown in UI
      "path": "/path/to/ComfyUI",   // Empty for remote
      "startup_mode": "auto"        // cpu/gpu/auto
    }
  ],
  
  // Active build
  "last_used_build_id": "unique-id",
  "comfyui_path": "/path/to/ComfyUI",  // Empty for remote
  
  // UI preferences
  "ui": {
    "show_manager_on_start": true   // Show build selector
  },
  
  // Remote server configuration
  "remote_server": {
    "enabled": false,               // true for remote mode
    "host": "192.168.1.100",       // Server IP/hostname
    "port": 8188                    // Server port
  }
}
```

## Switching Configurations

### Method 1: Replace Config File
```bash
cp config_examples/NEW_CONFIG.json user_config.json
```

### Method 2: Edit Existing Config
```bash
nano user_config.json
# Change "enabled": false to "enabled": true for remote
```

### Method 3: Use Build Manager
1. Launch ComfyLauncher
2. Add/edit builds in Build Manager
3. Select which build to use

## Troubleshooting

**Config not loading?**
- Check file location (project dir vs system dir)
- Verify JSON syntax (use jsonlint.com)
- Check file permissions

**Remote connection fails?**
- Verify IP address is correct
- Test with: `curl http://IP:8188`
- Check firewall rules
- Ensure ComfyUI uses `--listen 0.0.0.0`

**Build manager shows old builds?**
- Delete local `user_config.json` in project directory
- Launcher will use system config

## See Also

- `CONFIGURATION_GUIDE.md` - Detailed configuration documentation
- `REMOTE_SERVER_GUIDE.md` - Remote server setup guide
- `README_MACOS.md` - macOS-specific instructions
- `TROUBLESHOOTING.md` - Common issues and solutions
