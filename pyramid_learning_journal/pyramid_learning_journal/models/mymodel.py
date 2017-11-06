from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Date
)
import datetime
from .meta import Base


class MyModel(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    markdown = Column(Text)
    created = Column(Date)


Index('my_index', MyModel.id, unique=True, mysql_length=255)

