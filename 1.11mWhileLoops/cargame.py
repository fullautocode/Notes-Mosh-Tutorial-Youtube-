
def car_game():

	command = ""
	car_on = False

	while True:
		command = input("> ").upper()

		if command == "START":
			if car_on == False:
				print("Car started... Ready to go!")
				car_on = True
			else:
				print("Car is already started")

		elif command == "STOP":
			if car_on == True:	
				print("Car stopped")
				car_on = False
			else:
				print("Car is already stopped")

		elif command == "HELP":
			print("""start - start the car
stop - to stop the car
quit - to exit""")

		elif command == "QUIT":
			print("Thanks for playing")
			break

		else:
			print("I don't understand that")

car_game()
