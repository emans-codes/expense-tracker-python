print("==============")
print("Expense Tracker")
print("==============")
expenses = []
def add_expense():
    expense = input("Enter expense name : ").strip()
    if not expense :
            print("Expense name cannot be empty !")
            return
    try :
            amount = float(input("Enter expense amount : "))
    except ValueError :
        print("Please enter a valid amount !")
        return
    if amount < 0 :
        print("Amount cannot be negative !")
        return
    expenses.append([expense , amount])
    print("Expense added successfully ! ")
def view_expenses():
    if not expenses:
        print("No expenses found !")
    else:
        print("Expenses :")
        for i, expense in enumerate(expenses, start=1):
            print(f"{i}. {expense[0]} : Rs. {int(expense[1])}")
def calculate_total() :
    total = 0
    for expense in expenses :
        total = total + expense[1]
    print("==============================")
    print(f"Total Expense = Rs. {int(total)}")
    print("==============================")
def delete_expense() :
    if not expenses :
            print("No expenses to delete!")
    else :
        for i, expense in enumerate(expenses, start=1) :
                print(f"{i}. {expense[0]} : Rs. {int(expense[1])}")
        try :
                delete = int(input("Enter expense number to delete : "))
        except ValueError :
                print("Please enter a number !")
                return
        if 1 <= delete <= len(expenses) :
                removed = expenses.pop(delete - 1)
                print(f"{removed[0]} deleted successfully!")
        else :
                print("Invalid expense number!")
def edit_expense() :
    if not expenses :
        print("No expenses to edit !")
    else :
        for i, expense in enumerate(expenses, start=1) :
            print(f"{i}. {expense[0]} : Rs. {int(expense[1])}")
        try :
            edit = int(input("Enter expense number to edit : "))
        except ValueError :
            print("Please enter a number !")
            return
        if 1 <= edit <= len(expenses) :
            new_name = input("Enter new expense name : ").strip()
            if not new_name :
                print("Expense name cannot be empty !")
                return
            try :
                new_amount = float(input("Enter new amount : "))
            except ValueError :
                print("Please enter a valid amount !")
                return
            if new_amount < 0 :
                print("Amount cannot be negative !")
                return
            expenses[edit - 1] = [new_name, new_amount]
            print("Expense updated successfully!")
        else :
            print("Invalid expense number!")
def main() :
    while True :
        print("\n==============")
        print("1. Add Expense")
        print("2. View Expense")
        print("3. Calculate Total")
        print("4. Exit")
        print("5. Delete Expense")
        print("6. Edit expense")
        print("==============")
        try :
            choice = int(input("Enter your choice (1,2,3,4,5,6) = "))
        except ValueError :
            print("Please enter a number !")
            continue
        if choice == 4 :
            print("GoodBye !")
            break
        elif choice == 1 :
            add_expense()
        elif choice == 2 :
            view_expenses()
        elif choice == 3 :
            calculate_total()
        elif choice == 5 :
            delete_expense()
        elif choice == 6 :
            edit_expense()
        else :
            print("Invalid choice ! Please enter 1, 2, 3, 4, 5, 6.")
main()



            


            

        
        







