from enemy import *
import random


class Ogre(Enemy):

    def __init__(self, health_point: int, attack_damage: int):
        super().__init__(
            type_of_enemy= "Ogre",
            health_point= health_point,
            attack_damage= attack_damage
        )

    def talk(self):
        print("The Ogre is slamming its fist on the ground.")
    
    def special_attack(self):
        did_special_attack = random.random() < 0.10
        if did_special_attack:
            self.attack_damage += 4
            print("The Ogre gets angry and increased attack damage by 4!")