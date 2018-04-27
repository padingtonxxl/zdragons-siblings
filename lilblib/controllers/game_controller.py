from lilblib.models.game_model import GameModel
from lilblib.common.constants import *


class GameController:

    def __init__(self, runtime, game_id):
        self.runtime = runtime
        self.model = GameModel(runtime)
        self.model.read(game_id)
        self.new = False
        if self.model.game_id is None:
            self.model.game_id = game_id
            self.model.name = TEXT_GAME + ' ' + str(game_id)
            self.new = True

    def get_game_id(self):
        return self.model.game_id

    def get_name(self):
        return self.model.name

    def set_name(self, name):
        self.model.name = name

    def get_status(self):
        return self.model.status

    def set_status(self, status):
        self.model.status = status

    def get_updated_at(self):
        return self.model.updated_at

    def post(self):
        if self.new:
            self.model.create()
        else:
            self.model.update()

    def reset(self):
        game_id = self.model.game_id
        self.model.delete()
        self.__init__(self.runtime, game_id)


class GameListController:

    def __init__(self, runtime, number_of_games):
        self.runtime = runtime
        self.games = dict()
        for game_number in range(number_of_games):
            self.games[game_number] = GameController(self.runtime, game_number)
