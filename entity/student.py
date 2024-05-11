class Student:
    def __init__(self, studentId, firstName, lastName, dob, email, phoneNumber):
        self.studentId = studentId
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob
        self.email = email
        self.phoneNumber = phoneNumber

    def get_first_name(self):
        return self.firstName

    def get_last_name(self):
        return self.lastName

    def get_date_of_birth(self):
        return self.dob

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phoneNumber

    def set_first_name(self, firstName):
        self.firstName = firstName

    def set_last_name(self, lastName):
        self.lastName = lastName

    def set_date_of_birth(self, dob):
        self.dob = dob

    def set_email(self, email):
        self.email = email

    def set_phone_number(self, phoneNumber):
        self.phoneNumber = phoneNumber
