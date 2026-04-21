Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
                          #dict
#key:value, mutable,dynamic,order,value is allow duplicate,key is unqiue is cant change
d={}
d=dict()
type(d)
<class 'dict'>
d={'name':'yaswanth','batch':52,'skills':['python','css','html']}
d
{'name': 'yaswanth', 'batch': 52, 'skills': ['python', 'css', 'html']}
d['name']='pavan'
d['course']='pfs'
s{}
SyntaxError: invalid syntax
s={}
s['1']='int'
s['1.2']='float'
s['cssccs']='string'
s['(1,2,3,4)']='tuple'
s['False']='boolean'
s
{'1': 'int', '1.2': 'float', 'cssccs': 'string', '(1,2,3,4)': 'tuple', 'False': 'boolean'}
# no concatation,repataion,index,slicing
#only membership
d
{'name': 'pavan', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'pfs'}
'yaswanth' in d
False
'pavan' in d
False
'name'in d
True
d['name']
'pavan'
d['skills']
['python', 'css', 'html']
d.get('name')
'pavan'
d.get('age','age is not prestent')
'age is not prestent'
d.get('name','name is not present')
'pavan'
#update,modify,delete,add
d['name']='yaswanth'
d['age']='21'
d.update({'k1':'v1','k2':'v2'})
d
{'name': 'yaswanth', 'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'pfs', 'age': '21', 'k1': 'v1', 'k2': 'v2'}
d.popitem()
('k2', 'v2')
d.popitem()
('k1', 'v1')
d.pop('name')
'yaswanth'
d
{'batch': 52, 'skills': ['python', 'css', 'html'], 'course': 'pfs', 'age': '21'}
del d['batch']
d
{'skills': ['python', 'css', 'html'], 'course': 'pfs', 'age': '21'}
>>> del d[]
SyntaxError: invalid syntax
>>> del d
>>> d
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
>>> d={'name':'yaswanth','batch':52,'skills':['python','css','html']}
>>> d.clear()
>>> d
{}
>>> d={'name':'yaswanth','batch':52,'skills':['python','css','html']}
>>> d.keys()
dict_keys(['name', 'batch', 'skills'])
>>> d.values()
dict_values(['yaswanth', 52, ['python', 'css', 'html']])
>>> d.items()
dict_items([('name', 'yaswanth'), ('batch', 52), ('skills', ['python', 'css', 'html'])])
>>> sorted(d)
['batch', 'name', 'skills']
>>> len(d)
3
>>> max(d)
'skills'
>>> min(d)
'batch'
>>> 
>>> d
{'name': 'yaswanth', 'batch': 52, 'skills': ['python', 'css', 'html']}
>>> d.get('age')
>>> d.setdefault('age','21')
'21'
>>> d
{'name': 'yaswanth', 'batch': 52, 'skills': ['python', 'css', 'html'], 'age': '21'}
