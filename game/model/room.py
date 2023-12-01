class Room():
    def __init__(self, id, name, description, is_starting_room, starting_room_intro, is_ending_room, ending_room_outro, item_ids, npc_ids, connected_rooms):
        self.id = id
        self.name = name
        self.description = description
        self.is_starting_room = is_starting_room
        self.starting_room_intro = starting_room_intro
        self.is_ending_room = is_ending_room
        self.ending_room_outro = ending_room_outro
        self.item_ids = item_ids
        self.npc_ids = npc_ids
        self.connected_rooms = connected_rooms
