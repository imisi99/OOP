from enemy import *
import random


class Zombie(Enemy):

    def __init__(self, health_point: int, attack_damage: int):
        super().__init__(
            type_of_enemy = "Zombie",
            health_point= health_point,
            attack_damage= attack_damage
        )
    
    def talk(self):
        print("*Grumbling..*")


    def special_attack(self):
        did_special_attack = random.random() < 0.70
        if did_special_attack:
            self.health_points += 2
            print("The zombie regenerated 2HP!")

