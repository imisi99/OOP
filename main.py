from enemy import *
from zombie import *
from ogre import *
from weapon import *
from hero import *
import time

def round1(e1 : Enemy, hero : Hero):
    
    e1.talk()
    hero.talk()

    print('-----------Battle begins!------------')
    while e1.health_points > 0 and hero.health_point > 0:
        print('-------------------------------------')
        # Special attack is charging 
        e1.special_attack()
        time.sleep(1)
        if hero.health_point <= 5:
            hero.equip_weapon()
        time.sleep(1)
        print(f"{e1.get_type_of_enemy()} : {e1.health_points} HP")
        time.sleep(1)
        print(f"Hero : {hero.health_point} HP")
        time.sleep(1)

        #Player one attacks
        e1.dealing_damage()
        hero.health_point -= e1.attack_damage
        print(f"{e1.get_type_of_enemy()} has attacked the Hero for {e1.attack_damage} HP")
        time.sleep(1)

        #Player two attacks
        hero.attack()
        e1.health_points -= hero.attack_damage
        print(f"The Hero has attacked {e1.get_type_of_enemy()} for {hero.attack_damage} HP")
        time.sleep(3)

    print("------------Game Over!-----------")

    if e1.health_points > 0:
        print(f'The {e1.get_type_of_enemy()} won the battle')

    else:
        print(f'The Hero won the battle')
        time.sleep(1)
        print("The Hero will proceed to the next round with an extra 5HP")
        time.sleep(1)
        hero.health_point += 5




def round2(hero: Hero, enemy: Enemy):
    hero.talk()
    enemy.talk()

    print('--------Battle begins!--------')
    while hero.health_point > 0 and enemy.health_points > 0:
        print('----------------------')
        #Special attack
        if hero.health_point <= 5:
            hero.equip_weapon()
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
        time.sleep(1)
        print("Congratulations you have saved the hidden village!!!")
        time.sleep(1)
        print("Drop a star on the repository if you liked the game")

    else:
        print(f"The {enemy.get_type_of_enemy()} won the battle")
        time.sleep(1)
        print("Sorry Try again 😢")

    
zombie = Zombie(10,1)
ogre = Ogre(20,3)
hero = Hero(17, 3)
weapon = Weapon("Sword", 23)
hero.weapon = weapon

round1(zombie, hero)
round2(hero, ogre)
