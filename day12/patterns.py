'''patterns



for  i in range(5):
    for j in range(3):
        print('*',end=' ')
    print()



for row in range(5):
    for j in range(5):
        print('*',end=' ')
    print()


*  
* *  
* * *  
* * * *  
* * * * *
 0 1
 1 2
 2 3
 3 4
 

n=int(input("enter anumber"))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()


* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 


n=int(input("enter anumber"))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
* * * * * * * * * 
* * * * * * * * 
* * * * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

n=int(input("enter anumber"))
m=n//2

for i in range(n):
    if i<=m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for j in range(n-i):
            print('*',end=' ')
    print()


n=int(input("enter anumber"))
for i in range(n):
    for spaces in range(n-i-1):
        print(' ',end=' ')
    for j in range(n+1):
        print('*',end=' ')
    print()

    
        *       
      * * 
    * * * 
  * * * * 
* * * * * 

n=int(input("enter anumber"))
for i in range(n):
    for spaces in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()

* * * * * * * 
  * * * * * * 
    * * * * * 
      * * * * 
        * * * 
          * * 
            * 
n=int(input("enter anumber"))
for i in range(n):
    for spaces in range(i):
        print(' ',end=' ')
    for j in range(n-i):
        print('*',end=' ')
    print()

    
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
n=int(input("enter anumber"))
m=n//2

for i in range(n):
    if i<=m:
        for space in range(m-i):
            print(' ',end=' ')
        for j in range(i+1):
            print('*',end=' ')
    else:
        for space in range(i-m):
            print(' ',end=' ')
        for j in range(n-i):
            print('*',end=' ')
    print()



     * 
    ** 
   *** 
  **** 
 ***** 
****** 
 ***** 
  **** 
   *** 
    ** 
     * 

n=int(input("enter anumber"))
m=n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('*'*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('*'*(n-i),end=' ')
    print()

    
     *  
    * *  
   * * *  
  * * * *  
 * * * * *  
* * * * * *  
 * * * * *  
  * * * *  
   * * *  
    * *  
     *  

n=int(input("enter anumber"))
m=n//2

for i in range(n):
    if i<=m:
        print(' '*(m-i)+'* '*(i+1),end=' ')
    else:
        print(' '*(i-m)+'* '*(n-i),end=' ')
    print()



10101
01010
10101
01010
10101    

for  i in range(5):
    for j in range(5):
        print(int((i+j)%2==0),end='')
    print()

    
1 0 1 0 1 0 
1 0 1 0 1 0 
1 0 1 0 1 0 
1 0 1 0 1 0 
1 0 1 0 1 0 
1 0 1 0 1 0 


n=int(input("enter"))
for i in range(n):
    for j in range(n):
        print(int((j%2)==0),end=' ')
    print()


******
*    *
*    *
*    *
*    *
******

n=int(input("ennter"))
for i in range(n):
    for j in range(n):
        if j==0 or j==(n-1) or i==0 or i==(n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()




******
    * 
   *  
  *   
 *    
******


n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if i==0 or i==(n-1) or i+j==(n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()






*    *
 *  * 
  **  
  **  
 *  * 
*    *

n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if  i==j or i+j==(n-1):
            print('*',end='')
        else:
            print(' ',end='')
    print()

A

n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if  i==0 or j==(n-1) or j==0 or i==(n//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()
    '''
'''GJKMNQRVWY'''
'''
F
n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if  i==0  or j==0 or i==(n//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()
G

'''
n=int(input("enter"))
for i in range(n):
    for j in range(n):
        if  i==0  or j==0 or(i==(n-1) and j <=(n//2))or (j==(n//2)and i>=(n//2))or(i==(n//2) and j>=(n//2))or (j==(n-1) and i>=(n//2)):
            print('*',end='')
        else:
            print(' ',end='')
    print()

