from enemy import *

class Zombie(Enemy):

    def __init__(self, health_point: int, attack_damage: int):
        super().__init__(
            type_of_enemy = "Zombie",
            health_point= health_point,
            attack_damage= attack_damage
        )
    
    def talk(self):
        return "*Grumbling..*"