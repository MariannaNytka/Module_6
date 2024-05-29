from collections import UserList

class AmountPaymentList(UserList):
    def amount_payment(self):
        total_amount = 0
        for payment in self.data:
            if payment > 0:
                total_amount += payment
        return total_amount

# Приклад використання:
payments = AmountPaymentList([1, -3, 4])
print(payments.amount_payment())