import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from vk_api import VkApi
from config import TOKEN
from messages import hello_list, files_list, fantastic_list, multfilm_list

session = VkApi(token=TOKEN)
session_api = session.get_api()
longpoll = VkLongPoll(session)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print(f"Сообщение пришло в: {str(datetime.now())}")
            print(f"Текст сообщения: {str(event.text)}")
            responce = event.text.lower()
            if event.from_user and not event.from_me:
                if responce.find("привет") >= 0 or responce.find("здраствуй") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": random.choice(hello_list),
                            "random_id": 0,
                        },
                    )
                elif responce.find("как дела") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "sticker_id": 60943,
                            "random_id": 0,
                        },
                    )
                elif responce.find("аватарка") >= 0 or responce.find("ава") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": "audio-2001720502_8720502",
                            "random_id": 0,
                        },
                    )
                elif responce.find("мне грустно") >= 0 or responce.find("грустно") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "sticker_id": 63,
                            "random_id": 0,
                        },
                    )
                elif responce.find("файл") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": f"photo{random.choice(files_list)}",
                            "random_id": 0,
                        },
                    )
                elif responce.find("фильм") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "Выбери жанр фильма:\n1) Фантастика\n2) Мультфильм.\n Вводить нужно цифру.",
                            "random_id": 0,
                        },
                    )
                elif responce.find("1") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": random.choice(fantastic_list),
                            "random_id": 0,
                        },
                    )
                elif responce.find("2") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": random.choice(multfilm_list),
                            "random_id": 0,
                        },
                    )
