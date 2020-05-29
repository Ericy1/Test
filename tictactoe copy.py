import numpy as np
import sys

class Tictactoe:

	def __init__(self):
		self.grid = np.array(["-","-","-","-","-","-","-","-","-"])
		self.value = 0

	def start_game(self):
		while True:
			if (self.grid != "-").all():
				sys.exit()
			else:
				input_var = input("Choose a position from 1-9: ")
				if not(isinstance(int(input_var), int)):
					print("Please enter an integer from 1-9: ")
					continue
				elif int(input_var) < 1 or int(input_var) > 9:
					print("Number is out of range, please try again: ")
					continue
				elif self.grid[int(input_var)] == "O" or self.grid[int(input_var)] == "X":
					print("Invalid location, please try again: ")
					continue
				else:
					self.add_location(int(input_var))
					self.check_if_win()
			self.value += 1

	def add_location(self, input_var):
		if self.value%2 == 0:
			self.grid[input_var] = "X"
		elif self.value%2 == 1:
			self.grid[input_var] = "O"
		new_grid = np.reshape(self.grid,(-1,3))
		print(new_grid)

	def check_if_win(self): #could I use threading here?
		#first, the diagonals
		diagonal1 = self.grid[0] == self.grid[4] == self.grid[8] and self.grid[0] != "-"
		diagonal2 = self.grid[2] == self.grid[4] == self.grid[6] and self.grid[2] != "-"
		row1 = self.grid[0] == self.grid[1] == self.grid[2] and self.grid[0] != "-"
		row2 = self.grid[3] == self.grid[4] == self.grid[5] and self.grid[3] != "-"
		row3 = self.grid[6] == self.grid[7] == self.grid[8] and self.grid[6] != "-"
		col1 = self.grid[0] == self.grid[3] == self.grid[6] and self.grid[0] != "-"
		col2 = self.grid[1] == self.grid[4] == self.grid[7] and self.grid[1] != "-"
		col3 = self.grid[2] == self.grid[5] == self.grid[8] and self.grid[2] != "-"

		if diagonal1 or diagonal2 or row1 or row2 or row3 or col1 or col2 or col3:
			print("You've won!")
			sys.exit()

	def introduction(self):
		while True:
			input_var = input("Please type 'yes' to begin', 'quit' to quit the game:\n")
			if input_var.lower() == "yes":
				self.start_game()
				break
			elif input_var.lower() == "quit":
				print("Bye bye!")
				sys.exit()
			elif input_var.lower() != "yes" or input_var.lower() != "quit":
				continue

	def main(self):
		print("Hello fellow player, this is tic-tac-toe. You will be playing against yourself\n"
			  "for now, but there will be additional bot functionality soon. Have fun.\n")
		self.introduction()


t = Tictactoe()

if __name__ == "__main__":
	t.main()