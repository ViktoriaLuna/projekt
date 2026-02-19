print=("---Expedition---")

player = "Gustave"
boss = "Renoir"

Gustave_hp = 10030
Renoir_hp = 19700

while Renoir_hp >= 0 and Gustave_hp >= 0 :
    if player ("Lightning"):
        Renoir_hp -= 8000
    
    if boss ("Lampmaster"):
        Gustave_hp -= 7000
    
    if player ("Nightfall"):
        Renoir_hp -= 3000
    
    if boss ("Sandfall"):
        Gustave_hp -= 2000