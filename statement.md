# Problem Statement

## Personal Expense Manager

**Author:** Naman Vashistha | **Registration Number:** 26BAI11081 | **Programme:** B.Tech AI/ML

---

## 1. Problem Statement

Individuals frequently lose track of small, recurring expenses because there is no simple, always-available tool to log them at the moment they happen. Spreadsheet tools are powerful but heavyweight for a quick entry, and most budgeting apps require an internet connection, an account, or a smartphone. This creates a gap for a fast, offline, zero-friction tool that lets a single user log an expense in seconds, understand where their money is going by category, and get warned when a category goes over budget — without any setup overhead.

## 2. Scope of the Project

The **Personal Expense Manager** is a single-user, command-line Python application. Its scope covers:

- Recording individual expenses (title, category, amount) with input validation.
- Persisting all expense data locally in a plain CSV file (`expenses.txt`), with no external database or network dependency.
- Viewing all recorded expenses in a readable, formatted table.
- Aggregating expenses by category and generating simple budget-overrun alerts against a fixed limit.
- Ranking and displaying the top *N* highest-value expenses.
- Detecting and removing duplicate expense entries to keep the dataset clean.

**Out of scope** for this version: multi-user support, authentication, a graphical/web interface, date-based reporting, and integration with bank accounts or external APIs (these are listed as future enhancements in the Project Report, Section 13).

## 3. Target Users

- **Students and young professionals** who want a fast, no-frills way to track day-to-day spending without installing a heavyweight app.
- **Developers/CS students** comfortable working in a terminal who prefer a lightweight, scriptable tool over a GUI budgeting app.
- Anyone who wants their financial data stored locally, in a transparent, human-readable format (CSV) rather than inside a proprietary app or cloud service.

## 4. High-Level Features

| # | Feature | Description |
|---|---|---|
| 1 | Add New Expense | Capture title, category, and amount with validation; auto-assign a unique ID. |
| 2 | View All Expenses | Display every stored expense in a clean, aligned table. |
| 3 | Check Category Totals | Compute per-category totals and raise alerts when a category exceeds the budget limit. |
| 4 | View Top Expenses | Sort and display the top *N* most expensive entries. |
| 5 | Remove Duplicates | Identify and remove expenses that are exact duplicates (same title, category, and amount). |
| 6 | Persistent Storage | Automatically save all changes to `expenses.txt` so data survives between sessions. |

## 5. Non-Functional Considerations

As detailed in the Project Report (Section 4), the design also accounts for:

- **Reliability** — file operations are wrapped in error handling so a missing/corrupted data file never crashes the program.
- **Usability** — a simple numbered menu with clear, consistent message prefixes (`[+]`, `[!]`, `[ALERT]`).
- **Maintainability** — a fully modular codebase, with I/O, validation, business logic, and display kept in separate functions.
- **Portability** — pure Python 3 standard library, runs identically on Windows, macOS, and Linux.

## 6. Success Criteria

The project is considered successful if a user can, without any setup beyond installing Python:
1. Add several expenses across different categories.
2. See an accurate, correctly formatted summary of all expenses.
3. Receive a clear alert whenever a category's spending crosses the defined budget.
4. Identify their largest expenses at a glance.
5. Trust that their data is preserved correctly between separate runs of the program.

*(For the full system architecture, UML diagrams, implementation details, and the complete 13-scenario test matrix, refer to the accompanying Project Report PDF.)*
