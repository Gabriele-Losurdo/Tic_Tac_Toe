import random
import time


def display_board(board):
    for i in range(len(board)):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        for j in range(len(board)):
            print("|  ", board[i][j], end="   ")
        print("|")
        print("|       |       |       |")
    print("+-------+-------+-------+")
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    result = False
    k = 0
    print("---------------------------------------------------------------------------------------------")
    while not result:
        c = 0
        if k == 0:
            move = str(input("Enter your move: "))
        else:
            t = k+1
            print("Enter your move for the", t, "time: ")
            move = str(input())
        for i in range(len(board)):
            c += 1
            for j in range(len(board)):

                if move == board[i][j]:
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        board[i][j] = 'O'
                        result = True
                else:
                    if board[i][j] == 'X' and board[i][j] == 'O':
                        result = False
                c += 1
        k += 1
    time.sleep(1)
    display_board(board)
    print("---------------------------------------------------------------------------------------------")
    time.sleep(1)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_field_1 = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 'X' and board[i][j] != 'O':
                free_field_1 += 1
    return free_field_1


def victory_for(board,sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':  # first column
        sign = 1
    elif board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':  # first row
        sign = 1
    elif board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':  # second row
        sign = 1
    elif board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':  # second column
        sign = 1
    elif board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':  # third row
        sign = 1
    elif board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':  # third column
        sign = 1
    elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':  # first trav
        sign = 1
    elif board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':  # second trav
        sign = 1

    if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':  # first column
        sign = 2
    elif board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':  # first row
        sign = 2
    elif board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':  # second row
        sign = 2
    elif board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':  # second column
        sign = 2
    elif board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':  # third row
        sign = 2
    elif board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':  # third column
        sign = 2
    elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':  # first trav
        sign = 2
    elif board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':  # second trav
        sign = 2

    return sign


def draw_move(board):
    #The function draws the computer's move and updates the board.
    print("-------------------------------------------------------------------------------------------------")
    print("Turn of the computer")
    result = False
    while not result:
        move = str(random.randint(1, 9))
        c=0
        for i in range(len(board)):
            c += 1
            for j in range(len(board)):
                if move == board[i][j]:
                    if board[i][j] != 'X' and board[i][j] != 'O':
                        board[i][j] = 'X'
                        result = True
                else:
                    if board[i][j] == 'X' and board[i][j] == 'O':
                        result = False
                c += 1
    time.sleep(1)
    display_board(board)
    print("------------------------------------------------------------------------------------------------")
    time.sleep(1)


board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
board_of_rematch = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
print("----------------------------------------------------------------------------------------------------")
print("The computer will start with the first move...", "\nThe computer will start the game using the using X")
print("You will use O...")
print("Countdown \n3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0", "\nThe game is started")
display_board(board)
try1 = 1
free_field = 0
victory = 0  # False for computer and # True for the client
while victory == 0:
    draw_move(board)
    free_field = make_list_of_free_fields(board)
    counter_field = 9-free_field
    if counter_field > 4:
        victory = victory_for(board, victory)
    enter_move(board)
    free_field = make_list_of_free_fields(board)
    counter_field = 9 - free_field
    if counter_field > 4:
        victory = victory_for(board, victory)

print("The winner is... \n3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("0")
if victory == 2:
    print("Is you 'O'")
elif victory == 1:
    print("Is computer 'X'")
else:
    print("Draw")

