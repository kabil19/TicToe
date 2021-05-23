theBoard = {
    1: '', 2: '', 3: '',
    4: '', 5: '', 6: '',
    7: '', 8: '', 9: ''
}


def gameBoard(board):
    print("\t       |" + board[1] + "\t         |" + board[2] + "\t         |" + board[3] + "\t          |")
    print('-------------------------------------------------------------------------')
    print("\t       |" + board[4] + "\t         |" + board[5] + "\t         |" + board[6] + "\t          |")
    print('-------------------------------------------------------------------------')
    print("\t       |" + board[7] + "\t         |" + board[8] + "\t         |" + board[9] + "\t          |")
    print('-------------------------------------------------------------------------')


# since there I can't stop the 2ndWhile loop using check() meth, i had to create a universal break_out variable..
break_out = False
data = ''


def playGame():
    global data
    gameBoard(theBoard)
    count = 0
    while count == 0:
        data = input("Are u X or O\n")
        if data == "X" or data == "O":
            break
        else:
            print("Give a valid input Stupid!!")
    while count < 10:  # 2ndWhile
        place = int(input("Enter a Slot To Place Your Symbol\n "))
        if 0 < place <= 9:
            if theBoard[place] == "":
                count += 1
                print(count)
                theBoard[place] = data
                check()
                if break_out is True:  # used to break the loop using Universal Variable from check() meth
                    gameBoard(theBoard)
                    break
                gameBoard(theBoard)
                if count == 9:
                    print("Game Tied")
                    break
                elif data == "X":
                    print("O's Turn")
                    data = "O"
                else:
                    print("X's Turn")
                    data = "X"
            else:
                print(place)
                print("The Place is Already Taken")
        else:
            print("The Slot ", place, " isn't available")


#   To check who has won in any angle..
def check():
    global break_out
    if theBoard[1] == 'X' and theBoard[2] == 'X' and theBoard[3] == 'X':
        print("Game Over \nX Won")
        break_out = True
        # return gameBoard(theBoard)
    elif theBoard[1] == 'O' and theBoard[2] == 'O' and theBoard[3] == 'O':
        print("Game Over \nO Won")
        break_out = True
    elif theBoard[1] == 'X' and theBoard[5] == 'X' and theBoard[9] == 'X':
        print("Game Over \nX Won")
        break_out = True
    elif theBoard[1] == 'O' and theBoard[5] == 'O' and theBoard[9] == 'O':
        print("Game Over \nO Won")
        break_out = True
    elif theBoard[1] == 'X' and theBoard[4] == 'X' and theBoard[7] == 'X':
        print("Game Over \nX Won")
        break_out = True
    elif theBoard[1] == 'O' and theBoard[4] == 'O' and theBoard[7] == 'O':
        print("Game Over \nO Won")
        break_out = True
    elif theBoard[4] == "X" and theBoard[5] == "X" and theBoard[6] == "X":
        print("Game Over \nX Won")
        break_out = True
    elif theBoard[4] == "O" and theBoard[5] == "O" and theBoard[6] == "O":
        print("Game Over \nO Won")
        break_out = True
    elif theBoard[3] == "X" and theBoard[6] == "X" and theBoard[9] == "X":
        print("Game Over \nX Won")
        break_out = True
    elif theBoard[3] == "O" and theBoard[6] == "O" and theBoard[9] == "O":
        print("Game Over \nO Won")
        break_out = True
    elif theBoard[3] == "X" and theBoard[5] == "X" and theBoard[7] == "X":
        print("Game Over \nX Won")
        break_out = True
    elif theBoard[3] == "O" and theBoard[5] == "O" and theBoard[7] == "O":
        print("Game Over \nO Won")
        break_out = True
    elif theBoard[7] == "X" and theBoard[8] == "X" and theBoard[9] == "X":
        print("Game Over \nX Won")
        break_out = True
    elif theBoard[7] == "O" and theBoard[8] == "O" and theBoard[9] == "O":
        print("Game Over \nO Won")
        break_out = True
    elif theBoard[2] == "X" and theBoard[5] == "X" and theBoard[8] == "X":
        print("Game Over \nX Won")
        break_out = True
    elif theBoard[2] == "O" and theBoard[5] == "O" and theBoard[8] == "O":
        print("Game Over \nO Won")
        break_out = True


# execution
playGame()
