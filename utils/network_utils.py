import socket
import psutil
from utils.logger import log_event


def get_server_url(port: int = 8188) -> str:
    """
    Determines the correct URL to connect to ComfyUI server.
    Handles cases where server binds to 0.0.0.0, ::, or 127.0.0.1
    
    Returns the best URL to use for connecting.
    """
    # First, try to detect what interface the server is bound to
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr and conn.laddr.port == port:
                if conn.status == psutil.CONN_LISTEN:
                    bind_ip = conn.laddr.ip
                    
                    # If bound to 0.0.0.0 or ::, use localhost
                    if bind_ip in ('0.0.0.0', '::', '::1'):
                        log_event(f"ℹ️ Server bound to {bind_ip}, connecting via localhost")
                        return f"http://127.0.0.1:{port}"
                    
                    # If bound to specific IP, use that
                    log_event(f"ℹ️ Server bound to {bind_ip}")
                    return f"http://{bind_ip}:{port}"
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass
    
    # Default: use localhost
    return f"http://127.0.0.1:{port}"


def is_port_listening(port: int) -> bool:
    """
    Checks if any process is listening on the specified port.
    More reliable than socket connection test.
    """
    try:
        for conn in psutil.net_connections(kind='inet'):
            if conn.laddr and conn.laddr.port == port:
                if conn.status == psutil.CONN_LISTEN:
                    return True
    except (psutil.AccessDenied, psutil.NoSuchProcess):
        pass
    
    # Fallback to socket test
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.2)
        return s.connect_ex(("127.0.0.1", port)) == 0
