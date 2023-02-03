from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, DateTime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key = True)
    fullname = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)
    address = Column(String, nullable = False)
    phone_number = Column(Integer, nullable = False)
    birth_date = Column(String, nullable = False)

    def __str__(self) -> str:
        return self.fullname