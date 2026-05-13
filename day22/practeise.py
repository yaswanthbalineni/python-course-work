''' book selling  

class book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def info(self):
        print(f' these is the {self.title} and {self.author} and it{self.price}')
books=book('naku','neku',2020)
books.info()

calculating salary

class office:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def calculate(self):
        return self.salary*12
employee=office('yaswanth',45000)
print(employee.calculate())



student grade calculater

class grade:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def passed(self):
        avg=sum(self.marks)/len(self.marks)
        return avg>48
student=grade('yaswanth',[24,67,85,45])
print("u got the grade of",student.passed())

bank account

class bank:
    def __init__(self,owner):
        self.owner=owner
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("insufficient")

    def display(self):
        print(f'show,{self.balance}')

account=bank('yaswanth')
account.deposit(1000)
account.withdraw(500)
account.display()



class car:
    def __init__(self,model):
        self.model=model
        self.odometer=0

    def drive(self,km):
        self.odometer+=km
    def show(self):
        print(f'total odometer readings:{self.odometer}km')
yaswanth=car('bmw')
yaswanth.drive(120)
yaswanth.drive(45)
yaswanth.show()
f'movie{self.title} is average almost the rateing is given by{self.rating}')


movie rateing
 
class movie:
    def __init__(self,title,rating):
        self.title=title
        self.rating=rating
    def rate(self):
        if self.rating>7.5:
            print(f'movie{self.title} is hit almost the rateing is given by{self.rating}')
        elif self.rating==5:
            print(f'movie{self.title} is average almost the rateing is given by{self.rating}')
        else:
            print(f'movie{self.title} is flop almost the rateing is given by{self.rating}')
family=movie('naku nuvuu',4)
family.rate()


product discount

class product:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        self.discount=0
    def dis(self,percent):
        self.discount=self.price*(percent/100)
    def showdiscount(self):
        print(f'on your shoping on these {self.item}item u got discount upto {self.discount}')
costumer=product('milk',35)
costumer.dis(30)
costumer.showdiscount()


 converting 

class Temp:
    def __init__ (self,temp):
        self.temp=temp
    def ceis(self):
        return (self.temp*9/5)+32
    def fra(self,frae):
        return (frae-32)*5/9
T=Temp(25)
print(T.ceis())
print(T.fra(78))

'''
























