# Employee → Manager (Method Overriding)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def display(self):
        super().display()
        print("Role: Manager")

manager1 = Manager("Rohan", 60000)
manager1.display()
