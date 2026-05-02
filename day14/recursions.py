'''

pass by value and pass by reference


pass by value
when ever we interge as a input it wont relefect the out the function and

int
float
string     all are immutable items  and it  changes are reflecting only inside the function it is "pass by value"
tuple
bool

list
set          all are mutable items and it  changes are reflecting in and out of the function   so it is know as "pass by reference"
dict


int

def display(n):
    n+=10
    print("inside:",n)
n=10
display(n)
print("outside:",n)


def display(n):
    n+=10.6
    print("inside:",n)
n=10.3
display(n)
print("outside:",n)



def display(n):
    n+="program"
    print("inside:",n)
n="python"
display(n)
print("outside:",n)

def display(n):
    n+=(10,20)
    print("inside:",n)
n=(10,20)
display(n)
print("outside:",n)




scope of the function global

def display():
    global n
    print("inside:",n)
n=(10,20)
display()
print("outside:",n)







nested function



def display(course):
    print("starting",course)
    def change():
        nonlocal course
        course ='jfs'
        print("course changed:",course)
    change()
    print("final:",course)
course='pfs'
display(course)


s='python'
print(len(s))
len=23
print(len(s))



6
Traceback (most recent call last):
  File "C:/Users/Balineni Yaswanth/OneDrive/Desktop/python-course-work/day14/recursions.py", line 91, in <module>
    print(len(s))
TypeError: 'int' object is not callable




s='python'
print(len(s))
len=23
print(len)






recursions function call it self


fun():
    if condtion:
        return
    fun()






def  display(n):
    if n>10:
        return
    print(n)
    display(n+1)

display(1)



def  display(n):
    if n<1:
        return
    print(n)
    display(n-1)

display(10)


def  display(n):
    if n>10:
        return
    display(n+1)
    print(n)

display(1)

def  display(n,sum):
    if n>10:
        return sum
    return display(n+1,sum+n)
print(display(1,0))



def display(n,mul):
    if n>10:
        return mul
    return display(n+1,mul*n)
print(display(1,1))

def display(i,s):
    if i==len(s):
        return
    print(s[i])
    display(i+1,s)
s='python'
display(0,s)

def display(i,s):
    if i==len(s):
        return

    display(i+1,s)
    print(s[i])
s='python'
display(0,s)


def display(i,s):
    if i==len(s):
        return

    display(i+1,s)
    print(s[i])
s='python'
display(0,s)




def display(i,s):
    if i==len(s):
        return
    print(s[:i+1])
    display(i+1,s)
    print(s[:i+1])
    
s='python'
display(0,s)




def display(i,s):
    if i==len(s):
        return
    display(i+1,s)
    print(s[:i+1])
    
s='python'
display(0,s)


def display(i,s):
    if i==len(s):
        return
    print(s[:i+1])
    display(i+1,s)
    
s='python'
display(0,s)



def display(i,s):
    if i==len(s):
        return
    print(s[i:i+3])
    display(i+1,s)
    
s='python'
display(0,s)


factorial of a number!
n*n-1

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
n=int(input("enter"))
print(fact(n))

def digit(n):
    if n==0:
        return 0
    return (n%10)+ digit(n//10)
n=int(input("enter"))
print(digit(n))

'''
