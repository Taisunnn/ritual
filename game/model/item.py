class Item():
    def __init__(self, id, name, description, is_combined_item, combination, combine_success_description):
        self.id = id
        self.name = name
        self.description = description
        self.is_combined_item = is_combined_item
        self.combination = combination
        self.combine_success_description = combine_success_description

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "is_combined_item": self.is_combined_item,
            "combination": self.combination,
            "combine_success_description": self.combine_success_description
        }

    @classmethod
    def from_json(cls, json_data):
        return cls(
            id=json_data["id"],
            name=json_data["name"],
            description=json_data["description"],
            is_combined_item=json_data["is_combined_item"],
            combination=json_data["combination"],
            combine_success_description=json_data["combine_success_description"]
        )