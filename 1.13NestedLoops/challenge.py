# use a nested loop to make the following
# xxxxx
# xx
# xxxxx
# xx
# xx


list = [5, 2, 5, 2, 2]

for x in list:	
	message = ""
	for y in range(x):
		message += "x"
	print(message)	

	
