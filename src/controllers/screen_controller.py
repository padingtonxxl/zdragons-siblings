from src.common.constants import *
from src.views.intro_view import IntroView
from src.views.start_view import StartView
from src.views.game_creation_view import GameCreationView
from src.controllers.game_controller import *
from src.ui.text_input import TextInput
from src.ui.popup import PopUp
from datetime import datetime
import pygame


class ScreenController:

    def __init__(self, runtime):
        self.runtime = runtime
        self.last_generic_action = ''
        self._view = None
        self.active = True

    def display(self):
        self._view.display()

    def update(self):
        self.last_generic_action = 'UPDATE'

    def handle_event(self, event):
        self.last_generic_action = 'HANDLE_EVENT'

    def handle_switch_to(self):
        self.last_generic_action = 'HANDLE_SWITCH_TO'


class IntroScreenController(ScreenController):

    def __init__(self, runtime):
        super(self.__class__, self).__init__(runtime)
        self._start_time = datetime.now()
        self.first_start = True
        self._view = IntroView(self)

    def handle_event(self, event):
        if event.type == pygame.KEYUP or event.type == pygame.MOUSEBUTTONUP:
            self.runtime.set_current_screen(START_SCREEN)
            return True

    def update(self):
        time_elapsed = datetime.now() - self._start_time
        if time_elapsed.total_seconds() > 3:
            self.runtime.set_current_screen(START_SCREEN)
            return True
        if self.first_start:
            self.first_start = False
            return True


class StartScreenController(ScreenController):

    def __init__(self, runtime):
        super(self.__class__, self).__init__(runtime)
        self.games_list = None
        self.reset()

    def handle_event(self, event):
        if self.active:
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_object = self._view.get_object_under_mouse()
                if clicked_object is not None:
                    if str(clicked_object.element_id).startswith(GAME_BUTTON):
                        splits = str(clicked_object.element_id).split(':')
                        self.runtime.game = GameController(self.runtime, splits[1])
                        if self.runtime.game.new:
                            self.runtime.set_current_screen(GAME_CREATION_SCREEN)
                            return True
                    if str(clicked_object.element_id).startswith(GAME_DELETE):
                        splits = str(clicked_object.element_id).split(':')
                        self.runtime.game = GameController(self.runtime, splits[1])
                        self.active = False
                        deletion_confirmation = PopUp(self.runtime,
                                                      TEXT_DO_YOU_WANT_TO_DELETE,
                                                      ((1, TEXT_YES), (0, TEXT_NO)), 250, 125
                                                      ).display()
                        self.active = True
                        if deletion_confirmation == 1 and not self.runtime.game.new:
                            self.runtime.game.reset()
                            PopUp(self.runtime,
                                  'Löschen erfolgreich',
                                  ((1, TEXT_OK),), 250, 125
                                  ).display()
                            return True

    def reset(self):
        self.games_list = GameListController(self.runtime, int(self.runtime.config.values[CONFIG_NUMBER_OF_GAMES]))
        self._view = StartView(self)

    def update(self):
        return True


class GameCreationScreenController(ScreenController):

    def __init__(self, runtime):
        super(self.__class__, self).__init__(runtime)
        self.game_name_input = TextInput(self.runtime, 100, 100, 'game_name', TEXT_GAME_NAME)
        self._view = GameCreationView(self)

    def update(self):
        return self.game_name_input.update()

    def display(self):
        self._view.display()
