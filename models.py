from sqlalchemy import Column, Integer, String

from database import Base


class ToDo(Base):
    __tablename__ = 'todo'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __str__(self):
        return self.name
