import random
import os
import time
players = int(input("How many players are there? (2 minimum players): "))

for i in range(players):
  names = input("Player name: ")
  f = open('Players.txt', "a")
  f.write(names + "\n")
  f.close()
  print("Saved name")
  print("-"*10)

f = open('Players.txt', "r")
print(f.read())
time.sleep(2)

def hangman():
    word = ["dichlorodiphenyltrichloroethane","chlorobenzylidenemalononitrile","methylenedioxymethamphetamine","antiestablishmentarianism , antiestablishmentarianism","pneumonoultramicroscopicsilicovolcan" ,"supercalifragilisticexpialidocious", "pseudopseudohypoparathyroidism", "floccinaucinihilipilification","antidisestablishmentarianism", "honorificabilitudinitatibus", "thyroparathyroidectomized", "dichlorodifluoromethane","thyroparathyroidectomy","uvulopalatopharyngoplasty","hyperbetalipoproteinemia"," laryngotracheobronchitis"]
    word = random.choice(word)
    print(" "*2000)
    guessed = ['_'] * len(word)
    attempts = 10

    while True:
        print(" ".join(guessed))
        letter = input("Guess a letter: ").lower()

        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
        else:
            attempts -= 1
            print("-"*10)
            print("Hangman +1")
            print(f"Incorrect! You have {attempts} attempts left.")
        
        if "_" not in guessed:
            print("Congratulations! You guessed the word. " +word)
            break
        
        if attempts == 0:
            print("Out of attempts. The word was "+word)
            break

hangman()