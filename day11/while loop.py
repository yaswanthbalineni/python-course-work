'''
i=10
while i<51:
    print(i)
    i+=1
i=1
while i<11:
    if i==5:
        break
    print(i)
    i+=1


i=1
while i<11:
    i+=1
    if i==5:
        continue
    print(i)
    


i=1
while i<11:
    if i==14:
        break
    print(i)
    i+=1
else:
    print('1,....10 numbers are printed')

'''


l=[1,0,3,4,5,6,7,80,0,0,0,0,1,2,3,4,0,0,3,4,0,0]
n=len(l)
for i in range(n):
    if l[i]==0:
        l.remove(0)

