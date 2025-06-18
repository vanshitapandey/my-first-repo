class Person:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Name:", self.name)

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show(self):
        super().show()
        print("Employee ID:", self.emp_id)

# Test
e1 = Employee("Sita", 101)
e1.show()
