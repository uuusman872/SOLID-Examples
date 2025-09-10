from abc import ABC,  abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class PaypalPayment(PaymentMethod):
    def pay(self, amount):
        super().pay(amount)
        print(f"[+] Processing the paypal payment method {amount}")

class CreditCardPayment(PaymentMethod) :
    def pay(self, amount):
        super().pay(amount)
        print(f"[+] Processing the credit card payment {amount}")

class PaymentProcess:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method
    
    def process_payment(self, amount):
        self.payment_method.pay(amount)



payment_process = PaymentProcess(payment_method=PaypalPayment())
payment_process.process_payment(500)

payment_process = PaymentProcess(payment_method=CreditCardPayment())
payment_process.process_payment(500)