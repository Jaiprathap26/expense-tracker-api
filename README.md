# Expense Tracker API

A backend Expense Tracker API built using FastAPI and MySQL with JWT-based authentication.

## 🚀 Features
- User Signup & Login
- JWT Authentication
- Add, Update, Delete Expenses
- View Expenses per User
- Secure password hashing using bcrypt

## 🛠 Tech Stack
- FastAPI
- Python
- MySQL
- SQLAlchemy ORM
- JWT Authentication
- Passlib (bcrypt)

## 📂 Project Structure
app/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── dependencies.py
└── routes/
├── user.py
└── expense.py 


## ⚙️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/YOUR_USERNAME/expense-tracker-api.git
cd expense-tracker-api

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup MySQL Database
CREATE DATABASE expense_db;


Update DB credentials in database.py.

5️⃣ Run Server
uvicorn app.main:app --reload


Open:

http://127.0.0.1:8000/docs

🧪 API Testing

Swagger UI

Postman