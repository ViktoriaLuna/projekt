print=("---Expedition---")

player = "Gustave"
boss = "Renoir"

Gustave_hp = 10030
Renoir_hp = 19700
while Renoir_hp > 0 and Gustave_hp > 0 :
    
    player = input("Choose move (Lightning/Nightfall/Dodge/Parry): ")
    
    if player == ("Lightning"):
        Renoir_hp -= 8000
    
    elif player == ("Nightfall"):
        Renoir_hp -= 3000
        
    elif player == ("Dodge"):
        Renoir_hp -= 0
    
    elif player == ("Parry"):
        print("You prepare to parry!")
        
    else:
        print("No damage taken!")
        
    import random
    
    boss = input("Choose move (Lampmaster/Sandfall): ")
    
    if boss == ("Lampmaster"):
        if player == "Parry":
            print("Parry successful!Reduced damage!")
            Gustave_hp -= 2000
            if not dodged:
                Gustave_hp -= 7000
                else:
                    print("No damage taken!")
    
    elif boss == ("Sandfall"):
        if player == "Parry":
            print("Parry successful!Reduced damage!")
            Gustave_hp -= 500
            if not damaged:
                Gustave_hp -= 2000
            else:
                print("No damage taken!")
        
    elif boss == ("Dodge"):
        Gustave_hp -= 0
    
        
    dodge = False
    
    if player == "Dodge":
        chance = random.randint(1, 100)
        if chance <= 50:
            print("Dodge failed!")
    
    else:
        print("No damage taken!")
    
    if Renoir_hp <= 0:
        print("Gustave win!")
        break
        
    elif Gustave_hp <= 0:
        print("Renoir win!")
        break