# from item_controller import ItemController
from .item_controller import ItemController
from .npc_controller import NPCController
from .room_controller import RoomController
from .game_object_controller import GameObjectController
from .system_message_controller import SystemMessageController
from ..constants.keyword_constants import *

class GameStateController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameStateController, cls).__new__(cls)
            NPCController()
            RoomController()
            ItemController()
            GameObjectController()
            cls._instance.game_ongoing = True
            cls._instance.current_locaiton = 1
            cls._instance.inventory = []
        return cls._instance
    
    def start(self):
        # RoomController().to_start()
        GameObjectController().load_room_id(self.current_locaiton)

        while(self.game_ongoing):
            user_command = input('\tWhat do you do? : ')
            user_command = user_command.strip().lower()

            print('\n')
            if(len(user_command) == 1):
                for move_command in MOVE_KEYWORD:
                    if move_command in user_command:
                        self.move(move_command)
                        break
            else:
                is_action = False
                for action_command in ACTION_KEYWORD:
                    if action_command in user_command:
                        is_action = True
                        target  = user_command.replace(action_command, "").strip()
                        self.action(action_command, target)
                        break
                if not is_action:
                    print('Unrecognized Action: ' + '"'  + user_command + '"' + '\n\n')


    def move(self, command):
        print('UNIMPLEMENTED FUNCTIONALITY: ' + 'move' + " " + command + '\n\n')

    def action(self, action, target):
        if action in INVENTORY_KEYWORD:
            print('UNIMPLEMENTED FUNCTIONALITY: ' + action + '\n\n')
        else:
            # Determine which object the action is being used
            target_object = self._determine_target(target)            
            if target_object == None:
                print('Unrecognized Target: ' + '"' + target + '"' + '\n\n')
                return

            # Determine which action is used on the object
            if action in MOVE_ACTION_KEYWORD:
                self.move(target)
            elif action in TALK_KEYWORD:
                print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + target + '\n\n')
            elif action in PICK_UP_KEYWORD:
                if target_object.object_type == 'item':
                    print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + target + '\n\n')
                else:
                    print('You can\'t pick up ' + '"' + target + '"' + '\n\n')
            elif action in COMBINE_KEYWORD:
                print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + target + '\n\n')
            elif action in INTERACT_KEYWORD:
                print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + target + '\n\n')
            elif action in UNLOCK_KEYWORD:
                print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + target + '\n\n')
            elif action in LOOK_KEYWORD:
                GameObjectController().get_object_description(target, self.current_locaiton)


    def _determine_target(self, target):
        target_object = None
        for name in target.split():
            target_object = GameObjectController().get_object(name)
            if target_object is not None:
                break
        if target_object == None:
            target_object = GameObjectController().get_object(target)
        
        return target_object