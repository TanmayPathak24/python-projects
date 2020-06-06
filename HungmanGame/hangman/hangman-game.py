from hangman.wordslist import Words

class Hangman:

    @staticmethod
    def startGame():
        print("Hangman game is starting...")
        attempts = Hangman.getChances()
        word = Words.getRandomWord()
        correctWords = []
        incorrectWords = []

        while True



    @staticmethod
    def getChances():
        while True:
            try:
                attempts = input("Enter number of chances you want [1-15]")
                if 1<= attempts <= 15:
                    return attempts
                else:
                    print("{0} is not between [1-15]".format(attempts))
            except ValueError:
                print("{0} value is not integer between [0-15]".format(attempts))

    @staticmethod
    def getEncryptedLine(word, corrctWords):
        line = ""
        for _ in range(len(word)):
            line = line + "_"

        for char in corrctWords:
            