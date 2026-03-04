from PyQt6.QtCore import QObject, pyqtSignal
import time

from launcher import ensure_comfyui_running, is_port_open
from config import COMFYUI_PORT, MAX_WAIT_TIME, load_user_config
from utils.network_utils import is_port_listening


class ComfyLoaderWorker(QObject):
    # ── Signals ─────────────────────────────
    started = pyqtSignal()
    ready = pyqtSignal()
    timeout = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, comfy_path: str, first_launch: bool = False):
        super().__init__()
        self.comfy_path = comfy_path
        self.first_launch = first_launch
        self._running = True

    def stop(self):
        """Allows you to gently stop the worker if necessary."""
        self._running = False

    def run(self):
        """
        Main logic:
        - ComfyUI start
        - port wait
        - result signal
        """
        try:
            self.started.emit()

            cfg = load_user_config()
            remote_config = cfg.get("remote_server", {})
            remote_enabled = bool(
                remote_config.get("enabled") and remote_config.get("host")
            )
            remote_host = str(remote_config.get("host", "")).strip()
            remote_port = int(remote_config.get("port", COMFYUI_PORT))

            # 1️⃣ Launch ComfyUI (if it's already running, the function will figure it out automatically)
            ensure_comfyui_running(self.comfy_path)

            # 2️⃣ We're waiting for the server to go up.
            start_time = time.time()

            while self._running:
                if remote_enabled:
                    ready = is_port_listening(remote_port, remote_host)
                else:
                    ready = is_port_open(COMFYUI_PORT)

                if ready:
                    self.ready.emit()
                    return

                # We use timeout ONLY if this is not the first launch.
                if not self.first_launch and time.time() - start_time > MAX_WAIT_TIME:
                    self.timeout.emit()
                    return

                time.sleep(0.3)

        except Exception as e:
            self.error.emit(str(e))
