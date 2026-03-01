import os
from datetime import datetime
from utils.platform_utils import get_log_dir


LOG_DIR = get_log_dir("ComfyLauncher")
LOG_FILE = os.path.join(LOG_DIR, "launcher.log")


def log_event(message: str):
    """Writes an event to the console and log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print(formatted)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(formatted + "\n")
    except Exception as e:
        print(f"[LOGGER ERROR] {e}")
