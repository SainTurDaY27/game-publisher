class GameDao(object):
    def __init__(self, session):
        self.session = session

    def get_all_games(self):
        self.session.execute("SELECT * FROM game_data")
        return self.session.fetchall()

    def get_game_by_id(self, game_id):
        self.session.execute("SELECT * FROM game_data WHERE id = %s", (game_id,))
        return self.session.fetchone()

    def get_game_by_name(self, game_name):
        self.session.execute("SELECT * FROM game_data WHERE game_name = %s", (game_name,))
        return self.session.fetchone()

    def get_game_by_published_year(self, game_published_year):
        self.session.execute("SELECT * FROM game_data WHERE published_year = %s", (game_published_year,))
        return self.session.fetchall()

    def get_game_by_type(self, game_type):
        self.session.execute("SELECT * FROM game_data WHERE game_type = %s", (game_type,))
        return self.session.fetchall()

    def get_game_by_publisher_id(self, publisher_id):
        self.session.execute("SELECT * FROM game_data WHERE publisher_id = %s", (publisher_id,))
        return self.session.fetchall()

    def update_game_data(self, game_id, game_name, game_published_year, game_type, publisher_id):
        self.session.execute("UPDATE game_data SET game_name = %s, published_year = %s, game_type = %s, publisher_id = %s WHERE id = %s", (game_name, game_published_year, game_type, publisher_id, game_id))
        self.session.commit()

