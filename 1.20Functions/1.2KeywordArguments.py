# 2:39:35

def greet_user(first_name, last_name):
	print(f"Hi {first_name} {last_name}!")
	print("Welcome aboard!")

greet_user("John", "Smith")
# "John" and "Smith" are referred to as positional arguments
# They are positional arguments since their positon matters

greet_user(last_name = "Smith", first_name = "John")
# first_name = "John" is reffered to as a keyword argument
# with keyword arguments, position does not matter 	

# Example when keyword arguemnts would be useful
#calc_cost(total = 50, shipping = 5, discount = 0.1)

# Keyword Arguments should always be used after positional arguments
# Example:
#greet_user("John", last_name = "Smith"
# If you enter:
#greet_user(first_name = "John", "Smith")
# you will recieve an error since a keyword argument comes before




