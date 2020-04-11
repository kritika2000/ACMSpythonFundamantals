#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Student:
    
    def __init__(self, name = "", age = 0, course = ""):
        self.__name = name
        self.__age = age
        self.__course = course
        
    def set_name(self, name):
        self.__name = name
        
    def set_age(self, age):
        self.__age = age
        
    def set_course(self, course):
        self.__course = course 
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_course(self):
        return self.__course
    
    def print_Details(self):
        print(self.__name,self.__age,self.__course)
    
s1 = Student("Kritika", 20)

s2 = Student("Antosha")

s3 = Student()

s3.set_name("Heena")
s3.set_age(20)
s3.set_course("MBBS")

s1.set_course("B.Tech")
s1.print_Details()

s2.print_Details()

s3.print_Details()


# In[ ]:




