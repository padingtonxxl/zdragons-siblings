from lilblib.models.player_model import PlayerModel
import hashlib
import string
import random

STATE_UNCHANGED = 'I'
STATE_NEW = 'N'
STATE_CHANGED = 'C'


class PlayerController:

    def __init__(self, runtime, name):
        self._state = STATE_NEW
        self._model = PlayerModel(runtime)
        self._runtime = runtime
        if name is not None:
            self._model.read_by_name(name)

    def read_by_name(self, name):
        self._model.read_by_name(name)
        self._state = STATE_UNCHANGED

    def set_name(self, name):
        self._model.name = name
        self._handle_change()

    def post(self):
        if self._state == STATE_NEW:
            self._model.create()
        elif self._state == STATE_CHANGED:
            self._model.update()
        self.read_by_name(self._model.name)

    def delete(self):
        self._model.delete()
        self._state = STATE_NEW

    def set_password(self, password, salt=None):
        if salt is None:
            self._model.salt = ''.join(
                random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(16))
        else:
            self._model.salt = salt
        self._model.password = PlayerController._create_password_hash(
            self._runtime.config.salt, password, self._model.salt)
        self._handle_change()

    def check_password(self, password):
        password_hash = PlayerController._create_password_hash(
            self._runtime.config.salt, password, self._model.salt)
        if self._model.password == password_hash:
            return True
        else:
            return False

    def _handle_change(self):
        if self._state == STATE_UNCHANGED:
            self._state = STATE_CHANGED

    @staticmethod
    def _create_password_hash(password, salt1, salt2):
        return hashlib.md5(str(salt1 + password + salt2).encode('utf-8')).hexdigest()
