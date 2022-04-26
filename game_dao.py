class GameDao(object):
    def __init__(self, db):
        self.db = db
        self.cursor = self.db.cursor()

    def get_all_games(self):
        self.cursor.execute("SELECT * FROM game_data")
        return self.cursor.fetchall()

    def get_game_by_id(self, game_id):
        self.cursor.execute("SELECT * FROM game_data WHERE id = %s", (game_id,))
        return self.cursor.fetchone()

    def get_game_by_name(self, game_name):
        self.cursor.execute("SELECT * FROM game_data WHERE game_name = %s", (game_name,))
        return self.cursor.fetchone()

    def get_game_by_published_year(self, game_published_year):
        self.cursor.execute("SELECT * FROM game_data WHERE published_year = %s", (game_published_year,))
        return self.cursor.fetchall()

    def get_game_by_type(self, game_type):
        self.cursor.execute("SELECT * FROM game_data WHERE game_type = %s", (game_type,))
        return self.cursor.fetchall()

    def get_game_by_publisher_id(self, publisher_id):
        self.cursor.execute("SELECT * FROM game_data WHERE publisher_id = %s", (publisher_id,))
        return self.cursor.fetchall()

