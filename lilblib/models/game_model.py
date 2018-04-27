class GameModel:

    def __init__(self, runtime):
        self._runtime = runtime
        self.game_id = None
        self.name = ''
        self.status = ''
        self.salt = ''
        self.created_at = ''
        self.updated_at = ''

    def read(self, game_id):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "SELECT * FROM games WHERE `game_id` = %s"
            cursor.execute(sql, (game_id,))
            result = cursor.fetchone()
            if result is not None:
                self.game_id = result['game_id']
                self.name = result['name']
                self.status = result['status']
                self.created_at = result['created_at']
                self.updated_at = result['updated_at']

    def update(self):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "UPDATE games set `name` = %s, `status` = %s where `game_id` = %s"
            cursor.execute(sql, (self.name, self.status, self.game_id))

    def create(self):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "INSERT INTO games (`game_id`, `name`, `status`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (self.game_id, self.name, self.status))

    def delete(self):
        with self._runtime.db_connection.cursor() as cursor:
            sql = "DELETE from games where `game_id` = %s"
            cursor.execute(sql, (self.game_id,))
