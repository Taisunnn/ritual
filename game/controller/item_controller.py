import json
import os

from ..model import item

class ItemController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            f=open(os.getcwd() + '/data/item.json')
            itemData = json.load(f)
            # for item in itemData['items']:
            #     print(item)
            # print('ItemController Ready')
            cls._instance = super(ItemController, cls).__new__(cls)
            cls._instance.items = []
            cls._instance.inventory = []
        return cls._instance

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_id):
        self.items = [item for item in self.items if item.id != item_id]

    def get_item_by_id(self, item_id):
        return next((item for item in self.items if item.id == item_id), None)

    def get_all_items(self):
        return self.items

    def to_json(self):
        return [item.to_json() for item in self.items]

    @classmethod
    def from_json(cls, json_data):
        controller = cls()
        for item_data in json_data:
            item = item.from_json(item_data)
            controller.add_item(item)
        return controller