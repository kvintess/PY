#!/python.exe

from _token import token
from vk_api import VkApi
from vk_api import bot_longpoll

group_id = 216281614

class Bot:
    def __init__(self, group_id, token):
        self.group_id = group_id
        self.token = token
        self.vk = VkApi(token=token)
        self.long_poller = bot_longpoll.VkBotLongPoll(self.vk, self.group_id)

    def run(self):
        for event in self.long_poller.listen():
            print('Получено событие')
            # self.on_event(event)
            try:
                self.on_event(event)
            except Exception as exc:
                print(exc)

    def on_event(self, event):
# Намудрил
        f1 = (event.object.values())
        f2 = list(f1)
        f3 = f2[0]['text']
        print(f3)

# Намудрил

if __name__ == '__main__':
    bot = Bot(group_id, token)
    bot.run()
