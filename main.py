import random as r
import time as t
failed = [" ", " ", " ",
          " ", " ", " ",
          " ", " ", " "]
move = 1
win_x, win_O = False, False
game = True
place, ver, walk = 0, 0, 0

def count_pl(row, column):
    global place
    if row == 2 and column == 1:
        place = row * column * 2
    elif row == 2 and column == 2:
        place = row * column + 1
    elif row == 3 and column == 1:
        place = row * column * 2 + 1
    elif row == 3 and column == 2:
        place = row * column + 2
    else:
        place = row * column
while game:
    if move % 2 == 0:
        count_pl(row, column)
        for i in range(1, 10):
            if place == i and failed[i-1] == " ":
                failed[i-1] = "X"
                print("———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n",
                      )
                if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                    or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                    or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                    print("X wins")
                    game = False
                elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                    print("O wins")
                    game = False
                elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                      failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                    print("Draw")
                    game = False
                else:
                    move += 1
                    print("Move O")
            elif place == i and failed[i - 1] != " ":
                print("Invalid")
                print("Move 0")
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
            count_pl(row, column)
    elif move % 2 != 0:
        t.sleep(0.4)
        small_1 = [["O", " ", " ",
                    " ", "X", " ",
                    " ", " ", " "],

                   [" ", " ", "O",
                    " ", "X", " ",
                    " ", " ", " "],

                   [" ", " ", " ",
                    " ", "X", " ",
                    "O", " ", " "],

                   [" ", " ", " ",
                    " ", "X", " ",
                    " ", " ", "O"]]

        small_2 = [[["O", "X", "X",
                    " ", "X", " ",
                    "O", " ", "O"],

                    ["O", " ", "X",
                     " ", "X", "X",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     " ", "X", " ",
                     "O", "X", "O"],

                    ["O", " ", "X",
                     "X", "X", " ",
                     "O", " ", "O"],

                    ["O", "X", "O",
                     " ", "X", " ",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     " ", "X", "X",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     " ", "X", " ",
                     "X", "X", "O"],

                    ["O", " ", "O",
                     "X", "X", " ",
                     "X", " ", "O"]],


                    [["O","X", "O",
                     " ", "X", " ",
                     "O", " ", "X"],

                     ["O", " ", "O",
                      "X", "X", " ",
                      "O", " ", "X"],

                     ["O", " ", "O",
                      " ", "X", " ",
                      "O", "X", "X"],

                     ["O", " ", "O",
                      " ", "X", "X",
                      "O", " ", "X"],

                     ["X", "X", "O",
                      " ", "X", " ",
                      "O", " ", "O"],

                     ["X", " ", "O",
                      "X", "X", " ",
                      "O", " ", "O"],

                     ["X", " ", "O",
                      " ", "X", " ",
                      "O", "X", "O"],

                     ["X", " ", "O",
                      " ", "X", "X",
                      "O", " ", "O"]]]

        small_3 = [[["X", "X", "O",
                     "X", " ", " ",
                     "O", " ", "O"],

                    ["X", " ", "O",
                     "X", "X", " ",
                     "O", " ", "O"],

                    ["X", " ", "O",
                     "X", " ", " ",
                     "O", "X", "O"],

                    ["X", " ", "O",
                     "X", " ", "X",
                     "O", " ", "O"],

                    ["X", " ", "O",
                     "X", "X", " ",
                     "O", " ", "O"],

                    ["X", "X", "O",
                     " ", "X", " ",
                     "O", " ", "O"],

                    ["X", " ", "O",
                     " ", "X", " ",
                     "O", "X", "O"],

                    ["X", " ", "O",
                     " ", "X", "X",
                     "O", " ", "O"],

                    ["X", " ", "O",
                     "X", " ", " ",
                     "O", "X", "O"],

                    ["X", "X", "O",
                     " ", " ", " ",
                     "O", "X", "O"],

                    ["X", " ", "O",
                     " ", "X", " ",
                     "O", "X", "O"],

                    ["X", " ", "O",
                     " ", " ", "X",
                     "O", "X", "O"],

                    ["X", " ", "O",
                     "X", " ", "X",
                     "O", " ", "O"],

                    ["X", "X", "O",
                     " ", " ", "X",
                     "O", " ", "O"],

                    ["X", " ", "O",
                     " ", "X", "X",
                     "O", " ", "O"],

                    ["X", " ", "O",
                     " ", " ", "X",
                     "O", "X", "O"]],


                   [["O", "X", "X",
                     "X", " ", " ",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     "X", "X", " ",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     "X", " ", " ",
                     "O", "X", "O"],

                    ["O", " ", "X",
                     "X", " ", "X",
                     "O", " ", "O"],

                    ["O", "X", "X",
                     "X", " ", " ",
                     "O", " ", "O"],

                    ["O", "X", "X",
                     " ", "X", " ",
                     "O", " ", "O"],

                    ["O", "X", "X",
                     " ", " ", " ",
                     "O", "X", "O"],

                    ["O", "X", "X",
                     " ", " ", "X",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     "X", "X", " ",
                     "O", " ", "O"],

                    ["O", "X", "X",
                     " ", "X", " ",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     " ", "X", " ",
                     "O", "X", "O"],

                    ["O", " ", "X",
                     " ", "X", "X",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     "X", " ", " ",
                     "O", "X", "O"],

                    ["O", "X", "X",
                     " ", " ", " ",
                     "O", "X", "O"],

                    ["O", " ", "X",
                     " ", "X", " ",
                     "O", "X", "O"],

                    ["O", " ", "X",
                     " ", " ", "X",
                     "O", "X", "O"],

                    ["O", " ", "X",
                     "X", " ", "X",
                     "O", " ", "O"],

                    ["O", "X", "X",
                     " ", " ", "X",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     " ", "X", "X",
                     "O", " ", "O"],

                    ["O", " ", "X",
                     " ", " ", "X",
                     "O", "X", "O"]],


                   [["O", "X", "O",
                     "X", " ", " ",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     "X", "X", " ",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     "X", " ", " ",
                     "O", "X", "X"],

                    ["O", " ", "O",
                     "X", " ", "X",
                     "O", " ", "X"],

                    ["O", "X", "O",
                     " ", " ", " ",
                     "O", " ", "X"],

                    ["O", "X", "O",
                     "X", " ", " ",
                     "O", " ", "X"],

                    ["O", "X", "O",
                     " ", "X", " ",
                     "O", " ", "X"],

                    ["O", "X", "O",
                     " ", " ", " ",
                     "O", "X", "X"],

                    ["O", "X", "O",
                     " ", " ", "X",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     "X", "X", " ",
                     "O", " ", "X"],

                    ["O", "X", "O",
                     " ", "X", " ",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     " ", "X", " ",
                     "O", "X", "X"],

                    ["O", " ", "O",
                     " ", "X", "X",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     "X", " ", " ",
                     "O", "X", "X"],

                    ["O", "X", "O",
                     " ", " ", " ",
                     "O", "X", "X"],

                    ["O", " ", "O",
                     " ", "X", " ",
                     "O", "X", "X"],

                    ["O", " ", "O",
                     " ", " ", "X",
                     "O", "X", "X"],

                    ["O", " ", "O",
                     " ", " ", "X",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     "X", " ", "X",
                     "O", " ", "X"],

                    ["O", "X", "O",
                     " ", " ", "X",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     " ", "X", "X",
                     "O", " ", "X"],

                    ["O", " ", "O",
                     " ", " ", "X",
                     "O", "X", "X"]],


                   [["O", "X", "O",
                     "X", " ", " ",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     "X", "X", " ",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     "X", " ", " ",
                     "X", "X", "O"],

                    ["O", " ", "O",
                     "X", " ", "X",
                     "X", " ", "O"],

                    ["O", "X", "O",
                     "X", " ", " ",
                     "X", " ", "O"],

                    ["O", "X", "O",
                     " ", "X", " ",
                     "X", " ", "O"],

                    ["O", "X", "O",
                     " ", " ", " ",
                     "X", "X", "O"],

                    ["O", "X", "O",
                     " ", " ", "X",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     "X", "X", " ",
                     "X", " ", "O"],

                    ["O", "X", "O",
                     " ", "X", " ",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     " ", "X", " ",
                     "X", "X", "O"],

                    ["O", " ", "O",
                     " ", "X", "X",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     "X", " ", " ",
                     "X", "X", "O"],

                    ["O", "X", "O",
                     " ", " ", " ",
                     "X", "X", "O"],

                    ["O", " ", "O",
                     " ", "X", " ",
                     "X", "X", "O"],

                    ["O", " ", "O",
                     " ", " ", "X",
                     "X", "X", "O"],

                    ["O", " ", "O",
                     "X", " ", "X",
                     "X", " ", "O"],

                    ["O", "X", "O",
                     " ", " ", "X",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     " ", "X", "X",
                     "X", " ", "O"],

                    ["O", " ", "O",
                     " ", " ", "X",
                     "X", "X", "O"]]]
        small_4 = ["O", "X", "O",
                   "X", " ", "X",
                   "O", "X", "O"]

        bot_place = r.randint(0,3)
        if bot_place == 0:
            walk = 0
        elif bot_place == 1:
            walk = 2
        elif bot_place == 2:
            walk = 6
        elif bot_place == 3:
            walk = 8
        if failed == small_1[0] and ver == 1:
            failed[8] = "O"
            print("———————\n",
                  f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                  "———————\n",
                  f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                  "———————\n",
                  f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                  "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed == small_1[1] and ver == 1:
            failed[6] = "O"
            print(" ———————\n",
                  f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                  "———————\n",
                  f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                  "———————\n",
                  f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                  "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed == small_1[2] and ver == 1:
            failed[2] = "O"
            print("———————\n",
                  f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                  "———————\n",
                  f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                  "———————\n",
                  f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                  "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed == small_1[3] and ver == 1:
            failed[0] = "O"
            print("———————\n",
                  f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                  "———————\n",
                  f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                  "———————\n",
                  f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                  "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed in small_2[0] and ver == 3:
            if failed[3] == " " and failed[6] != "X":
                failed[3] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[7] == " " and failed[6] != "X":
                failed[7] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[1] == " " and failed[6] == "X":
                failed[1] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            else:
                failed[5] = "O"
                print("———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed in small_2[1] and ver == 3:
            if failed[7] == " " and failed[8] != "X":
                failed[7] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[5] == " " and failed[8] != "X":
                failed[5] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[3] == " " and failed[8] == "X":
                failed[3] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            else:
                failed[1] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed in small_3[0] and ver == 3:
            if failed[7] == " ":
                failed[7] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[5] == " ":
                failed[5] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[4] == " ":
                failed[4] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed in small_3[1] and ver == 3:
            if failed[7] == " ":
                failed[7] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[3] == " ":
                failed[3] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[4] == " ":
                failed[4] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed in small_3[2] and ver == 3:
            if failed[1] == " ":
                failed[1] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[3] == " ":
                failed[3] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[4] == " ":
                failed[4] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed in small_3[3] and ver == 3:
            if failed[1] == " ":
                failed[1] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[5] == " ":
                failed[5] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            elif failed[4] == " ":
                failed[4] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed == small_4:
            if failed[4] == " ":
                failed[4] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif failed[walk] == " ":
            failed[walk] = "O"
            print(" ———————\n",
                  f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                  "———————\n",
                  f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                  "———————\n",
                  f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                  "———————\n")
            if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                print("X wins")
                game = False
            elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                  or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                print("O wins")
                game = False
            elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                  failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                print("Draw")
                game = False
            else:
                move += 1
                print("Move X")
                ver += 1
                try:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                except:
                    row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
        elif ver > 4:
            random_choice = r.randint(0,8)
            if failed[random_choice] == " ":
                failed[random_choice] = "O"
                print(" ———————\n",
                      f"|{failed[0]}|{failed[1]}|{failed[2]}|\n",
                      "———————\n",
                      f"|{failed[3]}|{failed[4]}|{failed[5]}|\n",
                      "———————\n",
                      f"|{failed[6]}|{failed[7]}|{failed[8]}|\n",
                      "———————\n")
                if (failed[0] == "X" and failed[1] == "X" and failed[2] == "X" or failed[3] == "X" and failed[4] == "X" and failed[5] == "X" or failed[6] == "X" and failed[7] == "X" and failed[8] == "X"
                    or failed[0] == "X" and failed[3] == "X" and failed[6] == "X" or failed[1] == "X" and failed[4] == "X" and failed[7] == "X" or failed[2] == "X" and failed[5] == "X" and failed[8] == "X"
                    or failed[0] == "X" and failed[4] == "X" and failed[8] == "X" or failed[2] == "X" and failed[4] == "X" and failed[6] == "X"):
                    print("X wins")
                    game = False
                elif (failed[0] == "O" and failed[1] == "O" and failed[2] == "O" or failed[3] == "O" and failed[4] == "O" and failed[5] == "O" or failed[6] == "O" and failed[7] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[3] == "O" and failed[6] == "O" or failed[1] == "O" and failed[4] == "O" and failed[7] == "O" or failed[2] == "O" and failed[5] == "O" and failed[8] == "O"
                      or failed[0] == "O" and failed[4] == "O" and failed[8] == "O" or failed[2] == "O" and failed[4] == "O" and failed[6] == "O"):
                    print("O wins")
                    game = False
                elif (failed[0] != " " and failed[1] != " " and failed[2] != "" and failed[3] != " " and failed[4] and
                      failed[5] != " " and failed[6] and failed[7] != " " and failed[8] != " "):
                    print("Draw")
                    game = False
                else:
                    move += 1
                    print("Move X")
                    ver += 1
                    print(ver)
                    try:
                        row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
                    except:
                        row, column = int(input("Enter a row: ")), int(input("Enter a column: "))
    count_pl(row,column)

