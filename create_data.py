from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from model import GameData, Publisher
import model

# base = declarative_base()
engine = create_engine('sqlite:///game_data.db')
model.base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

with open('data/game_data.csv', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        record = GameData(game_name=line[1], published_year=line[2], game_type=line[3], publisher_id=int(line[4]))
        session.add(record)
session.commit()

with open('data/publisher_data.csv', 'r', encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        line = line.split(',')
        record = Publisher(publisher_name=line[1])
        session.add(record)
session.commit()