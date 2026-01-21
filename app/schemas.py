from pydantic import BaseModel
from datetime import date

class UserCreate(BaseModel):
    email: str
    password: str

class ExpenseCreate(BaseModel):
    title: str
    amount: float
    Category: str
    date: date

class ExpenseOut(BaseModel):
    id: int
