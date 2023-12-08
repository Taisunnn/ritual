from game.controller.game_output_controller import *

class GameObject():

    def __init__(self, object_type, name, description, long_description):
        self.object_type = object_type
        self.name = name
        self.description = description
        self.long_description = long_description

    def inspect(self, room_id):
        GameOutputController.terminal_print(self.description)

    def inspect_in_detail(self, room_id):
        GameOutputController.terminal_print(self.long_description)

    def interact(self):
        pass

    def interact(self, item):
        pass

    def is_in_room(self, id):
        pass