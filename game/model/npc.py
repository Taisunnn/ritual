from .game_object import *
from game.controller.game_output_controller import *   
import random

class NPC(GameObject):
    def __init__(self, id, name, description, long_description, dialogue, npc_location, item_interactions, ending_items, ending_quote):
        super().__init__('npc', name, description, long_description)
        self.id = id
        self.dialogue = dialogue
        self.npc_location = npc_location
        self.item_interactions = item_interactions
        self.ending_items = ending_items
        self.ending_quote = ending_quote

    def is_in_room(self, id):
        return self.npc_location == id

    def speak(self):
        GameOutputController.terminal_print(self.name + ': "' + random.choice(self.dialogue) + '"')

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data.get("id", 0),
            name = data.get("name", ""),
            description = data.get("description", ""),
            long_description = data.get("long_description", ""),
            dialogue = data.get("dialogue", []),
            npc_location = data.get("npc_location", 0),
            item_interactions = data.get("item_interactions", []),
            ending_items = data.get("ending_items", []),
            ending_quote = data.get("ending_quote", "")
        )
