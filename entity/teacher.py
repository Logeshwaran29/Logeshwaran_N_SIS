class Teacher:
    def __init__(self, teacherID, firstName, lastName, email):
        self.teacherID = teacherID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email

    def getTeacherID(self):
        return self.teacherID

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

    def getEmail(self):
        return self.email

    def setTeacherId(self, id):
        self.teacherID = id

    def setFirstName(self, firstName):
        self.firstName = firstName

    def setLastName(self, lastName):
            self.lastName = lastName

    def setEmail(self, email):
        self.email = email