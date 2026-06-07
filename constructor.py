import random
class GameCharactor:
    def __init__(self,name,character_type):
        self.name=name
        self.role=character_type
        self.health=random.randint(80,100)
        self.attack_power=random.randint(15,25)
        print(f"[system]:new character '{self.name} ({self.role}) has been spawned!")

    def show_stats(self):
        print(f"\n----{self.name}'s profile----")
        print(f'Role         :{self.role}')
        print(f"Health (HP)  :{self.health}")
        print(f"Attack Power :{self.attack_power}")
        print(f"-" * 28)
    def attack(self,enemy):
        print(f"\n {self.name} attacks {enemy.name}!")
        enemy.health-=self.attack_power
        print(f"{enemy.name} took {self.attack_power} damage! Remaining Health: {enemy.health} HP")
    if __name__=="__main__":
        print("===Welcome to Rpg Charachter Creator===")
hero1=GameCharactor("IronMan","Tech-Worrior")
hero2=GameCharactor("Saktimaan","harryPotter")
hero1.show_stats()
hero2.show_stats()
hero1.attack(hero2)


 

      
        