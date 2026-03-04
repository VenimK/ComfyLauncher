#!/usr/bin/env python3
"""
Quick configuration script for remote ComfyUI server.
Run this before launching ComfyLauncher for the first time with a remote server.
"""

import os
import json
import sys

# Determine config path based on platform
if sys.platform == "darwin":
    config_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "ComfyLauncher")
elif sys.platform == "win32":
    config_dir = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")), "ComfyLauncher")
else:
    config_dir = os.path.join(os.path.expanduser("~"), ".local", "share", "ComfyLauncher")

os.makedirs(config_dir, exist_ok=True)
config_path = os.path.join(config_dir, "user_config.json")

print("🌐 ComfyLauncher Remote Server Configuration")
print("=" * 50)
print()

# Get user input
remote_host = input("Enter remote server IP or hostname (e.g., 192.168.1.100): ").strip()
if not remote_host:
    print("❌ Host cannot be empty!")
    sys.exit(1)

remote_port = input("Enter port (default 8188): ").strip()
if not remote_port:
    remote_port = "8188"

try:
    remote_port = int(remote_port)
except ValueError:
    print("❌ Invalid port number!")
    sys.exit(1)

# Test connection
print()
print(f"🔍 Testing connection to {remote_host}:{remote_port}...")

import socket
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)
    result = sock.connect_ex((remote_host, remote_port))
    sock.close()
    
    if result == 0:
        print(f"✅ Successfully connected to {remote_host}:{remote_port}")
    else:
        print(f"⚠️  Cannot connect to {remote_host}:{remote_port}")
        print("   Make sure ComfyUI is running with --listen 0.0.0.0")
        proceed = input("   Continue anyway? (y/n): ").strip().lower()
        if proceed != 'y':
            sys.exit(1)
except Exception as e:
    print(f"⚠️  Connection test failed: {e}")
    proceed = input("   Continue anyway? (y/n): ").strip().lower()
    if proceed != 'y':
        sys.exit(1)

# Load or create config
if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as f:
        config = json.load(f)
    print()
    print("📝 Existing configuration found, updating...")
else:
    config = {
        "ask_on_exit": True,
        "exit_mode": "always_stop",
        "browser_patch_registry": {},
        "builds": [],
        "last_used_build_id": "",
        "startup_mode": "cpu",
        "ui": {
            "show_manager_on_start": True,
        },
        "update_etag": None,
        "last_update_check": None,
        "update_interval_hours": 48,
        "updates_enabled": True,
    }
    print()
    print("📝 Creating new configuration...")

# Update remote server config
config["remote_server"] = {
    "enabled": True,
    "host": remote_host,
    "port": remote_port,
}

# Create a dummy build entry for remote server
remote_build = {
    "id": "remote_server",
    "name": f"Remote: {remote_host}:{remote_port}",
    "path": "",  # Empty path for remote
    "startup_mode": "auto",
}

# Add or update remote build
builds = config.get("builds", [])
remote_exists = False
for i, build in enumerate(builds):
    if build.get("id") == "remote_server":
        builds[i] = remote_build
        remote_exists = True
        break

if not remote_exists:
    builds.append(remote_build)

config["builds"] = builds
config["last_used_build_id"] = "remote_server"
config["comfyui_path"] = ""  # No local path needed

# Save config
with open(config_path, 'w', encoding='utf-8') as f:
    json.dump(config, f, indent=2, ensure_ascii=False)

print()
print("✅ Configuration saved!")
print()
print(f"📁 Config file: {config_path}")
print()
print("Configuration:")
print(f"  Remote Host: {remote_host}")
print(f"  Remote Port: {remote_port}")
print(f"  Enabled: Yes")
print()
print("🚀 You can now run ComfyLauncher:")
print("   ./run_macos.sh")
print()
print("   or")
print()
print("   source venv/bin/activate")
print("   python main.py")
print()
