from .game_object import *
from game.controller.game_output_controller import *

class Door(GameObject):
    def __init__(self, room1_id, room1_location, room2_id, room2_location, name, description, long_description, is_locked, key_item_id):
        super().__init__('door', name, description, long_description)
        self.room1_id = room1_id
        self.room1_location = room1_location
        self.room2_id = room2_id
        self.room2_location = room2_location
        self.is_locked = is_locked
        self.key_item_id = key_item_id

    def is_in_room(self, id):
        return self.room1_id == id or self.room2_id == id

    def inspect(self, room_id):
        door_location = ''
        if room_id == self.room1_id:
            door_location = self.room1_location
        elif room_id == self.room2_id:
            door_location = self.room2_location

        door_description = ''

        if door_location == 'n':
            door_description += 'To your north'
        elif door_location == 'e':
            door_description += 'To your east'
        elif door_location == 's':
            door_description += 'To your south'
        elif door_location == 'w':
            door_description += 'To your west'

        door_description += ', you see a ' + self.name + '. ' + self.description
        GameOutputController.terminal_print(door_description)
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            room1_id = data.get("room1_id", 0),
            room1_location = data.get("room1_location", ""),
            room2_id = data.get("room2_id", 0),
            room2_location = data.get("room2_location", ""),
            name = data.get("name", ""),
            description = data.get("description", ""),
            long_description = data.get("long_description", ""),
            is_locked = data.get("is_locked", False),
            key_item_id = data.get("key_item_id", 0),
        )
