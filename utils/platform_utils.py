import sys
import os
import subprocess
import platform


def get_platform():
    """Returns the current platform: 'windows', 'darwin', or 'linux'."""
    return sys.platform


def is_windows():
    return sys.platform == "win32"


def is_macos():
    return sys.platform == "darwin"


def is_linux():
    return sys.platform.startswith("linux")


def open_file_manager(path: str):
    """Opens the file manager at the specified path in a cross-platform way."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path does not exist: {path}")
    
    if is_windows():
        os.startfile(path)
    elif is_macos():
        subprocess.run(["open", path], check=False)
    elif is_linux():
        subprocess.run(["xdg-open", path], check=False)
    else:
        raise NotImplementedError(f"Unsupported platform: {sys.platform}")


def get_python_executable_name():
    """Returns the platform-specific Python executable name."""
    if is_windows():
        return "python.exe"
    else:
        return "python3"


def get_embedded_python_paths(base_dir: str):
    """
    Returns possible paths for embedded Python in portable builds.
    Returns a list of candidates to check.
    """
    candidates = []
    
    if is_windows():
        candidates.extend([
            os.path.join(base_dir, "python_embeded", "python.exe"),
            os.path.join(base_dir, "python_embedded", "python.exe"),
        ])
    elif is_macos():
        candidates.extend([
            os.path.join(base_dir, "python_embeded", "bin", "python3"),
            os.path.join(base_dir, "python_embedded", "bin", "python3"),
            os.path.join(base_dir, ".venv", "bin", "python3"),
            os.path.join(base_dir, "venv", "bin", "python3"),
        ])
    elif is_linux():
        candidates.extend([
            os.path.join(base_dir, "python_embeded", "bin", "python3"),
            os.path.join(base_dir, "python_embedded", "bin", "python3"),
            os.path.join(base_dir, ".venv", "bin", "python3"),
            os.path.join(base_dir, "venv", "bin", "python3"),
        ])
    
    return candidates


def get_startup_script_names():
    """Returns platform-specific startup script names to look for."""
    if is_windows():
        return ["run_nvidia_gpu.bat", "run_cpu.bat", "run_nvidia_gpu_fast_fp16.bat"]
    elif is_macos():
        return ["run_nvidia_gpu.sh", "run_cpu.sh", "run.sh", "start.sh"]
    elif is_linux():
        return ["run_nvidia_gpu.sh", "run_cpu.sh", "run.sh", "start.sh"]
    else:
        return []


def get_shell_command():
    """Returns the shell command for the current platform."""
    if is_windows():
        return ["cmd.exe", "/k"]
    else:
        return ["/bin/bash", "-c"]


def get_no_window_flag():
    """Returns subprocess creation flags for hiding console window."""
    if is_windows():
        return subprocess.CREATE_NO_WINDOW
    else:
        return 0


def get_new_console_flag():
    """Returns subprocess creation flags for new console window."""
    if is_windows():
        return subprocess.CREATE_NEW_CONSOLE
    else:
        return 0


def get_user_data_dir(app_name: str = "ComfyLauncher"):
    """Returns the platform-specific user data directory."""
    if is_windows():
        base = os.environ.get("LOCALAPPDATA") or os.path.join(os.path.expanduser("~"), "AppData", "Local")
    elif is_macos():
        base = os.path.join(os.path.expanduser("~"), "Library", "Application Support")
    elif is_linux():
        base = os.environ.get("XDG_DATA_HOME") or os.path.join(os.path.expanduser("~"), ".local", "share")
    else:
        base = os.path.expanduser("~")
    
    return os.path.join(base, app_name)


def get_log_dir(app_name: str = "ComfyLauncher"):
    """Returns the platform-specific log directory."""
    if is_windows():
        base = os.getenv("APPDATA") or os.getenv("LOCALAPPDATA") or os.path.expanduser("~")
    elif is_macos():
        base = os.path.join(os.path.expanduser("~"), "Library", "Logs")
    elif is_linux():
        base = os.environ.get("XDG_STATE_HOME") or os.path.join(os.path.expanduser("~"), ".local", "state")
    else:
        base = os.path.expanduser("~")
    
    log_dir = os.path.join(base, app_name, "logs")
    os.makedirs(log_dir, exist_ok=True)
    return log_dir
