hossz = 12
magasság = 10

for i in range(hossz):
    for j in range(magasság):
        if i == 0:
            print("-", end = '')
        elif i == hossz-1:
            print("-", end = '')
        elif j == 0:
                print("|", end = '')
        elif j == magasság-1:
                print("|", end = '')
        else:
            print(" ", end = '')
    print("\n", end = '')

