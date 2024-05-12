class Course:
    def __init__(self, courseID, course_name, courseCode, instructor_name):
        self.courseID = courseID
        self.courseName = course_name
        self.courseCode = courseCode
        self.instructorName = instructor_name

    def get_course_name(self):
        return self.courseName

    def set_course_name(self, value):
        self.courseName = value

    def get_course_code(self):
        return self.courseCode

    def set_course_code(self, courseCode):
        self.courseCode = courseCode

    def get_instructor_name(self):
        return self.instructorName

    def set_instructor_name(self, value):
        self.instructorName = value
