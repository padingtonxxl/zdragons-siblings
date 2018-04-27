from src.runtime import Runtime
from src.ui.popup import PopUp
from src.controllers.screen_controller import *
import pygame
import sys


class GameLoop:

    def __init__(self):
        pygame.init()
        self.runtime = Runtime()
        pygame.display.set_caption(self.runtime.config.values[CONFIG_WINDOW_TITLE])
        self._event_happened = True
        self._update_happened = False

    def start(self):
        while 1:
            self.runtime.clock.tick(60)
            for event in pygame.event.get():
                self._handle_event(event)
            self._update()
            self._display()
            self._event_happened = False
            self._update_happened = False

    def _handle_event(self, event):
        if event.type == pygame.QUIT:
            self.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            if PopUp(self.runtime, TEXT_DO_YOU_WANT_TO_QUIT, ((1, TEXT_YES), (0, TEXT_NO)), 250, 125).display():
                self.exit()
        else:
            self._event_happened = self.runtime.screens[self.runtime.current_screen].handle_event(event)

    def _update(self):
        self._update_happened = self.runtime.screens[self.runtime.current_screen].update()

    def _display(self):
        if self._event_happened or self._update_happened:
            self.runtime.screens[self.runtime.current_screen].display()
            pygame.display.flip()

    def save(self):
        self.runtime.game.post()

    def exit(self):
        self.save()
        sys.exit()
