class Dog:
    def make_sound(self): 
        return "Woof"
    
class Cat:
    def make_sound(self): #both have same name but both work differantly
        return "Meow"
    
def animal_behavior(animal_object):
    print(f"this animal sound like ",{animal_object.make_sound()})

husky=Dog()
safira=Cat()

animal_behavior(husky)# same function but with different answer
animal_behavior(safira)# same funciton but with differnt anser