class GameOutputController:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameOutputController, cls).__new__(cls)
        return cls._instance
    
    @staticmethod
    def terminal_print(message, no_ending = False):
        if no_ending:
            print(message + '\n\n')
        else:
            print(message + '.\n\n')

    @staticmethod
    def terminal_print_single_nextline(message, no_ending = False):
        if no_ending:
            print(message + '\n')
        else:
            print(message + '.\n')
