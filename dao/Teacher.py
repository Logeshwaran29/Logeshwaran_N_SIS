from util.DBConnection import DBConnUtil
from exception.TeacherNotFoundException import TeacherNotFoundException

class teacher:
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def UpdateTeacherInfo(self, Teacher):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Teacher where teacherID = {Teacher.teacherId}''')
            res = stmt.fetchall()
            if not res:
                raise TeacherNotFoundException('Teacher Not Found...')
            query = '''update Teacher set firstName = %s, lastName = %s, email = %s where teacherId = %s'''
            data = [Teacher.firstName, Teacher.lastName, Teacher.email, Teacher.teacherId]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            print('Teacher Details Updated...')
        except Exception as e:
            print(e)

    def DisplayTeacherInfo(self, teacherID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Teacher where teacherID = {teacherID}''')
            res = stmt.fetchall()
            if not res:
                raise TeacherNotFoundException('Teacher Not Found...')
            self.connection.commit()
            stmt.close()
            return res
        except Exception as e:
            print(e)
            return []

    def GetAssignedCourses(self, teacherID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Teacher where teacherID = {teacherID}''')
            res = stmt.fetchall()
            if not res:
                raise TeacherNotFoundException('Teacher Not Found...')
            query = f'''select * from Course 
            where name = (select concat(firstName,' ',lastName) as name from Teacher where teacherId = {teacherID}'''
            stmt.execute(query)
            res1 = stmt.fetchall()
            self.connection.commit()
            stmt.close()
            return res1
        except Exception as e:
            print(e)
            return []

    def createTeacher(self, Teacher):
        try:
            stmt = self.connection.cursor()
            query = '''insert into Teacher values(%s, %s, %s, %s)'''
            data = [Teacher.teacherId, Teacher.firstName, Teacher.lastName, Teacher.email]
            stmt.execute(query, data)
            self.connection.commit()
            print('Teacher Created Successfully...')
        except Exception as e:
            print(e)
