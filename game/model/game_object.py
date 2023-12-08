class GameObject():

    def __init__(self, object_type, name, description):
        self.object_type = object_type
        self.name = name
        self.description = description

    def inspect(self, room_id):
        print(self.description + "\n\n")

    def interact(self):
        pass

    def interact(self, item):
        pass

    def is_in_room(self, id):
        pass