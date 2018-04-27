from src.views.view import View
from src.ui.window import Window
from src.common.constants import *
from src.ui.button import Button


class StartView(View):

    def __init__(self, screen_controller):
        super(self.__class__, self).__init__(screen_controller)
        self.window = Window(self._screen_controller.runtime, TEXT_GAME_SELECTION, 600, 400, 2)
        for key, game in self._screen_controller.games_list.games.items():
            self.window.add_display_element(
                Button(screen_controller.runtime,
                       GAME_BUTTON+str(game.get_game_id()),
                       game.get_name()+' '+str(game.get_status())+' '+str(game.get_updated_at()))
            )
            self.window.add_display_element(
                Button(screen_controller.runtime,
                       GAME_DELETE + str(game.get_game_id()), TEXT_DELETE)
            )

    def display(self):
        self._screen_controller.runtime.screen.fill((243, 72, 4))
        self.window.display()

    def get_object_under_mouse(self):
        for input_element in self.window.display_elements:
            if input_element[0].mouse_over():
                return input_element[0]
