from util.DBConnection import DBConnUtil
from exception.StudentNotFoundException import StudentNotFoundException
from exception.CourseNotFoundException import CourseNotFoundException
class student:
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def EnrollInCourse(self, enrollments):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {enrollments.studentId}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            stmt.execute(f'''select * from Course where courseID = {enrollments.course_id}''')
            res1 = stmt.fetchall()
            if not res1:
                raise CourseNotFoundException('Course Not Found...')
            query = '''insert into Enrollment(studentID, courseID, enrollDate) values(%s, %s, %s)'''
            data = [enrollments.student_id, enrollments.course_id, enrollments.enrollment_date]
            stmt.execute(query, data)
            self.connection.commit()
            print('Enroll in Course is completed...')
            stmt.close()
        except Exception as e:
            print(e)

    def UpdateStudentInfo(self, Student):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {Student.studentId}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            query = '''update Student set firstName = %s, lastName = %s, dob = %s, email = %s, phoneNumber = %s
                    where studentId = %s'''
            data = [Student.firstName, Student.lastName, Student.dob, Student.email, Student.phoneNumber, Student.studentId]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            print('Student Details Updated...')
        except Exception as e:
            print(e)

    def makePayment(self, Payment):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {Payment.studentId}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            query = '''insert into Payment(studentID, amount, paymentDate) values(%s, %s, %s)'''
            data = [Payment.studentId, Payment.amount, Payment.paymentDate]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            print('Payment Done Successfully...')
        except Exception as e:
            print(e)

    def displayStudentInfo(self, studentID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {studentID}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            stmt.close()
            return res
        except Exception as e:
            print(e)
            return []

    def getEnrolledCourses(self, studentID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {studentID}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            query = f'''select courseID, courseName, courseCode from Course c join 
            (select courseID from Enrollment where studentID = {studentID}) as c1 on c.courseId = c1.courseID'''
            stmt.execute(query)
            res1 = stmt.fetchall()
            stmt.close()
            return res1
        except Exception as e:
            print(e)
            return []

    def getPaymentHistory(self, studentID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {studentID}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            query = f'''select * from Payment where studentID = {studentID}'''
            stmt.execute(query)
            res1 = stmt.fetchall()
            stmt.close()
            return res1
        except Exception as e:
            print(e)
            return []

    def createStudent(self, Student):
        try:
            stmt = self.connection.cursor()
            query = '''insert into Student values(%s, %s, %s, %s, %s, %s)'''
            data = [Student.studentId, Student.firstName, Student.lastName, Student.dob, Student.email, Student.phoneNumber]
            stmt.execute(query, data)
            self.connection.commit()
            print('Student Created Successfully...')
        except Exception as e:
            print(e)

    def getStudent(self, studID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {studID}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            return res
        except Exception as e:
            print(e)
            return []
