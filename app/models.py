from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    email = Column(String(100), unique = True, index = True)
    password = Column(String(255))

    expenses = relationship("Expense", back_populates = "owner")


class Expense(Base):
    __tablename__ = "Expenses"

    id = Column(Integer, primary_key = True)
    title = Column(String(100))
    amount = Column(Float)
    Category = Column(String(50))
    date = Column(Date)
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates = "expenses")
