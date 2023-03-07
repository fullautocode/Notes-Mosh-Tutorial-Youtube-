import random

def guess(x):

	random_number = random.randint(1, x)
	lives = 3
	user_guess = ""

	while user_guess != random_number and lives > 0:
	
		while True:
			user_guess = input(f"Guess the magic number between 1 and {x}: ")
			try:
				user_guess = int(user_guess)
				break

			except ValueError:
				print("Guess a valid integer")

		if user_guess == random_number:
			print(f"Congrats, you guessed the magic number: {random_number}")
			break

		elif user_guess < random_number:
			print("The magic number is higher")
			lives = lives - 1
			print(f"You have {lives} lives left")


		elif user_guess > random_number:
			print("The magic number is lower")
			lives = lives - 1
			print(f"You have {lives} lives left")

	
	else:
		print(f"You lose! The magic number was {random_number}")



guess(10)

	
