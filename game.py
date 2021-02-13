import numpy as np 
import pandas as pd
import random
import sys

np.set_printoptions(precision=0)

class Game():
	def __init__(self):
		self.score = 0
		self.best = 0
		self.board = np.zeros((4,4))
		x1 = np.random.randint(0,3)
		y1 = np.random.randint(0,3)
		x2 = np.random.randint(0,3)
		y2 = np.random.randint(0,3)
		if (x1 == x2 and y1 == y2):
			y2 = 3 - y2
		self.board[x1,y1] = 2
		self.board[x2,y2] = 2
		self.locs = []
		self.old_board = self.board
		self.equal = False
		self.another_move = True


	def print_board(self):
		print("------",int(self.score), "--------")
		print(self.board)
		print("------------------")

	#Puts zeros on one side of the row for simple computation
	def new_row(self, row, up_special):
		non_zeros = []
		new = []
		for i in range(len(row)):
			if row[i] == 0:
				new.append(0)
			else:
				non_zeros.append(row[i])

		if up_special:
			array = non_zeros + new
		else:
			array = new + non_zeros

		return array

	#Executes the movement computation
	#Takes direction as an argument
	def move(self, direction):
		self.old_board = self.board.copy()
		self.equal = False
		vertical = False
		if direction == "up" or direction == 'down':
			self.board = self.board.transpose()
			vertical = True
		for j in range(0,4):
			test = self.new_row(self.board[j], False)
			for i in reversed(range(0,3)):
				if test[i] == test[i+1]:
					test[i+1] *= 2
					self.score += test[i+1]
					if i-1>=0:
						test[i] = test[i-1]
						if i-2 >= 0:
							test[i-1] = test[i-2]
							test[i-2] = 0
						else:
							test[i-1] = 0
					else:
						test[i] = 0
					break
			if direction == "right" or direction == "down":
				self.board[j] = test
			elif direction == "left" or direction == "up":
				self.board[j] = self.new_row(test,True)

		if vertical:
			self.board = self.board.transpose()
		self.equal = np.array_equal(self.old_board, self.board)

	#After a move, this function adds a '2' to the board w.p 2/3
	#and adds a '4' to the board w.p 1/3
	def add_two_or_four(self):
		pick = np.random.randint(0,len(self.locs))
		two_or_four = random.uniform(0,1)
		if two_or_four >= 0.33:
			self.board[self.locs[pick]] = 2
		else:
			self.board[self.locs[pick]] = 4

	#Checks if there is another move possible when the board has no zeros
	def like_neighbors(self):
		like = False
		for i in range(0,3):
			for j in range(0,3):
				if (self.board[i,j] == self.board[i,j+1]) or (self.board[i,j] == self.board[i+1,j]):
					like = True
		for i in range(0,3):
			if (self.board[3,i] == self.board[3,i+1]) or (self.board[i,3] == self.board[i+1,3]):
				like = True
		return like

	'''
	Updates the board with a two or four, checks if another move is possible
	Returns boolean 'another_move', which, if false, should end the game.
	'''
	def update(self):
		#another_move = True
		num_zeros = len(self.locs)
		if self.equal is False:
			self.locs = []
			for i in range(0,4):
				for j in range(0,4):
					if self.board[i,j] == 0:
						self.locs.append((i,j))
			num_zeros = len(self.locs)
			if num_zeros>0:
				self.add_two_or_four()

		if num_zeros == 1 or num_zeros == 0:
			self.another_move = self.like_neighbors()
		
		if not self.another_move:
			print("Game over! Final Score: ", self.score)
			self.print_board()
			sys.exit(0)




