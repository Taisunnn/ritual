import json
import os

from ..model import npc

class NPCController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NPCController, cls).__new__(cls)
            cls._instance.npcs = []
            cls._instance.current_npcs = []
            f=open(os.getcwd() + '/data/NPC.json')
            npcData = json.load(f)
            for npc in npcData['npcs']:
                # print(npc)
                cls._instance.add_npc(npc)
            # print('NPCController Ready')
        return cls._instance

    def add_npc(self, npc):
        self.npcs.append(npc)

    def remove_npc(self, npc_id):
        self.npcs = [npc for npc in self.npcs if npc.id != npc_id]

    def get_npc_by_id(self, npc_id):
        return next((npc for npc in self.npcs if npc.id == npc_id), None)

    def get_all_npcs(self):
        return self.npcs

    def set_current_npcs(self, npcs):
        self.current_npcs = npcs

    def get_current_npcs(self):
        return self.current_npcs

    def to_json(self):
        return [npc.to_json() for npc in self.npcs]

    @classmethod
    def from_json(cls, json_data):
        controller = cls()
        for npc_data in json_data:
            npc = npc.from_json(npc_data)
            controller.add_npc(npc)
        return controller