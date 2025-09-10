class Invoice:
    def __init__(self, customer, amount):
        self.customer = customer
        self.amount = amount

    def calculate_tax(self):
        return self.amount * 0.15  # 15% tax

    def generate_invoice_text(self):
        return f"Invoice for {self.customer}\nAmount: {self.amount}\nTax: {self.calculate_tax()}"

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.generate_invoice_text())

    def send_email(self, email):
        # fake send
        print(f"Sending email to {email}:\n{self.generate_invoice_text()}")




class Invoice:
    def __init__(self, consumer, amount):
        self.consumer = consumer
        self.amount = amount


class TaxCalculator:
    def calculate_tax(self, amount):
        return amount * 0.15 

class InvlocePrinter:
    def __init__(self, tax_calculator: TaxCalculator):
        self.tax_calculator = tax_calculator

    def generate_invoice_text(self, invoice: Invoice):
        tax = self.tax_calculator.calculate_tax()
        return f"Invoice for {invoice.consumer} \nAmount: {invoice.amount} \nTax: {tax}"


class EmailServer:
    def send_email(self, email):
        print(f"Sending email to {email}:\n{self.generate_invoice_text()}")


class FileSaver():
    def save_to_file(self, invoice_text, filename):
        with open(filename, "w") as f:
            f.write(invoice_text)
