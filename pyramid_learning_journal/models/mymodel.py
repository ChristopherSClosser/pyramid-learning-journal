"""Entry model."""

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date
)
from .meta import Base


class MyModel(Base):
    """Entry class."""

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Text)
    markdown = Column(Text)
    created = Column(Date)
