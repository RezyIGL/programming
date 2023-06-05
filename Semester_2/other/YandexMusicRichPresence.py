from pypresence import Presence
from yandex_music import Client
import time

TOKEN = "token" # Токен Яндекс Музыки

client_id = "id" # ID бота в Discord

RPC = Presence(client_id=client_id) # Подключение RPC
RPC.connect()                       #

client = Client(TOKEN).init() # Поключение API Яндекс Музыки

while True:  
    try:
        queues = client.queues_list()
        last_queue = client.queue(queues[0].id)
        last_track_id = last_queue.get_current_track()
        last_track = last_track_id.fetch_track()
        artists = ', '.join(last_track.artists_name())
        title = last_track.title
        track_link = f"https://music.yandex.ru/album/{last_track['albums'][0]['id']}/track/{last_track['id']}/" # Получение ссылки на трек
        image_link="https://" + last_track.cover_uri.replace("%%", "1000x1000") # Обложка трека
        image_link1="link" # Можно указать ссылку на любую вашу гиф/картинку и в 35-ой строке заменить переменную image_link на image_link1
        btns = [
                { 
            "label": "Открыть на Яндекс.Музыке",
            "url": track_link
                }
        ]

        RPC.update(
            details=title, # Название трека
            state=artists, # Исполнитель трека
            large_image=image_link, # Обложка
            small_image="image",
            #large_text=title,
            large_text="",
            small_text="",
            buttons=btns
        )
    except:
        RPC.update(
            details="Моя волна",
            state="Слушаю и наслаждаюсь",
            large_image="https://dijf55il5e0d1.cloudfront.net/images/na/6/8/7/68786_1000.jpg"
        )
        
    time.sleep(1) # Обновление RPC (в секундах, стандарт = 1)
