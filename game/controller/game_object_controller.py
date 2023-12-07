import json
import os

from game.controller import game_state_controller

from ..model.door import Door
from ..model.item import Item
from ..model.npc import NPC
from ..model.room import Room


class GameObjectController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:

            game_objects = []

            f=open(os.getcwd() + '/data/door.json')
            doorsData = json.load(f)
            for doorData in doorsData['doors']:
                game_objects.append(Door.from_dict(doorData))

            # f=open(os.getcwd() + '/data/item.json')
            # itemsData = json.load(f)
            # for itemData in itemsData['items']:
            #     game_objects.append(Item.from_dict(itemData))

            # f=open(os.getcwd() + '/data/npc.json')
            # npcsData = json.load(f)
            # for npcData in npcsData['npcs']:
            #     game_objects.append(NPC.from_dict(npcData))

            f=open(os.getcwd() + '/data/room.json')
            roomsData = json.load(f)
            for roomData in roomsData['rooms']:
                game_objects.append(Room.from_dict(roomData))

            cls._instance = super(GameObjectController, cls).__new__(cls)
            cls._instance.game_objects = game_objects
            cls._instance.current_objects = []
        return cls._instance
    
    @staticmethod
    def _current_room():
        return game_state_controller.GameStateController().current_location

    def load_room_id(self, id):
        self.current_objects = [game_object for game_object in self.game_objects if game_object.is_in_room(id)]
        self.current_objects.reverse()
        self.get_descriptions(id)

    def get_descriptions(self, room_id):
        temp_object_list = [game_object for game_object in self.game_objects if game_object.is_in_room(room_id)]
        temp_object_list.reverse()
        for game_object in temp_object_list:
            game_object.inspect(room_id)

    def get_object(self, name):
        object = next((game_object for game_object in self.current_objects if game_object.name.lower() == name), None)
        return object

    def get_object_description(self, name, room_id):
        object = next((game_object for game_object in self.current_objects if game_object.name.lower() == name), None)
        if object is not None:
            object.inspect(room_id) 

    def get_item_description(self, name):
        object = next((game_object for game_object in self.current_objects if game_object.object_type == 'item' and game_object.name.lower() == name), None)
        if object is not None:
            object.inspect(self._current_room) 

    def get_object_category(self, category_name):
        temp_object_list = [game_object for game_object in self.game_objects if game_object.is_in_room(self._current_room()) and game_object.object_type == category_name]
        return temp_object_list 

    def remove_object(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]
