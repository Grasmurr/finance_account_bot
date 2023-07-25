from sqlalchemy import Integer, Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class Spending(Base):
    __tablename__ = 'spendings'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="spendings")
