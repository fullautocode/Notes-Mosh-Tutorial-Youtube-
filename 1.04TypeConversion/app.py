birth_year = input('Birth year: ')
age = 2022 - int(birth_year)
print(age)

# by default, input() is saved as a string, even if the input is a number.
# Subtracting strings from integers will return a TypeError
# To fix this, convert the type to integer using the int() command.
# The type() command returns the type of a variable
 
