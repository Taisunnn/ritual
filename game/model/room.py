from .game_object import GameObject


class Room(GameObject):
    def __init__(self, id, name, description, long_description, is_starting_room, starting_room_intro, is_ending_room, ending_room_outro, npc_ids, connected_rooms):
        super().__init__('room', name, description, long_description)
        self.id = id
        self.is_starting_room = is_starting_room
        self.starting_room_intro = starting_room_intro
        self.is_ending_room = is_ending_room
        self.ending_room_outro = ending_room_outro
        self.npc_ids = npc_ids
        self.connected_rooms = connected_rooms

    def is_in_room(self, id):
        return self.id == id

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_starting_room": self.is_starting_room,
            "starting_room_intro": self.starting_room_intro,
            "is_ending_room": self.is_ending_room,
            "ending_room_outro": self.ending_room_outro,
            "npc_ids": self.npc_ids,
            "connected_rooms": self.connected_rooms
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data.get("id", 0),
            name = data.get("name", ""),
            description = data.get("description", ""),
            long_description  =  data.get("long_description", ""),
            is_starting_room = data.get("is_starting_room", False),
            starting_room_intro = data.get("starting_room_intro", ""),
            is_ending_room = data.get("is_ending_room", False),
            ending_room_outro = data.get("ending_room_outro", ""),
            npc_ids = data.get("npc_ids", []),
            connected_rooms = data.get("connected_rooms", [])
        )

    def __str__(self):
        return f"Room ID: {self.id}, Name: {self.name}, Description: {self.description}"
