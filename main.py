from enemy import *
from zombie import *
from ogre import *
from weapon import *
from hero import *
import time

def enemy_battle(e1 : Enemy, e2 : Enemy):
    
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
        time.sleep(1)
        print(f"{e2.get_type_of_enemy()} : {e2.health_points} HP")
        time.sleep(1)

        #Player one attacks
        e1.dealing_damage()
        e2.health_points -= e1.attack_damage
        print(f"{e1.get_type_of_enemy()} has attacked {e2.get_type_of_enemy()} for {e1.attack_damage} HP")
        time.sleep(1)

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




def hero_battle(hero: Hero, enemy: Enemy):
    hero.talk()
    enemy.talk()

    print('--------Battle begins!--------')
    while hero.health_point > 0 and enemy.health_points > 0:
        print('----------------------')
        #Special attack
        enemy.special_attack()
        time.sleep(1)
        print(f"{enemy.get_type_of_enemy()} : {enemy.health_points} HP")
        time.sleep(1)
        print(f"Hero : {hero.health_point} HP")
        time.sleep(1)

        #Hero attacks
        hero.attack()
        enemy.health_points -= hero.attack_damage
        print(f"Hero has attacked {enemy.get_type_of_enemy()} for {hero.attack_damage} HP")
        time.sleep(1)

        #Enemy attacks
        enemy.dealing_damage()
        hero.health_point -= enemy.attack_damage
        print(f"{enemy.get_type_of_enemy()} has attacked the Hero for {enemy.attack_damage} HP")
        time.sleep(2)

    print('-------Game Over!-------')

    if hero.health_point > 0:
        print("The Hero won the battle")

    else:
        print(f"{enemy.get_type_of_enemy()} won the battle")


    
zombie = Zombie(10,1)
ogre = Ogre(20,3)

enemy_battle(zombie, ogre)


hero = Hero(15, 3)
weapon = Weapon("Sword", 23)
hero.weapon = weapon
hero_battle(hero, ogre)
