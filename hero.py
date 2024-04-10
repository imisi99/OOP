from weapon import *

class Hero:
    
    def __init__(self, health_point: int, attack_damage: int):
        self.health_point = health_point
        self.attack_damage = attack_damage
        self.weapon_is_equipped = False
        self.weapon: Weapon = None

        # print(f"A new Hero of {self.health_point} HP and {self.attack_damage} attack_damage has been created!")

    def equip_weapon(self):
        if self.weapon is not None and not self.weapon_is_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.weapon_is_equipped = True
            print(f"The hero has equipped his {self.weapon.weapon_type} and increased his attack_damage by {self.weapon.attack_increase} damage")
    
    def attack(self):
        print(f"Hero attacks for {self.attack_damage} HP")

    def talk(self):
        print("I see you have come to accept DEATH!!")
