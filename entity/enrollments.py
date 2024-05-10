class Enrollment:
    def __init__(self, student_id, course_id, enrollment_date):
        self.enrollment_id = None
        self.student_id = student_id
        self.course_id = course_id
        self.enrollment_date = enrollment_date

    def enrollment_id(self):
        return self.enrollment_id

    def set_enrollment_id(self, value):
        self.enrollment_id = value

    def student_id(self):
        return self.student_id

    def set_student_id(self, value):
        self.student_id = value

    def course_id(self):
        return self.course_id

    def set_course_id(self, value):
        self.course_id = value

    def enrollment_date(self):
        return self.enrollment_date

    def set_enrollment_date(self, value):
        self.enrollment_date = value

