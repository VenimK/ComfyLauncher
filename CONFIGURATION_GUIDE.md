# Configuration Guide - Different User Setups

ComfyLauncher supports multiple configuration scenarios to fit different workflows.

## Configuration Scenarios

### 1. **Local Only** (Default)
Best for: Single machine, portable ComfyUI installations

```json
{
  "builds": [
    {
      "id": "local-cpu",
      "name": "ComfyUI CPU",
      "path": "/path/to/ComfyUI",
      "startup_mode": "cpu"
    },
    {
      "id": "local-gpu",
      "name": "ComfyUI GPU",
      "path": "/path/to/ComfyUI",
      "startup_mode": "gpu"
    }
  ],
  "last_used_build_id": "local-gpu",
  "comfyui_path": "/path/to/ComfyUI",
  "remote_server": {
    "enabled": false,
    "host": "",
    "port": 8188
  }
}
```

**Features:**
- ✅ Launcher starts/stops local ComfyUI
- ✅ Multiple builds with different settings
- ✅ Full process control
- ✅ Works offline

---

### 2. **Remote Only** (Proxmox LXC, Dedicated Server)
Best for: Connecting to always-on remote ComfyUI server

```json
{
  "builds": [
    {
      "id": "remote_server",
      "name": "Proxmox LXC ComfyUI",
      "path": "",
      "startup_mode": "auto"
    }
  ],
  "last_used_build_id": "remote_server",
  "comfyui_path": "",
  "ui": {
    "show_manager_on_start": false
  },
  "remote_server": {
    "enabled": true,
    "host": "192.168.1.61",
    "port": 8188
  }
}
```

**Features:**
- ✅ No local ComfyUI needed
- ✅ Connect to existing server
- ✅ Lightweight client
- ✅ Access from multiple devices

**Requirements:**
- Remote ComfyUI must be started with `--listen 0.0.0.0`
- Network access to remote server
- Remote server must be running before launching

---

### 3. **Hybrid** (Local + Remote)
Best for: Developers, power users with multiple environments

```json
{
  "builds": [
    {
      "id": "local-dev",
      "name": "Local Development",
      "path": "/Users/me/ComfyUI-dev",
      "startup_mode": "cpu"
    },
    {
      "id": "local-production",
      "name": "Local Production",
      "path": "/Users/me/ComfyUI-stable",
      "startup_mode": "gpu"
    },
    {
      "id": "remote-workstation",
      "name": "Remote Workstation",
      "path": "",
      "startup_mode": "auto",
      "remote": true,
      "remote_host": "192.168.1.100",
      "remote_port": 8188
    },
    {
      "id": "remote-cloud",
      "name": "Cloud Server",
      "path": "",
      "startup_mode": "auto",
      "remote": true,
      "remote_host": "comfyui.example.com",
      "remote_port": 8188
    }
  ],
  "last_used_build_id": "local-dev",
  "comfyui_path": "/Users/me/ComfyUI-dev",
  "remote_server": {
    "enabled": false,
    "host": "",
    "port": 8188
  }
}
```

**Features:**
- ✅ Switch between local and remote
- ✅ Multiple remote servers
- ✅ Different environments (dev, staging, prod)
- ✅ Maximum flexibility

**Note:** Currently, global `remote_server.enabled` overrides all builds. Per-build remote support is planned for future versions.

---

### 4. **Team/Studio Setup**
Best for: Multiple users sharing remote resources

```json
{
  "builds": [
    {
      "id": "team-gpu-1",
      "name": "Team GPU Server 1",
      "path": "",
      "startup_mode": "auto",
      "remote": true,
      "remote_host": "gpu1.studio.local",
      "remote_port": 8188
    },
    {
      "id": "team-gpu-2",
      "name": "Team GPU Server 2",
      "path": "",
      "startup_mode": "auto",
      "remote": true,
      "remote_host": "gpu2.studio.local",
      "remote_port": 8188
    },
    {
      "id": "local-fallback",
      "name": "Local CPU (Offline)",
      "path": "/Users/me/ComfyUI",
      "startup_mode": "cpu"
    }
  ],
  "last_used_build_id": "team-gpu-1",
  "comfyui_path": "",
  "remote_server": {
    "enabled": true,
    "host": "gpu1.studio.local",
    "port": 8188
  }
}
```

**Features:**
- ✅ Load balancing across servers
- ✅ Fallback to local if remote unavailable
- ✅ Centralized model storage
- ✅ Team collaboration

---

## Quick Configuration Templates

### Template 1: Simple Local Setup

```bash
# user_config.json
{
  "builds": [{
    "id": "default",
    "name": "ComfyUI",
    "path": "/path/to/ComfyUI",
    "startup_mode": "auto"
  }],
  "last_used_build_id": "default",
  "comfyui_path": "/path/to/ComfyUI"
}
```

### Template 2: Simple Remote Setup

```bash
# user_config.json
{
  "builds": [{
    "id": "remote",
    "name": "Remote ComfyUI",
    "path": ""
  }],
  "last_used_build_id": "remote",
  "comfyui_path": "",
  "ui": {"show_manager_on_start": false},
  "remote_server": {
    "enabled": true,
    "host": "YOUR_SERVER_IP",
    "port": 8188
  }
}
```

### Template 3: Docker Container

```bash
# user_config.json
{
  "builds": [{
    "id": "docker",
    "name": "ComfyUI Docker",
    "path": ""
  }],
  "last_used_build_id": "docker",
  "comfyui_path": "",
  "remote_server": {
    "enabled": true,
    "host": "localhost",
    "port": 8188
  }
}
```

**Docker command:**
```bash
docker run -d -p 8188:8188 \
  -v ~/ComfyUI/models:/app/models \
  -v ~/ComfyUI/output:/app/output \
  comfyui/comfyui:latest \
  --listen 0.0.0.0
```

---

## Switching Between Configurations

### Method 1: Edit Config File

**macOS:**
```bash
nano ~/Library/Application\ Support/ComfyLauncher/user_config.json
# or for local config:
nano /path/to/ComfyLauncher/user_config.json
```

**Windows:**
```cmd
notepad %LOCALAPPDATA%\ComfyLauncher\user_config.json
```

**Linux:**
```bash
nano ~/.local/share/ComfyLauncher/user_config.json
```

### Method 2: Use Build Manager

1. Launch ComfyLauncher
2. Build Manager dialog appears
3. Click "Add Build" for new configurations
4. Click gear icon to edit existing builds
5. Select which build to launch

### Method 3: Configuration Script

Use the provided `configure_remote.py` script:

```bash
python configure_remote.py
```

---

## Common Use Cases

### Use Case 1: Developer with Local and Remote

**Scenario:** Test locally, deploy to remote server

**Config:**
```json
{
  "builds": [
    {
      "id": "dev",
      "name": "Local Dev",
      "path": "/Users/me/ComfyUI-dev",
      "startup_mode": "cpu"
    },
    {
      "id": "prod",
      "name": "Production Server",
      "path": ""
    }
  ]
}
```

**Workflow:**
1. Develop with "Local Dev" build
2. Test workflows locally
3. Switch to "Production Server" for final renders
4. Toggle `remote_server.enabled` as needed

### Use Case 2: Laptop + Desktop

**Scenario:** Laptop for portability, desktop for power

**Laptop Config:**
```json
{
  "remote_server": {
    "enabled": true,
    "host": "desktop.local",
    "port": 8188
  }
}
```

**Desktop Config:**
```json
{
  "builds": [{
    "id": "local",
    "name": "Desktop GPU",
    "path": "/home/user/ComfyUI",
    "startup_mode": "gpu"
  }]
}
```

**Setup:**
1. Desktop runs ComfyUI with `--listen 0.0.0.0`
2. Laptop connects remotely
3. Use laptop as thin client
4. All processing on desktop GPU

### Use Case 3: Multiple ComfyUI Versions

**Scenario:** Stable vs. Experimental

**Config:**
```json
{
  "builds": [
    {
      "id": "stable",
      "name": "ComfyUI Stable",
      "path": "/opt/ComfyUI-stable",
      "startup_mode": "gpu"
    },
    {
      "id": "nightly",
      "name": "ComfyUI Nightly",
      "path": "/opt/ComfyUI-nightly",
      "startup_mode": "gpu"
    },
    {
      "id": "custom",
      "name": "Custom Build",
      "path": "/opt/ComfyUI-custom",
      "startup_mode": "cpu"
    }
  ]
}
```

---

## Environment Variables

Override config location:

```bash
# Custom config path
export COMFYLAUNCHER_CONFIG="/path/to/custom/config.json"

# Custom data directory
export COMFYLAUNCHER_DATA_DIR="/path/to/data"
```

---

## Best Practices

### Security

1. **Never expose ComfyUI to internet without VPN/authentication**
2. **Use firewall rules for remote access**
3. **Keep remote servers on private networks**
4. **Use SSH tunnels for remote connections:**
   ```bash
   ssh -L 8188:localhost:8188 user@remote-server
   # Then connect to localhost:8188
   ```

### Performance

1. **Local:** Best for low latency, offline work
2. **Remote LAN:** Good for powerful remote hardware
3. **Remote WAN:** Only for non-interactive workflows
4. **Hybrid:** Use local for testing, remote for production

### Organization

1. **Name builds descriptively:** "GPU Server 1" not "Build 1"
2. **Use consistent ports:** Stick to 8188 or document changes
3. **Document custom setups:** Add notes in config comments
4. **Backup configs:** Keep `user_config.json` in version control

---

## Troubleshooting

### Build Manager Shows Wrong Build

**Solution:** Delete or edit `user_config.json` in project directory

```bash
rm /path/to/ComfyLauncher/user_config.json
# Launcher will recreate from system config
```

### Can't Switch Between Local and Remote

**Current Limitation:** Global `remote_server.enabled` affects all builds

**Workaround:** Toggle in config file:
```bash
# Enable remote
sed -i 's/"enabled": false/"enabled": true/' user_config.json

# Disable remote
sed -i 's/"enabled": true/"enabled": false/' user_config.json
```

### Multiple Users on Same Machine

**Solution:** Use separate user accounts or custom config paths

```bash
# User 1
COMFYLAUNCHER_CONFIG=~/.config/comfy-user1.json ./run_macos.sh

# User 2
COMFYLAUNCHER_CONFIG=~/.config/comfy-user2.json ./run_macos.sh
```

---

## Future Enhancements

Planned features for better multi-setup support:

- [ ] Per-build remote configuration (no global toggle)
- [ ] GUI for remote server management
- [ ] Connection testing before launch
- [ ] Profile system (quick switch between configs)
- [ ] Import/export configurations
- [ ] Cloud sync for configs across devices
- [ ] Auto-discovery of local network ComfyUI instances

---

## Examples by User Type

### **Casual User**
- Single local ComfyUI installation
- Default settings
- Minimal configuration

### **Power User**
- Multiple local builds (stable, experimental)
- Occasional remote access
- Custom startup modes per build

### **Developer**
- Local development environment
- Remote staging server
- Remote production server
- Version control integration

### **Studio/Team**
- Shared remote GPU servers
- Load balancing
- Centralized model storage
- User-specific local fallbacks

### **System Administrator**
- Manage multiple remote instances
- Monitor server health
- Deploy updates
- User access control

---

For specific setup instructions, see:
- `README_MACOS.md` - macOS installation
- `REMOTE_SERVER_GUIDE.md` - Remote server setup
- `TROUBLESHOOTING.md` - Common issues
