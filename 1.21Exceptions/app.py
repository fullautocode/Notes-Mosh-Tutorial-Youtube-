# 2:53:53

try:
	age = int(input('Age: '))
	print(age)
	income = 20000
	risk = income / age
except ValueError:
	print('Invalid value')
except ZeroDivisionError:
	print('Age cannot be zero')

# except stands for exception
# the try except strategy attempts to execute code that may return an error



