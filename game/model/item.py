from game_object import GameObject
from game.controller.game_output_controller import *

class Item(GameObject):
    def __init__(self, id, name, description, long_description, item_location, location_description, is_combined_item, combination, combine_success_description):
        super().__init__('item', name, description, long_description)
        self.id = id
        self.item_location = item_location
        self.location_description = location_description
        self.is_combined_item = is_combined_item
        self.combination = combination
        self.combine_success_description = combine_success_description

    def is_in_room(self, id):
        return self.item_location == id
    
    def inspect(self, room_id):
        GameOutputController.terminal_print(self.location_description)
    
    def inventory_inspect(self):
        GameOutputController.terminal_print(' - ' + self.name + ': ' +self.description)

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data.get("id", 0),
            name = data.get("name", ""),
            description = data.get("description", ""),
            long_description = data.get("long_description", ""),
            item_location = data.get("item_location", 0),
            location_description = data.get("location_description", ""),
            is_combined_item = data.get("is_combined_item", False),
            combination = data.get("combination", []),
            combine_success_description = data.get("combine_success_description", "")
        )
    
    def __str__(self):
        return f"Item ID: {self.id}, Name: {self.name}, Description: {self.description}"