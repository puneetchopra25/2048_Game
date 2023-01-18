# student name: Puneet Chopra
# student number: 95311767

# A command-line 2048 game

import random, sys

board: list = []  # a 2-D list to keep current status of the game board

def init() -> None:  # Use as is
    """ 
        initializes the board variable
        and displays the initial board
        and prints a welcome message
    """
    for _ in range(4):     # initialize the board cells with ''
        rowList = []
        for _ in range(4):
            rowList.append('')
        board.append(rowList)

    # add two starting 2's at random cells:
    countOfTwosPlacedAtTheBeginning = 0  
    while countOfTwosPlacedAtTheBeginning < 2:  
        row = random.randint(0, 3)
        column = random.randint(0, 3)
        if board[row][column] == '': # if not already taken
            board[row][column] = 2
            countOfTwosPlacedAtTheBeginning += 1
    
    print(); print("Welcome! Let's play the 2048 game."); print()


def displayGame() -> None:  # Use as is
    """ displays the current board on the console """

    print("+-----+-----+-----+-----+")
    for row in range(4): 
        for column in range(4):
            cell = board[row][column] 
            print(f"|{str(cell).center(5)}", end="")
        print("|")
        print("+-----+-----+-----+-----+")


def promptGamerForTheNextMove() -> str: # Use as is
    """
        prompts the gamer to select the next move or Q (to quit)
        valid move direction: one of 'W', 'A', 'S' or 'D'.
        either returns a valid move direction or terminates the game
    """
    print("Enter one of WASD (move direction) or Q (to quit)")
    while True:  # prompt until a valid input is entered
        move = input('> ').upper()
        if move in ('W', 'A', 'S', 'D'): # a valid move direction
            return move  
        if move == 'Q': # for quit
            print("Exiting the game. Thanks for playing!")
            sys.exit()
        print('Enter one of "W", "A", "S", "D", or "Q"') # otherwise inform the user about valid input


def addANewTwoToBoard() -> None:
    is_empty = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == '':
                is_empty.append((i,j))
  
    if is_empty:
        row,col = random.choice(is_empty)
        board[row][col] = 2
    """ 
        adds a new 2 at a random available cell
    """ 
    pass #To Implement


def isFull() -> bool:
    b = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] == '':
                b = b+1
    if b > 0:
        return False
    else:
        return True
    """ returns True if no empty cell is left, False otherwise """
    pass #To Implement


def getCurrentScore() -> int:
    sum = 0
    for i in range(4):
        for j in range(4):
            if board[i][j] != '':
                sum += board[i][j]
    return sum
    """ 
        calculates and returns the score
        the score is the sum of all the numbers currently on the board
    """
    pass #To Implement


def updateTheBoardBasedOnTheUserMove(move: str) -> None:
    """
        updates the board variable based on the move argument
        the move argument is either 'W', 'A', 'S', or 'D'
        directions: W for up; A for left; S for down, and D for right
    """
    def move_left():
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == '':
                    for i in range(col,cols-1):
                        board[row][i] = board[row][i+1]
                    board[row][cols-1] = ''
    def transpose():
        global board 
        board = [[row[i] for row in board] for i in range(4)]
    def move_right():
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols-1,-1,-1):
                if board[row][col] == '':
                    for i in range(col,0,-1):
                        board[row][i] = board[row][i-1]
                    board[row][0] = ''
    if move == 'W':
        transpose()
        move_left()
        for i in range(4):
            for j in range(3):
                if board[i][j] == board[i][j+1]:
                    board[i][j] *= 2
                    board[i][j+1] = ''
                    move_left()           
        transpose()
    if move == 'A':
        move_left()
        for i in range(4):
            for j in range(3):
                if board[i][j] == board[i][j+1]:
                    board[i][j] *= 2
                    board[i][j+1] = ''
                    move_left()
    if move == 'S':
        transpose()
        move_right()
        for i in range(4):
            for j in range(3):
                if board[i][j] == board[i][j+1]:
                    board[i][j] *= 2
                    board[i][j+1] = ''
                    move_right()
        transpose()
    if move == 'D':
        move_right()
        for i in range(4):
            for j in range(3,-1,-1):
                if board[i][j] == board[i][j-1]:
                    board[i][j] *= 2
                    board[i][j-1] = ''
                    move_right()

    pass #To Implement

if __name__ == "__main__":  # Use as is 
    
    init()  # initialize a game
    while True:  # Super-loop for the game
        displayGame()
        print(f"Score: {getCurrentScore()}")
        updateTheBoardBasedOnTheUserMove(promptGamerForTheNextMove())
        addANewTwoToBoard()

        if isFull():
            displayGame()
            print("Game is Over. Check out your score.")
            print("Thanks for playing!")
            break