**Kudasai Discord Bot**

Este repositorio contiene un bot de Discord que publica diariamente las noticias de anime extraídas de SomosKudasai usando request y BeautifulSoup. Es un proyecto de código abierto, desarrollado por fans para fans, sin ánimo de lucro.

![image alt](https://github.com/isaiahlovescoding/kudasai-news-bot/blob/main/kudasai-bot-image.png?raw=true)

---

## 📋 Descripción

`kudasai-bot` es un bot basado en `discord.py` que:

* Extrae enlaces de noticias de anime de [https://somoskudasai.com/noticias/](https://somoskudasai.com/noticias/).
* Publica automáticamente los enlaces en un canal de Discord a una hora programada.
* Permite consultas manuales mediante comandos (por ejemplo, `!news`).

## 🚀 Características

* Extracción de noticias con `extract_news.py`.
* Tarea programada diaria para publicación automática.
* Servidor web opcional para mantener el bot despierto o disparar manualmente la publicación.
* Configuración mediante variables de entorno.

## 🛠️ Instalación

1. Clona este repositorio:

   ```bash
   git clone https://github.com/tu-usuario/kudasai-bot.git
   cd kudasai-bot
   ```

2. Crea y activa un entorno virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuración

1. Crea un archivo `.env` en la raíz del proyecto con las siguientes variables:

   ```ini
   # Token de tu bot de Discord
   DISCORD_TOKEN=tu_token_aquí

   # (Opcional) Clave de API para servicios de noticias
   NEWS_API_KEY=tu_api_key
   ```

2. Asegúrate de no subir nunca tu `.env` al repositorio. Está incluido en `.gitignore`.

## 🚴‍♂️ Uso local

Para ejecutar el bot en tu máquina:

```bash
source .venv/bin/activate
python main.py
```

El bot iniciará, mostrará en consola su hora de servidor y comenzará a escuchar Discord.

## ☁️ Despliegue en Render

1. Crea un servicio **Web** (solo si necesitas un ping externo) y/o un servicio **Worker** para el bot.
2. Define en el panel de Render las variables de entorno (`DISCORD_TOKEN`, etc.).
3. Usa `python main.py` como comando de inicio del worker.

Render instalará automáticamente las dependencias desde `requirements.txt`.

## 🤝 Contribuciones

Las aportaciones son bienvenidas. Si quieres colaborar:

1. Haz un fork.
2. Crea una rama para tu feature: `git checkout -b feature/nombre`
3. Haz tus cambios y commitea: `git commit -m "Añade nueva característica"`
4. Envía un Pull Request.

## 📜 Licencia

No tiene de fans para fans, puedes hacer lo que quieras (legalmente)

---

## ⚠️ Aviso Legal / Disclaimer

Este bot y su código son **un proyecto fan-made**, desarrollado únicamente con fines educativos y de entretenimiento, sin ánimo de lucro. No estamos afiliados, respaldados ni patrocinados por **SomosKudasai** o ninguna otra entidad. Todos los contenidos enlazados (noticias, imágenes, textos) son propiedad de sus respectivos autores y sitios web de origen.

![image alt](https://github.com/isaiahlovescoding/kudasai-news-bot/blob/main/kudasai.jpg?raw=true)


Siempre respeta los términos de uso de *SomosKudasai* y utiliza este bot de manera responsable y ética.


