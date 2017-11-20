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

    def to_dict(self):
        """Take all model attributes and render them as a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'markdown': self.markdown,
            'created': self.created
        }

Index('my_index', MyModel.id, unique=True, mysql_length=255)

