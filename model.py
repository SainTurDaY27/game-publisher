import sqlalchemy
from sqlalchemy import Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Publisher(base):
    __tablename__ = 'publisher'
    publisher_id = Column(Integer, primary_key=True)
    publisher_name = Column(String)


class GameData(base):
    __tablename__ = 'game_data'
    id = Column(Integer, primary_key=True, nullable=False)
    game_name = Column(String)
    published_year = Column(Integer)
    game_type = Column(String)
    publisher_id = Column(Integer, ForeignKey('publisher.publisher_id'))


