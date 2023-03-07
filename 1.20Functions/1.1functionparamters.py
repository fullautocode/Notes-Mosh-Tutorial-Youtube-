# 2:35:33
# How to pass information to your function

def greet_user(name):
	print(f'Hi there {name}!')
	print(f'Welcome aboard')

greet_user('John')
greet_user('Mary')

# When a function has a parameter, you are obligated to pass a value for that parameter.
# greet_user() will return an TypeError if the parameter isn't given a value.


# Parameters vs Arguments
# Parameters are the placeholders that we define in a function for receing information.
# Example: (name)
# Arguments are the actual pieces of information that we supply to the funciton.
# Example: 'John'


# Function can also have multiple parameters
#def greet_user(fname, lname):



