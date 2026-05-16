'''
polymorphism

method overriding

class hotstar:
    def login(self):
        print("you can login")
    def search(self):
        print("you can search")
    def otp(self):
        print("verfiy by using otp")
    def movies(self):
        print("limited")
    def user(self):
        print("limited user")
    def video(self):
        print("ads will run")
class premium(hotstar):
    def movies(self):
        print("unlimited")
    def user(self):
        print("unlimited user")
    def video(self):
        print("ads not run , full hd quality")

yaswanth=hotstar()
 

yaswanth.login()
yaswanth.user()
yaswanth.otp()
yaswanth.search()
yaswanth.movies()
yaswanth.video()
pavan=premium()

pavan.login()
pavan.user()
pavan.otp()
pavan.search()
pavan.movies()
pavan.video()







'''
#operator overloding



class number:
    def __init__(self,num):
        self.num=num
    def __add__(self,other):
        return self.num + other.num
    def __sub__(self,other):
        return self.num - other.num
    def __mul__(self,other):
        return self.num * other.num
    def __gt__(self,other):
        return self.num > other.num
    def __lt__(self,other):
        return self.num < other.num
    def __eq__(self,other):
        return self.num == other.num
    def __str__(self):
        return f'{self.num}'
a=number(10)
b=number(5)
print(a+b)
print(a-b)
print(a*b)
print(a>b)
print(a<b)
print(a==b)
print(a,b)























