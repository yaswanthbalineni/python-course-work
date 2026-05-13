'''
inhertance



                "single inheritance"
class A:
    def printa(self):                       #parent class
        print("parent class --A")
class B(A):
    def printb(self):                       #child class
        print("child class--B")
b=B()                     #object of child class
b.printb()
b.printa()                #calling parent class using child class object


                    "multi level inheritance"

class A:
    def printa(self):                       #parent class
        print("parent class --A")
class B(A):
    def printb(self):                       #child class
        print("child class 1--B")
class C(B):
    def printc(self):                       #grand child class
        print("child class 2 --C")
c=C()                     #object of child class
c.printb()
c.printa()                #calling parent class using child class object
c.printc()
                            #"mulitple inheritance"
                        
class A:
    def printa(self):                       #parent class
        print("parent class --A")
class B:
    def printb(self):                       #parentclass
        print("parent class 1--B")
class C:
    def printc(self):                       #parent class
        print("parent class 2 --C")

class D(A,B,C):
    def printd(self):
        print("child class for A,B,C")
d=D()                     #object of child class
d.printa()
d.printb()
d.printc()           #calling parent class using child class object
d.printd()


                        hierarchical

class A:
    def printa(self):                       #parent class
        print("parent class --A")
class B(A):
    def printb(self):                       #child class
        print("1st child class 1 --B")
class C(A):
    def printc(self):                       #child class
        print("2nd child class 2 --C")

class D(A):                                 #child class
    def printd(self):
        print("3rd child class 3 --D,")
d=D()                     #object of child class
d.printa()
d.printd()
c=C()
c.printc()           #calling parent class using child class object
c.printa()
b=B()
b.printb()
b.printa()


 


class A:
    def printa(self):                       #parent class
        print("parent class --A")
class B(A):
    def printb(self):                       #childclass
        print("1st child class 1--B")
class C(A):
    def printc(self):                       #child class
        print("2nd child class 2 --C")

class D(A,B):
    def printd(self):
        print(" 3rd child class for B,")
d=D()                     #object of child class
d.printa()
d.printd()
c=C()
c.printc()           #calling parent class using child class object
c.printa()



                                # supermethod


class A:
    def display(self):
        print("class A")
class B(A):
    def display(self):
        super().display()
        print("class B")
b=B()
b.display()


'''

                            # when ever we have mulitple parents use class method

class A:
    def display(self):
        print("class A")
class C:
    def display(self):
        print("class C")
        
class B(A,C):
    def display(self):
        A.display(self)
        C.display(self)
        print("class B")
b=B()
b.display()































