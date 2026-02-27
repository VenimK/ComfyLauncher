<div align="center">
  <a href="https://github.com/nondeletable/ComfyLauncher">
    <img src="/README/icon/256-main.png" alt="Logo" width="100" height="100">
  </a>
<h2>Manual de Usuario</h2>
Capturas de pantalla e instrucciones paso a paso para usar ComfyLauncher. <br>
Este manual está disponible en varios idiomas. Selecciona tu idioma abajo.
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

**1. Iniciar mediante .exe**  
Después de la instalación, puedes ejecutar ComfyLauncher usando el archivo ".exe". También puedes crear un acceso directo en el escritorio o en la barra de tareas para un acceso rápido.

![1](/README/screenshots/01_shortcut.png)
&nbsp;
&nbsp;

**2. Añadir y configurar una build de ComfyUI**  
En el primer inicio, ComfyLauncher te pedirá que selecciones la carpeta que contiene tu versión portable de ComfyUI. Elige el directorio donde se encuentra `main.py` — esta es la carpeta raíz de ComfyUI.  
También puedes asignar un nombre a la build y elegir un icono. Estos se mostrarán en el gestor de builds. En la parte inferior encontrarás parámetros adicionales de línea de comandos (flags).

![2](/README/screenshots/17-build-settings.png)
&nbsp;
&nbsp;

**3. Gestor de Builds (Build Manager)**  
Aquí puedes añadir, editar y ejecutar builds directamente. Todas las builds activas se muestran en esta ventana. Opciones adicionales de gestión están disponibles en **Settings**.

![3](/README/screenshots/16-build-selector.png)
&nbsp;
&nbsp;

**4. Pantalla de carga (Preloader)**  
Pantalla de carga de ComfyUI. Por defecto, la ventana CMD está desactivada y no aparece al iniciar. Si la activas, el terminal se mostrará junto con la pantalla de carga. El Preloader también puede desactivarse en **Settings**.

![4](/README/screenshots/05-preloader.png)
&nbsp;
&nbsp;

**5. Ventana principal (Main UI)**  
La ventana principal de la aplicación. Todos los controles están ubicados en la barra superior. La ventana no tiene bordes, por lo que el marco estándar de Windows no afecta el estilo visual.

![5](/README/screenshots/06-main%20window.png)
&nbsp;
&nbsp;

**6. Panel izquierdo**
- Icono y nombre de la aplicación
- **Settings** — abre la configuración de ComfyLauncher
- **Open ComfyUI folder** — abre la carpeta raíz de ComfyUI (donde están "main.py", "custom_nodes", "models", etc.)
- **Open Output folder** — abre la carpeta "Output" con el contenido generado
- **Refresh UI** — actualiza la interfaz de ComfyUI

![6](/README/screenshots/07-left%20corner.png)
&nbsp;
&nbsp;

**7. Panel derecho**
- **Status** — indicador del estado del servidor (Online, Offline, Restarting)
- **Console** — abre la consola integrada con salida CMD (solo visible si CMD está desactivado en Settings)
- **Restart ComfyUI** — reinicia el servidor. Si el servidor está detenido (Offline), el botón funciona como **Start**. Decidí no dividirlo en dos botones separados y combinar ambos comportamientos en uno solo.
- **Stop ComfyUI** — detiene completamente el servidor
- Controles de ventana

![7](/README/screenshots/08-right%20corner.png)
&nbsp;
&nbsp;

**8. Settings / Builds**  
En esta sección puedes gestionar tus builds de ComfyUI.  
En la parte inferior hay un enlace al sitio oficial para descargar diferentes versiones de ComfyUI.

![8](/README/screenshots/18-build%20menu.png)
&nbsp;
&nbsp;

**9. Settings / Startup**  
Aquí se configura el comportamiento de inicio y las opciones de visualización.  
CMD Window — activa o desactiva el terminal al iniciar ComfyUI.  
Splash Screen — activa o desactiva la pantalla de carga.

![9](/README/screenshots/19-startup%20settings.png)
&nbsp;
&nbsp;

**10. Settings / Exit Options**  
Exit Options — al cerrar ComfyLauncher, la aplicación pregunta si deseas detener el servidor de ComfyUI. En esta sección puedes desactivar el diálogo y elegir una acción automática:
- **Always stop server** — detiene completamente tanto ComfyLauncher como ComfyUI
- **Never stop server** — cierra ComfyLauncher pero deja el servidor de ComfyUI funcionando en segundo plano

![10](/README/screenshots/11-exit.png)
&nbsp;
&nbsp;

**11. Settings / Color Themes**  
Color Themes — personalización de la apariencia de ComfyLauncher. Incluye 4 temas integrados y soporte para temas de ComfyUI.
- **Select** — seleccionar un archivo de tema en formato JSON
- **Download** — descargar temas desde "www.comfyui-themes.com"

![11](/README/screenshots/12-themes.png)
&nbsp;
&nbsp;

**12. Ejemplos de diferentes temas**

![12](/README/screenshots/13-themes.png)
&nbsp;
&nbsp;

**13. Settings / Launcher Logs**  
Launcher Logs — muestra el registro de actividades del launcher, principalmente para depuración.

![13](/README/screenshots/14-logs.png)
&nbsp;
&nbsp;

**14. Settings / About**  
About — información breve sobre la aplicación, sobre mí y enlaces de contacto.

![14](/README/screenshots/15-about.png)
&nbsp;
&nbsp;

---

## ☎ Contacto

Si deseas colaborar o discutir un proyecto, utiliza cualquiera de los contactos a continuación.  
Para soporte o reportes de errores, utiliza Discord o GitHub Issues. Normalmente respondo dentro de 24 horas.

- 🐙 **GitHub** — documentación, lanzamientos, código fuente  
  https://github.com/nondeletable

- 💬 **Discord** — novedades, soporte, preguntas y reportes de errores  
  https://discord.com/invite/6nvXwXp78u

- ✈️ **Telegram** — mensajes directos  
  https://t.me/nondeletable

- 📧 **Email** — para consultas oficiales y de negocios  
  nondeletable@gmail.com

- 💼 **LinkedIn** — perfil profesional  
  https://www.linkedin.com/in/aleksandra-gicheva-3b0264341/

- ☕ **Boosty** — apoyar el proyecto con donaciones  
  https://boosty.to/codebird/donate

---

¡Gracias por usar ComfyLauncher! He puesto mucho trabajo en este proyecto y espero que haga tu flujo de trabajo más rápido y cómodo 🙂