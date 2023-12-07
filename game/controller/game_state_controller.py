# from item_controller import ItemController
from .item_controller import ItemController
from .npc_controller import NPCController
from .room_controller import RoomController
from .game_object_controller import GameObjectController
from .system_message_controller import SystemMessageController
from ..constants.keyword_constants import ACTION_KEYWORD, MOVE_KEYWORD

class GameStateController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameStateController, cls).__new__(cls)
            # cls._instance.npc_controller = NPCController()
            # cls._instance.room_controller = RoomController()
            # cls._instance.item_controller = ItemController()
            cls._instance.game_object_controller = GameObjectController()
            cls._instance.game_ongoing = True
            cls._instance.current_locaiton = 1
        return cls._instance

    def get_npc_controller(self):
        return self.npc_controller

    def get_room_controller(self):
        return self.room_controller

    def get_item_controller(self):
        return self.item_controller
    
    def start(self):
        # RoomController().to_start()
        GameObjectController().load_room_id(self.current_locaiton)

        while(self.game_ongoing):
            user_commands = input('\tWhat do you do? : ')
            user_commands = user_commands.strip().lower().split()

            if user_commands[0] in MOVE_KEYWORD:
                self.move(user_commands[0])
            else:
                for user_command in user_commands:
                    if user_command in ACTION_KEYWORD:
                        user_commands.remove(user_command)
                        self.action(user_command, user_commands)
                        break 
                    elif (user_command == 'exit'):
                        self.game_ongoing = False



    def move(self, command):
        RoomController().navigate(command)

    def action(self, action, commands):
        target = []
        if action == 'move':
            self.move('n')
        elif action == 'talk':
            print('UNIMPLEMENTED FUNCTIONALITY')
        elif action == 'pickup' or action == 'get':
            print(commands)
            RoomController().get_all_rooms()[0].interact()
            print('UNIMPLEMENTED FUNCTIONALITY')
        elif action == 'combine':
            print('UNIMPLEMENTED FUNCTIONALITY')
        elif action == 'use' or action == 'interact':
            print('UNIMPLEMENTED FUNCTIONALITY')
        elif action == 'open' or action == 'unlock':
            print('UNIMPLEMENTED FUNCTIONALITY')
        elif action == 'inspect' or action == 'look':

            print('UNIMPLEMENTED FUNCTIONALITY')
