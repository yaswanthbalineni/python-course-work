'''
                            file handling
there are 5 main opertaion in the file handling
open
read
close
write
append

#read

file= open('pfs-52.txt','r')
print(file.read())
file.close()



#list of "readlines" you want to read


file= open('pfs-52.txt','r')
print(file.readlines())
file.close()

#read line

file= open('pfs-52.txt','r')
print(file.readline())
file.close()




#seek()


file= open('pfs-52.txt','r')
print(file.readline())
file.seek(0)
print(file.readlines())
file.seek(0)
print(file.read())
file.close()

with open('pfs-52.txt','r') as file:
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.seek(0)
    print(file.read())  

#write

file= open('pfs-52.txt','w')
file.write('yaswanth is working')
file.close()



with open('pfs-52.txt','w') as file:
    file.write('good go and sit in the class')

#append


with open('pfs-52.txt','a') as file:
    file.write('good morning')




with open('pfs-52.txt','a+') as file:
    file.write('good morning')
    file.seek(0)
    print(file.read())


with open('pfs.txt','a+') as file:
    file.write('good morning')
    file.seek(0)
    print(file.read())

try:
    with open('pf.txt','r+') as file:
        file.write('good morning')
        file.seek(0)
        print(file.read())
except Exception as e:
    print("error occured:",e)



try:
    with open('pfs-52.txt','w+') as file:
        for i in range(5):
            name = input("enter")
            marks = int(input("enter the name"))
            file.write(f'{name}:{marks}')
        file.seek(0)
        print(file.read())
except Exception as e:
    print("error occured:",e)









file=open("pfs-52.txt",'r')
print(file.read())
print(file.readlines())
print(file.readline())
file.close()






with open("pfs-52.txt",'r') as file:
    print(file.read())



import os
if os.path.exists('pfs-52.txt'):
    file=open('pfs-52.txt','r')
    print("file is opened")
else:
    print("not there")



with open("pfs-52.txt",'a') as file:
    file.write("hello,world")



import os
file_path=os.path.join('day20-1','pfs-52')
with open("pfs-52.txt",'r') as file:
    print(file.read())


'''

import os
file_path="pfs-52"
if os.path.exists(file_path):
    print("file Size",os.path.getsize(file_path),'bytes')
    print("absoluten path:",os.path.abspath(file_path))
else:
    print('not found')











