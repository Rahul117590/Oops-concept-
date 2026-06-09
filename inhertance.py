class student:
    def __init__(self,name,grade,percentage):
        self.name=name
        self.grade=grade
        self.percentage=percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade} with {self.percentage}")
class graduate(student):
    def __init__(self,name,grade,percentage,stream): # see here we copy all things from parents class 
        super().__init__(name,grade,percentage) # this is the process from this parents class attribute run by
        self.stream=stream                       # - using super() keyword function 
        

#student1=student("rahul","betch-4th_year",7.34)
graduate_student=graduate("rahul","btech-4th_year",70.34,"CSE")
print(graduate_student.student_details())

