# Terminal-Tic-Tac-Toe  #
'''	   X | - | - 
			 - | O | -
			 - | - | X    '''


# ---- Global Variables ---- #

# Game board
board = ["-", "-", "-",
				 "-", "-", "-",
				 "-", "-", "-",]

# If game is still going
game_still_going = True

# Who won or tie?
winner = True

# Who's turn is it?
current_player = "X"


# Display board
def display_board():
	print(board[0] + " | " + board[1] + " | " + board[2])
	print(board[3] + " | " + board[4] + " | " + board[5])
	print(board[6] + " | " + board[7] + " | " + board[8])


# Check rows of board for 3 in a row
def check_rows():
	# Setup global variables
	global game_still_going
	# Check if all of the rows have the same value and no dashes
	row_1 = board[0] == board[1] == board[2] != "-"
	row_2 = board[3] == board[4] == board[5] != "-"
	row_3 = board[6] == board[7] == board[8] != "-"
	# If any of the rows match, end the game
	if row_1 or row_2 or row_3:
		game_still_going = False
	# Return the winner either X or O
	if row_1:
		return board[0]
	elif row_2:
		return board[3]
	elif row_3:
		return board[6]
	return


# Check columns of board for 3 in a row
def check_columns():

	# Setup global variables
	global game_still_going

	# Check if all of the columns have the same value and no dashes
	column_1 = board[0] == board[3] == board[6] != "-"
	column_2 = board[1] == board[4] == board[7] != "-"
	column_3 = board[2] == board[5] == board[8] != "-"

	# If any of the columns match, end the game
	if column_1 or column_2 or column_3:
		game_still_going = False

	# Return the winner either X or O
	if column_1:
		return board[0]
	elif column_2:
		return board[1]
	elif column_3:
		return board[2]
	return


# Check diagonals of board for 3 in a row
def check_diagonal():

	# Setup global variables
	global game_still_going

	# Check if either of the diagonals have the same value and no dashes
	diagonal_1 = board[0] == board[4] == board[8] != "-"
	diagonal_2 = board[6] == board[4] == board[2] != "-"

	# If either of the diagonals match, end the game
	if diagonal_1 or diagonal_2:
		game_still_going = False

	# Return the winner either X or O
	if diagonal_1:
		return board[0]
	elif diagonal_2:
		return board[1]
	return


# Check if the players have tied
def check_for_tie():

	# Setup global variables
	global game_still_going

	# If no more dashes are present on the board, then end the game
	if "-" not in board:
		game_still_going = False
	return


# Check if a player has won
def check_for_winner():

	# Setup global variables
	global winner

	# Check rows
	row_win = check_rows()
	# Check columns
	column_win = check_columns()
	# Check diagonals
	diagonal_win = check_diagonal()

	# Get the winner 
	if row_win:
		winner = row_win
	elif column_win:
		winner = column_win
	elif diagonal_win:
		winner = diagonal_win
	else:
		winner = None
	return


# Check if the game is over
def check_if_game_over():
	check_for_winner()
	check_for_tie()


# Change turn to the other player
def flip_player():

	# Setup global variables
	global current_player

	# If the last turn was X, then change it to O
	if current_player == "X":
		current_player = "O"

	# If the current player was O, then change it to X
	elif current_player == "O":
		current_player = "X"
	return


# Handle a single turn of a player
def handle_turn(player):

	print(f"{player}'s turn! ")
	position = input("Choose a board position (1 to 9): ")

	valid = False
	while not valid:

		# Check that player input is within range of board size
		while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
			position = input("Choose a board position (1 to 9): ")

		# Update board position with user input
		position = int(position) - 1

		# Check that the board position is available
		if board[position] == "-":
			valid = True
		else:	
			print("SPOT ALREADY TAKEN!")

	# Update board position with player icon (X or O)
	board[position] = player

	# Display the updated board
	display_board()


# Play a game of tic-tac-toe
def play():

	# Display initial board
	display_board()

	# While game is still going
	while game_still_going:

		# Handle a single turn of a player
		handle_turn(current_player)

		# Check if the game is over
		check_if_game_over()

		# Change turn to the other player
		flip_player()

	# Check if game is over
	if winner == "X" or winner == "O":
		print(f"GAME OVER\n{winner} won!")
	elif winner == None:
		print("Tie Game!")


# RUN PROGRAM
play()

