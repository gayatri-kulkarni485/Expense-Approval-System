# Expense Approval System

This project is a simple and practical Expense Approval System built using FastAPI.

The idea behind it was to automate a process that is usually manual and repetitive — checking expense details, verifying receipts, and deciding whether an expense follows company policy or not. Instead of doing this by hand, the system applies rules automatically and gives a clear approval or review outcome.

---

## What this project does

- Allows users to submit expenses with a category, amount, and receipt
- Automatically checks the expense against predefined policies
- Flags expenses that require manual review
- Stores expense records so past submissions can be viewed
- Keeps the logic modular and easy to extend

This project is structured like a real backend system, not just a basic demo.

---

## Tech used

- **Python & FastAPI** for the backend
- **HTML + Jinja templates** for the user interface
- **SQLite** for storing expense data
- Modular Python files to keep business logic clean and readable

---

## Project structure (high level)
---

## How to run it locally

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt

2. Stsrt the server:
   uvicorn main:app --reload   

3. Open your browser and visit:
   http://127.0.0.1:8000

**Why I built this**
I built this project to get hands-on experience with:
Designing backend APIs using FastAPI
Structuring code in a clean, modular way
Implementing real-world workflows like approvals and validations
Connecting backend logic with a simple frontend
The project is designed so that new rules or features can be added easily without breaking existing functionality.

**Possible future improvements:**

1.User authentication and role-based access
2.Advanced receipt validation using OCR
3.An admin dashboard for approvals
4.Deployment to a cloud platform

**This project helped me understand how real backend systems are designed and structured, not just how they run.**  
