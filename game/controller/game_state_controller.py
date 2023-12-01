from game.controller.item_controller import ItemController
from game.controller.npc_controller import NPCController
from game.controller.room_controller import RoomController
from game.controller.system_message_controller import SystemMessageController


class GameStateController:

    def __init__(self):
        self.roomController = RoomController()
        self.itemController = ItemController()
        self.NPCController = NPCController()
        self.SystemMessageController = SystemMessageController()

    @staticmethod
    def getItemController(self, id):
        return self.itemController
    
    def start(self):
        gameOngoing = True
        while(gameOngoing):
            print('Enter your move: ')
            move = input()
            if (move == 'e'):
                gameOngoing = False
        print('The game is over')


