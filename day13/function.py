'''
function


two type of function

bulit in function
user function


syntax of function

def function_name(arg):

      #stats
      return  ....
function_name(para)



def wish(name):
    print(f'good Afternoon {name}!')
    print('welcome to the python class')

wish('yashwanth')
wish('vishun')
wish('pavan sai')


def iseven(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
num=int(input("enter"))
print(iseven(num))


def iseven(num):
    if num%2==0:
        return("even")
    else:
        return("odd")
num=int(input("enter"))
print(iseven(num))


def avg(a,b,c):
    return (a+b+c)/3
a,b,c=map(int,input("enter").split(' '))
print(avg(a,b,c))
    

n=int(input("enter the number"))
for i in range(2,n//2+1):
    if n%i==0:
        print("not prime")
        break

else:
    print("prime")
    

def prime(num):
    for i in range(2,num//2+1):
        if num%i==0:
            return False
    return True
num =int(input("enter the number"))
print( "prime number " if prime(num) else "not prime")



passing different  parameter    to the same arguments position arguments
def display(name,email,password):
    print('name:',name)
    print('email:',email)
    print('password:',password)
display('username','@useremail.com','pass@123')
display('@123useremail.com','user1','pssw')
display('@name123email.com','passw','user2')


 key arguments

 
def display(name,email,password):
    print('name:',name)
    print('email:',email)
    print('password:',password)
display(name='username',email='@useremail.com',password='pass@123')
display(email='@123useremail.com',name='user1',password='pssw')
display(email='@name123email.com',password='passw',name='user2')

default arguments

def display(name,email,password, phoneno=None):
    print('name:',name)
    print('email:',email)
    print('password:',password)
    print('phoneno:',phoneno)
display('username','@useremail.com','pass@123')
display('username','@useremail.com','pass@123','90633123456')




variable positional parameter

def sum_(*n):
    print(n,sum(n))
sum_(1,2,3,4,5,6,67)
sum_(1,3,2)
sum_(1,2,3,4,5,6)


variable with  key parameters
def ss(**n):
    print(n)
ss(k1='v1',k2='n2')

'''








