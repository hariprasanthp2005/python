class Employee:

    def __init__(self, name, work, salary):
        self.name = name
        self.work = work
        self.salary = salary

    def details(self):
        print("\nEmployee Details")
        print("Name   :", self.name)
        print("Work   :", self.work)
        print("Salary :", self.salary)
        print("------------------------")


# Empty list to store employee objects
employees = []

# Taking input for 5 employees (change to 50 if needed)
for i in range(5):
    print(f"\nEnter details for Employee {i+1}")

    name = input("Enter name: ")
    work = input("Enter work: ")
    salary = int(input("Enter salary: "))

    # Create object
    emp = Employee(name, work, salary)

    # Store object in list
    employees.append(emp)


# Display all employee details
print("\nAll Employee Records")
print("========================")

for emp in employees:
    emp.details()