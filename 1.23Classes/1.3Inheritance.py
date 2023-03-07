# 3:14:55

class Mammal:
	def walk(self):
		print("walk")



class Dog(Mammal):
# The dog class will inherit all the methods from the mamal class
	def bark(self):
		print("bark")


class Cat(Mammal):
	pass
# Classes in python can't be empty
# The pass statement means "nothing"

# DRY, Don't Repeat Yourself

dog1 = Dog()
dog1.walk()
dog1.bark()
