# if name is less than 3 characters long
# 	name must be at least 3 characters
# otherwise if it's more than 50 characters long
# name can be a maximum of 50 characters
# otherwise
# name looks good

def set_password():

	while True:
		password = input("Password: ")

		if len(password) < 3:
			print("Password must be at least 3 characters")

		elif len(password) > 50:
			print("Password can be a maximum of 50 characters long")

		else:
			print("Looks good!")
			break

set_password()


