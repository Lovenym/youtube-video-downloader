from pytube import YouTube #import pytube

url = input('Введите ссылку на видео: ')

yt = YouTube(url)

print('Подождите, видео загружается...')

stream = yt.streams.get_highest_resolution()

stream.download()

print('Видео было успешно загружено!')