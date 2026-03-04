# Remote Server Guide - Connecting to ComfyUI on Proxmox LXC

This guide explains how to connect ComfyLauncher to a remote ComfyUI instance running on a Proxmox LXC container or any other remote server.

## Use Cases

- ComfyUI running on a Proxmox LXC container
- ComfyUI on a dedicated server/workstation
- ComfyUI in a Docker container
- ComfyUI on another machine in your network
- Cloud-hosted ComfyUI instance

## Quick Setup

### 1. Configure Remote Server in ComfyLauncher

Edit your `user_config.json`:

**Location:**
- **Windows:** `%LOCALAPPDATA%\ComfyLauncher\user_config.json`
- **macOS:** `~/Library/Application Support/ComfyLauncher/user_config.json`
- **Linux:** `~/.local/share/ComfyLauncher/user_config.json`

**Add/modify the remote_server section:**

```json
{
  "remote_server": {
    "enabled": true,
    "host": "192.168.1.100",
    "port": 8188
  }
}
```

Replace `192.168.1.100` with your Proxmox LXC IP address.

### 2. Ensure ComfyUI is Accessible

On your Proxmox LXC container, ComfyUI must be configured to accept external connections:

```bash
# Start ComfyUI with --listen flag
python main.py --listen 0.0.0.0 --port 8188
```

Or create a startup script (`start_comfy.sh`):

```bash
#!/bin/bash
cd /path/to/ComfyUI
python3 main.py --listen 0.0.0.0 --port 8188
```

### 3. Test Connection

From your client machine, test if the server is accessible:

```bash
# Using curl
curl http://192.168.1.100:8188

# Using browser
# Open: http://192.168.1.100:8188
```

If you see the ComfyUI interface, you're ready to connect with ComfyLauncher.

### 4. Launch ComfyLauncher

When remote server is enabled:
- ComfyLauncher will **NOT** start a local ComfyUI instance
- It will connect directly to your remote server
- All other features work normally (browser, controls, etc.)

## Proxmox LXC Specific Setup

### Network Configuration

1. **Check LXC IP Address:**
   ```bash
   # In Proxmox web UI: Container → Summary → IP Address
   # Or via SSH to LXC:
   ip addr show
   ```

2. **Ensure Firewall Allows Port 8188:**
   ```bash
   # On LXC container
   ufw allow 8188/tcp
   # Or
   iptables -A INPUT -p tcp --dport 8188 -j ACCEPT
   ```

3. **Test from Proxmox Host:**
   ```bash
   curl http://<LXC_IP>:8188
   ```

### ComfyUI Installation in LXC

If you haven't installed ComfyUI in your LXC yet:

```bash
# Update system
apt update && apt upgrade -y

# Install Python and dependencies
apt install -y python3 python3-pip python3-venv git

# Clone ComfyUI
cd /opt
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install -r requirements.txt

# Start ComfyUI (accessible from network)
python main.py --listen 0.0.0.0 --port 8188
```

### Auto-Start ComfyUI on LXC Boot

Create a systemd service:

```bash
sudo nano /etc/systemd/system/comfyui.service
```

Add:

```ini
[Unit]
Description=ComfyUI Server
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/ComfyUI
Environment="PATH=/opt/ComfyUI/venv/bin"
ExecStart=/opt/ComfyUI/venv/bin/python main.py --listen 0.0.0.0 --port 8188
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable comfyui
sudo systemctl start comfyui
sudo systemctl status comfyui
```

## Configuration Examples

### Example 1: Proxmox LXC on Local Network

```json
{
  "remote_server": {
    "enabled": true,
    "host": "192.168.1.100",
    "port": 8188
  }
}
```

### Example 2: Using Hostname

```json
{
  "remote_server": {
    "enabled": true,
    "host": "comfyui.local",
    "port": 8188
  }
}
```

### Example 3: Custom Port

```json
{
  "remote_server": {
    "enabled": true,
    "host": "192.168.1.100",
    "port": 8080
  }
}
```

### Example 4: Disable Remote (Use Local)

```json
{
  "remote_server": {
    "enabled": false,
    "host": "",
    "port": 8188
  }
}
```

## Troubleshooting

### Cannot Connect to Remote Server

**Check 1: Network Connectivity**
```bash
ping 192.168.1.100
```

**Check 2: Port is Open**
```bash
telnet 192.168.1.100 8188
# Or
nc -zv 192.168.1.100 8188
```

**Check 3: ComfyUI is Running**
```bash
# SSH to LXC
ps aux | grep comfyui
# Or
systemctl status comfyui
```

**Check 4: Firewall Rules**
```bash
# On LXC
ufw status
iptables -L -n
```

### Connection Timeout

- Increase timeout in network settings
- Check if Proxmox firewall is blocking
- Verify LXC network mode (bridge vs NAT)

### "Server Not Found"

- Verify IP address is correct
- Try using IP instead of hostname
- Check DNS resolution: `nslookup comfyui.local`

### Blank Browser Window

- Open browser console (F12)
- Check if you can access `http://<IP>:8188` directly
- Verify CORS settings on ComfyUI server

## Performance Considerations

### Network Latency
- **LAN:** <1ms - Excellent, no noticeable delay
- **WiFi:** 5-20ms - Good, minor delay
- **VPN:** 20-100ms - Acceptable for most tasks
- **Internet:** >100ms - May feel sluggish

### Bandwidth Requirements
- **Idle:** ~1 KB/s
- **Active workflow:** 10-100 KB/s
- **Image generation:** 1-10 MB per image
- **Video preview:** 1-5 MB/s

### Optimization Tips

1. **Use Wired Connection:** Ethernet is more stable than WiFi
2. **Disable Image Preview:** Reduces bandwidth usage
3. **Local Model Storage:** Keep models on LXC, not NFS
4. **Increase LXC Resources:** More CPU/RAM = faster generation

## Security Considerations

### ⚠️ Important Security Notes

1. **Do NOT expose ComfyUI to the internet without authentication**
   - ComfyUI has no built-in authentication
   - Anyone with access can execute code on your server

2. **Use VPN for remote access:**
   ```bash
   # Instead of exposing port 8188, use WireGuard/OpenVPN
   # Connect to VPN first, then use local IP
   ```

3. **Firewall Rules:**
   ```bash
   # Only allow from specific IP
   ufw allow from 192.168.1.0/24 to any port 8188
   ```

4. **Reverse Proxy with Authentication:**
   ```nginx
   # Nginx with basic auth
   location / {
       auth_basic "ComfyUI";
       auth_basic_user_file /etc/nginx/.htpasswd;
       proxy_pass http://localhost:8188;
   }
   ```

## Advanced: Multiple Remote Servers

You can create multiple "builds" in ComfyLauncher, each pointing to different remote servers:

```json
{
  "builds": [
    {
      "id": "local",
      "name": "Local ComfyUI",
      "path": "/path/to/local/ComfyUI",
      "remote": false
    },
    {
      "id": "proxmox-gpu",
      "name": "Proxmox GPU Server",
      "path": "",
      "remote": true,
      "remote_host": "192.168.1.100",
      "remote_port": 8188
    },
    {
      "id": "proxmox-cpu",
      "name": "Proxmox CPU Server",
      "path": "",
      "remote": true,
      "remote_host": "192.168.1.101",
      "remote_port": 8188
    }
  ]
}
```

## FAQ

**Q: Can I use HTTPS?**
A: Currently only HTTP is supported. Use a reverse proxy for HTTPS.

**Q: Does remote mode work with all features?**
A: Yes, except:
- Cannot start/stop remote server (use systemd)
- Cannot access remote file system directly
- Cannot patch remote main.py

**Q: Can I switch between local and remote?**
A: Yes, just toggle `"enabled": true/false` in config.

**Q: What about model files?**
A: Models must be on the remote server. ComfyLauncher only provides the UI.

**Q: Can multiple clients connect to one server?**
A: Yes, ComfyUI supports multiple concurrent connections.

## Support

For issues specific to:
- **Proxmox:** Check Proxmox forums
- **LXC networking:** Verify bridge configuration
- **ComfyUI:** Check ComfyUI GitHub issues
- **ComfyLauncher:** Report on ComfyLauncher GitHub

## Example: Complete Proxmox LXC Setup

```bash
# 1. Create LXC container in Proxmox
#    - Template: Ubuntu 22.04
#    - RAM: 8GB+
#    - CPU: 4+ cores
#    - Disk: 50GB+
#    - Network: Bridge to vmbr0

# 2. SSH into LXC
ssh root@192.168.1.100

# 3. Install ComfyUI
apt update && apt upgrade -y
apt install -y python3 python3-pip python3-venv git
cd /opt
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI
python3 -m venv venv
source venv/bin/activate
pip install torch torchvision torchaudio
pip install -r requirements.txt

# 4. Create systemd service (see above)

# 5. Start service
systemctl start comfyui

# 6. Configure ComfyLauncher (on client)
#    Edit user_config.json:
#    "remote_server": {
#      "enabled": true,
#      "host": "192.168.1.100",
#      "port": 8188
#    }

# 7. Launch ComfyLauncher and enjoy!
```

---

**Enjoy using ComfyLauncher with your remote Proxmox LXC server! 🚀**
