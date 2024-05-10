class Course:
    def __init__(self, course_id, course_name, credits, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.instructor_name = instructor_name

    def course_id(self):
        return self.course_id

    def set_course_id(self, value):
        self.course_id = value

    def course_name(self):
        return self.course_name

    def set_course_name(self, value):
        self.course_name = value

    def credits(self):
        return self.credits

    def set_credits(self, value):
        self.credits = value

    def instructor_name(self):
        return self.instructor_name

    def set_instructor_name(self, value):
        self.instructor_name = value
