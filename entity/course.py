class Course:
    def __init__(self, course_name, credits, instructor_name):
        self.courseName = course_name
        self.credits = credits
        self.instructorName = instructor_name

    def course_name(self):
        return self.courseName

    def set_course_name(self, value):
        self.courseName = value

    def credits(self):
        return self.credits

    def set_credits(self, value):
        self.credits = value

    def instructor_name(self):
        return self.instructorName

    def set_instructor_name(self, value):
        self.instructorName = value
