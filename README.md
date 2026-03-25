# CLI Expense Tracker

##  Description

CLI Expense Tracker is a Python-based command-line application that helps users efficiently manage their daily expenses. It allows users to record expenses, view transaction history, and analyze spending patterns through category-wise summaries. The application uses JSON for persistent data storage and runs entirely in a terminal environment.

---

##  Features

* Add new expenses with amount and category
* View all recorded expenses
* Display category-wise expense summary
* Automatic date tracking for each expense
* Data stored locally using JSON

---

##  Tech Stack

* Python
* JSON (for data storage)

---

##  Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/yadavalli25bai10136-a11y/CLI-Based-Expense-Tracker
```

### Step 2: Navigate to the project directory

```bash
cd CLI-Based-Expense-Tracker
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

---

##  Usage

Run the application using:

```bash
python main.py
```

---

##  Project Structure

```
CLI-Based-Expense-Tracker/
│
├── main.py         # Entry point (CLI interface)
├── expense.py      # Handles expense operations
├── storage.py      # Manages JSON file operations
├── data.json       # Auto-created data storage file
├── requirements.txt
└── README.md
```

---

##  Example Output

```
--- Expense Tracker ---
1. Add Expense
2. View Expenses
3. Show Summary
4. Exit
```

---

##  Notes

* Ensure Python is installed on your system
* No external libraries are required
* The `data.json` file will be created automatically after adding the first expense
* The application runs entirely through the terminal (no GUI required)

---

## Learning Outcomes

* Understanding file handling in Python
* Working with JSON for data storage
* Designing a command-line interface
* Writing modular and structured code

---

##  Author

Lokesh Yadavalli
