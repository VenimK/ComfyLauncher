<div align="center">
  <a href="https://github.com/nondeletable/ComfyLauncher">
    <img src="/README/icon/256-main.png" alt="Logo" width="100" height="100">
  </a>
<h2>Benutzerhandbuch</h2>
Screenshots und Schritt-für-Schritt-Anleitung zur Nutzung von ComfyLauncher. <br>
Dieses Handbuch ist in mehreren Sprachen verfügbar. Wähle unten deine Sprache aus.
  <p>
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual-en.md">English </a> |  
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual-de.md">Deutsch </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual-es.md">Español </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual-cn.md">简体中文 </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual-ru.md">Русский </a>
    <br>
    <br>
  </p>
</div>

**1. Start über .exe**  
Nach der Installation kannst du ComfyLauncher über die ".exe"-Datei starten. Du kannst außerdem eine Desktop- oder Taskleisten-Verknüpfung für schnellen Zugriff erstellen.

![1](/README/screenshots/01_shortcut.png)
&nbsp;
&nbsp;

**2. ComfyUI-Build hinzufügen und konfigurieren**  
Beim ersten Start fordert ComfyLauncher dich auf, den Ordner deiner portablen ComfyUI-Version auszuwählen. Wähle das Verzeichnis, in dem sich `main.py` befindet – das ist das Stammverzeichnis von ComfyUI.  
Du kannst dem Build außerdem einen Namen geben und ein Icon auswählen. Diese werden im Build-Manager angezeigt. Unten stehen zusätzliche Kommandozeilen-Parameter (Flags) zur Verfügung.

![2](/README/screenshots/17-build-settings.png)
&nbsp;
&nbsp;

**3. Build-Manager**  
Hier kannst du Builds hinzufügen, bearbeiten und direkt starten. Alle aktiven Builds werden in diesem Fenster angezeigt. Weitere Verwaltungsoptionen findest du unter **Settings**.

![3](/README/screenshots/16-build-selector.png)
&nbsp;
&nbsp;

**4. Ladebildschirm (Preloader)**  
Der Ladebildschirm von ComfyUI. Standardmäßig ist das CMD-Fenster deaktiviert und erscheint beim Start nicht. Wenn aktiviert, wird das Terminal zusammen mit dem Ladebildschirm angezeigt. Der Preloader kann ebenfalls in den **Settings** deaktiviert werden.

![4](/README/screenshots/05-preloader.png)
&nbsp;
&nbsp;

**5. Hauptfenster (Main UI)**  
Das Hauptfenster der Anwendung. Alle Steuerungselemente befinden sich in der oberen Leiste. Das Fenster ist rahmenlos, sodass der Standard-Windows-Rahmen das visuelle Design nicht beeinflusst.

![5](/README/screenshots/06-main%20window.png)
&nbsp;
&nbsp;

**6. Linke Leiste**
- App-Icon und Name
- **Settings** — öffnet die ComfyLauncher-Einstellungen
- **Open ComfyUI folder** — öffnet den ComfyUI-Stammordner (mit "main.py", "custom_nodes", "models" usw.)
- **Open Output folder** — öffnet den Ordner "Output" mit generierten Inhalten
- **Refresh UI** — aktualisiert die ComfyUI-Oberfläche

![6](/README/screenshots/07-left%20corner.png)
&nbsp;
&nbsp;

**7. Rechte Leiste**
- **Status** — Serverstatus-Anzeige (Online, Offline, Restarting)
- **Console** — öffnet die integrierte Konsole mit CMD-Ausgabe (nur sichtbar, wenn CMD in den Einstellungen deaktiviert ist)
- **Restart ComfyUI** — startet den Server neu. Wenn der Server gestoppt ist (Offline), funktioniert die Schaltfläche als **Start**. Ich habe bewusst keine zwei separaten Buttons erstellt, sondern beide Funktionen kombiniert.
- **Stop ComfyUI** — stoppt den Server vollständig
- Fenstersteuerung

![7](/README/screenshots/08-right%20corner.png)
&nbsp;
&nbsp;

**8. Settings / Builds**  
In diesem Bereich kannst du deine ComfyUI-Builds verwalten.  
Unten befindet sich ein Link zur offiziellen Website, um verschiedene ComfyUI-Versionen herunterzuladen.

![8](/README/screenshots/18-build%20menu.png)
&nbsp;
&nbsp;

**9. Settings / Startup**  
Hier wird das Startverhalten und die Anzeige konfiguriert.  
CMD Window — aktiviert oder deaktiviert das Terminal beim Start von ComfyUI.  
Splash Screen — aktiviert oder deaktiviert den Ladebildschirm.

![9](/README/screenshots/19-startup%20settings.png)
&nbsp;
&nbsp;

**10. Settings / Exit Options**  
Exit Options — Beim Schließen von ComfyLauncher fragt die Anwendung, ob der ComfyUI-Server gestoppt werden soll. In diesem Abschnitt kannst du den Dialog deaktivieren und eine automatische Aktion festlegen:
- **Always stop server** — beendet sowohl ComfyLauncher als auch ComfyUI vollständig
- **Never stop server** — schließt ComfyLauncher, lässt den ComfyUI-Server jedoch im Hintergrund weiterlaufen

![10](/README/screenshots/11-exit.png)
&nbsp;
&nbsp;

**11. Settings / Color Themes**  
Color Themes — Anpassung des Erscheinungsbilds von ComfyLauncher. Enthält 4 integrierte Themes sowie Unterstützung für ComfyUI-Themes.
- **Select** — Auswahl eines JSON-Theme-Files
- **Download** — Themes herunterladen von "www.comfyui-themes.com"

![11](/README/screenshots/12-themes.png)
&nbsp;
&nbsp;

**12. Beispiele verschiedener Themes**

![12](/README/screenshots/13-themes.png)
&nbsp;
&nbsp;

**13. Settings / Launcher Logs**
Launcher Logs — zeigt das Protokoll der Launcher-Aktivitäten an, hauptsächlich für Debugging-Zwecke.

![13](/README/screenshots/14-logs.png)
&nbsp;
&nbsp;

**14. Settings / About**
About — kurze Informationen über die Anwendung, über mich und Kontaktlinks.

![14](/README/screenshots/15-about.png)
&nbsp;
&nbsp;


## ☎ Kontakt

Wenn du zusammenarbeiten oder ein Projekt besprechen möchtest, nutze einen der folgenden Kontakte.  
Für Support oder Bug-Reports verwende bitte Discord oder GitHub Issues. Ich antworte in der Regel innerhalb von 24 Stunden.

- 🐙 **GitHub** — Dokumentation, Releases, Quellcode  
  https://github.com/nondeletable

- 💬 **Discord** — Updates, Support, Fragen und Bug-Reports  
  https://discord.com/invite/6nvXwXp78u

- ✈️ **Telegram** — Direktnachrichten  
  https://t.me/nondeletable

- 📧 **Email** — für offizielle und geschäftliche Anfragen  
  nondeletable@gmail.com

- 💼 **LinkedIn** — berufliches Profil  
  https://www.linkedin.com/in/aleksandra-gicheva-3b0264341/

- ☕ **Boosty** — Projekt durch Spenden unterstützen  
  https://boosty.to/codebird/donate


Danke, dass du ComfyLauncher verwendest! Ich habe viel Arbeit hineingesteckt und hoffe, dass es deinen Workflow schneller und komfortabler macht 🙂