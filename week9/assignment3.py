#!/usr/bin/python3
import random

def main():
	# Basic game board initialization.
	game_board = ['', '', '',
				'', '', '',
				'', '', '',]
	# Initialize the game state by determining
	# who has what piece and whose turn it will
	# be to start the game.
	game_over = False
	
	# Set these up:
	user = 'X'
	computer = 'O'
	whose_turn = 'user'
		
	# We'll stay in this loop until the game is over due to someone winning
	# or until it's declared a draw.
	while not game_over:
		if whose_turn == 'user':  # Human player's turn
			# fill this out
			get_user_move(game_board, user)
			display_board(game_board)
			if has_player_won(game_board, user):
				# fill this out
				game_over = True
			else:
				whose_turn = 'computer'
		else:  # Computer's turn
			pass
			# fill this out
		
		# Check to see if the game is over without a winner
		if not game_over and is_draw(game_board):
			print('Its a draw')
			game_over = True
		
	print('Thanks for playing!')
   
 
def display_board(game_board):
	"""This function prints the game board for the user to see its state."""
	print(game_board[0], game_board[1], game_board[2])
	print(game_board[3], game_board[4], game_board[5])
	print(game_board[6], game_board[7], game_board[8])				
				
def get_user_move(game_board, symbol):
	"""Ask the user for their row and column move and set the game_board with
	   their symbol."""
	pass

def get_computer_move(game_board, symbol):
	"""Generate random number coordinates for the computer to place their
	symbol."""
	pass
	

def is_legal_move(game_board, move):
	"""Check to see if the row and col provided are within the boundaries of 
	   the board and if the space is unoccupied."""
	pass
	
def is_draw(game_board):
	"""Determine if a game is a draw by checking each space. Once we find at
	   least one empty spot, we can return False since it's a playable spot."""
	pass

def has_player_won(game_board, symbol):
	"""Check to see if the given symbol has won the game in any of the possible
	   ways."""
	pass
	

def play_again():
	""" Get user input and ask if they want to play again """
	return True

main()