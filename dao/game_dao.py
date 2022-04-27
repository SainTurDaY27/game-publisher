from model import GameData


class GameDao(object):
    def __init__(self, session):
        self.session = session

    def get_all_games(self):
        return self.session.query(GameData).all()

    def get_game_by_id(self, game_id):
        return self.session.query(GameData).filter_by(id=game_id).first()

    def get_game_by_name(self, game_name):
        return self.session.query(GameData).filter_by(game_name=game_name).first()

    def get_game_by_published_year(self, game_published_year):
        return self.session.query(GameData).filter_by(published_year=game_published_year).first()

    def get_game_by_type(self, game_type):
        return self.session.query(GameData).filter_by(game_type=game_type).all()

    def get_game_by_publisher_id(self, publisher_id):
        return self.session.query(GameData).filter_by(publisher_id=publisher_id).all()

    def update_game_data(self, game_id, game_name, game_published_year, game_type, publisher_id):
        game = self.session.query(GameData).filter_by(id=game_id).first()
        game.game_name = game_name
        game.published_year = game_published_year
        game.game_type = game_type
        game.publisher_id = publisher_id
        self.session.commit()

    def add_game_data(self, game_name, game_published_year, game_type, publisher_id):
        game = GameData(game_name, game_published_year, game_type, publisher_id)
        self.session.add(game)
        self.session.commit()

    def remove_game_data_by_id(self, game_id):
        game = self.session.query(GameData).filter_by(id=game_id).first()
        self.session.delete(game)
        self.session.commit()

    def remove_game_data_by_name(self, game_name):
        game = self.session.query(GameData).filter_by(game_name=game_name).first()
        self.session.delete(game)
        self.session.commit()




