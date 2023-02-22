class Student:
    schoolName  = None
    schoolAddress = None

    def __init__(self,studentid=None,studentRollno=None,studentName=None,studentMailid=None,studentPercentage=None):
        self.studentid = studentid
        self.studentRollno = studentRollno
        self.studentName = studentName
        self.studentMailid = studentMailid
        self.studentPercentage = studentPercentage

    def get_student_name(self):
        return self.studentName

    def get_name_with_percentage(self):
        return "Hi " + self.studentName + "- Your Percentage is " + str(self.studentPercentage)

