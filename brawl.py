from random import randint

spelare_1_namn = input("Choose a name for player 1: ")
spelare_2_namn = input("Choose a name for player 2: ")

spelare_1_score = 10
spelare_2_score = 10

while True:
    spel_runda = 0
    
    spelare_1_kast = randint(1, 6)
    spelare_2_kast = randint(1, 6)
    if spelare_1_score > 0 or spelare_2_score > 0:
        if spelare_1_kast > spelare_2_kast:
            skada = spelare_1_kast - spelare_2_kast
            
            spelare_2_score -= skada
            print("#----------------------------#")
            print(f"{spelare_1_namn} rullar {spelare_1_kast}! ")
            print(f"{spelare_2_namn} rullar {spelare_2_kast}! ")
            print("#----------------------------#")

            print(f"{spelare_1_namn} gör {skada} skada!")
            print(f"{spelare_2_namn} har nu {spelare_2_score} liv kvar!")
            print("#----------------------------#")
            kasta_om = input("Klicka enter för att kasta igen!")


        elif spelare_2_kast > spelare_1_kast :
            skada = spelare_2_kast - spelare_1_kast

            spelare_1_score -= skada
            print("#----------------------------#")
            print(f"{spelare_1_namn} rullar {spelare_1_kast}! ")
            print(f"{spelare_2_namn} rullar {spelare_2_kast}! ")
            print("#----------------------------#")

            print(f"{spelare_2_namn} gör {skada} skada!")
            print(f"{spelare_1_namn} har nu {spelare_1_score} liv kvar!")
            print("#----------------------------#")
            kasta_om = input("Klicka enter för att kasta igen! ")
    else:
        if spelare_1_score < 0:
            print(f"{spelare_1_namn} har inga liv kvar!")
            print(f"{spelare_2_namn} vinner!")

        else spelare_2_score < 0:
            print(f"{spelare_2_namn} har inga liv kvar!")
            print(f"{spelare_1_namn} vinner!")