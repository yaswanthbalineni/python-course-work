Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
S='SSSDDFF'
S
'SSSDDFF'
type(S)
<class 'str'>
s="yaswanth"
s='''dfgh'''
s=''
#operation of the string
#concatetion
fname='abc'
lname='edf'
name=fname+lname
name
'abcedf'
#repetaion
fname*7
'abcabcabcabcabcabcabc'
#indexing
s='python'
s[4]
'o'
s[3]
'h'
s[-1]
'n'
[-2]
[-2]
s[-2]
'o'
name[1]
'b'
name[3]
'e'
name[4]
'd'

#slicing
#syntax var[start:stop+1:step]
name[0:4]
'abce'
name[0:6:2]
'acd'
name[::2]
'acd'
name[::-1]
'fdecba'
#membership
a in name
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a in name
NameError: name 'a' is not defined
'a'in name
True
'j' in name
False
#built in function
#len()
len(name)
6
sorted(name)
['a', 'b', 'c', 'd', 'e', 'f']
max(name)
'f'
min(name)
'a'
# to know the  ascc value of the a particular value
ord(a)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    ord(a)
NameError: name 'a' is not defined
ord('a')
97
ord('A')
65
ord('@')
64
ord(' ')
32
char(97)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    char(97)
NameError: name 'char' is not defined. Did you mean: 'chr'?
chr(97)
'a'
chr()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    chr()
TypeError: chr() takes exactly one argument (0 given)
chr(110)
'n'
chr(150)
'\x96'
            #string method
name='yaswanth sai pavan sharon'
name.upper()
'YASWANTH SAI PAVAN SHARON'
name.lower()
'yaswanth sai pavan sharon'
name.capitalize()
'Yaswanth sai pavan sharon'
name.title()
'Yaswanth Sai Pavan Sharon'
name.swapcase()
'YASWANTH SAI PAVAN SHARON'
#casefold an anthor method
         #alignment& formateing
name.center(10,'3')
'yaswanth sai pavan sharon'
name.center(50,'*')
'************yaswanth sai pavan sharon*************'
name.center(50,'^')
'^^^^^^^^^^^^yaswanth sai pavan sharon^^^^^^^^^^^^^'

name.ljust(70,'-')
'yaswanth sai pavan sharon---------------------------------------------'
name.rjust(70,'_')
'_____________________________________________yaswanth sai pavan sharon'
num='123445667'
num.zfill.fill(10)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    num.zfill.fill(10)
AttributeError: 'builtin_function_or_method' object has no attribute 'fill'
numm.zfill(10)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    numm.zfill(10)
NameError: name 'numm' is not defined. Did you mean: 'num'?
num.zfill(10)
'0123445667'
num.zfill(21)
'000000000000123445667'
        #serch&find methods
name.find('sai')
9
name.find('s')
2
name.rfind('s')
19
name.index('o')
23
name.rindex('o')
23
name.count('s')
3
name.count()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    name.count()
TypeError: count expected at least 1 argument, got 0
      #replace&modify
name
'yaswanth sai pavan sharon'
name.replace('a','*')
'y*sw*nth s*i p*v*n sh*ron'
name.replace('p','-')
'yaswanth sai -avan sharon'
name.maketrans('aeiou','12345')
{97: 49, 101: 50, 105: 51, 111: 52, 117: 53}
name.translate(name.maketrans('aeiou','12345'))
'y1sw1nth s13 p1v1n sh1r4n'
           #spliting &joining
name.split()
['yaswanth', 'sai', 'pavan', 'sharon']
name.lsplit()
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    name.lsplit()
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
name.lsplit(' ',3)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    name.lsplit(' ',3)
AttributeError: 'str' object has no attribute 'lsplit'. Did you mean: 'rsplit'?
name.rsplit(' ',3)
['yaswanth', 'sai', 'pavan', 'sharon']
s='python\njava\nlang'
s.splitlines()
['python', 'java', 'lang']
','.join(1)
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    ','.join(1)
TypeError: can only join an iterable
>>> s
'python\njava\nlang'
>>> s=s.splitlines()
>>> s
['python', 'java', 'lang']
>>> ','.join(s)
'python,java,lang'
>>>  '@'.join(s)
...  
SyntaxError: unexpected indent
>>> '@'.join(s)
'python@java@lang'
>>> name.partition(' ')
('yaswanth', ' ', 'sai pavan sharon')
>>> name.partition('p')
('yaswanth sai ', 'p', 'avan sharon')
>>> name.rpartition('b')
('', '', 'yaswanth sai pavan sharon')
>>>        #white space & trimmer
>>> name.strip()
'yaswanth sai pavan sharon'
>>> name.lstrip()
'yaswanth sai pavan sharon'
>>> s='    hello         world         '
>>> s.strip()
'hello         world'
>>> s.lstrip()
'hello         world         '
>>> s.rstrip()
'    hello         world'
>>>     #encodeing and decodeing
>>> text='hello'
>>> text.encode()
b'hello'
>>> b'hello'.decode()
'hello'
