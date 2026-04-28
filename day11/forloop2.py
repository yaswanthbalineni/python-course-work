'''
password=input("enter the password")
if len(password)>=8:
    s=set()
    for i in password:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s)==4:
        print("strong")
    else:
        print("weak is")
else:
    print("weak")


product={1:{'name':'rice','price':60},
         2:{'name':'sugar','price':80},
         3:{'name':'milk','price':70}
         }
print("---------welcome to store-----------")
print("here is the available product")
print('index'.ljust(10,' '),'pro

'''


