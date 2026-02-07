from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import sqlite3
import shutil
import os
from datetime import datetime

app = FastAPI()

# Templates & Static
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

DB_NAME = "expenses.db"

# ---------------- DATABASE ----------------
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,
            amount REAL,
            status TEXT,
            policy TEXT,
            time TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# ---------------- HOME ----------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM expenses ORDER BY id DESC")
    expenses = cur.fetchall()
    conn.close()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "expenses": expenses
        }
    )

# ---------------- SUBMIT ----------------
from fastapi.responses import RedirectResponse

@app.post("/submit-expense")
async def submit_expense(
    category: str = Form(...),
    amount: float = Form(...),
    receipt: UploadFile = File(...)
):
    os.makedirs("receipts", exist_ok=True)
    receipt_path = f"receipts/{receipt.filename}"

    with open(receipt_path, "wb") as buffer:
        shutil.copyfileobj(receipt.file, buffer)

    # Policy logic
    if category.lower() == "food" and amount <= 500:
        status = "APPROVED"
        policy = "Within food limit"
    else:
        status = "PENDING"
        policy = "Manual review required"

    conn = sqlite3.connect("expenses.db")
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO expenses (category, amount, status, policy, time)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            category,
            amount,
            status,
            policy,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )
    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=303)