class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def display_table(self):
        print("Employee ID\tName\tAge\tSalary")
        for employee in self.employees:
            print(employee)

    def sort_table(self, sort_parameter):
        if sort_parameter == 1:
            self.employees.sort(key=lambda x: x.age)
        elif sort_parameter == 2:
            self.employees.sort(key=lambda x: x.name)
        elif sort_parameter == 3:
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid sorting parameter. Please choose 1 (Age), 2 (Name), or 3 (Salary).")

    def user_input_sort_parameter(self):
        try:
            sort_parameter = int(input("Enter sorting parameter (1. Age, 2. Name, 3. Salary): "))
            self.sort_table(sort_parameter)
            self.display_table()
        except ValueError:
            print("Invalid input. Please enter a valid number.")


employees_data = [
    Employee("161E90", "Ramu", 35, 59000),
    Employee("171E22", "Tejas", 30, 82100),
    Employee("171G55", "Abhi", 25, 100000),
    Employee("152K46", "Jaya", 32, 85000),
]


employee_table = EmployeeTable(employees_data)


employee_table.user_input_sort_parameter()
