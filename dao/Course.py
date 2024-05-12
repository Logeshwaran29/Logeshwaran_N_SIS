from util.DBConnection import DBConnUtil
from exception.CourseNotFoundException import CourseNotFoundException

class course:
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def UpdateCourseInfo(self, Course):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Course where courseCode = {Course.courseCode}''')
            res = stmt.fetchall()
            if not res:
                raise CourseNotFoundException('Course Not Found...')
            query = f'''update Student set courseName = {Course.courseName}, Course.courseCode = {Course.courseCode}, 
                    instructorName = {Course.instructorName} where courseCode = {Course.courseCode}'''
            stmt.execute(query)
            self.connection.commit()
            stmt.close()
            print('Course Details Updated...')
        except Exception as e:
            print(e)

    def DisplayCourseInfo(self):
        try:
            stmt = self.connection.cursor()
            stmt.execute('''select * from Course''')
            res = stmt.fetchall()
            stmt.close()
            return res
        except Exception as e:
            print(e)
            return []

    def GetEnrollments(self, courseID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Course where courseID = {courseID}''')
            res = stmt.fetchall()
            if not res:
                raise CourseNotFoundException('Course Not Found...')
            stmt.execute(f'''select * from Enrollment where courseID = {courseID}''')
            res1 = stmt.fetchall()
            stmt.close()
            return res1
        except Exception as e:
            print(e)
            return []

    def GetTeacher(self, courseID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Course where courseID = {courseID}''')
            res = stmt.fetchall()
            if not res:
                raise CourseNotFoundException('Course Not Found...')
            stmt.execute(f'''select name from Course where courseID = {courseID}''')
            res1 = stmt.fetchall()
            stmt.close()
            return res1
        except Exception as e:
            print(e)
            return []

    def CreateCourse(self, Course):
        try:
            stmt = self.connection.cursor()
            query = '''insert into Course(courseName, courseCode, name) values(%s, %s, %s)'''
            data = [Course.courseName, Course.courseCode, Course.instructorName]
            stmt.execute(query, data)
            self.connection.commit()
            stmt.close()
            print('Course Added...')
        except Exception as e:
            print(e)
