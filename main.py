from enemy import *
from zombie import *
from ogre import *
from weapon import *
from hero import *
import time

def battle(e1 : Enemy, e2 : Enemy):
    
    e1.talk()
    e2.talk()

    print('-----------Battle begins!------------')
    while e1.health_points > 0 and e2.health_points > 0:
        print('-------------------------------------')
        # Special attack is charging 
        e1.special_attack()
        time.sleep(1)
        e2.special_attack()
        time.sleep(1)
        print(f"{e1.get_type_of_enemy()} : {e1.health_points} HP")
        print(f"{e2.get_type_of_enemy()} : {e2.health_points} HP")

        #Player one attacks
        e1.dealing_damage()
        e2.health_points -= e1.attack_damage
        print(f"{e1.get_type_of_enemy()} has attacked {e2.get_type_of_enemy()} for {e1.attack_damage} HP")

        #Player two attacks
        e2.dealing_damage()
        e1.health_points -= e2.attack_damage
        print(f"{e2.get_type_of_enemy()} has attacked {e1.get_type_of_enemy()} for {e2.attack_damage} HP")
        time.sleep(3)

    print("------------Game Over!-----------")

    if e1.health_points > 0:
        print(f'The {e1.get_type_of_enemy()} won the battle')

    else:
        print(f'The {e2.get_type_of_enemy()} won the battle')


zombie = Zombie(10,1)
ogre = Ogre(20,3)


battle(zombie, ogre)

hero = Hero(2,2)
weapon = Weapon("Sword", 23)
hero.equip_weapon()
hero.attack()