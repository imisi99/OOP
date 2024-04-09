from enemy import *


class Ogre(Enemy):

    def __init__(self, health_point: int, attack_damage: int):
        super().__init__(
            type_of_enemy= "Ogre",
            health_point= health_point,
            attack_damage= attack_damage
        )

    def talk(self):
        return f"The Ogre is slamming its fist on the ground."
    
    