
'''

OOPS

1.class
 class class_name:

class is combination of attributs,methods
class attribute,class methods
instance methods , instance attributes, static methods





 
2.object

yaswanth=class_name()





class flipkart:
    discount=10                                                     #class attributs
    product=["mens footware","watchs","shoes","tshrits","pants"]   #class attributs

    @classmethod
    def showproduct(cls):                              #class methods
        for i in cls.product:
            print(i)
    def showdiscount(cls):
        print("Discount",cls.discount)               #class methods


    def userinfo(self,username,phoneno):                       #instance attributs
        self.username = username                               #instance methods
        self.phoneno = phoneno
        print(f"welcome to the flipkart {self.username}.shop now")
    @staticmethod
    def banner():
        print("10% discount is going on")                       #static method
        
yaswanth=flipkart()
yaswanth.userinfo("asif",'9063375775') # only object can call the instances
yaswanth.banner()              # both object and class name can call the static method
flipkart.banner()
yaswanth.showproduct()
yaswanth.showdiscount()
                 # it can be call by using both object name and class name

'''


class instagram:                                                #class
    settings=["unfollow list","follow list","history"]     #class attribute

    @classmethod
    def showsettings(cls):                              #class method
        for i in cls.settings:
            print(i)
    def userinfo(self,username,dataofbirth):        #instance attribute
        self.username=username
        self.dataofbirth=dataofbirth            #instance method
        print("u login page to the ur instapage with {self.username}")
yaswanth=instagram()                        #object
yaswanth.userinfo("yaswanth",'1-04-2005')
yaswanth.showsettings()

    





 
