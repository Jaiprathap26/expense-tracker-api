from fastapi import FastAPI
from app.database import Base, engine
from app.routes import user, expense

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

app.include_router(user.router)
app.include_router(expense.router)