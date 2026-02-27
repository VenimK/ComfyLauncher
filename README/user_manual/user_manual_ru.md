<div align="center">
  <a href="https://github.com/nondeletable/ComfyLauncher">
    <img src="/README/icon/256-main.png" alt="Logo" width="100" height="100">
  </a>
<h2>Руководство пользователя</h2>
Скриншоты и пошаговые инструкции по работе с ComfyLauncher. <br>
Это руководство доступно на нескольких языках. Выберите нужный ниже.
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

**1. Запуск через .exe**  
После установки вы можете запустить ComfyLauncher с помощью файла ".exe". Также можно создать ярлык на рабочем столе или в панели задач для быстрого доступа.

![1](/README/screenshots/01_shortcut.png)
&nbsp;
&nbsp;

**2. Добавление и настройка сборки ComfyUI**  
При первом запуске ComfyLauncher попросит указать папку, содержащую вашу портативную версию ComfyUI. Выберите директорию, где находится `main.py` — это корневая папка ComfyUI.  
Вы также можете задать имя сборки и выбрать иконку. Они будут отображаться в менеджере сборок. Внизу доступны параметры командной строки (flags).

![2](/README/screenshots/17-build-settings.png)
&nbsp;
&nbsp;

**3. Менеджер сборок (Build Manager)**  
Добавляйте, редактируйте и запускайте сборки прямо из этого окна. Здесь отображаются все активные сборки. Дополнительные параметры управления доступны в разделе **Settings**.

![3](/README/screenshots/16-build-selector.png)
&nbsp;
&nbsp;

**4. Экран загрузки (Preloader)**  
Экран загрузки ComfyUI. По умолчанию окно CMD отключено и не появляется при запуске. Если включить его, терминал будет отображаться вместе с экраном загрузки. Также Preloader можно отключить в разделе **Settings**.

![4](/README/screenshots/05-preloader.png)
&nbsp;
&nbsp;

**5. Главное окно (Main UI)**  
Основное окно приложения. Все элементы управления расположены в верхней панели. Окно безрамочное, поэтому стандартная рамка Windows не влияет на общий визуальный стиль.

![5](/README/screenshots/06-main%20window.png)
&nbsp;
&nbsp;

**6. Левая панель**
- Иконка и название приложения
- **Settings** — открывает настройки ComfyLauncher
- **Open ComfyUI folder** — открывает корневую папку ComfyUI (где находятся "main.py", "custom_nodes", "models" и т.д.)
- **Open Output folder** — открывает папку "Output" с сгенерированным контентом
- **Refresh UI** — обновляет интерфейс ComfyUI

![6](/README/screenshots/07-left%20corner.png)
&nbsp;
&nbsp;

**7. Правая панель**
- **Status** — индикатор состояния сервера (Online, Offline, Restarting)
- **Console** — открывает встроенную консоль с выводом CMD (появляется только если CMD отключён в настройках)
- **Restart ComfyUI** — перезапускает сервер. Если сервер остановлен (Offline), кнопка работает как **Start** и запускает его. Я решил не разделять это на две отдельные кнопки и объединил оба поведения в одной.
- **Stop ComfyUI** — полностью останавливает сервер
- Управление окном

![7](/README/screenshots/08-right%20corner.png)
&nbsp;
&nbsp;

**8. Settings / Builds**  
В этом разделе вы можете управлять списком сборок ComfyUI.  
Внизу размещена ссылка на официальный сайт для загрузки различных версий ComfyUI.

![8](/README/screenshots/18-build%20menu.png)
&nbsp;
&nbsp;

**9. Settings / Startup**  
Здесь настраивается поведение при запуске и параметры отображения.  
CMD Window — включает или отключает отображение терминала при старте ComfyUI.  
Splash Screen — включает или отключает стартовый экран загрузки.

![9](/README/screenshots/19-startup%20settings.png)
&nbsp;
&nbsp;

**10. Settings / Exit Options**  
Exit Options — при закрытии ComfyLauncher приложение спрашивает, нужно ли остановить сервер ComfyUI. В этом разделе можно отключить диалог и выбрать автоматическое действие:
- **Always stop server** — полностью останавливает и ComfyLauncher, и ComfyUI
- **Never stop server** — закрывает ComfyLauncher, но оставляет сервер ComfyUI работать в фоновом режиме

![10](/README/screenshots/11-exit.png)
&nbsp;
&nbsp;

**11. Settings / Color Themes**  
Color Themes — настройка внешнего вида ComfyLauncher. Включает 4 встроенные темы и поддержку тем ComfyUI.
- **Select** — выбор темы в формате JSON
- **Download** — загрузка тем с "www.comfyui-themes.com"

![11](/README/screenshots/12-themes.png)
&nbsp;
&nbsp;

**12. Примеры различных тем**

![12](/README/screenshots/13-themes.png)
&nbsp;
&nbsp;

**13. Settings / Launcher Logs**  
Launcher Logs — отображает журнал действий лаунчера, в основном для отладки.

![13](/README/screenshots/14-logs.png)
&nbsp;
&nbsp;

**14. Settings / About**
About — краткая информация о приложении, обо мне и ссылки для связи.

![14](/README/screenshots/15-about.png)
&nbsp;
&nbsp;


## ☎ Контакты

Если вы хотите сотрудничать или обсудить работу — используйте любой из контактов ниже.  
Для поддержки и сообщений об ошибках используйте Discord или GitHub Issues. Обычно отвечаю в течение 24 часов.

- 🐙 **GitHub** — документация, релизы, исходный код  
  https://github.com/nondeletable

- 💬 **Discord** — новости, поддержка, вопросы и баг-репорты  
  https://discord.com/invite/6nvXwXp78u

- ✈️ **Telegram** — личные сообщения  
  https://t.me/nondeletable

- 📧 **Email** — для официальных и деловых запросов  
  nondeletable@gmail.com

- 💼 **LinkedIn** — профессиональный профиль  
  https://www.linkedin.com/in/aleksandra-gicheva-3b0264341/

- ☕ **Boosty** — поддержка проекта донатами  
  https://boosty.to/codebird/donate


Спасибо, что используете ComfyLauncher! Я вложила в него много труда и надеюсь, что он сделает вашу работу быстрее и удобнее 🙂