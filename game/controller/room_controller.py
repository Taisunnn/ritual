import json
import os

from ..controller import game_state_controller
from ..model.room import Room

class RoomController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            f=open(os.getcwd() + '/data/room.json')
            roomsData = json.load(f)
            rooms = []
            for roomData in roomsData['rooms']:
                rooms.append(Room.from_dict(roomData))
            cls._instance = super(RoomController, cls).__new__(cls)
            cls._instance.rooms = rooms
            cls._instance.current_room = 0
        return cls._instance

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room_id):
        self.rooms = [room for room in self.rooms if room.id != room_id]

    def get_room_by_id(self, room_id):
        return next((room for room in self.rooms if room.id == room_id), None)

    def get_all_rooms(self):
        return self.rooms
    
    def print_room_description(self):
        print('\n\n\t' + self.current_room.description + '\n\n')

    def to_start(self):
        start_room = next((room for room in self.rooms if room.is_starting_room == True), None)
        self.current_room = start_room
        self.print_room_description()

    def navigate(self, direction):
        next_room = next((connected_room for connected_room in self.current_room.connected_rooms if connected_room['room_direction'] == direction), None)
        if next_room is not None:
            self.current_room = self.get_room_by_id(next_room['room_id'])
            self.print_room_description()
            if self.current_room.is_ending_room:
                game_state_controller.GameStateController().game_ongoing = False
        else:
            print('\n\n\tThere is nothing over there\n\n')

    def to_json(self):
        return [room.to_json() for room in self.rooms]

    # @classmethod
    # def from_json(cls, json_data):
    #     controller = cls()
    #     for room_data in json_data:
    #         room = room.from_json(room_data)
    #         controller.add_room(room)
    #     return controller
    