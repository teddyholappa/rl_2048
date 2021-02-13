from game import Game 
import numpy as np
import random
import sys

inputs = ['w','a','s','d']

def main():
	game = Game()
	print("WELCOME TO 2048")
	game.print_board()
	while(True):
		user_input = inputs[random.randint(0,3)]
		direction = ""
		if user_input == "w": direction = "up"
		if user_input == "a": direction = "left"
		if user_input == "s": direction = "down"
		if user_input == "d": direction = "right"
		game.move(direction)
		another_move = game.update()
		print("Another Move?: ", another_move)
		print("Direction: ", direction)
		game.print_board()
		if not another_move:
			print("You lost")
			sys.exit(0)

main()