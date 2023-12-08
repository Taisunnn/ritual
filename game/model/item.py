from .game_object import GameObject

class Item(GameObject):
    def __init__(self, id, name, description, item_location, location_description, is_combined_item, combination, combine_success_description):
        super().__init__('item', name, description)
        self.id = id
        self.item_location = item_location
        self.location_description = location_description
        self.is_combined_item = is_combined_item
        self.combination = combination
        self.combine_success_description = combine_success_description

    def is_in_room(self, id):
        return self.item_location == id
    
    def inspect(self, room_id):
        print(self.location_description + '.\n\n')
    
    def inventory_inspect(self):
        print(' - ' + self.name + ': ' +self.description + '.\n\n')

    # def to_json(self):
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "description": self.description,
    #         "is_combined_item": self.is_combined_item,
    #         "combination": self.combination,
    #         "combine_success_description": self.combine_success_description
    #     }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data.get("id", 0),
            name = data.get("name", ""),
            description = data.get("description", ""),
            item_location = data.get("item_location", 0),
            location_description = data.get("location_description", ""),
            is_combined_item = data.get("is_combined_item", False),
            combination = data.get("combination", []),
            combine_success_description = data.get("combine_success_description", "")
        )
    
    def __str__(self):
        return f"Item ID: {self.id}, Name: {self.name}, Description: {self.description}"