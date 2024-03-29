board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
current_player = "X"
winner = None
gamerunning = True

#print the game board
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take the player input
def playerinput(board):
    inp = int(input("Enter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp - 1] = current_player
    else:
        print("invalid spot")
        playerinput(board)

#check for win or tie
def horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
def vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
def diagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
def checktie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It is a tie!")
        gamerunning = False
def checkwin():
    global gamerunning
    if horizontal(board) or vertical(board) or diagonal(board):
        print(f"The Winner is {winner}")
        gamerunning = False

#switch the player
def switchplayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

#check for win or tie again
while gamerunning:
    playerinput(board)
    printboard(board)
    checkwin()
    if gamerunning:
        checktie(board)
    switchplayer()