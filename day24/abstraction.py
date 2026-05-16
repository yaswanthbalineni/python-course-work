'''
abstractation


'''

from abc import ABC,abstractmethod

class payment(ABC):
    def input(self):
        print("enter the amount")
    @abstractmethod
    def checkbalance(self):
        pass
    @abstractmethod
    def verfiy(self):
        pass
class cards(payment):
    def checkbalance(self):
        print("check")
    def verfiy(self):
        print(" enetr pin")
    
class netbanking(payment):
    def checkbalance(self):
        print("cb")
    def verfiy(self):
        print("pine")
    
class UPI(payment):
    def checkbalance(self):
        print("uu")
    def verfiy(self):
        print("pin")
class wallet(payment):
    def checkbalance(self):
        print("ch")
    def verfiy(self):
        print("pin")
yaswanth=wallet()
print("yaswanth")
yaswanth.input()
yaswanth.checkbalance()
yaswanth.verfiy()
