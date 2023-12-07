class Room():
    def __init__(self, id, name, description, is_starting_room, starting_room_intro, is_ending_room, ending_room_outro, item_ids, npc_ids, connected_rooms):
        self.id = id
        self.name = name
        self.description = description
        self.is_starting_room = is_starting_room
        self.starting_room_intro = starting_room_intro
        self.is_ending_room = is_ending_room
        self.ending_room_outro = ending_room_outro
        self.item_ids = item_ids
        self.npc_ids = npc_ids
        self.connected_rooms = connected_rooms

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_starting_room": self.is_starting_room,
            "starting_room_intro": self.starting_room_intro,
            "is_ending_room": self.is_ending_room,
            "ending_room_outro": self.ending_room_outro,
            "item_ids": self.item_ids,
            "npc_ids": self.npc_ids,
            "connected_rooms": self.connected_rooms
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data["id"],
            name=json_data["name"],
            description=json_data["description"],
            is_starting_room=json_data["is_starting_room"],
            starting_room_intro=json_data["starting_room_intro"],
            is_ending_room=json_data["is_ending_room"],
            ending_room_outro=json_data["ending_room_outro"],
            item_ids=json_data["item_ids"],
            npc_ids=json_data["npc_ids"],
            connected_rooms=json_data["connected_rooms"]
        )
    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id", 0),
            name=data.get("name", ""),
            description=data.get("description", ""),
            is_starting_room=data.get("is_starting_room", False),
            starting_room_intro=data.get("starting_room_intro", ""),
            is_ending_room=data.get("is_ending_room", False),
            ending_room_outro=data.get("ending_room_outro", ""),
            item_ids=data.get("item_ids", []),
            npc_ids=data.get("npc_ids", []),
            connected_rooms=data.get("connected_rooms", [])
        )

    def __str__(self):
        return f"Room ID: {self.id}, Name: {self.name}, Description: {self.description}"
