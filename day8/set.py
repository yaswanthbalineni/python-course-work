Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>>                          #sets
>>> #it is a mutable ,no duplicate,unordered,dymanim,membership operator is faster
>>> s=set()
>>> s={1,2,3,4,54,53,212,3,12,3,2,3,45,}
>>> s
{1, 2, 3, 4, 12, 45, 212, 53, 54}
>>> s.add(0)
>>> s
{0, 1, 2, 3, 4, 12, 45, 212, 53, 54}
>>> s.add(10.2)
>>> s.add('string')
>>> s.add((1,2,3))
>>> s
{0, 1, 2, 3, 4, 10.2, (1, 2, 3), 12, 45, 212, 53, 54, 'string'}
>>> # no concateation repation,indexing slicing and only membership and accesss is by only for loop by iteration
>>> 1 in s
True
>>> 2 not in s
False
>>>  # method s union, intersection,difference,symtricdifference,subset,superset,isdisjoint
...  
>>> a={1,2,3,4,5,6,9,8}
>>> b=(1,2,3,4,10,7)
>>> a
{1, 2, 3, 4, 5, 6, 8, 9}
>>> b
(1, 2, 3, 4, 10, 7)
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>>> a|b
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a|b
TypeError: unsupported operand type(s) for |: 'set' and 'tuple'
>>> a.intersection(b)
{1, 2, 3, 4}
a-b
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a-b
TypeError: unsupported operand type(s) for -: 'set' and 'tuple'
a.difference(b)
{5, 6, 8, 9}
a.isdisjoint(b)
False
a | b
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a | b
TypeError: unsupported operand type(s) for |: 'set' and 'tuple'
b={1,2,3,4,5,6,7,898}
b
{1, 2, 3, 4, 5, 6, 7, 898}
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 898}
a-b
{8, 9}
a^b
{7, 898, 8, 9}
{1}>a
False
{1}<a
True
#we can add and delete but vcan not modify
a
{1, 2, 3, 4, 5, 6, 8, 9}
a.add(10)
a
{1, 2, 3, 4, 5, 6, 8, 9, 10}
a.update(12,1,34,5,1,3123)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.update(12,1,34,5,1,3123)
TypeError: 'int' object is not iterable
a.update({1,2,3,32,32,3,21,4,23})
a
{32, 1, 2, 3, 4, 5, 6, 8, 9, 10, 21, 23}
a.remove(32)
a.remove(21)
a.clear()
a
set()
b
{1, 2, 3, 4, 5, 6, 7, 898}
b.pop()
1
