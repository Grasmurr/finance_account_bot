from sqlalchemy import Integer, Column, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, default=None)
    full_name = Column(String, default=None)

    spendings = relationship("Spending", back_populates='user')
    categories = relationship("Category", back_populates='user')


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user(self, user_id: int):
        return self.session.query(User).filter_by(id=user_id).first()

    def create_user(self, user_id: int, username: str, full_name: str):
        new_user = User(id=user_id, username=username, full_name=full_name)
        self.session.add(new_user)
        self.session.commit()
        return new_user


