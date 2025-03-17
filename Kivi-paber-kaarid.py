import random

list = ["kivi", "paber", "käärid"]
results = []
player1_score = 0
player2_score = 0

print("Tere tulemast mängu 'Kivi, paber, käärid'!")
game_mode = input("Valige, kas soovite mängida /1/ teise inimesega või /2/ robotiga: ")

while True:
    try:
        if game_mode == "1":
            player1 = input("Mängija 1, sisestage oma valik (kivi, paber, käärid): ")
            if player1 not in list:
                ValueError("Vale valik, proovige uuesti.")
            
            player2 = input("Mängija 2, sisestage oma valik (kivi, paber, käärid): ")
            if player2 not in list:
                raise ValueError("Vale valik, proovige uuesti.")
        
        elif game_mode == "2":
            player1 = input("Mängija 1, sisestage oma valik (kivi, paber, käärid): ")
            if player1 not in list:
                raise ValueError("Vale valik, proovige uuesti.")
            
            player2 = random.choice(list)
            print(f"Robot valis: {player2}")
        
        if player1 == player2:
            winner = "Viik"
        elif player1 == "kivi" and player2 == "käärid":
             player1 == "paber" and player2 == "kivi"
             player1 == "käärid" and player2 == "paber"
             winner = "Mängija 1 võidab"
             player1_score += 1
        else:
            winner = "Mängija 2 võidab"
            player2_score += 1
        
        results.append((player1, player2, winner))
        print(f"Tulemus: {winner}")
        
        again = input("Kas soovite mängida uuesti? (jah/ei): ")
        if again == "ei":
            break
        elif again == "jah":
            print("Mäng jätkub!")
            continue

    except ValueError:
        print("Vale valik, proovige uuesti.")

print("Mängu tulemused:")
for i in results:
    print(f"Mängija 1 - {i[0]}, Mängija 2 - {i[1]}, Tulemus - {i[2]}")
    print("Mäng läbi!")