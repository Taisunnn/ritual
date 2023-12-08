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
            cls._instance.current_location = 1
            cls._instance.inventory = []
        return cls._instance
    
    def start(self):
        GameObjectController().load_room_id(self.current_location)

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
                        command  = user_command.replace(action_command, "").strip()
                        self.action(action_command, command)
                        break
                if not is_action:
                    print('Unrecognized Action: ' + '"'  + user_command + '"' + '\n\n')


    def move(self, command):
        doors = GameObjectController().get_object_category('door')
        moved = False
        for door in doors:
            if door.room1_id == self.current_location and door.room1_location == command:
                # self.current_location = door.room2_id
                # GameObjectController().load_room_id(self.current_location)
                self.use_door(door.room2_id, door)
                moved = True
                break
            elif door.room2_id == self.current_location and door.room2_location == command:
                self.current_location = door.room1_id
                GameObjectController().load_room_id(self.current_location)
                self.use_door(door.room1_id, door)
                moved = True
                break
        if not moved:
            print('"There is no pathway in that direction..."\n\n')

    def use_door(self, new_location_id, door):
        if not door.is_locked:
            self.current_location = new_location_id
            GameObjectController().load_room_id(self.current_location)
        else:
            print('You try the door and realize that the ' + door.name + ' is locked' + '\n\n')


    def action(self, action, command):
        if action in INVENTORY_KEYWORD:
            print('You look at what you currently have\n')
            if len(self.inventory) == 0:
                print("You currently don't have anything\n")
            else:
                for item in self.inventory:
                    item.inventory_inspect()
        else:
            # Determine which object the action is being used
            target_objects = GameObjectController().determine_targets(command, self.inventory)            
            if len(target_objects) == 0:
                print('Unrecognized Target: ' + '"' + command + '"' + '\n\n')
                return

            # Determine which action is used on the object
            if action in TALK_KEYWORD:
                print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + command + '\n\n')
            elif action in PICK_UP_KEYWORD:
                if len(target_objects) == 1:
                    if target_objects[0].object_type == 'item':
                        if target_objects[0] not in self.inventory:
                            self.inventory.append(target_objects[0])
                            GameObjectController().remove_object(target_objects[0])
                            print('You picked up the ' + target_objects[0].name + ' and added to your bag' + '\n\n')
                        else:
                            print('That item is already in your bag' + '\n\n')
                    else:
                        print('You can\'t pick up ' + '"' + command + '"' + '\n\n')
                else:
                    print('Enter one object at a time when picking things up' + '\n\n')
            elif action in COMBINE_KEYWORD:
                temp_object_list = [object for object in target_objects if object.object_type == 'item']
                combined_item = GameObjectController().combine_item(temp_object_list)
                if combined_item is not None:
                    for inventory_object in temp_object_list:
                        if inventory_object in self.inventory:
                            self.inventory.remove(inventory_object)
                    self.inventory.append(combined_item)
                    print('You combine the items and get ' + ('an ' if combined_item.name[0] in ['a', 'e', 'i', 'o', 'u'] else 'a ') + combined_item.name + '.' + '\n\n')
                else:
                    print('You can\'t combine these items.' + '\n\n')
            elif action in INTERACT_KEYWORD:
                print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + command + '\n\n')
            elif action in UNLOCK_KEYWORD:
                print('UNIMPLEMENTED FUNCTIONALITY: ' + action + " " + command + '\n\n')
            elif action in LOOK_KEYWORD:
                GameObjectController().get_object_description(command, self.current_location)
