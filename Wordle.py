import random

words = ["poiss", "mets", "kodutöö", "andmebaas", "programmeerimine"]

word_to_guess = random.choice(words)
word_length = len(word_to_guess)

popitki = 5
popitka = 0

while popitka < popitki:
    try:
        guess = input(f"Katse {popitka + 1}/{popitki} (Sisesta {word_length} tähte sõna): ").strip().lower()
        if len(guess) != word_length:
            raise ValueError(f"Palun sisestage sõna, mis koosneb {word_length} tähest.")

    except ValueError as e:
        print(e)
        continue

    result = []
    for i in range(word_length):
        if guess[i] == word_to_guess[i]:
            result.append(f"\033[92m{guess[i]}\033[0m")
        elif guess[i] in word_to_guess:
            result.append(f"\033[93m{guess[i]}\033[0m")
        else:
            result.append(guess[i])

    print(" ".join(result))

    if guess == word_to_guess:
        print("Õnnitleme! Olete sõna ära arvanud.")
        break
    popitka += 1

else:
    print(f"Kahjuks ei õnnestunud. Õige sõna oli: {word_to_guess}")
