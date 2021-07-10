from models import Payment


class PaymentStrategy:
    def __init__(self, paymentInfo):
        self.paymentInfo = paymentInfo

    def get_payment(self):
        pass


class ExactPaymentStrategy(PaymentStrategy):
    def __init__(self, paymentInfo):
        super().__init__(paymentInfo)

    def get_payment(self):
        payments = []

        for user, amount in self.paymentInfo.items():
            payments.append(Payment(user, amount))

        return payments
