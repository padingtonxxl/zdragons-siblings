import pymysql
from lilblib.common.config import Config
from lilblib.controllers.screen_controller import *
import lilblib.controllers.screen_controller


class Runtime:

    def __init__(self):
        self.db_connection = pymysql.connect(
            host='localhost',
            user='zubi',
            password='zubi',
            db='zubi_zdragons_siblings',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True)
        self.config = Config(self.db_connection)
        self.clock = pygame.time.Clock()
        # info_object = pygame.display.Info()
        # self.size = self.width, self.height = info_object.current_w, info_object.current_h
        self.width = int(self.config.values[CONFIG_WINDOW_WIDTH])
        self.height = int(self.config.values[CONFIG_WINDOW_HEIGHT])
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode(
            (int(self.config.values[CONFIG_WINDOW_WIDTH]),
             int(self.config.values[CONFIG_WINDOW_HEIGHT])))  # , pygame.FULLSCREEN)
        self.current_screen = None
        self.screens = dict()  # {INTRO_SCREEN: IntroScreenController(self), }
        self.set_current_screen(self.config.values[CONFIG_FIRST_SCREEN])
        self.game = None

    def set_current_screen(self, screen_name):
        self.current_screen = screen_name
        if self.current_screen not in self.screens:
            screen_class = getattr(lilblib.controllers.screen_controller, self.current_screen)
            self.screens[self.current_screen] = screen_class(self)
