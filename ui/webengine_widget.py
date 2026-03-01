from PyQt6.QtCore import pyqtSignal, QUrl
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineSettings


class WebEngineWidget(QWidget):
    """Cross-platform web browser widget using Qt WebEngine."""
    
    loaded = pyqtSignal(bool)

    def __init__(self, url: str, parent: QWidget | None = None):
        super().__init__(parent)
        self._url = url
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        self._webview = QWebEngineView(self)
        
        settings = self._webview.settings()
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebAttribute.LocalContentCanAccessRemoteUrls, True)
        
        self._webview.loadFinished.connect(self._on_load_finished)
        
        layout.addWidget(self._webview)
        
        self.navigate(url)
    
    def _on_load_finished(self, ok: bool):
        self.loaded.emit(ok)
    
    def navigate(self, url: str):
        """Navigate to the specified URL."""
        self._url = url
        self._webview.setUrl(QUrl(url))
    
    def reload(self):
        """Reload the current page."""
        self._webview.reload()
    
    def go_back(self):
        """Navigate back in history."""
        if self._webview.history().canGoBack():
            self._webview.back()
    
    def go_forward(self):
        """Navigate forward in history."""
        if self._webview.history().canGoForward():
            self._webview.forward()
    
    def shutdown(self):
        """Clean shutdown of the web engine."""
        try:
            self._webview.setUrl(QUrl("about:blank"))
        except Exception:
            pass
