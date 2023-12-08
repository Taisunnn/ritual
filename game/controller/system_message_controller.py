import json
import os

class SystemMessageController:
    def __init__(self):
        f=open(os.getcwd() + '/data/system_message.json')
        messageData = json.load(f)
        # for message in messageData['messages']:
        #     print(message)
        # print('SystemMessageController Ready')
