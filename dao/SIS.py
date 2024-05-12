from util.DBConnection import DBConnUtil
from exception.StudentNotFoundException import StudentNotFoundException
from exception.TeacherNotFoundException import TeacherNotFoundException
from datetime import date

class SIS:
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def enrollStudent(self, student, course):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {student.studentId}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            query = '''insert into Enrollment(studentID, courseID, enrollDate) values(%s, %s, %s)'''
            data = [student.studentId, course.courseID, date.today()]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            print('Student Enrollment Successful...')
        except Exception as e:
            print(e)

    def assignTeacherToCourse(self, course, teacher):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Teacher where teacherID = {teacher.teacherID}''')
            res = stmt.fetchall()
            if not res:
                raise TeacherNotFoundException('Teacher Not Found...')
            query = '''update Course set name = %s where courseID = %s'''
            name = teacher.firstName+' '+teacher.lastName
            data = [name, course.courseID]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            print('Teacher Assigned...')
        except Exception as e:
            print(e)

    def recordPayment(self, student, amount, paymentDate):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentID = {student.studentId}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            query = '''insert into Payment(studentID, amount, paymentDate) values(%s, %s, %s)'''
            data = [student.studentId, amount, paymentDate]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            print('Payment Done...')
        except Exception as e:
            print(e)

    def generateEnrollmentReport(self, course):
        try:
            stmt = self.connection.cursor()
            query = f'''select * from Student where studentID in 
                    (select studentID from Enrollment where courseID = {course.courseID})'''
            stmt.execute(query)
            res = stmt.fetchall()
            stmt.close()
            return res
        except Exception as e:
            print(e)
            return []

    def generatePaymentReport(self, student):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Student where studentId = {student.studentId}''')
            res = stmt.fetchall()
            if not res:
                raise StudentNotFoundException('Student Not Found...')
            query = f'''select * from Payment where studentID = {student.studentId}'''
            stmt.execute(query)
            res1 = stmt.fetchall()
            stmt.close()
            return res1
        except Exception as e:
            print(e)
            return []
