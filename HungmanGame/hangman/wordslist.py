from random import randint

# class words handles random words
class Words:
    workList = [] # hold word list
    workListFile = "./wordlist.txt";

    @staticmethod
    def getRandomWord():
        if len(Words.workList) == 0:
            # load the words
            file = open(Words.workListFile, "r")
            for line in file:
                Words.workList.append(line)

        return Words.workList[randint(0, (len(Words.workList)))]