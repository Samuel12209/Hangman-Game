def hangman():
    word = input("Word For others to guess: ").lower()
    print(" "*2000)
    guessed = ['_'] * len(word)
    attempts = 8

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
