
#construtor


class instagram:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        print(f'hi {self.username},welcome !!!')

yaswanth=instagram('yaswanth','yaswanth@04')


#encapsulation
                #public variable
                #protected variable
                #private variable


                #public variable

class instagram:
    def __init__(self,username, email,password):
        self.username=username #public variable . we access or update public variable outside also
        self._email =email 
        self.__password=password 
yaswanth=instagram('yaswanth','@gmail.com','yaswanth@04')
print('username:',yaswanth.username)#access
print('beforeusername:',yaswanth.username)
yaswanth.username='sai'                     #update
print('after username:',yaswanth.username)

                                   # protected
class instagram:
    def __init__(self,username, email,password):
        self.username=username 
        self._email =email     # protected variable
        self.__password=password
    @property
    def emailaccess(self):
        return self.email
    @emailaccess.setter
    def emailaccess(self,new_email):
        self._email =new_email
   
yaswanth=instagram('yaswanth','@gmail.com','yaswanth@04')
print("email",yaswanth._email)#access

print("before",yaswanth._email)
yaswanth._email='yaswanth@gmail.com' #update
print("after",yaswanth._email)


                               # private variable

class instagram:
    def __init__(self,username, email,password):
        self.username=username 
        self._email =email     
        self.__password=password     #private variable
    
    def getpassword(self):
        return self.__password
    def setpassword(self,new_password):
        self.__password=new_password
    
    
yaswanth=instagram('yaswanth','@gmail.com','yaswanth@04')
print("password:",yaswanth.getpassword())#access
print("before",yaswanth.getpassword())
yaswanth.setpassword('yaswanth@304') #update
print("after",yaswanth.getpassword())


