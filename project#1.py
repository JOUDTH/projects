from termcolor import colored
from os import system

columns = [[" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],
           [" ", " ", " ", " ", " ", " "]]

player = 1

print("\n player turn : 1\n ")

columnInput = int(input("enter column number(1 - 7)\n : ")) - 1

while columnInput<0 or columnInput>6:
    system("cls")
    columnInput = int(input("enter column number(1 - 7)\n : ")) - 1
    

while True:
    if " " in columns[columnInput]:
        if player == 1:
            a = -1
            player = 2
            for rows in (columns[columnInput]):
                a += 1
                if rows == " ":
                    columns[columnInput][len(range(a))] = colored("o", "red")
                    # print(columns)
                    break

        elif player == 2:
            a = -1
            player = 1
            for rows in (columns[columnInput]):
                a += 1
                if rows == " ":
                    columns[columnInput][len(range(a))] = colored("o", "yellow")
                    break

        b = 0
        for l in range(11):
            if l % 2 == 0:
                b -= 1
                for k in range(13):
                    if k % 2 == 0:
                        a = k // 2
                        print(str(columns[a][b]), end="")
                    elif k % 2 == 1:
                        print("|", end="")
                print("\n", end="")
            else:
                print("-------------")

    winning = 0
    for win in range(1):
        for pq in range(7):
            t = ""
            t1, t2, t3 = "", "", ""
            for q in range(0, 4):
                t = str(columns[pq][q])
                t1 = t1 + t
                if t1 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t1 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(1, 5):
                t = str(columns[pq][q])
                t2 = t2 + t
                if t2 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t2 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(2, 6):
                t = str(columns[pq][q])
                t3 = t3 + t
                if t3 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t3 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break

        for pq in range(4):
            t = ""
            t4, t5 = "", ""
            for q in range(4):
                t = str(columns[q + pq][q])
                t4 = t4 + t
                if t4 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t4 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(4):
                t = str(columns[6 - q - pq][q])
                t5 = t5 + t
                if t5 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t5 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
        for pq in range(1):
            t = ""
            t6, t7, t8, t9 = "", "", "", ""
            for q in range(4):
                t = str(columns[q][q + 1])
                t6 = t6 + t
                if t6 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t6 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(4):
                t = str(columns[q][q + 2])
                t7 = t7 + t
                if t7 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t7 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(4):
                t = str(columns[6 - q - pq][q + 1])
                t8 = t8 + t
                if t8 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t8 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(4):
                t = str(columns[6 - q - pq][q + 2])
                t9 = t9 + t
                if t9 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t9 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
        for pq in range(6):
            t = ""
            t10, t11, t12, t13 = "", "", "", ""
            for q in range(0, 4):
                t = str(columns[q][pq])
                t10 = t10 + t
                if t10 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t10 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(1, 5):
                t = str(columns[q][pq])
                t11 = t11 + t
                if t11 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t11 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(2, 6):
                t = str(columns[q][pq])
                t12 = t12 + t
                if t12 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t12 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break
            for q in range(3, 7):
                t = str(columns[q][pq])
                t13 = t13 + t
                if t13 == 4 * (colored("o", "red")):
                    print("\n 1st player wins \n")
                    winning = 1
                    break
                elif t13 == 4 * (colored("o", "yellow")):
                    print("\n 2nd player wins \n")
                    winning = 1
                    break


    if winning == 1:
        break

    if player == 1:
        print("\n player turn : 1\n ")
    elif player == 2:
        print("\n player turn : 2\n ")

    columnInput = int(input("enter column number\n : ")) - 1
