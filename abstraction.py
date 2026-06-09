class student:
    def __init__(self,percentage,grade,roll):
        self.percentage=percentage
        self.grade=grade
        self.roll=roll

    

    def student_details(self): # this is method what is run inside that and how it work internally no one know
        name=input("---fill your name sir-- :  ")
        print(f"the student name is {name}")
        print(f"the student percentage marks is {self.percentage}")
        print(f"the student grade is {self.grade}")
        print(f"the student  roll no is {self.roll}")
student1=student(80.4,10,59903) # object of the above class 
student1.student_details()