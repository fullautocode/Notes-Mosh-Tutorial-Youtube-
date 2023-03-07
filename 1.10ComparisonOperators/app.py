# if temperature is greater than 30C
#	it's a hot day
# if temperature is less than 10C
# 	it's a cold day
# otherwise
#	it's neither hot nor cold


def hot_or_cold():


	while True:
		temp = input("Temperature in Celsius: ")

		try:
			temp = int(temp)
			break

		except ValueError:
			print("Please enter a valid temperature")

	if int(temp) >= 30:
		print("It's a hot day")
	
	elif int(temp) <= 10:
		print("It's a cold day")
	
	else:
		print("It's neither hot nor cold")

# Start of Program


hot_or_cold()

