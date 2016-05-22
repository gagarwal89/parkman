from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relation, sessionmaker

Base = declarative_base()

class UserTweets(Base):
    __tablename__ = 'user_tweets'

    status_id = Column(String(255), primary_key=True)
    screen_name = Column(String(255), nullable=False)
    in_reply_to_status_id = Column(String(255), nullable=True)

    def __init__(self, status_id, screen_name, in_reply_to_status_id):
        self.status_id = status_id
        self.screen_name = screen_name
        self.in_reply_to_status_id = in_reply_to_status_id

class Tweets(Base):
    __tablename__ = 'tweets'

    status_id = Column(String(255), primary_key=True)
    text = Column(String(255), nullable=True)

    def __init__(self, status_id, text=None):
        self.status_id = status_id
        self.text = text

engine = create_engine('dbms://root:1q2w3e4r@host/dbname')
Base.metadata.create_all(engine)