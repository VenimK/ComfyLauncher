"""
Resource monitoring utilities for ComfyLauncher.
Tracks memory, CPU usage, and provides optimization recommendations.
"""

import psutil
import os
from typing import Dict, Optional
from utils.logger import log_event


class ResourceMonitor:
    """Monitor and report resource usage"""
    
    def __init__(self):
        self.process = psutil.Process(os.getpid())
        self._baseline_memory = None
        
    def get_memory_usage(self) -> Dict[str, float]:
        """
        Get current memory usage.
        
        Returns:
            dict with 'rss' (resident set size) and 'vms' (virtual memory size) in MB
        """
        mem_info = self.process.memory_info()
        return {
            'rss_mb': mem_info.rss / 1024 / 1024,  # Resident Set Size
            'vms_mb': mem_info.vms / 1024 / 1024,  # Virtual Memory Size
            'percent': self.process.memory_percent()
        }
    
    def get_cpu_usage(self, interval: float = 0.1) -> float:
        """
        Get CPU usage percentage.
        
        Args:
            interval: Measurement interval in seconds
            
        Returns:
            CPU usage percentage
        """
        return self.process.cpu_percent(interval=interval)
    
    def get_thread_count(self) -> int:
        """Get number of threads"""
        return self.process.num_threads()
    
    def get_open_files_count(self) -> int:
        """Get number of open file descriptors"""
        try:
            return len(self.process.open_files())
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            return 0
    
    def set_baseline(self):
        """Set baseline memory usage for comparison"""
        self._baseline_memory = self.get_memory_usage()['rss_mb']
    
    def get_memory_delta(self) -> Optional[float]:
        """Get memory usage change from baseline in MB"""
        if self._baseline_memory is None:
            return None
        current = self.get_memory_usage()['rss_mb']
        return current - self._baseline_memory
    
    def get_full_report(self) -> Dict:
        """Get comprehensive resource usage report"""
        mem = self.get_memory_usage()
        cpu = self.get_cpu_usage()
        
        return {
            'memory': mem,
            'cpu_percent': cpu,
            'threads': self.get_thread_count(),
            'open_files': self.get_open_files_count(),
            'memory_delta_mb': self.get_memory_delta()
        }
    
    def log_usage(self, prefix: str = ""):
        """Log current resource usage"""
        report = self.get_full_report()
        mem = report['memory']
        
        msg = f"{prefix}Memory: {mem['rss_mb']:.1f}MB ({mem['percent']:.1f}%), "
        msg += f"CPU: {report['cpu_percent']:.1f}%, "
        msg += f"Threads: {report['threads']}"
        
        if report['memory_delta_mb'] is not None:
            msg += f", Delta: {report['memory_delta_mb']:+.1f}MB"
        
        log_event(f"📊 {msg}")
    
    def check_memory_threshold(self, threshold_mb: float = 500) -> bool:
        """
        Check if memory usage exceeds threshold.
        
        Args:
            threshold_mb: Memory threshold in MB
            
        Returns:
            True if over threshold
        """
        mem = self.get_memory_usage()['rss_mb']
        return mem > threshold_mb
    
    def get_optimization_suggestions(self) -> list[str]:
        """Get optimization suggestions based on current usage"""
        suggestions = []
        report = self.get_full_report()
        
        mem_mb = report['memory']['rss_mb']
        cpu = report['cpu_percent']
        threads = report['threads']
        
        # Memory suggestions
        if mem_mb > 500:
            suggestions.append("High memory usage (>500MB). Consider:")
            suggestions.append("  - Clear browser cache")
            suggestions.append("  - Reduce console buffer size")
            suggestions.append("  - Close unused builds")
        
        if mem_mb > 300:
            suggestions.append("Memory usage elevated. Enable 'Show CMD' to reduce internal buffering")
        
        # CPU suggestions
        if cpu > 20:
            suggestions.append("High CPU usage. Consider:")
            suggestions.append("  - Increase server check interval")
            suggestions.append("  - Disable auto-refresh features")
        
        # Thread suggestions
        if threads > 20:
            suggestions.append(f"Many threads ({threads}). Check for resource leaks")
        
        return suggestions


# Global instance
_monitor = None

def get_monitor() -> ResourceMonitor:
    """Get global resource monitor instance"""
    global _monitor
    if _monitor is None:
        _monitor = ResourceMonitor()
    return _monitor


def log_resource_usage(prefix: str = ""):
    """Convenience function to log resource usage"""
    get_monitor().log_usage(prefix)


def optimize_for_low_memory():
    """Apply optimizations for low-memory systems"""
    from utils.console_buffer import ConsoleBuffer
    
    suggestions = [
        "Low memory mode activated:",
        "  - Console buffer: 500 lines (default: 1000)",
        "  - Reduced polling frequency",
        "  - Disabled video splash screen"
    ]
    
    for s in suggestions:
        log_event(f"⚡ {s}")
