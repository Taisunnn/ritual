from .game_object_controller import *
from .game_output_controller import *
from ..constants.keyword_constants import *

class GameStateController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameStateController, cls).__new__(cls)
            
            # ? init GameObjectController to load all game objects
            GameObjectController()

            # ? Variables to keep track of current state of the progress
            cls._instance.game_ongoing = True
            cls._instance.current_location = 1
            cls._instance.inventory = []

        return cls._instance
    
    def start(self):
        # ? Load starting room
        GameObjectController().load_room_id(self.current_location)

        # ? Get user input until game is over
        while(self.game_ongoing):
            user_command = input('\tWhat do you do? : ')
            user_command = user_command.strip().lower()

            GameOutputController.terminal_print_single_nextline('', no_ending=True)
            if(len(user_command) == 1) and user_command in MOVE_KEYWORD:
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
                    GameOutputController.terminal_print('Unrecognized command: ' + '"'  + user_command + '"')
        # end of start function

    def move(self, command):
        doors = GameObjectController().get_object_category('door')
        moved = False
        for door in doors:
            if door.room1_id == self.current_location and door.room1_location == command:
                self.use_door(door.room2_id, door)
                moved = True
                break
            elif door.room2_id == self.current_location and door.room2_location == command:
                self.use_door(door.room1_id, door)
                moved = True
                break
        if not moved:
            GameOutputController.terminal_print('"There is no pathway in that direction..."', no_ending=True)

    def use_door(self, new_location_id, door):
        if not door.is_locked:
            self.current_location = new_location_id
            GameObjectController().load_room_id(self.current_location)
        else:
            GameOutputController.terminal_print('You try the door and realize that the ' + door.name + ' is locked')


    def action(self, action, command):
        if action in INVENTORY_KEYWORD:
            GameOutputController.terminal_print_single_nextline('You look at what you currently have', no_ending=True)
            if len(self.inventory) == 0:
                GameOutputController.terminal_print_single_nextline("You currently don't have anything")
            else:
                for item in self.inventory:
                    item.inventory_inspect()
        elif action in LOCATION_KEYWORD:
            GameObjectController().load_room_id(self.current_location)
        else:
            # Determine which object the action is being used
            target_objects = GameObjectController().determine_targets(command, self.inventory)            
            if len(target_objects) == 0:
                GameOutputController.terminal_print('Unrecognized Target: ' + '"' + command + '"', no_ending=True)
                return

            # Determine which action is used on the object
            if action in NPC_TALK_KEYWORD:
                self.talk_npc(target_objects)
            elif action in NPC_GIVE_KEYWORD:
                self.give_npc(action, target_objects, command)
            elif action in PICK_UP_KEYWORD:
                self.pick_up_item(target_objects, command)
            elif action in COMBINE_KEYWORD:
                self.combine_item(target_objects)
            elif action in UNLOCK_KEYWORD:
                self.unlock(action, target_objects, command)
            elif action in LOOK_KEYWORD:
                GameOutputController.terminal_print(target_objects[0].long_description)
            elif action in SPECIAL_KEYWORD:
                if all(game_object.object_type == 'item' for game_object in target_objects):
                    self.combine_item(target_objects)
                elif all(game_object.object_type == 'room' for game_object in target_objects):
                    GameOutputController.terminal_print('Not a valid command')
                else:
                    if any(game_object.object_type == 'npc' for game_object in target_objects):
                        self.give_npc(action, target_objects, command)
                    elif any(game_object.object_type == 'door' for game_object in target_objects):
                        self.unlock(action, target_objects, command)

    # -- Action functions --

    def pick_up_item(self, target_objects, command):
        if len(target_objects) == 1:
            if target_objects[0].object_type == 'item':
                if target_objects[0] not in self.inventory:
                    self.inventory.append(target_objects[0])
                    GameObjectController().remove_object(target_objects[0])
                    GameOutputController.terminal_print('You picked up the ' + target_objects[0].name + ' and added to your bag')
                else:
                    GameOutputController.terminal_print('That item is already in your bag')
            else:
                GameOutputController.terminal_print('You can\'t pick up ' + '"' + command + '"')
        else:
            GameOutputController.terminal_print('Enter one object at a time when picking things up')

    def combine_item(self, target_objects):
        temp_object_list = [object for object in target_objects if object.object_type == 'item']
        combined_item = GameObjectController().combine_item(temp_object_list)
        if combined_item is not None:
            for inventory_object in temp_object_list:
                if inventory_object in self.inventory:
                    self.inventory.remove(inventory_object)
            self.inventory.append(combined_item)
            GameOutputController.terminal_print(combined_item.combine_success_description)
        else:
            GameOutputController.terminal_print('You can\'t combine these items')

    def talk_npc(self, target_objects):
        if target_objects[0].object_type == 'npc':
            target_objects[0].speak()
        else:
            GameOutputController.terminal_print('Why are you trying to talk to that?', no_ending=True)

    def give_npc(self, action, target_objects, command):
        temp_item_list = [object for object in target_objects if object.object_type == 'item']
        temp_npc_list = [object for object in target_objects if object.object_type == 'npc']
        if len(temp_item_list) == 0 or len(temp_npc_list) == 0 :
            GameOutputController.terminal_print('Target Not Found', no_ending=True)
        elif len(temp_item_list) > 1 or len(temp_npc_list[0].ending_items) > 0:
            if temp_item_list == temp_npc_list[0].ending_items:
                GameOutputController.terminal_print('You are missing something')
                self.game_ongoing = False
        else:
            item_from_npc = GameObjectController().give_npc(temp_npc_list[0], temp_item_list[0])
            if item_from_npc is not None:
                self.inventory.remove(temp_item_list[0])
                self.inventory.append(item_from_npc)

    def unlock(self, action, target_objects, command):
        temp_item_list = [object for object in target_objects if object.object_type == 'item']
        temp_npc_list = [object for object in target_objects if object.object_type == 'door']
        if len(temp_item_list) == 0 or len(temp_npc_list) == 0 :
            GameOutputController.terminal_print('Target Not Found', no_ending=True)
        else:
            unlocked = GameObjectController().unlock_door(temp_npc_list[0], temp_item_list[0].id)
            if unlocked:
                GameOutputController.terminal_print('You hear a click. It seems unlocked')
            else:
                GameOutputController.terminal_print('It doesn\'t seem to do anything...', no_ending=True)