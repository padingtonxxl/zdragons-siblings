class PlayerModel:

    def __init__(self, runtime):
        self._runtime = runtime
        self.id = 0
        self.name = ''
        self.password = ''
        self.salt = ''
        self.created_at = ''
        self.updated_at = ''

    def read(self, player_id):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "SELECT * FROM players WHERE `id` = %s"
            cursor.execute(sql, (player_id,))
            result = cursor.fetchone()
            self._apply_read_result(result)

    def read_by_name(self, player_name):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "SELECT * FROM players WHERE `name` = %s"
            cursor.execute(sql, (player_name,))
            result = cursor.fetchone()
            self._apply_read_result(result)

    def update(self):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "UPDATE players set `name` = %s, `password` = %s, `salt` = %s where `id` = %s"
            cursor.execute(sql, (self.name, self.password, self.salt, self.id))

    def create(self):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "INSERT INTO players (`name`, `password`, `salt`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (self.name, self.password, self.salt))
        self.read_by_name(self.name)

    def delete(self):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "DELETE from players where `id` = %s"
            cursor.execute(sql, (self.id))

    def _apply_read_result(self, result):
        self.id = result['id']
        self.name = result['name']
        self._password = result['password']
        self._salt = result['salt']
        self.created_at = result['created_at']
        self.updated_at = result['updated_at']
