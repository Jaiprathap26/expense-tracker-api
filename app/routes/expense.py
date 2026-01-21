from fastapi import APIRouter, Depends 
from sqlalchemy.orm import Session
from datetime import date, timedelta
from app.database import SessionLocal
from app.models import Expense
from app.schemas import ExpenseCreate
from app.dependencies import get_current_user

router = APIRouter(prefix="/expenses")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def add_expense(expense: ExpenseCreate, db: Session = Depends(get_db)):
    new_expense = Expense(**expense.dict())
    db.add(new_expense)
    db.commit()
    return {"message": "Expense added"}

@router.get("/")
def list_expenses(filter: str = "week", db: Session = Depends(get_db)):
    today = date.today()

    if filter == "week":
        start = today - timedelta(days=7)
    elif filter == "month":
        start = today - timedelta(days=30)
    elif filter == "3months":
        start = today - timedelta(days=90)
    else:
        start = date(2000, 1, 1)

    return db.query(Expense).filter(Expense.date >= start).all()