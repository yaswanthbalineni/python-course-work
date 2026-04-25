'''  iteration sequence of  string list tuple set dict



string



s='string'
for i in s:
    print(i)
a=[1,2,3,4,5]
for j in a:
    print(j)
t=(1,2,3,4)
for i in t:
    print(i)
set={1,2,3,45,6}
for i in set:
    print(i)
dict={1:2,2:3}
for i in dict:
    print(i,dict[i])


    -------range()-----


for i in range(0,10,1):
    print(i)
for i in range(5,51,5):
    print(i)
for i in range(2,11,2):
    print(i)
for i in range(1,10,2):
    print(i)
for i  in range(31,41):
    print(i)
 enumerate method  --- to access the  index value
and range(len(n)

s='python'
for i in enumerate(s):
    print(i)
for i in range(len(s)):
    print(i,s[i])

name=['dheshik','saikiran','pavan','sai']
for i in range(len(name)):
    print(i,name[i])
for i  in enumerate(name):
    print(i)
s={1,2,3,4}
for i in enumerate(s):
    print(i,)
    
break, continue, pass


for i in range(10):
    pass
for i  in range(10):
    if i==5:
        break
    print(i)
for i in range(15):
    if i==5:
        continue
    print(i)


'''

'''for with  else'''

products=['b','s','j','m']
a='a'
for i in products:
    if i==a:
        print(a)
        break
else:
    print("not found")

pin=12345
for i in range(5):
    epin=int(input("enter the pin:"))
    if pin==epin:
        print("log")
        break
    else:
        print("incorrect")
else:
    print("try again after 60 seconds")
