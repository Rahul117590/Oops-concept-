class Employee:
    def __init__(self): # it is construcator - it mean it called itself by creating the object by itself
        self.id=123
        self.salary=50000
        self.designation="SDE"

    def travel(self,destination):
        print(f"i want to visit {destination} urgently")



user1=Employee()
print(user1.salary)
user1.travel("patna")


