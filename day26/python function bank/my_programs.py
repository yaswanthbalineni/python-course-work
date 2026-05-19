
def even():
    print('''
    n=int(input())
    if n%2==0:
       print("even")
    else:
       print("odd")
    ''')

def factors():
    print('''
    n=int(input())
    re=[]
    for i in range(1,n+1):
        if n%i==0:
            re.append(i)
    print("re",re)
    ''')

def factorial():
    print('''
    n=int(input())
    fact=1
    for i in range(1,n+1):
        fact*=i
    print("factorial of number is ",fact)
    ''')

def prime():
    print('''
    n= int(input())
    for i in range(2,n//2+1):
        if n%i==1:
            print("it is a prime")
        else:
            print("not prime")

        ''')
def sum_of_digit():
    print('''
n=int(input("enter a number"))
sum=0
while n>0:
    r=n%10
    sum+=r
    n=n//10
print(sum)
''')

def double_list():
    print('''
    l=[1,2,3,4]
    res=[ i*2 for i in l]
    print(res)
    ''')
 



    
