<div align="center">
  <a href="https://github.com/nondeletable/ComfyLauncher">
    <img src="/README/icon/256-main.png" alt="Logo" width="100" height="100">
  </a>
<h2>User Manual</h2>
Screenshots and step-by-step instructions for ComfyLauncher. <br>
This guide is available in multiple languages. You can select yours below.
  <p>
    <a href="https://github.com/nondeletable/ComfyLauncher/tree/master/README/user_manual/user_manual-en.md">English </a> |  
    <a href="https://github.com/nondeletable/ComfyLauncher/tree/master/README/user_manual/user_manual-de.md">Deutsch </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/tree/master/README/user_manual/user_manual-es.md">Español </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/tree/master/README/user_manual/user_manual-cn.md">简体中文 </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/tree/master/README/user_manual/user_manual-ru.md">Русский </a>
    <br>
    <br>
  </p>
</div>

**1. Start with exe**  
After installation, you can launch ComfyLauncher using the ".exe". You can also create a desktop or taskbar shortcut for quicker access.

![1](/README/screenshots/01_shortcut.png)
&nbsp;
&nbsp;

**2. Add and configure the ComfyUI build**  
On first launch, ComfyLauncher will ask you to select the directory that contains your portable ComfyUI. Choose the folder where `main.py` is located - that is, the root ComfyUI directory.
You can also name your build and choose an icon. These will be displayed in the Build Manager. Command-line flags are available at the bottom.

![2](/README/screenshots/17-build-settings.png)
&nbsp;
&nbsp;

**3. Build Manager**  
Add, edit, and launch your builds directly from this window. All active builds are displayed here. Additional management options are also available in **Settings**.

![3](/README/screenshots/16-build-selector.png)
&nbsp;
&nbsp;

**4. Preloader**  
ComfyUI loading screen. By default, the CMD window is disabled and won’t appear during startup. If you enable it, the terminal window will show up alongside the preloader. You can also disable the preloader in **Settings**.

![4](/README/screenshots/05-preloader.png)
&nbsp;
&nbsp;

**5. Main UI**  
The main application window. All controls are placed in the top bar. The window is frameless, so the standard Windows border doesn’t interfere with the overall visual style.

![5](/README/screenshots/06-main%20window.png)
&nbsp;
&nbsp;

**6. Left panel**
- App icon and name
- **Settings** - opens Comfy Launcher settings
- **Open ComfyUI folder** - opens the main ComfyUI directory (where "main.py", "custom_nodes", "models", etc. are located)
- **Open Output folder** - opens the "Output" folder containing generated content
- **Refresh UI** - refreshes the ComfyUI interface

![6](/README/screenshots/07-left%20corner.png)
&nbsp;
&nbsp;

**7. Right panel**
- **Status** - server state indicator (Online, Offline, Restarting)
- **Console** - opens the built-in console with CMD output (only appears when CMD is disabled in settings)
- **Restart ComfyUI** - restarts the server. If the server is stopped (Offline), this button acts as **Start** and launches it. I decided not to split these into two separate buttons and implemented both behaviors in one.
- **Stop ComfyUI** - fully stops the server
- Window controls

![7](/README/screenshots/08-right%20corner.png)
&nbsp;
&nbsp;

**8. Settings / Builds**  
This page allows you to manage your list of ComfyUI builds.
At the bottom, you'll find a link to the official website to download different ComfyUI versions.

![8](/README/screenshots/18-build%20menu.png)
&nbsp;
&nbsp;

**9. Settings / Startup**  
Manage startup behavior and display options here.
CMD Window - Toggle whether the terminal window appears when ComfyUI starts.
Splash Screen - Enable or disable the startup splash screen.

![9](/README/screenshots/19-startup%20settings.png)
&nbsp;
&nbsp;

**10. Settings / Exit Options**  
Exit Options - when closing Comfy Launcher, the app asks whether you want to stop the ComfyUI server. On this tab you can disable that dialog and choose an automatic action:
- **Always stop server** - fully stops both Comfy Launcher and ComfyUI
- **Never stop server** - closes Comfy Launcher, but keeps the ComfyUI server running in the background

![10](/README/screenshots/11-exit.png)
&nbsp;
&nbsp;

**11. Settings / Color Themes**  
Color Themes - customize Comfy Launcher appearance. Includes 4 built-in themes and support for ComfyUI themes.
- **Select** - choose a theme in JSON format
- **Download** - download themes from "www.comfyui-themes.com"

![11](/README/screenshots/12-themes.png)
&nbsp;
&nbsp;

**12. Different theme examples**

![12](/README/screenshots/13-themes.png)
&nbsp;
&nbsp;

**13. Settings / Launcher Logs**  
Launcher Logs - shows the launcher action log, primarily for debugging.

![13](/README/screenshots/14-logs.png)
&nbsp;
&nbsp;

**14. Settings / About**  
About - brief info about the app, about me, and contact links.

![14](/README/screenshots/15-about.png)
&nbsp;
&nbsp;


## ☎ Contacts

If you’d like to collaborate or discuss a job opportunity - use any of the contacts below.
For support/bugs, please use Discord or GitHub Issues. I usually reply within 24 hours.

- 🐙 **GitHub** page (docs, releases, source code)  
  https://github.com/nondeletable

- 💬 **Discord** - news, support, questions, and bug reports  
  https://discord.com/invite/6nvXwXp78u

- ✈️ **Telegram** - direct messages  
  https://t.me/nondeletable

- 📧 **Email** - for formal or business inquiries  
  nondeletable@gmail.com

- 💼 **LinkedIn** - professional profile  
  https://www.linkedin.com/in/aleksandra-gicheva-3b0264341/

- ☕ **Boosty** - support my work and projects with donations  
  https://boosty.to/codebird/donate  
&nbsp;

Thank you for using ComfyLauncher! I’ve put a lot of work into it, and I hope it makes your workflow easier and faster 🙂
