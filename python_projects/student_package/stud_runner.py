from student_package.student_module import Student

Student.schoolName = "Global school"
Student.schoolAddress = "chennai"

student1 = Student()
student2 = Student()
student3 = Student()

student1.studentRollno = 1001
student1.studentName = "jack"
student1.studentMailid ="jack@gmail.com"
student1.studentPercentage = 45.2

student2.studentRollno = 1002
student2.studentName = "Max5"
student2.studentMailid ="max@gmail.com"
student2.studentPercentage = 85.2

student3.studentRollno = 1003
student3.studentName = "Peter"
student3.studentMailid ="peter@gmail.com"
student3.studentPercentage = 56.2

print(student1.studentMailid)
student2.studentMailid = student1.studentMailid
print(student2.studentMailid)
print(student3.studentMailid)

