Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
bool(a)
True
tuple(a)
Traceback (most recent call last):'
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
b=10.8
int(b)
10
complex(b)
(10.8+0j)
str(b)
'10.8'

list(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> bool(b)
True
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
>>> c=10+9j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(c)
'(10+9j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
bool(c)
True
s="yaswanth"
set(s)
{'t', 'h', 'n', 'a', 's', 'w', 'y'}
list(s)
['y', 'a', 's', 'w', 'a', 'n', 't', 'h']
tuple(s)
('y', 'a', 's', 'w', 'a', 'n', 't', 'h')
dict(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(s)
True
d='100'
int(d)
100
float(d)
100.0
complex(d)
(100+0j)
l=[1,2,3,4,5]
int(l)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
str(l)
'[1, 2, 3, 4, 5]'
tuple(l)
(1, 2, 3, 4, 5)
set(l)
{1, 2, 3, 4, 5}
bool(l)
True
t=(1,2,3,4,5,6)
str(t)
'(1, 2, 3, 4, 5, 6)'
list(t)
[1, 2, 3, 4, 5, 6]
bool(t)
True
set(t)
{1, 2, 3, 4, 5, 6}
e={1,2,3,4,5,3,4,4}
list(e)
[1, 2, 3, 4, 5]
tuple(e)
(1, 2, 3, 4, 5)
str(e)
'{1, 2, 3, 4, 5}'
bool(e)
True
dict={"name":"yash","no":'10',"batc":'52'}
str(dict)
"{'name': 'yash', 'no': '10', 'batc': '52'}"
list(dict)
['name', 'no', 'batc']
tuple(dict)
('name', 'no', 'batc')
set(dict)
{'no', 'batc', 'name'}
bool(dict)
True
bo=True
int(bo)
1
float(bo)
1.0
complex(bo)
(1+0j)
str(bo)
'True'
