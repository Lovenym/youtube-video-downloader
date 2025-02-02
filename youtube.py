import yt_dlp

try:
       link = input('Добавьте ссылку на видео: ').strip()

       if not link:
              raise ValueError('Ссылка не может быть пустой!')
       

       ydl_opts = {
              "format": "best[ext=mp4]/best",

              "outtmpl"": "%(title)s.%(ext)s",

              "socket_timeout": 100,

              "retries": 5,

              "noplaylist": True,
       }

       with yt_dlp.YoutubeDL(ydl_opts) as ydl:
              ydl.download([link])

except ValueError as ve:
       print(f"Ошибка {ve}")
except yt_dlp.utils.DownloadError as de:
       print(f"Ошибка загрузки: {de}")
except Exception as e:
       print(f"Неизвестная ошибка: {e}")