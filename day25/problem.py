''' university management system

from abc import ABC,abstractmethod

class person(ABC):
    def __init__(self,name,phoneno):
        self.name=name
        self.phoneno=phoneno
    @abstractmethod
    def displayinfo(self):
        pass
    
class teacher(person):
    def __init__(self,name,phoneno,subject,salary):
        super().__init__(name,phoneno)
        self.subject=subject
        self.salary=salary

        
    def displayinfo(self):
        print("--------------teacher information------------------")
        print(f'name:{self.name}\nphoneno:{self.phoneno}\nsubject:{self.subject}\nsalary:{self.salary}')

class student(person):
    def __init__(self,name,phoneno,course,grade):
        super().__init__(name,phoneno)
        self.course=course
        self.grade=grade


        
    @staticmethod
    def check(g):
        if g=='A+':
            return "A+ is excellent"
        elif g=='A':
            return "A is good "
        elif g=='B':
            return "B is  better "
        elif g=='C':
            return "Cis  not good "
        elif g=='D':
            return "D is bad"
        elif g=='F':
            return "F is worst"
        
        

    def displayinfo(self):
        print('-------------------student information---------------------')
        print(f'name:{self.name}\nphoneno:{self.phoneno}\ncourse:{self.course}\ngrade:{self.check(self.grade)}')

yaswanth=student('yaswanth','9087654387','PFS','A+')
raj=teacher('raj','987654323456','telugu',2345678)
yaswanth.displayinfo()
raj.displayinfo()


'''






