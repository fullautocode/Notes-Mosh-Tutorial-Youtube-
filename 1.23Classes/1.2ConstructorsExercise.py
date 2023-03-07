# Class called person
# 	- "name" attribute
#	- talk() method


class Person:
	
	def __init__(self, name):
		self.name = name


	def talk(self):
		print(f"{self.name} is talking")


person = Person("John")
person.talk()

bob = Person("Bob Smith")
bob.talk()

# Each objectis a different instance of a Person class

  
