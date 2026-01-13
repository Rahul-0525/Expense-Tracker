# Monthly Expense Tracker (Python CLI)

A command-line based expense tracking system that allows users to record, manage, and analyze their expenses month by month.
The project was built to explore object-oriented design, modularity, persistence, and real-world data modeling in Python.

## What this project does

This program allows a user to:
• Add expenses with amount, category, and date <br>
• Automatically organize expenses by month and year<br>
• Switch between different months<br>
• View all expenses of a selected month<br>
• View expenses across all months<br>
• Save all data to a file so nothing is lost between runs<br>

All months are stored internally in a single database, while the program dynamically loads and edits one month at a time.

---
## Design overview

The system is built around three main ideas.

### Month-wise data storage
All expense data is stored in a dictionary of dictionaries.
Each key represents a month and year in the form MMYYYY (for example 032024).
Each value stores all expenses for that month.
This makes it possible to keep all history in one place while still working on one month at a time.

### ExpenseList as a worker object
Only one ExpenseList object exists at any moment.
It does not own data itself. Instead, it operates on whichever month’s dictionary is currently active.

When the user switches months, the object simply switches which dictionary it works on.
This keeps the system modular, efficient, and easy to extend.

### Persistent storage
All data is saved in a file called data.json using Python’s json module.
When the program starts, this file is loaded so all previous expenses are restored automatically.

---

## File structure

The project contains:<br>
• ExpenseTracker.py – the main program<br>
• data.json – stored expense data (created automatically)<br>
• README.md – project documentation<br>

---

## What this project demonstrates

This project was built to practice:
• OOP design<br>
• Exception handling<br>
• File handling<br>
• Data modeling<br>
• State management<br>
• Modular thinking<br>
• Git and GitHub workflow<br>

---

## Technologies used

• Python 3<br>
• Object-oriented programming<br>
• JSON for file storage<br>
• datetime module for handling dates<br>

---

## How to run

Make sure Python 3 is installed

Clone the repository

Run the program using:
python main.py

The file data.json will be created automatically when you save data.

---

## Author

Built by Rahul as a learning project to explore real-world software design using Python.
