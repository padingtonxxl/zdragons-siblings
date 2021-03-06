from src.views.view import View
from src.ui.window import Window
from src.common.constants import *


class IntroView(View):
    def __init__(self, screen_controller):
        super(self.__class__, self).__init__(screen_controller)

    def display(self):
        self._screen_controller.runtime.screen.fill((63, 72, 204))
        Window(self._screen_controller.runtime, TEXT_GAMETITLE, 400, 70).display()
