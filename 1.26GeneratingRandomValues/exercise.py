import random


class Dice:
	def roll(self):
		dice1 = random.randint(1,6)
		dice2 = random.randint(1,6)
		return dice1, dice2
		# NOTE: you don't need paranthesis around tuples when using the return command in a function


dice = Dice()
print(dice.roll())


