from .game_object import GameObject
import random

class NPC(GameObject):
    def __init__(self, id, name, description, dialogue, npc_location, item_interactions):
        super().__init__('npc', name, description)
        self.id = id
        self.dialogue = dialogue
        self.npc_location = npc_location
        self.item_interactions = item_interactions

    def is_in_room(self, id):
        return self.npc_location == id
    
    def inspect(self, room_id):
        print(self.location_description + '.\n\n')

    def speak(self):
        print(self.name + ': "' + random.choice(self.dialogue) + '"')

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data.get("id", 0),
            name = data.get("name", ""),
            description = data.get("description", ""),
            dialogue = data.get("dialogue", []),
            npc_location = data.get("npc_location", 0),
            item_interactions = data.get("item_interactions", [])
        )
