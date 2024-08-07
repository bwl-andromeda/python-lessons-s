from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from vk_api import VkApi
from config import TOKEN

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
                if responce == "Привет":
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "И тебе привет!",
                            "random_id": 0,
                        },
                    )
