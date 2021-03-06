from random import randint

board = []

# Create a 5 x 5 grid initialized to all 'O's and store it in board.
for x in range(5):
    board.append(["O"] * 5)

# Print the board out like a grid with each row on its own line.
def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

# Use two variables to store the ship's location, ship_row and ship_col.
ship_row = random_row(board)
ship_col = random_col(board)

for turn in range(4):
    print "Turn", turn + 1
    # Let the player guess where the ship is.
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    # If the guess is right.
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif (board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print "Game Over"
        print_board(board)