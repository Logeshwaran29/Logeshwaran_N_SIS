from entity.student import Student
from entity.course import Course
from entity.teacher import Teacher
from dao.SIS import SIS
from dao.Course import course
from dao.Student import student
from dao.Teacher import teacher
from datetime import date


class Main:
    def __init__(self):
        self.sisMethod = SIS()
        self.stuMethod = student()
        self.teachMethod = teacher()
        self.courseMethod = course()

    def create_Student(self):
        print('\n--- Create Student ---')
        studID = int(input('Enter Student ID:'))
        firstName = input('Enter FirstName:')
        lastName = input('Enter LastName:')
        dob = input('Enter dob:')
        email = input('Enter Email:')
        phNo = input('Enter Phone Number:')
        stu = Student(studID, firstName, lastName, dob, email, phNo)
        self.stuMethod.createStudent(stu)

    def create_Teacher(self):
        print('\n--- Create Teacher ---')
        teachID = int(input('Enter Teacher ID:'))
        firstName = input('Enter FirstName:')
        lastName = input('Enter LastName:')
        email = input('Enter Email:')
        teach = Teacher(teachID, firstName, lastName, email)
        self.teachMethod.createTeacher(teach)

    def create_Course(self):
        print('\n--- Create Course ---')
        courseID = int(input('Enter Course ID:'))
        courseName = input('Enter Course Name:')
        courseCode = input('Enter Course Code:')
        cour = Course(courseID, courseName, courseCode, None)
        self.courseMethod.CreateCourse(cour)

    def enroll_Course(self):
        print('\n--- Enroll Course ---')
        studID = int(input('Enter StudentID:'))
        s = self.stuMethod.getStudent(studID)
        if not s:
            print('Enter Correct StudentID!')
        stu = Student(s[0][0], s[0][1], s[0][2], s[0][3], s[0][4], s[0][5])
        c = self.courseMethod.DisplayCourseInfo()
        print('--- Course List ---')
        n = 1
        for i in c:
            print(f'''{n}:''', i)
            n += 1
        op = int(input('Enter Option from Course List:'))-1
        cour = Course(c[op][0], c[op][1], c[op][2], c[op][3])
        self.sisMethod.enrollStudent(stu, cour)

    def assign_Teacher(self):
        c = self.courseMethod.DisplayCourseInfo()
        print('--- Course List ---')
        n = 1
        for i in c:
            print(f'''{n}:''', i)
            n += 1
        op = int(input('Enter Option from Course List:')) - 1
        cour = Course(c[op][0], c[op][1], c[op][2], c[op][3])
        t = int(input('Enter TeacherID:'))
        r = self.teachMethod.DisplayTeacherInfo(t)
        if not r:
            print('Enter Correct TeacherID!')
        teach = Teacher(r[0][0], r[0][1], r[0][2], r[0][3])
        self.sisMethod.assignTeacherToCourse(cour, teach)

    def make_payment(self):
        print('\n--- Make Payment ---')
        studID = int(input('Enter Student ID:'))
        firstName = input('Enter FirstName:')
        lastName = input('Enter LastName:')
        dob = input('Enter dob:')
        email = input('Enter Email:')
        phNo = input('Enter Phone Number:')
        stu = Student(studID, firstName, lastName, dob, email, phNo)
        amt = int(input('Enter Amount:'))
        self.sisMethod.recordPayment(stu, amt, date.today())

    def run(self):
        while True:
            print("\n1. Create Student")
            print("2. Create Teacher")
            print("3. Create Course")
            print("4. Enroll Course")
            print("5. Assign Teacher")
            print("6. Make Payment")
            print("0. Exit")
            option = int(input('Enter Option:'))

            if option == 1:
                self.create_Student()
            elif option == 2:
                self.create_Teacher()
            elif option == 3:
                self.create_Course()
            elif option == 4:
                self.enroll_Course()
            elif option == 5:
                self.assign_Teacher()
            elif option == 6:
                self.make_payment()
            elif option == 0:
                return
            else:
                print('Enter Correct Option...')


if __name__ == "__main__":
    app = Main()
    app.run()
