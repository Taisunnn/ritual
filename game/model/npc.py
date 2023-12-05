import json

class NPC():
    def __init__(self, id, name, description, dialogue, item_interactions):
        self.id = id
        self.name = name
        self.description = description
        self.dialogue = dialogue
        self.item_interactions = item_interactions

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "dialogue": self.dialogue,
            "item_interactions": self.item_interactions
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data["id"],
            name=json_data["name"],
            description=json_data["description"],
            dialogue=json_data["dialogue"],
            item_interactions=json_data["item_interactions"]
        )
