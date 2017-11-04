from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)
import datetime
from .meta import Base


class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)


class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    body = Column(Text)
    date_created = Column(DateTime)


Index('my_index', MyModel.name, unique=True, mysql_length=255)
