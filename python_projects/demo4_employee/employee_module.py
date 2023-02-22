class Employee:
    company_name = None
    company_location = None

    def __init__(self):
        self.employee_id = None
        self.employee_name = None
        self.employee_salary = None
        self.employee_performance = None

    @staticmethod
    def print_author():
        print("Maulin Desai")

    def display_employee_record(self):
        print(35 * "-")
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Employee SaLary:", self.employee_salary)
        print("Employee Performance:", self.employee_performance)
        print("Company Location:", Employee.company_location)
        print("Company Name:", Employee.company_name)
        print(35 * "-")

    def calculate_bonus(self):
        if self.employee_performance == "A":
            self.employee_salary = self.employee_salary + self.employee_salary * 10 / 100
        elif self.employee_performance == "B":
            self.employee_salary = self.employee_salary+ self.employee_salary * 5 / 100
        elif self.employee_performance == "C":
            self.employee_salary = self.employee_salary + self.employee_salary * 2 / 100

