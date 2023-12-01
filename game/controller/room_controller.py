import json
import os

from game.model.room import Room

class RoomController:

    def __init__(self):
        self.rooms = []
        f=open(os.getcwd() + '/data/room.json')
        roomData = json.load(f)
        for room in roomData['rooms']:
            rooms.append(Room(**room))
        print('RoomController Ready')
