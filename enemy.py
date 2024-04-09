class Enemy:

    def __init__(self, type_of_enemy : str, health_point : int, attack_damage : int):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_point
        self.attack_damage = attack_damage

        print(f"A new enemy has been created:\n Type of enemy = {type_of_enemy} \n Health point = {health_point}\n attack damage = {attack_damage} \n")

    
    def talk(self):
        print(f"I am {self.__type_of_enemy}, Be prepared to fight!")

    def move_forward(self):
        print(f"The {self.__type_of_enemy} is moving forward to fight, proceed with caution it deals {self.attack_damage} damage point and it has an health of {self.health_points}!")
    
    def dealing_damage(self):
        print(f"The {self.__type_of_enemy} has made contact with you and has attacked you are down {self.attack_damage} health point")

    def get_type_of_enemy(self):
        return self.__type_of_enemy