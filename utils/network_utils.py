import socket
import psutil
import requests
from utils.logger import log_event


def get_server_url(port: int = 8188, remote_host: str = None) -> str:
    """
    Determines the correct URL to connect to ComfyUI server.
    Handles cases where server binds to 0.0.0.0, ::, or 127.0.0.1
    Also supports remote servers.
    
    Args:
        port: Port number (default 8188)
        remote_host: Remote host IP/hostname (e.g., "192.168.1.100" or "comfyui.local")
    
    Returns the best URL to use for connecting.
    """
    # If remote host is specified, use it directly
    if remote_host:
        # Clean up the host (remove http://, trailing slashes, etc.)
        host = remote_host.strip()
        if host.startswith("http://"):
            host = host[7:]
        if host.startswith("https://"):
            host = host[8:]
        host = host.rstrip("/")
        
        # Remove port if included in host
        if ":" in host and not host.startswith("["):  # Not IPv6
            host = host.split(":")[0]
        
        url = f"http://{host}:{port}"
        log_event(f"🌐 Using remote server: {url}")
        return url
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


def is_port_listening(port: int, host: str = "127.0.0.1") -> bool:
    """
    Checks if any process is listening on the specified port.
    More reliable than socket connection test.
    
    Args:
        port: Port number to check
        host: Host to check (default localhost)
    """
    # For localhost, check psutil first
    if host in ("127.0.0.1", "localhost"):
        try:
            for conn in psutil.net_connections(kind='inet'):
                if conn.laddr and conn.laddr.port == port:
                    if conn.status == psutil.CONN_LISTEN:
                        return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass
    
    # Socket test (works for both local and remote)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1.0)  # Longer timeout for remote connections
        try:
            return s.connect_ex((host, port)) == 0
        except socket.gaierror:
            return False


def validate_remote_server(url: str) -> tuple[bool, str]:
    """
    Validates that a remote ComfyUI server is accessible.
    
    Args:
        url: Full URL to test (e.g., "http://192.168.1.100:8188")
    
    Returns:
        (is_valid, message) tuple
    """
    try:
        # Try to connect to the server
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True, "✅ Remote server is accessible"
        else:
            return False, f"⚠️ Server responded with status {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "❌ Cannot connect to server. Check IP/hostname and port."
    except requests.exceptions.Timeout:
        return False, "❌ Connection timeout. Server may be slow or unreachable."
    except Exception as e:
        return False, f"❌ Error: {str(e)}"
