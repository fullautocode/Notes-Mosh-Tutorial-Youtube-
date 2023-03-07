password = " "

while len(password) < 8:
	password = input("Create password: ")
	
	if len(password) < 8:
		print("Password must be atleast 8 characters")
	else:
		print("Password set")
