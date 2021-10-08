from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker


engine = create_engine('sqlite:////home/charliefunk/flask-projects/message/database/message.db', echo=True)
Base = declarative_base()
 
########################################################################
class Message(Base):
    """"""
    __tablename__ = "message"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    userid = Column(String)
    subject = Column(String)
    content = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, username, userid, subject, content):
        """"""
        self.username = username
        self.userid = userid
        self.subject = subject
        self.content = content

########################################################################
class User(Base):
    """"""
    __tablename__ = "user"
 
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    email = Column(String)

    #----------------------------------------------------------------------
    def __init__(self, username, password, email):
        """"""
        self.username = username
        self.password = password
        self.email = email

# create tables
Base.metadata.create_all(engine)

Database = sessionmaker(bind=engine)
database = Database()
