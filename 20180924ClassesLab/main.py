class Student:
    def __init__(self, fullName, studentID):
        self.name = fullName
        self.id = studentID
        self.credits = 0

    def addCredits(self, creditAddition):
        self.credits += creditAddition

    def getLoginName(self):
        print(self.name[0:4] + self.id[0:3])

    def printStudent(self):
        print("Full name: " + self.name + ", Student ID: " + self.id + ", Amount of Credits: " + repr(self.credits))

    def changeName(self, newName):
        self.name = newName

class Lab:
    def __init__(self, maximumStudents):
        self.teacher = "unknown"
        self.room = "unknown" 
        self.timeAndDay = "unknown"
        self.listOfStudents = []

    def addStudentToCourse(self, student):
        self.listOfStudents.append(student)

    def setTeacher(self, teacherName):
        self.teacher = teacherName

    def setTimeAndDay(self, date):
        self.timeAndDay = date

if __name__ == "__main__":
    s1 = Student("Dries Augustyns", "DG35FQSF")
    s2 = Student("Marcin Kostulski", "EZGGNORE")
    s3 = Student("Bats Mos", "E523FHR")
    l1 = Lab(10)
    l2 = Lab(5)