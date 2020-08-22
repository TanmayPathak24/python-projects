from hangman.wordslist import Words

class Hangman:

    @staticmethod
    def startGame():
        print("Hangman game is starting...")
        attempts = Hangman.getChances()
        word = Words.getRandomWord()
        correctWords = []
        incorrectWords = []
        encLine = Hangman.getEncryptedLine(word, [])

        while True:
            print("Gess the word for : {0}".format(encLine))
            print("Incorrect characters : {0}".format(incorrectWords))
            print("Chances left : {0}".format(attempts))
            inputchar = input("Enter a letter : ")

            if inputchar in list(word):
                print("{0} is correct.".format(inputchar))
                correctWords.append(inputchar)
                encLine = Hangman.getEncryptedLine(word, correctWords)
            else:
                print("{0} is incorrect.".format(inputchar))
                incorrectWords.append(inputchar)
                attempts = attempts - 1

            # fail condition
            if attempts == 0:
                print("You loose the game")
                print("Correct word is : {0}".format(word))
                print("Try again")
                return

            # win condition
            if "_" not in list(encLine):
                print("You won the game")
                print("Try again")
                return

            print("=========================================================")





    @staticmethod
    def getChances():
        while True:
            try:
                attempts = input("Enter number of chances you want [1-15]")
                if 1<= int(attempts) <= 15:
                    return int(attempts)
                else:
                    print("{0} is not between [1-15]".format(attempts))
            except ValueError:
                print("{0} value is not integer between [0-15]".format(attempts))

    @staticmethod
    def getEncryptedLine(word, correctWords):
        line = ""
        for index in range(len(word)):
            if word[index] in correctWords:
                line = line + word[index]
            elif word[index] == " ":
                line = line + " "
            else:
                line = line + "_"

        return line





# lest play the game
Hangman.startGame()