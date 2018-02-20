import telegram
from configurations import configuration
from telethon import TelegramClient
from telethon.utils import get_display_name
from telethon.utils import *
from telethon.errors.rpc_error_list import  SessionPasswordNeededError

class MainBot:
    # (1) Use your own values here
    api_id = configuration.API_ID
    api_hash = configuration.API_HASH

    phone = configuration.PHONE
    username = configuration.USERNAME

    # (2) Create the client and connect
    client = TelegramClient(username, api_id, api_hash)
    client.start()

    def connect(self):
        # Getting information about yourself
        print(MainBot.client.get_me().stringify())
        MainBot.client.send_message(MainBot.username, 'Hello Shirish')

    def print(self):
        bot = telegram.Bot(token=configuration.TOKEN)
        print(bot.get_me())

     # def fetchAllChannelsChats(self):
     #
     #   offset = 0
     #   limit = 100
     #   all_participants = []
     #
     #   while True:
     #     participants = MainBot.client(GetParticipantsRequest(
     #       channel, ChannelParticipantsSearch(''), offset, limit,
     #       hash=0
     #     ))
     #     if not participants.users:
     #       break
     #     all_participants.extend(participants.users)
     #     offset += len(participants.users)

    def fetchGroupIds(self):
       dialog_count = 1000
       entities = MainBot.client.get_dialogs(dialog_count)
       for i, entity in enumerate(entities):
         i += 1  # 1-based index
         print(entity.name)
         print(entity.message)

mb = MainBot()
#mb.print();
mb.fetchGroupIds();


# # Ensure you're authorized
#         if not MainBot.client.is_user_authorized():
#             MainBot.client.send_code_request(MainBot.phone)
#             try:
#                 MainBot.client.sign_in(MainBot.phone, input('Enter the code: '))
#             except SessionPasswordNeededError:
#                 MainBot.client.sign_in(password=input('Password: '))

