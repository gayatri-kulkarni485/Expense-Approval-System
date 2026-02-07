# Expense Approval System – Project Documentation

## Overview
The Expense Approval System is a FastAPI-based backend application designed to automate
expense validation and approval workflows. It replaces manual checking with rule-based
decisions, improving consistency and efficiency.

---

## Problem Statement
Manual expense approvals are time-consuming, repetitive, and error-prone.
This project automates policy checks, validates expense details, and provides
clear approval or review outcomes.

---

## Tech Stack
- Backend: FastAPI (Python)
- Database: SQLite
- Frontend: HTML (Jinja Templates)
- File Handling: Receipt uploads
- Architecture: Modular, agent-based design

---

## System Architecture
The application follows a modular backend structure:
- API layer handles requests
- Policy and fraud checks are isolated into agents
- Database persists expense data
- Frontend renders results dynamically

---

## Key Features
- Expense submission with category, amount, and receipt
- Automatic policy validation
- Approval or manual review decision
- Persistent expense storage
- Clean and extensible backend design

---

## Workflow
1. User submits an expense
2. System validates input data
3. Policy rules are applied
4. Expense is auto-approved or flagged
5. Result is stored and displayed

---

## Folder Structure
agents/        → Business logic (policy, fraud, routing)  
templates/     → HTML frontend  
data/          → Policy configuration  
main.py        → FastAPI entry point  
docs/          → Project documentation  

---

## How to Run Locally
1. Install dependencies  
   pip install -r requirements.txt

2. Start the server  
   uvicorn main:app --reload

3. Open browser  
   http://127.0.0.1:8000

---

## Future Improvements
- Authentication and role-based access
- OCR-based receipt validation
- Admin dashboard for approvals
- Cloud deployment

---

## Conclusion
This project demonstrates how real-world backend systems are structured,
not just how APIs are written. It focuses on clean architecture,
scalability, and maintainable code.
