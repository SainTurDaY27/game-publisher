import sqlalchemy
from numpy import genfromtxt
from sqlalchemy import create_engine, Integer, String, ForeignKey, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

base = declarative_base()


class Publisher(base):
    __tablename__ = 'publisher'
    publisher_id = Column(Integer, primary_key=True)
    publisher_name = Column(String)

    # def __repr__(self):
    #     return f'publisher_id = {self.publisher_id}, publisher_name = {self.publisher_name}'


class Game_data(base):
    __tablename__ = 'game_data'
    id = sqlalchemy.Column(Integer, primary_key=True, nullable=False)
    game_name = Column(String)
    published_year = Column(Integer)
    game_type = Column(String)
    publisher_id = Column(Integer, ForeignKey('publisher.publisher_id'))

    # def __repr__(self):
    #     return "<Game_data(id='%s', game_name='%s', published_year='%s', publisher_id='%s')>" % (self.id, self.game_name, self.published_year, self.publisher_id)


engine = create_engine('sqlite:///game_data.db')
base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

with open('data/game_data.csv', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        record = Game_data(game_name=line[1], published_year=line[2], game_type=line[3], publisher_id=int(line[4]))
        session.add(record)
session.commit()

with open('data/publisher_data.csv', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        record = Publisher(publisher_name=line[1])
        session.add(record)
session.commit()

