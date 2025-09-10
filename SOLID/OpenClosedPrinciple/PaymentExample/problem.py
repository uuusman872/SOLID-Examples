


class PaymentProcess:
    def process_payment(self, method, amount):
        if method == "credit_card":
            print(f"[+] Processing credit card payment of {amount}")
        elif method == "paypal":
            print(f"[+] Processing Paypal payment of {amount}")

