class Weapon:

    def __init__(self, weapon_type: str, attack_increase: int):
        self.weapon_type = weapon_type
        self.attack_damage = attack_increase

        print(f"A new weapon has been found, Type of weapon: {self.weapon_type}, Attack_damage: {self.attack_damage}")


    