class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"<Student {self.name}, {self.grade}>"

student = Student("Maulin", 1)
student1 = Student("Maulin1", 2)
student2 = Student("Maulin2", 3)
stu = [Student("Maulin", 2), Student("Max", 1),Student("Max1", 3)]
stu.sort(key=lambda x: x.grade)
print(stu)
print(student1)

