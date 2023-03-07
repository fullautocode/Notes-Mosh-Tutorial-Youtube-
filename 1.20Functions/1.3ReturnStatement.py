# 2:45:04

def square(number):
	return number * number
#	return None
# Default return value is None
# by not entering a return statement the function returns None. 
# None means nothing, as in absence of a value

while True:
	x = input("Square: ")
	try:
		x = int(x)
		break

	except ValueError:
		print("Invalid input, try again")


y = square(x)
print(y)
