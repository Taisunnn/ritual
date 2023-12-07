# from item_controller import ItemController
from .item_controller import ItemController
from .npc_controller import NPCController
from .room_controller import RoomController
from .system_message_controller import SystemMessageController
from ..constants.keyword_constants import ACTION_KEYWORD, MOVE_KEYWORD

class GameStateController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameStateController, cls).__new__(cls)
            cls._instance.npc_controller = NPCController()
            cls._instance.room_controller = RoomController()
            cls._instance.item_controller = ItemController()
            cls._instance.game_ongoing = True
        return cls._instance

    def get_npc_controller(self):
        return self.npc_controller

    def get_room_controller(self):
        return self.room_controller

    def get_item_controller(self):
        return self.item_controller
    
    def start(self):
        RoomController().to_start()

        while(self.game_ongoing):
            user_commands = input('Enter your move: ')
            user_commands = user_commands.strip().lower().split()

            if user_commands[0] in MOVE_KEYWORD:
                self.move(user_commands[0])
            else:
                for user_command in user_commands:
                    if user_command in ACTION_KEYWORD:
                        break 
                    elif (user_command == 'exit'):
                        self.game_ongoing = False



    def move(self, command):
        RoomController().navigate(command)