from util.DBConnection import DBConnUtil
from exception.TeacherNotFoundException import TeacherNotFoundException
from exception.CourseNotFoundException import CourseNotFoundException

class course:
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def AssignTeacher(self, teacher):
        pass

    def UpdateCourseInfo(self, Course):
        pass

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
        pass

    def CreateCourse(self, Course):
        pass
