from employee_module import Employee

Employee.company_name = "iFuture"
Employee.company_location = "Pune"

print(Employee.company_name)
print(Employee.company_location)

emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp2.employee_id=102
emp2.employee_name="kim"
emp2.employee_salary=5000
emp2.employee_performance="B"


print(emp1.employee_id)
print(emp2.employee_id)
print(emp3.employee_id)

Employee.print_author()


emp2.display_employee_record()
emp2.calculate_bonus()
emp2.display_employee_record()
