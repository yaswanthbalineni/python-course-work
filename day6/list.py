Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list is acollection elements
''' it is mutalble
add,del,mod
allow duplictae
it is hetrogeous
it is a dynmice
it is a ordered
it is mulitdatatypes can allow'''
' it is mutalble\nadd,del,mod\nallow duplictae\nit is hetrogeous\nit is a dynmice\nit is a ordered\nit is mulitdatatypes can allow'
              #list operation
#concation
l=[]

type(l)
<class 'list'>
l=list()
l
[]
l=[6,90,9.0,'string',[],{},(),True]
a=[1,2,34,5]
b=[23,4,5,6,7]
a+b
[1, 2, 34, 5, 23, 4, 5, 6, 7]
a*8
[1, 2, 34, 5, 1, 2, 34, 5, 1, 2, 34, 5, 1, 2, 34, 5, 1, 2, 34, 5, 1, 2, 34, 5, 1, 2, 34, 5, 1, 2, 34, 5]
b*9
[23, 4, 5, 6, 7, 23, 4, 5, 6, 7, 23, 4, 5, 6, 7, 23, 4, 5, 6, 7, 23, 4, 5, 6, 7, 23, 4, 5, 6, 7, 23, 4, 5, 6, 7, 23, 4, 5, 6, 7, 23, 4, 5, 6, 7]
     #indexing
s=['yawanth','pavan','sai','sharon','vamshi']
s[1]
'pavan'
[0]
[0]
s[0]
'yawanth'
s[-1]
'vamshi'
s[::-1]
['vamshi', 'sharon', 'sai', 'pavan', 'yawanth']
s[1:4]
['pavan', 'sai', 'sharon']
'yaswanth'in s
False
'sai' in s
True
min(s)
'pavan'
max(s)
'yawanth'
len(s)
5
sorted(s)
['pavan', 'sai', 'sharon', 'vamshi', 'yawanth']
id(s)
2925048316416
s[4]='vamshii'
s
['yawanth', 'pavan', 'sai', 'sharon', 'vamshii']
s[0]='yaswanth'
s
['yaswanth', 'pavan', 'sai', 'sharon', 'vamshii']
s.append('sai kiran')
s
['yaswanth', 'pavan', 'sai', 'sharon', 'vamshii', 'sai kiran']
s.insert(4,'shiva')
s
['yaswanth', 'pavan', 'sai', 'sharon', 'shiva', 'vamshii', 'sai kiran']
s.extend(['dheshik','nagarju']
         s
         
SyntaxError: '(' was never closed
s.extend(['dheshik','nagarju'])
         
s
         
['yaswanth', 'pavan', 'sai', 'sharon', 'shiva', 'vamshii', 'sai kiran', 'dheshik', 'nagarju']
s.pop(3)
         
'sharon'
s.pop(2)
         
'sai'
s.remove('shiva')
         
del s[0]
         
s
         
['pavan', 'vamshii', 'sai kiran', 'dheshik', 'nagarju']
s.clear()
         
s
         
[]
s=['yaswanth', 'pavan', 'sai', 'sharon', 'shiva', 'vamshii', 'sai kiran', 'dheshik', 'nagarju']
         
s.index('nagarju')
         
8
l=[1,2,3,4,5,4,32,1,23,43]
         
l.count(1)
         
2
sorted(l)
         
[1, 1, 2, 3, 4, 4, 5, 23, 32, 43]
l.sort()
         
l
         
[1, 1, 2, 3, 4, 4, 5, 23, 32, 43]
l.sort(reverse=True)
         
l
         
[43, 32, 23, 5, 4, 4, 3, 2, 1, 1]

l.reverse()
         
l
         
[1, 1, 2, 3, 4, 4, 5, 23, 32, 43]
a=[1,2,34,5,55,676,]
...          
>>> b=[1,2,34,5,6,7,8]
...          
>>> b=a
...          
>>> b
...          
[1, 2, 34, 5, 55, 676]
>>> a
...          
[1, 2, 34, 5, 55, 676]
>>> c=a.copy()
...          
>>> c
...          
[1, 2, 34, 5, 55, 676]
>>> sum(c)
...          
773
>>> len(l)
...          
10
>>> #[0,0.0,'',[],{},(),set(),False]
...          
>>> any([0,0.0,'',[],{},(),set(),False])
...          
False
>>> any([0,0.0,'',[],{},(),set(),False,12,3])
...          
True
>>> all([0,0.0,'',[],{},(),set(),False,1,2])
...          
False
>>> all(1,2,3,4,5,7,0,0.0,'',[],{},(),set(),False])
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> all([1,2,3,4,5,7,0,0.0,'',[],{},(),set(),False])
False
