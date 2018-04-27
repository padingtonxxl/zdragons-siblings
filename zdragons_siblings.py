from lilblib.game_loop import *
from lilblib.models.player_model import PlayerModel

game = GameLoop()
game.start()

game.runtime.db_connection.close()
