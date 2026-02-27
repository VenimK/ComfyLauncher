<div align="center">
  <a href="https://github.com/nondeletable/ComfyLauncher">
    <img src="/README/icon/256-main.png" alt="Logo" width="100" height="100">
  </a>
<h2>用户手册</h2>
ComfyLauncher 的截图和分步使用说明。<br>
本手册提供多种语言版本。请在下方选择你的语言。
  <p>
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual_en.md">English </a> |  
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual_de.md">Deutsch </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual_es.md">Español </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual_cn.md">简体中文 </a> |
    <a href="https://github.com/nondeletable/ComfyLauncher/blob/master/README/user_manual/user_manual_ru.md">Русский </a>
    <br>
    <br>
  </p>
</div>

**1. 通过 .exe 启动**  
安装完成后，你可以通过 “.exe” 文件启动 ComfyLauncher。你也可以创建桌面或任务栏快捷方式以便快速访问。

![1](/README/screenshots/01_shortcut.png)
&nbsp;
&nbsp;

**2. 添加并配置 ComfyUI 构建版本**  
首次启动时，ComfyLauncher 会提示你选择包含便携版 ComfyUI 的文件夹。请选择包含 `main.py` 的目录——这是 ComfyUI 的根目录。  
你还可以为该构建设置名称并选择图标。它们会显示在构建管理器中。底部提供额外的命令行参数（flags）。

![2](/README/screenshots/17-build-settings.png)
&nbsp;
&nbsp;

**3. 构建管理器（Build Manager）**  
你可以在此添加、编辑和启动构建版本。所有已添加的构建都会显示在此窗口中。更多管理选项可在 **Settings** 中找到。

![3](/README/screenshots/16-build-selector.png)
&nbsp;
&nbsp;

**4. 加载界面（Preloader）**  
ComfyUI 的加载界面。默认情况下，CMD 窗口被禁用，启动时不会显示。如果启用，终端窗口将与加载界面同时显示。你也可以在 **Settings** 中关闭 Preloader。

![4](/README/screenshots/05-preloader.png)
&nbsp;
&nbsp;

**5. 主界面（Main UI）**  
应用程序的主窗口。所有控制按钮位于顶部栏。窗口为无边框设计，因此不会受到 Windows 默认边框样式的影响。

![5](/README/screenshots/06-main%20window.png)
&nbsp;
&nbsp;

**6. 左侧面板**
- 应用图标和名称
- **Settings** — 打开 ComfyLauncher 设置
- **Open ComfyUI folder** — 打开 ComfyUI 根目录（包含 "main.py"、"custom_nodes"、"models" 等）
- **Open Output folder** — 打开包含生成内容的 “Output” 文件夹
- **Refresh UI** — 刷新 ComfyUI 界面

![6](/README/screenshots/07-left%20corner.png)
&nbsp;
&nbsp;

**7. 右侧面板**
- **Status** — 服务器状态指示（Online、Offline、Restarting）
- **Console** — 打开内置控制台（显示 CMD 输出，仅在 Settings 中禁用 CMD 时可见）
- **Restart ComfyUI** — 重启服务器。如果服务器处于停止状态（Offline），按钮将作为 **Start** 使用。我将两种功能合并为一个按钮，而不是分成两个独立按钮。
- **Stop ComfyUI** — 完全停止服务器
- 窗口控制按钮

![7](/README/screenshots/08-right%20corner.png)
&nbsp;
&nbsp;

**8. Settings / Builds**  
在此部分你可以管理 ComfyUI 构建版本。  
底部提供官方链接，可下载不同版本的 ComfyUI。

![8](/README/screenshots/18-build%20menu.png)
&nbsp;
&nbsp;

**9. Settings / Startup**  
此处可配置启动行为和显示选项。  
CMD Window — 启用或禁用启动 ComfyUI 时显示终端窗口。  
Splash Screen — 启用或禁用加载启动界面。

![9](/README/screenshots/19-startup%20settings.png)
&nbsp;
&nbsp;

**10. Settings / Exit Options**  
Exit Options — 关闭 ComfyLauncher 时，应用会询问是否停止 ComfyUI 服务器。在此可以关闭该对话框并设置自动操作：
- **Always stop server** — 完全关闭 ComfyLauncher 和 ComfyUI
- **Never stop server** — 关闭 ComfyLauncher，但让 ComfyUI 服务器在后台继续运行

![10](/README/screenshots/11-exit.png)
&nbsp;
&nbsp;

**11. Settings / Color Themes**  
Color Themes — 自定义 ComfyLauncher 的界面外观。包含 4 个内置主题，并支持 ComfyUI 主题。
- **Select** — 选择 JSON 格式主题文件
- **Download** — 从 “www.comfyui-themes.com” 下载主题

![11](/README/screenshots/12-themes.png)
&nbsp;
&nbsp;

**12. 不同主题示例**

![12](/README/screenshots/13-themes.png)
&nbsp;
&nbsp;

**13. Settings / Launcher Logs**  
Launcher Logs — 显示启动器的操作日志，主要用于调试。

![13](/README/screenshots/14-logs.png)
&nbsp;
&nbsp;

**14. Settings / About**  
About — 关于应用程序、作者信息及联系方式。

![14](/README/screenshots/15-about.png)
&nbsp;
&nbsp;


## ☎ 联系方式

如果你希望合作或讨论项目，请使用以下任意联系方式。  
如需支持或报告错误，请使用 Discord 或 GitHub Issues。通常会在 24 小时内回复。

- 🐙 **GitHub** — 文档、发布版本、源代码  
  https://github.com/nondeletable

- 💬 **Discord** — 更新、支持、问题与错误报告  
  https://discord.com/invite/6nvXwXp78u

- ✈️ **Telegram** — 私信联系  
  https://t.me/nondeletable

- 📧 **Email** — 官方及商务咨询  
  nondeletable@gmail.com

- 💼 **LinkedIn** — 专业资料  
  https://www.linkedin.com/in/aleksandra-gicheva-3b0264341/

- ☕ **Boosty** — 通过捐赠支持项目  
  https://boosty.to/codebird/donate


感谢你使用 ComfyLauncher！我为这个项目投入了大量精力，希望它能让你的工作流程更加高效、便捷 🙂