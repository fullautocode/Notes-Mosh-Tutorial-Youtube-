day_hot = True
day_cold = True

if day_hot:
	print("It's a hot day")
	print("Drink plenty of water")
elif day_cold:
	print("It's a cold day")
	print("Wear warm clothes")
else:
	print("It's a lovely day")
print("Have a good day")

# if vs elif
# if the first if statement gets executed and another if statement is true, then that statement will be executed as well.
# if the first if statement is true and gets exectued, the elif statement will not execute. The elif statement will only execute if no if statement before it was executed.
