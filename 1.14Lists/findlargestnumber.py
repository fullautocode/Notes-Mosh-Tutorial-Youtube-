# Find the largest number in a list

numbers = [1, 8, 16, 99, 43, 22, 9, 52, 54, 12, 65]
highest_number = numbers[0]
# setting the original highest_number as the first number in the list

for number in numbers:
	if number > highest_number:
		highest_number = number
	
print(highest_number)
