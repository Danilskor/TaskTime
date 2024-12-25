
class Employees:
    def __init__(self):
        self._employees = []

    def add_employee(self, name, surname):
        employee = {"name": name, "surname": surname}
        self._employees.append(employee)

    def dell_employee(self, name, surname):
        pass