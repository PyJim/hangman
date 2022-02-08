#----
# Project instructions: https://kiboschool.notion.site/Project-Hangman-e7e41de2fbc2462091bccd9034f83baf
# Team Member 1: [Jimmy, Kodwo Essel]
# Team Member 2: [Fadeela, Sheini]
#----
#Beginning
SecretWord = "Coding"
SecretWord = SecretWord.upper()
encryptedWord = ["_"]*len(SecretWord)
print("Let's play Hangman!")
print("  _ _ _ _")
print(" |       |")
print(" |")
print(" |")
print(" |")
print(" |")
print("_|_")
attempts = 0
r = 0
hang = [" |       |", " |       |", " |       0", " |      \|/", " |      / \\"]
while attempts < 6:
    guess = input("Guess a letter in the secret word: ").upper()
    if guess in SecretWord:
        a = []
        for i in range(len(SecretWord)):
            if SecretWord[i] == guess:
                a.append(i)
        for index in a:
            encryptedWord[index] = guess
        print("Good Job, "+guess+" is in the word")
    else:
        print(guess+" is not in the word")
        print("  _ _ _ _")
        for x in hang[0:r]:
            print(x)  
        r+=1
        attempts+=1
        print(" |")
        print(" |")
        print("_|_")
    print("".join(encryptedWord))
    if "".join(encryptedWord)== SecretWord:
        print("CONGRATULATIONS!!! YOU ARE AMAZING")
        break
    if attempts == 6:
        print("Sorry! The secret word is "+ SecretWord)
