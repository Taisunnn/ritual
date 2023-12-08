class GameOutputController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameOutputController, cls).__new__(cls)
        return cls._instance
    
    @staticmethod
    def terminal_print(message):
        print(message + '.\n\n')

