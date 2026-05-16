
'''
application --phonepay
 parentclass---user
 child class---coustmer,merchent
 
 user attributes
 
 username           
phone_number
upi_id
bank_account
balance


user methods

login()
logout()
check_balance()



costumer attributes

transaction_history
recharge_history
bill_payments

costumer methods

send_money()
receive_money()
scanqr()

merchant methods

receive_payment()
generate_qr()

merchant attributes
shop_name
business_type

abstraction
user

login()
logout()
check_balance()
make_payment()

send_money()
mobile_recharge()
pay_bill()
scan_qr()


receive_payment()
generate_qr()


'''
from abc import ABC,abstractmethod
class user(ABC):
    def __init__(self,username,phoneno,upiid,balance):
        self.username=username
        self.phoneno=phoneno
        self.upiid=upiid
        self.balance=balance
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
    @abstractmethod
    def check(self):
        pass
    
class costumer(user):
    def __init__(self,username,phoneno,upiid,balance,costumer_id,pin):
        super().__init__(username,phoneno,upiid,balance)
        self.costumer_id=costumer_id
        self.pin=pin
        
    def send_money(self,amount,pin,transaction_id):
        self.pin=pin
        self.amount=amount
        self.transaction_id=transaction_id
        print(f"enter amount{self.amount}")
        print(f"enter ur pin {self.pin}")
        print("successfull money send")
        print(f"u get ur transaction id {self.transaction_id}")
              
    def scan_qr(self,qr_code,merchant_id):
        self.qr_code=qr_code
        self.merchant_id=merchant_id
        print(f"please scan the qr code{self.qr_code}")
        print(f"u will see the {self.merchant_id}")
    def login(self):
        print("u should login to account")
        print(f"name:{self.username} /n phoneno:{self.phoneno}")
        print("-------------login successfully completed--------------")
    def logout(self):
        print("------------logout successfully-----------")
    def check(self):
        print("click on the check balance")
        print("enter your pin")
        print(f"pin:{self.pin}")
        print(f"here is ur money{self.balance}")
        
class merchant(user):
    def __init__(self,username,phoneno,upiid,balance,merchant_id,pin):
        super().__init__(username,phoneno,upiid,balance)
        self.merchant_id=merchant_id
        self.pin=pin
        
    def receive_payment(self,invoice_number):
        self.invoice_number=invoice_number
        print(f"ok i receive it look these is ur /n {self.invoice_number}")
    def login(self):
        print("u should login to account")
        print(f'name:{self.username} /n phoneno:{self.phoneno}')
        print("-------------login successfully completed--------------")
    def logout(self):
        print("------------logout successfully-----------")
    def check(self):
        print("click on the check balance")
        print("enter your pin")
        print(f"pin:{self.pin}")
        print(f"here is ur money {self.balance}") 
    

yaswanth=costumer("yaswanth",9876543210,"yaswanth@upi",5000,"C101",222322)
pavan=merchant("pavan",9876500000,"pavan@upi",10000,"M201" ,3334434)

yaswanth.login()
yaswanth.logout()
yaswanth.check()
yaswanth.scan_qr("!@##$$%%","M201")
yaswanth.send_money(230,222322,'sbi122345')
pavan.login()
pavan.logout()
pavan.check()
pavan.receive_payment(77)



        
        
        
    

