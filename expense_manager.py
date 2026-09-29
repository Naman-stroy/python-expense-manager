import csv
import os

fileName = os.path.join(os.path.dirname(os.path.abspath(__file__)), "expenses.txt")


def loadData():
    expenses = []

    try:
        with open(fileName, "r", newline="") as file:
            rows = csv.reader(file)

            for row in rows:
                if len(row) != 4:
                    continue

                try:
                    expense = {
                        "id": int(row[0]),
                        "title": row[1],
                        "category": row[2],
                        "amount": float(row[3])
                    }

                    expenses.append(expense)

                except ValueError:
                    continue

    except OSError:
        pass

    return expenses


def saveData(expenses):
    with open(fileName, "w", newline="") as file:
        writer = csv.writer(file)

        for expense in expenses:
            writer.writerow([
                expense["id"],
                expense["title"],
                expense["category"],
                expense["amount"]
            ])


def getAmount():
    while True:
        try:
            amount = float(input("Enter the amount: "))

            if amount > 0:
                return amount

            print("[!] Amount must be more than 0.")

        except ValueError:
            print("[!] Please enter a number.")


def getNumber():
    while True:
        try:
            number = int(input("Enter the number: "))

            if number > 0:
                return number

            print("[!] Number must be more than 0.")

        except ValueError:
            print("[!] Please enter a whole number.")


def addExpense(expenses, title, category, amount):

    if len(expenses) == 0:
        newId = 1
    else:
        newId = max(x["id"] for x in expenses) + 1

    expense = {
        "id": newId,
        "title": title.strip().title(),
        "category": category.strip().capitalize(),
        "amount": amount
    }

    expenses.append(expense)
    saveData(expenses)


def getTotals(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]

        if category not in totals:
            totals[category] = 0

        totals[category] += expense["amount"]

    return totals


def getTopExpenses(expenses, number):
    expenses = sorted(
        expenses,
        key=lambda x: x["amount"],
        reverse=True
    )

    return expenses[:number]


def removeDuplicates(expenses):
    seen = set()
    newList = []

    for expense in expenses:

        check = (
            expense["title"].lower(),
            expense["category"].lower(),
            expense["amount"]
        )

        if check not in seen:
            seen.add(check)
            newList.append(expense)

    return newList


def showExpenses(expenses):

    if len(expenses) == 0:
        print("\n[!] No expenses yet.")
        return

    print("\n" + "=" * 50)

    print("{:<5} | {:<15} | {:<12} | {:<8}".format(
        "ID", "Title", "Category", "Amount"
    ))

    print("=" * 50)

    for expense in expenses:
        print("{:<5} | {:<15} | {:<12} | ${:<8.2f}".format(
            expense["id"],
            expense["title"],
            expense["category"],
            expense["amount"]
        ))

    print("=" * 50)


def showAlerts(totals, limit):

    print("\n--- BUDGET ALERTS (Limit: ${:.2f}) ---".format(limit))

    found = False

    for category in totals:
        total = totals[category]

        if total > limit:
            print(
                "[ALERT] {} is over by ${:.2f} (Total: ${:.2f})".format(
                    category,
                    total - limit,
                    total
                )
            )

            found = True

    if found == False:
        print("[+] All categories are within budget.")


def main():

    expenses = loadData()
    limit = 500.0

    while True:

        print("\n-- PERSONAL EXPENSE MANAGER --")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Check Category Totals")
        print("4. View Top Expenses")
        print("5. Remove Duplicates")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":

            title = input("Enter expense title: ")
            category = input("Enter category: ")

            if title == "" or category == "":
                print("[!] Title and category cannot be empty.")
                continue

            amount = getAmount()

            addExpense(expenses, title, category, amount)

            print("[+] Expense saved.")

        elif choice == "2":

            showExpenses(expenses)

        elif choice == "3":

            totals = getTotals(expenses)

            showAlerts(totals, limit)

        elif choice == "4":

            if len(expenses) == 0:
                print("[!] No expenses found.")
                continue

            number = getNumber()

            top = getTopExpenses(expenses, number)

            showExpenses(top)

        elif choice == "5":

            oldNumber = len(expenses)

            expenses = removeDuplicates(expenses)

            saveData(expenses)

            removed = oldNumber - len(expenses)

            print("[+] Removed {} duplicate(s).".format(removed))

        elif choice == "6":

            print("Goodbye!")
            break

        else:

            print("[!] Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
