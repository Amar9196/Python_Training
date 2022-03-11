'''
Created on Jul 17, 2019

@author: srilakshmig
'''

class Student:
    course = "Python"
    def __init__(self, sid=0,name="",age=18): #constructor
        self.__sid = sid
        self.__name = name
        self.__age = age

    def get_id(self):
        return self.__sid


    def get_name(self):
        return self.__name


    def get_age(self):
        return self.__age


    def set_id(self, value):
        self.__id = value


    def set_name(self, value):
        self.__name = value


    def set_age(self, value):
        self.__age = value


    def del_id(self):
        del self.__sid


    def del_name(self):
        del self.__name


    def del_age(self):
        del self.__age
      
    id = property(get_id, set_id, del_id, "id's docstring")
    name = property(get_name, set_name, del_name, "name's docstring")
    age = property(get_age, set_age, del_age, "age's docstring")
#     def __init__(self,id,name,age):
#         pass

student1 = Student(sid=1010,name="sai")
print("The student name is ",student1.get_name())
student2 = Student(101,"srilakshmi",22)

print(student1._Student__sid)

print(student2.course)
print(Student.course)