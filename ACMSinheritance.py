#!/usr/bin/env python
# coding: utf-8

# In[38]:


from abc import ABC, abstractmethod

class Person(ABC):
    
    __name = None
    __age = None
    
    def set_name(self, name):
        self.__name = name
    
    def set_age(self, age):
        self.__age = age
            
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    @abstractmethod
    def get_Details(self):pass
    
class Result:
    __marks = []
    __totalMarks = 0
    
    def __init__(self, marks):
        for i in marks:
            self.__totalMarks += i
            self.__marks.append(i)
        
    def get_result(self):
        if self.__totalMarks == 0:
            return 0
        return self.__totalMarks / len(self.__marks)    
        
class Student(Person, Result):
    
    __course = None
    __dept = None
    __rollno = None
    
    def __init__(self, name, age, course, dept, roll_no):
        Person.set_name(self, name)
        Person.set_age(self, age)
        self.__course = course
        self.__dept = dept
        self.__rollno = roll_no
        
    def get_Details(self):
        print(Person.get_name(self), Person.get_age(self), self.__course, self.__dept, self.__rollno)
        
    def set_Marks(self, marks):
        Result.__init__(self, marks)
    
        
class Faculty(Person):
    
    __subjects = []
    __facID = None
    
    def __init__(self, name, age, facId, *sub):
        super().set_name(name)
        super().set_age(age)
        self.__facID = facId
        for i in sub:
            self.__subjects.append(i)
        
    def get_Details(self):
        print(super().get_name(), super().get_age(), self.__facID)    
        for i in self.__subjects:
            print(i)
        
s = Student("Kritika", 20, "BTech", "CSE",109)
s.get_Details()

s.set_Marks([100, 99, 95, 96, 91])
s.get_result()

f = Faculty("XYZ", 45, "CSE","Networking", "Programming Fundamentals", "Algorithm Design")
f.get_Details()


# In[ ]:




