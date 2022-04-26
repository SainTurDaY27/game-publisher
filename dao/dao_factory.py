from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from game_dao import GameDao
from publisher_dao import PublisherDao


class DaoFactory:
    def __init__(self):
        engine = create_engine('sqlite:///game_data.db', echo=True)
        self.session = Session(bind=engine)

    def get_dao(self, dao_type):
        if dao_type == 'publisher':
            return PublisherDao(self.session)
        elif dao_type == 'game':
            return GameDao(self.session)

