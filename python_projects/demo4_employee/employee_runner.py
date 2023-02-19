from demo4_employee.employee_module import Employee

Employee.company_name = "iFuture"
Employee.company_location = "Pune"

print(Employee.company_name)
print(Employee.company_location)

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp2.employee_id=102
emp2.employee_name="kim"
emp2.employee_salary=10000
emp2.employee_performance="B"


print(emp1.employee_id)
print(emp2.employee_id)
print(emp3.employee_id)
