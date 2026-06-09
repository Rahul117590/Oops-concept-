class Student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.__percentage=percentage # now it make this attributes private although in python nothing is private
                                     # unlike the other language that's why people say that python is mature language
    #getter method    
    def get_percentage(self): # this is the way to call the private variable 
        return self.__percentage
    #setter method
    def set_percentage(self,new_percentage_value):
        self.percentage=new_percentage_value
        print(f"your value will upated here so your new value is --> {self.percentage}")

student1=Student('rahul',10,84) # this is the object call 
print(student1.get_percentage()) 
#student1.__percentage # you can't call like that so you need to call it by using method 
print(student1._Student__percentage) # you can also call like it but this is not the good way to call that why we use getter and setter method

#student1.set_percentage(90)       

