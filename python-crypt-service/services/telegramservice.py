import telegram
from configurations import configuration
from configurations import keywords
from telethon import TelegramClient,events
from telethon.utils import get_display_name
from telethon.utils import *
from telethon.errors.rpc_error_list import  SessionPasswordNeededError
from models.streamdata import StreamData
from datetime import datetime
import pytz
from  services.dbservice import DBConnection
from telethon.network import ConnectionMode
from datetime import datetime, timedelta
from telethon.tl.types import (
    DocumentAttributeAudio, DocumentAttributeFilename,
    InputDocumentFileLocation, InputFileLocation,
    InputMediaUploadedDocument, InputMediaUploadedPhoto, InputPeerEmpty,
    Message, MessageMediaContact, MessageMediaDocument, MessageMediaPhoto,
    InputUserSelf, UserProfilePhoto, ChatPhoto, UpdateMessageID,
    UpdateNewChannelMessage, UpdateNewMessage, UpdateShortSentMessage,
    PeerUser, InputPeerUser, InputPeerChat, InputPeerChannel, MessageEmpty,
    ChatInvite, ChatInviteAlready, PeerChannel, Photo, InputPeerSelf,
    InputSingleMedia, InputMediaPhoto, InputPhoto, InputFile, InputFileBig,
    InputDocument, InputMediaDocument, Document, MessageEntityTextUrl,
    InputMessageEntityMentionName, DocumentAttributeVideo,
    UpdateEditMessage, UpdateEditChannelMessage, UpdateShort, Updates
)

SRC_TYPE="TWEETER"
dbconnection = DBConnection();

SEARCH_WORDS = ['buy', '#buy']


def isValidMessage(message):
  if any( x in message.lower() for x in SEARCH_WORDS):
    return True
  return False

class MainBot:
    # (1) Use your own values here
    api_id = configuration.API_ID
    api_hash = configuration.API_HASH

    phone = configuration.PHONE
    username = configuration.USERNAME

    # (2) Create the client and connect
    client = TelegramClient(username, api_id, api_hash,ConnectionMode.TCP_FULL,
                 False,
                 None,
                 1,timedelta(seconds=5),spawn_read_thread=False)

    def connect(self):
        # Getting information about yourself
        print(MainBot.client.get_me().stringify())
        MainBot.client.send_message(MainBot.username, 'Hello Shirish')

    def print(self):
        bot = telegram.Bot(token=configuration.TOKEN)
        print(bot.get_me())

    def update_handler(update_object):
      print(update_object)
      MainBot.fetchGroupIds()

    def fetchGroupIds(self):
       dialog_count = 1000
       #entities = MainBot.client.get_dialogs(dialog_count)
       entities = MainBot.client.get_dialogs(1000, None,0,InputPeerEmpty())
       for i, entity in enumerate(entities):
         i += 1  # 1-based index
         #print(entity.name)
         #print(entity.message)
         if entity.message is not None and \
         hasattr(entity.message, 'message') and \
         isValidMessage(entity.message.message):
             streamdata = StreamData();
             streamdata.data = entity.message.message
             streamdata.keyword = MainBot.fetchKeywords(entity.message.message);
             streamdata.srcType = SRC_TYPE
             streamdata.createdDate = datetime.now(pytz.timezone('Asia/Kolkata'));
             streamdata.status = "NEW"
             #dbconnection.getConnection().twittersearch.insert(streamdata.__dict__)
             print('>>>>>'+streamdata.keyword)
             print(streamdata.data)

    def fetchKeywords(message):
      for x in keywords.TELEGRAM_WORDS:
        if x in message:
          return x;
      return 'UNDEFINED'

    @client.on(events.Raw)
    def my_event_handler(event):
      print('event occured')
      mb = MainBot()
      mb.fetchGroupIds();



mb = MainBot()
#mb.print();
print('Telegram Service is running')
mb.client.start()
mb.client.idle()




# # Ensure you're authorized
#         if not MainBot.client.is_user_authorized():
#             MainBot.client.send_code_request(MainBot.phone)
#             try:
#                 MainBot.client.sign_in(MainBot.phone, input('Enter the code: '))
#             except SessionPasswordNeededError:
#                 MainBot.client.sign_in(password=input('Password: '))


# Coin name :
# Coin name
# Coin Buy counter for last hr/24hr etc
# Coin  Comments scrolling
