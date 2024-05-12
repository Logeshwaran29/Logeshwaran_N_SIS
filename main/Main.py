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
        pass

    def assign_Teacher(self):
        pass

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

    def get_Enrollments(self):
        pass

    def run(self):
        while True:
            print("\n1. Create Student")
            print("2. Create Teacher")
            print("3. Create Course")
            print("4. Enroll Course")
            print("5. Assign Teacher")
            print("6. Make Payment")
            print("7. Get Enrollments")
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
            elif option == 7:
                self.get_Enrollments()
            elif option == 0:
                return
            else:
                print('Enter Correct Option...')


if __name__ == "__main__":
    app = Main()
    app.run()
