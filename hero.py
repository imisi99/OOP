from weapon import *

class Hero:
    
    def __init__(self, health_point: int, attack_damage: int):
        self.health_point = health_point
        self.attack_damage = attack_damage
        self.weapon_is_equipped = False
        self.weapon = None

        print(f"A new Hero of {self.health_point} HP and {self.attack_damage} attack_damage has been created!")

    def equip_weapon(self):
        if self.weapon is not None and not self.weapon_is_equipped:
            self.attack_damage += self.weapon.attack_increase
            self.weapon_is_equipped = True
        
    
    def attack(self):
        print(f"Hero attacks for {self.attack_damage} damage")