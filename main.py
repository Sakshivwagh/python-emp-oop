# Main file
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, employee_id, name, department):
        print("__init__ of Employee")
        self.__employee_id = employee_id
        self.__name = name
        self.__department = department

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_details(self):
        print("\n--- Employee Details ---")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Name: {self.__name}")
        print(f"Department: {self.__department}")

class PermanentEmployee(Employee):
    def __init__(self, employee_id, name, department, basic_salary, bonus):
        print("__init__ of PermanentEmployee")
        super().__init__(employee_id, name, department)
        self.__basic_salary = basic_salary
        self.__bonus = bonus

    def calculate_salary(self):
        return self.__basic_salary + self.__bonus

    def display_details(self):
        super().display_details()
        print(f"Basic Salary: ${self.__basic_salary:.2f}")
        print(f"Bonus: ${self.__bonus:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

class ContractEmployee(Employee):
    def __init__(self, employee_id, name, department, hourly_rate, hours_worked):
        print("__init__ of ContractEmployee")
        super().__init__(employee_id, name, department)
        self.__hourly_rate = hourly_rate
        self.__hours_worked = hours_worked

    def calculate_salary(self):
        return self.__hourly_rate * self.__hours_worked

    def display_details(self):
        super().display_details()
        print(f"Hourly Rate: ${self.__hourly_rate:.2f}")
        print(f"Hours Worked: {self.__hours_worked}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

class Intern(Employee):
    def __init__(self, employee_id, name, department, stipend):
        print("__init__ of Intern")
        super().__init__(employee_id, name, department)
        self.__stipend = stipend

    def calculate_salary(self):
        return self.__stipend

    def display_details(self):
        super().display_details()
        print(f"Stipend: ${self.__stipend:.2f}")
        print(f"Total Salary: ${self.calculate_salary():.2f}")

permanent_emp = PermanentEmployee("P123", "Alice Johnson", "IT", 60000, 5000)
contract_emp = ContractEmployee("C456", "Bob Smith", "HR", 50, 160)
intern = Intern("I789", "Charlie Brown", "Finance", 1500)

permanent_emp.display_details()
contract_emp.display_details()
intern.display_details()
