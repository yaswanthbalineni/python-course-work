from my_programs import *
while True:
    print("1.even")
    print("2.factor")
    print("3.factorial")
    print("4.prime")
    print("5.sum_of_digit")
    print("6.gcd")
    print("7.countvol")
    print("8.double_list")
    print("0.Exit")
    ch=int(input("enter ur choice"))
    if ch==1:
        even()
    elif ch==2:
        factor()
    elif ch==3:
        factorial()
    elif ch==4:
        prime()
    elif ch==5:
       sum_of_digit()
    elif ch==8:
        double_list()
       
    elif ch==0:
        break
    else:
        print("correct values")
        
    
