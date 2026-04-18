Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Input formate
#input()function
name=input()
yaswanth
name
'yaswanth'
name=input("enter the name")
enter the nameyaswanth
name
'yaswanth'
age=int(input())
21
age
21
age=int(input("enter the age"))
enter the age21
age
21
price=float(input("enter the price"))
enter the price23
price
23.0
#split()function
name=input("enter the name").split()
enter the nameyaswanth
name
['yaswanth']
name=input("enter the name").split(',',2)
enter the nameyaswanth ram sita tejia
name
['yaswanth ram sita tejia']
number=list(map(int,input("enter the number").split()))
enter the number1,2 4 5 6 77 88
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    number=list(map(int,input("enter the number").split()))
ValueError: invalid literal for int() with base 10: '1,2'

number=list(map(int,input("enter the number").split()))
enter the number1 2 34 56 78 89
number
[1, 2, 34, 56, 78, 89]
number=list(map(float,input("enter the number").split()))
enter the number100 200 32 43 54 65 76 
number
[100.0, 200.0, 32.0, 43.0, 54.0, 65.0, 76.0]
number=tuple(map(int,input("enter the number").split()))
enter the number1 23 45 67  8 9
number
(1, 23, 45, 67, 8, 9)
number=tuple(map(float,input("enter the number").split()))
enter the number1 23 45 6 7
number
(1.0, 23.0, 45.0, 6.0, 7.0)
number=set(map(int,input("enter the number").split()))
enter the number1 23 45 6
number
{1, 45, 6, 23}
a,b,c=list(map(int,input("enter the values").split()))
enter the values1 22 3
a
1
b
22
c
3
name,password=input("enter").split()
enteryaswanth Yaswa@123
name
'yaswanth'
password
'Yaswa@123'
#output formate
a,b,c=1,2,3
print(a,b,c)
1 2 3
print("a=",a 'b=',b 'c=',c)
SyntaxError: invalid syntax
print("a=",a"b=",b"c=",c)
SyntaxError: invalid syntax
print("a=",a,'b=',b,'c=',c)
a= 1 b= 2 c= 3
>>> print("a=",a,'b=',b,'c=',c,sep='\n')
a=
1
b=
2
c=
3
>>> print("a=",a,'b=',b,'c=',c,sep='')
a=1b=2c=3
>>> print("a=",a,'b=',b,'c=',c,sep='@@@')
a=@@@1@@@b=@@@2@@@c=@@@3
>>> print("a=",a,'b=',b,'c=',c,sep='@@@',end='###')
a=@@@1@@@b=@@@2@@@c=@@@3###
>>> 
>>> print(f'a={a},b={b},c={c}')
a=1,b=2,c=3
>>> a,b,c=1,20.3,python
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b,c=1,20.3,python
NameError: name 'python' is not defined
>>> a,b,c=1,20.3,"python"
>>> print('a=%d,b=%f,c=%s'%(a,b,c))
a=1,b=20.300000,c=python
>>> print('a={},b={},c={}'.formate(a,b,c))
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    print('a={},b={},c={}'.formate(a,b,c))
AttributeError: 'str' object has no attribute 'formate'. Did you mean: 'format'?
>>> y
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> print('a={},b={},c={}'.format(a,b,c))
a=1,b=20.3,c=python
