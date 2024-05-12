from util.DBConnection import DBConnUtil
from exception.PaymentValidationException import PaymentValidationException

class payment:
    def __init__(self):
        self.connection = DBConnUtil.getConnection()

    def GetStudent(self, paymentID):
        try:
            stmt = self.connection.cursor()
            stmt.execute(f'''select * from Payment where paymentId = {paymentID}''')
            res = stmt.fetchall()
            if not res:
                raise PaymentValidationException('Payment Not Found...')
            query = f'''select concat(firstName,' ',lastName) as name, dob, email, phoneNumber, amount, paymentDate 
            from Student s join (select * from Payment where paymentID = {paymentID}) as s1 on s.studentID = s1.studentID'''
            stmt.execute(query)
            res1 = stmt.fetchall()
            stmt.close()
            return res1
        except Exception as e:
            print(e)
            return []
