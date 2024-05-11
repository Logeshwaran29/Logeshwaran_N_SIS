class Payment:
    def __init__(self, studentID, amount, paymentDate):
        self.studentId = studentID
        self.amount = amount
        self.paymentDate = paymentDate

    def getStudent(self):
        return self.studentId

    def getPaymentAmount(self):
        return self.amount

    def getPaymentDate(self):
        return self.paymentDate

    def setStudent(self, id):
        self.studentId = id

    def setPaymentAmount(self, amt):
        self.amount = amt

    def setPaymentDate(self, date):
        self.paymentDate = date
