



class IMultiFunctionDevice:
    def print_statement(self):
        pass

    def scan(self):
        pass

    def copy(self):
        pass

    def fax(self):
        pass


class Printer(IMultiFunctionDevice):
    def print_statement(self):
        print("Printing... ")
    

class Scanner(IMultiFunctionDevice):
    def scan(self):
        return super().scan()
    
class Copier(IMultiFunctionDevice):
    def copy(self):
        return super().copy()
    
    






