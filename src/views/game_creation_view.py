from src.views.view import View
from src.ui.text_input import TextInput


class GameCreationView(View):

    def __init__(self, screen_controller):
        super(self.__class__, self).__init__(screen_controller)

    def display(self):
        self._screen_controller.runtime.screen.fill((143, 72, 104))
        self._screen_controller.game_name_input.display()
