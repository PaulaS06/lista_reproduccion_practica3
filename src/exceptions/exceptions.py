class Player(Exception):
    pass

class EmptyPlaylistError(Player):
    def __init__(self, message):
        self.message = message

class AlreadyExistsError(Player):
    def __init__(self, message):
        self.message = message

class InvalidSongError(Player):
    def __init__(self, message):
        self.message = message