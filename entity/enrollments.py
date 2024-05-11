class Enrollment:
    def __init__(self, student_id, course_id, enrollment_date):
        self.studentId = student_id
        self.courseId = course_id
        self.enrollmentDate = enrollment_date

    def student_id(self):
        return self.studentId

    def set_student_id(self, studentId):
        self.studentId = studentId

    def course_id(self):
        return self.courseId

    def set_course_id(self, courseId):
        self.courseId = courseId

    def enrollment_date(self):
        return self.enrollmentDate

    def set_enrollment_date(self, enrollmentDate):
        self.enrollmentDate = enrollmentDate

