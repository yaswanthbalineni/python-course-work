'''
exception handling

two types

runtime error
complie error


there are 4 blocks


1}try
2}except
3)else
4)finally

try:
    n+=10
except NameError:
    print("variable is not defined")
else:
    print("no error")
finally:
    print("end of the programming")




mulitipal exception



try:
    n+=10
    a=int(input("enter the value"))
    m=10+'a'
    d={1:2,3:4}
    print(d[5])
    l=[1,2,3,4]
    print(l[5])
    x=int(input("enter a value"))
    s=10/x   
except NameError:
    print("variable is not defined")
except ValueError:
    print("enter the correct datatype")
except IndexError:
    print("index is out of range")
except KeyError:
    print("key is not found")
except ZeroDivisionError:
    print("can't divide with zero")
except TypeError:
    print("can't add 2 diiferent datatypes")
else:
    print("no error")
finally:
    print("end of the programming")


try:
    n+=10
    a=int(input("enter the value"))
    m=10+'a'
    d={1:2,3:4}
    print(d[5])
    l=[1,2,3,4]
    print(l[5])
    x=int(input("enter a value"))
    s=10/x   
except (NameError,ValueError,KeyError,ZeroDivisionError,TypeError,IndexError)as e:
    print(f'error occured:{e}')

else:
    print("no error")
finally:
    print("end of the programming")




try:
    n+=10
    a=int(input("enter the value"))
    m=10+'a'
    d={1:2,3:4}
    print(d[5])
    l=[1,2,3,4]
    print(l[5])
    x=int(input("enter a value"))
    s=10/x   
except Exception as e:
    print(f'error occured:{e}')

else:
    print("no error")
finally:
    print("end of the programming")

                                                   #raise#

try:
    balance=100
    wd=-2000
    if wd <0:
        raise Exception("pleas enter positive number")
except Exception as e:
    print(f'error occured:{e}')

else:
    print("no error")
finally:
    print("end of the programming")


'''






