import random
from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 12, 124, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic

cure= Spell("Cure", 12, 120, "white")
cura= Spell("Cura", 18, 200, "white")


# magic = [{"name": "Fire", "cost": 10, "dmg": 100},
#          {"name": "Thunder", "cost": 12, "dmg": 124},
#          {"name": "Blizzard", "cost": 10, "dmg": 100}] 

# Create some items
portion = Item("Portion", "portion", "Heals 50 HP", 50)
hipotion = Item("Hi-Potion", "hipotion", "Heals 100 HP", 100)
superpotion = Item("Super Potion", "superpotion", "Heals 500 HP", 500)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
megaelixir = Item("Mega Elixir", "megaelixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# initilize player and enemy
player_spells = [fire, thunder, blizzard, meteor, cure, cura]

# player_items = [portion,hipotion,superpotion,elixir,megaelixir,grenade]
player_items = [{"item": portion, "quantity": 15},
                {"item": hipotion, "quantity": 5},
                {"item": superpotion, "quantity": 5},
                {"item": elixir, "quantity": 5},
                {"item": megaelixir, "quantity": 2},
                {"item": grenade, "quantity": 5}]

                
player1 = Person("Sumith",3260, 132, 300, 34, player_spells, player_items)
player2 = Person("Sam",4160, 188, 311, 34, player_spells, player_items)
player3= Person("John",3009, 174, 288, 34, player_spells, player_items)

enemyspells = [fire, thunder, meteor,cure]

enemy1 = Person("Mighty Robot",10500, 132, 300, 25,enemyspells,[])
enemy2 = Person("Imp",1200, 130, 560, 325,enemyspells,[])
enemy3 = Person("Imp",1200, 130, 560, 325,enemyspells,[])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True
i=0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("====================")
    print("\n\n")
    print("NAME                   HP                                     MP")   
    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
         
    for player in players:
      
        player.choose_action()
        choice = input("    Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_damage()
            enemy = player.choose_target(enemies)

            enemies[enemy].take_damage(dmg)

            print("You attacked ", enemies[enemy].name, " for " ,  dmg, "points of damage. Enemy HP:", enemies[enemy].get_hp())

            if enemies[enemy].get_hp() == 0:
                print(enemies[enemy].name + " has died")
                del enemies[enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("    Choose magic: ")) - 1

            if magic_choice == -1:
                continue

            # magic_dmg = player.generate_spell_damage(magic_choice)
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            cost = spell.cost
            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == "black":
                
                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(magic_dmg)
           
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage to"+ enemies[enemy].name + bcolors.ENDC)
        
            # print("You attacked for", magic_dmg, "points of damage. Enemy HP:", enemy.get_hp())

        elif index == 2:
            player.choose_item()
            item_choice = int(input("    Choose item: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]["item"]
            
            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + item.name + " is out of stock" + bcolors.ENDC)
                continue
            player.items[item_choice]["quantity"] -= 1
            
        

            if item.type == "portion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)
            elif item.type == "elixir":

                if item.name == "Mega Elixir":
                    for i in players:
                        i.hp = i.maxhp
                        i.mp = i.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restores party's HP/MP" + bcolors.ENDC)
                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.OKGREEN + "\n" + item.name + " fully restores HP/MP" + bcolors.ENDC)
            elif item.type == "attack":

                enemy = player.choose_target(enemies)

                enemies[enemy].take_damage(item.prop)

                print(bcolors.FAIL + "\n" + item.name + " deals", str(item.prop), "points of damage to " + enemies[enemy].name + bcolors.ENDC)

                if enemies[enemy].get_hp() == 0:
                    print(enemies[enemy].name + " has died")
                    del enemies[enemy]

            elif item.type == "hipotion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)   
            elif item.type == "superpotion": 
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item.name + " heals for", str(item.prop), "HP" + bcolors.ENDC)

        # Check if battle is over
        defeted_enemies = 0
        defeted_players = 0

        for enemy in enemies:
            if enemy.get_hp() == 0:
                defeted_enemies += 1    
        
        for player in players:
            if player.get_hp() == 0:
                defeted_players += 1

        # Check if player won
        if defeted_enemies == 3:
            print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
            running = False
        #Check if enemy won
        elif defeted_players == 3:
            print(bcolors.FAIL + "You have been defeated by the enemy!" + bcolors.ENDC)
            running = False
        
        # Enemy attack phase
        for enemy in enemies:

            enemy_choice = random.randrange(0,3)

            if enemy_choice == 0:
                #choose attack
                target = random.randrange(0,3)
                enemy_dmg = enemies[0].generate_damage()
                players[target].take_damage(enemy_dmg)
                print(enemy.name + " attacks " + players[target].name +" for", enemy_dmg, )

            elif enemy_choice == 1:
                spell, magic_dmg = enemy.choose_enemy_spell()
                enemy.reduce_mp(spell.cost)
                if spell.type == "white":
                    enemy.heal(magic_dmg)
                    print(bcolors.OKBLUE + spell.name + " heals " + enemy.name + " for", str(magic_dmg), "HP" + bcolors.ENDC)
                elif spell.type == "black":
                    target = random.randrange(0,3)
                    players[target].take_damage(magic_dmg)
                    
                    print(bcolors.OKBLUE + "\n" +  enemy.name + " chose", spell.name, "damage is", magic_dmg)

                    if players[target].get_hp() == 0:
                        print(players[target].name + " has died")
                        del players[target]

                # print("Enemy chose", spell.name, "damage is", magic_dmg)
        

        # print("=====================================")
        # print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

        # print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)   
        # print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)
        # print("=====================================")
        
        # elif player.get_hp() == 0:
        #     print(bcolors.FAIL + "You have been defeated by the enemy!" + bcolors.ENDC)
        #     running = False
        # elif enemy.get_hp() == 0:
        #     print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        #     running = False
            
        # print("====================")
        # print("You chose", player.actions[index])
        # print("====================")

# print(player.generate_damage())
# print(player.generate_spell_damage(0))
# print(player.generate_damage(1))
