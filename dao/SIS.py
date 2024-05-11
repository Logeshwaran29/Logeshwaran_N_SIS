from util.DBConnection import DBConnUtil
from exception.CourseNotFoundException import CourseNotFoundException
from exception.StudentNotFoundException import StudentNotFoundException
from exception.TeacherNotFoundException import TeacherNotFoundException

class SIS:
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def enrollStudent(self, student, course):
        # Logic to enroll student in course and insert into database
        pass

    def assignTeacherToCourse(self, course, teacher):
        # Logic to assign teacher to course and update database
        pass

    def recordPayment(self, student, amount, payment_date):
        # Logic to record payment for student and update database
        pass

    def generateEnrollmentReport(self, course):
        # Logic to generate enrollment report for specified course
        pass

    def generatePaymentReport(self, student):
        # Logic to generate payment report for specified student
        pass

    def calculateCourseStatistics(self, course):
        pass