# python-expense-manager
# 💰 Personal Expense Manager

A lightweight, command-line Python application to track, analyse, and manage personal expenses — built for the VITyarthi **"Build Your Own Project"** evaluation.

**Author:** Naman Vashistha
**Registration Number:** 26BAI11081
**Programme:** B.Tech — Artificial Intelligence & Machine Learning
**Full documentation:** see the accompanying **Project Report (PDF)** for diagrams, architecture, and test results.

---

## 📖 Overview

Managing day-to-day personal finances is a challenge most people face, yet most rely on memory or scattered notes to track where their money goes. **Personal Expense Manager** solves this with a fast, offline, zero-dependency CLI: log an expense in seconds, view everything in a clean table, see category-wise totals with budget alerts, find your biggest expenses, and clean up duplicates — all backed by durable local storage.

## ✨ Features

| Feature | Description |
|---|---|
| **Add New Expense** | Capture title, category, and amount with input validation; auto-assigns a unique ID. |
| **View All Expenses** | Neatly formatted table of every stored expense. |
| **Check Category Totals** | Per-category spending totals with automatic budget-overrun alerts (default limit: $500/category). |
| **View Top Expenses** | Shows the top *N* biggest expenses, ranked highest to lowest. |
| **Remove Duplicates** | Detects and removes accidental duplicate entries (same title + category + amount). |
| **Persistent Storage** | All data is saved to `expenses.txt` (CSV format) immediately after every change. |

## 🏗️ Architecture

The app follows a simple, single-process, layered design (see Section 5 of the Project Report for the full diagram):

- **Presentation / Control Layer** — `main()` renders the menu, reads choices, and routes them.
- **Core Logic Layer** — pure functions operating on the in-memory expense list: `addExpense`, `getTotals`, `getTopExpenses`, `removeDuplicates`, `showAlerts`.
- **Persistence Layer** — `loadData()` / `saveData()` translate between memory and the CSV file on disk.

Each expense is a Python dictionary: `{"id": int, "title": str, "category": str, "amount": float}`.

## 🛠️ Technologies / Tools Used

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Storage | Flat CSV file (`expenses.txt`) via the built-in `csv` module |
| Interface | Command-line (stdin/stdout) |
| Dependencies | None — Python standard library only |
| Version Control | Git & GitHub |

## 📂 Project Structure

```
personal-expense-manager/
├── expenses.py      # Main application source code
├── expenses.txt      # Auto-created CSV data file (generated on first run)
├── README.md         # This file
├── statement.md       # Problem statement, scope, target users & features
└── .gitignore         # Excludes expenses.txt, __pycache__, etc.
```

## 🚀 Steps to Install & Run

1. **Prerequisite:** Python 3.10+ installed ([download here](https://www.python.org/downloads/)).
2. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/personal-expense-manager.git
   cd personal-expense-manager
   ```
3. Run the application (no extra packages required):
   ```bash
   python3 expenses.py
   ```
4. Use the on-screen menu (options `1`–`6`) to manage your expenses. Data is saved automatically to `expenses.txt` in the same folder.

## 🧪 Instructions for Testing

The application was verified through 13 manual test scenarios covering normal paths, boundary conditions, and invalid input (full matrix in Section 10 of the Project Report). Quick checks you can run yourself:

1. **Add an expense** → option `1` → confirm `[+] Expense saved.` and a new row in `expenses.txt`.
2. **View all expenses** → option `2` → confirm a formatted table appears.
3. **Trigger a budget alert** → add expenses in one category totalling more than $500 → option `3` → confirm an `[ALERT]` line prints.
4. **View top expenses** → option `4`, enter a number → confirm results are sorted highest to lowest.
5. **Remove duplicates** → add the exact same expense twice → option `5` → confirm one copy is removed.
6. **Persistence check** → exit (`6`) and re-run → confirm previous expenses are still there.
7. **Invalid input handling** → enter text for an amount, or `0`/negative values → confirm the program re-prompts instead of crashing.
8. **Invalid menu choice** → enter e.g. `9` → confirm `[!] Please choose a number from 1 to 6.` prints.

## 📸 Screenshots

Real terminal screenshots (adding an expense, viewing the table, and budget alerts) are included in the **Project Report (PDF)**, Section 9.

## 📈 Future Enhancements

- Per-category, user-configurable budget limits (instead of a fixed $500).
- Date tracking for monthly/weekly spending summaries and trend charts.
- Edit/delete operations for individual expense records.
- Migration to SQLite for stronger data integrity at scale.
- Optional GUI/web front-end and spending visualisations (matplotlib charts).
- Automated unit tests using `pytest`.

## 📄 License

This project was created for academic purposes as part of a VITyarthi course evaluation.

