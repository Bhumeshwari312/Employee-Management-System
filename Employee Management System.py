employees = {101: {
            'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000.0},
        102: {
            'name': 'Arjun', 'age': 30, 'department': 'IT', 'salary': 75000}}

def add_employee():
    while True:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee ID already exists!")
        else:
            break
    name = input("Enter Employee Name: ")
    age = int(input("Enter Employee Age: "))
    department = input("Enter Department: ")
    salary = int(input("Enter Salary: "))

    employees[emp_id] = {
        "name": name,
        "age": age,
        "department": department,
        "salary": salary
    }

    print("Employee added sucessfully!")
        
def view_employees():
    if not employees:
        print("No employee available.")
    else:
        print("\nEmployee Details: ")

        for emp_id, details in employees.items():
            print("ID:", emp_id)
            print("Name:", details["name"])
            print("Department:", details["department"])
            print("Salary:", details["salary"])
            print("-" * 45)

def search_employee():
    emp_id = int(input("Enter Employee ID to search: "))
    if emp_id in employees:
        emp = employees[emp_id]

        print("\nEmployee Found: ")
        print("Name:", emp["name"])
        print("Age:", emp["age"])
        print("salary:", emp["salary"])
    else:
        print("Employee not found.")

def main_menu():
    while True:
        
        print("\n -----Employee Management System-----")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice from 1-4: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            print("Thank you for using EMS!")
            break
        
        else:
            print("Invalid choice.Try again.")

main_menu()