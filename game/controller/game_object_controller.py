import json
import os

from game.controller import game_state_controller
from game.controller.game_output_controller import *
from ..model.door import Door
from ..model.item import Item
from ..model.npc import NPC
from ..model.room import Room


class GameObjectController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            game_objects = []

            # ? Load all objects from json file
            f=open(os.getcwd() + '/data/door.json')
            doorsData = json.load(f)
            for doorData in doorsData['doors']:
                game_objects.append(Door.from_dict(doorData))

            f=open(os.getcwd() + '/data/item.json')
            itemsData = json.load(f)
            for itemData in itemsData['items']:
                game_objects.append(Item.from_dict(itemData))

            f=open(os.getcwd() + '/data/npc.json')
            npcsData = json.load(f)
            for npcData in npcsData['npcs']:
                game_objects.append(NPC.from_dict(npcData))

            f=open(os.getcwd() + '/data/room.json')
            roomsData = json.load(f)
            for roomData in roomsData['rooms']:
                game_objects.append(Room.from_dict(roomData))

            # ? Create instance of the object
            cls._instance = super(GameObjectController, cls).__new__(cls)

            # ? array that will hold all the game objects and relevant game objects
            cls._instance.game_objects = game_objects
            cls._instance.relevant_objects = []
        return cls._instance
    
    @staticmethod
    def _current_room():
        return game_state_controller.GameStateController().current_location

    def load_room_id(self, id):
        self.relevant_objects = [game_object for game_object in self.game_objects if game_object.is_in_room(id)]
        self.relevant_objects.reverse()
        temp_object_list = [game_object for game_object in self.game_objects if game_object.is_in_room(id)]
        temp_object_list.reverse()
        for game_object in temp_object_list:
            game_object.inspect(id)

    def determine_targets(self, command, inventory):
        target_objects = []
        for object in self.relevant_objects + inventory:
            if object.name.lower() in command:
                command  = command.replace(object.name, "").strip()
                command  = command.replace(object.name.lower(), "").strip()
                target_objects.append(object)
        return target_objects

    def get_item_id(self, id):
        object = next((game_object for game_object in self.game_objects if game_object.object_type == 'item' and game_object.id == id), None)
        return object

    def get_object_category(self, category_name):
        temp_object_list = [game_object for game_object in self.game_objects if game_object.is_in_room(self._current_room()) and game_object.object_type == category_name]
        return temp_object_list 

    def combine_item(self, items):
        item_ids = []
        for item in items:
            item_ids.append(item.id)
        item_ids.sort()

        object = next((game_object for game_object in self.game_objects if game_object.object_type == 'item' and game_object.combination == item_ids), None)
        self.remove_object(object)
        return object

    def remove_object(self, game_object):
        if game_object in self.game_objects:
            self.game_objects.remove(game_object)
        if game_object in self.relevant_objects:
            self.relevant_objects.remove(game_object)

    def unlock_door(self, door, key_id):
        index = -1
        try:
            index = self.game_objects.index(door)
        except ValueError:
            return False
        if not index == -1 and self.game_objects[index].key_item_id == key_id:
            self.game_objects[index].is_locked = False
            return True
        return False
        
    def give_npc(self, npc, item):
        if npc.item_interactions[0]["interact_item_id"] == item.id:
            npc_item = self.get_item_id(npc.item_interactions[0]["give_item_id"])
            GameOutputController.terminal_print(npc.name + ': "' + npc.item_interactions[0]["dialogue"] + '"', no_ending=True)
            GameOutputController.terminal_print(npc.name + ' gives you ' + npc_item.name)
            self.remove_object(npc)
            self.remove_object(item)
            return npc_item
        GameOutputController.terminal_print('They don\'t seem to respond to it...')
        return None