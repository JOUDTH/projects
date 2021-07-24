from os import system
from time import sleep

word = str(input("type a word here: "))
system("cls")
print("")

mainList = list(" ") * len(word)
dashList = list("-") * len(word)
repeated = {}
wrongAnswers = []
wrongAnswersNO = 0
lettersList = []
fileNO = 0
listOfAll = []
index = 0
wordDict0 = {}
wordDict = {}

for i in word:
    if i in wordDict0:
        wordDict0[i] += 1
    else:
        wordDict0[i] = 1

for i in wordDict0:
    if wordDict0[i] >= 2:
        wordDict[i] = wordDict0[i]

for i in range(len(word) * 2):
    if i % 2 == 0:
        listOfAll.append(word[i // 2])
        listOfAll.append(index)
        index += 1

while len(lettersList) < len(word) and wrongAnswersNO < 7:

    letterInput = str(input("Guess a letter,(just one): "))
    system("cls")

    if len(letterInput) == 1:

        for i in range(0, len(word) * 2, 2):

            if letterInput == listOfAll[i] and mainList[listOfAll[i + 1]] == " ":
                if letterInput in wordDict:
                    for i in range(0, len(word) * 2, 2):
                        if letterInput == listOfAll[i]:
                            mainList[listOfAll[i + 1]] = letterInput
                            lettersList.append(letterInput)
                else:
                    mainList[listOfAll[i + 1]] = letterInput
                    lettersList.append(letterInput)
                break

            elif letterInput not in word and letterInput not in wrongAnswers:
                wrongAnswers.append(letterInput)
                wrongAnswersNO += 1
                fileNO = wrongAnswersNO
                break
        for i in range(2):

            if i == 0:

                for i in mainList:
                    print(i, end=" ")
                print("\n", end="")

            else:

                for i in dashList:
                    print(i, end=" ")
                print("\n", end="")

        with open(str(fileNO) + ".txt", "r") as file:

            for l in file:
                print(file.read(), end="")

        print("\n", end="")

        print("                                               wrong choices: ")

        print("                                                             -> ", end="")

        for i in wrongAnswers:

            if len(wrongAnswers) == 1:
                print(i, end="")

            else:

                if i == wrongAnswers[-1]:
                    print(i)

                else:
                    print(i, end=",")

        print("\n", end="")
    else:
        continue

system("cls")

while True:
    if len(lettersList) == len(word) and wrongAnswersNO < 7:
        print("you won")
    elif len(lettersList) < len(word) and wrongAnswersNO == 7:
        print("you lost")
    sleep(10)
    system("cls")


