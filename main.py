from game import Game 
import numpy as np
import random
import sys

inputs = ['w','a','s','d']

def main():
	game = Game()
	game.print_board()
	while(True):
		#change this to input() if you would like to play yourself.
		user_input = inputs[random.randint(0,3)]
		direction = ""
		if user_input == "w": direction = "up"
		if user_input == "a": direction = "left"
		if user_input == "s": direction = "down"
		if user_input == "d": direction = "right"
		game.move(direction)
		game.update()
		print("Another Move?: ", game.another_move)
		print("Last move: ", direction)
		game.print_board()

main()