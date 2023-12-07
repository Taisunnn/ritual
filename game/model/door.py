from .game_object import GameObject


class Door(GameObject):
    def __init__(self, room1_id, room1_location, room2_id, room2_location, name, description, is_locked, key_item_id):
        super().__init__('door', name, description)
        self.room1_id = room1_id
        self.room1_location = room1_location
        self.room2_id = room2_id
        self.room2_location = room2_location
        self.is_locked = is_locked
        self.key_item_id = key_item_id

    def is_in_room(self, id):
        # return self.room1_id == id or self.room2_id == id
        if self.room1_id == id or self.room2_id == id:
            return True
        return False

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

        door_description += ', you see a ' + self.name + '. ' + self.description + '\n\n'
        print(door_description)

    def to_json(self):
        return {
            "room1_id": self.room1_id,
            "room1_location": self.room1_location,
            "room2_id": self.room2_id,
            "room2_location": self.room2_location,
            "description": self.description,
            "is_locked": self.is_locked,
            "key_item_id": self.key_item_id
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            room1_id=data.get("room1_id", 0),
            room1_location=data.get("room1_location", ""),
            room2_id=data.get("room2_id", 0),
            room2_location=data.get("room2_location", ""),
            name=data.get("name", ""),
            description=data.get("description", ""),
            is_locked=data.get("is_locked", False),
            key_item_id=data.get("key_item_id", 0),
        )

    def __str__(self):
        return f"Room ID: {self.id}, Name: {self.name}, Description: {self.description}"
