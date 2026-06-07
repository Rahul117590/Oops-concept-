class Employee:
    def __init__(self): # it is construcator - it mean it called itself by creating the object by itself
        self.id=123
        self.salary=50000
        self.designation="SDE"

user1=Employee()
print(user1.salary)

