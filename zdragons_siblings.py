from lib.game_loop import *
from lib.models.player_model import PlayerModel

game = GameLoop()
game.start()

game.runtime.db_connection.close()
