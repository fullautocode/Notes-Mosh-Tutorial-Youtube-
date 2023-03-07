# 3:01:59

# Classes define new types
# Basic types in python:
# Numbers
# Strings
# Booleans
# ------ More Complex Types -----
# Lists
# Dictionaries

class Point:
	def move(self):
		print("move")
	
	def draw(self):
		print("draw")

# with this class, we defines a new type
# In this class, Point is the new type
# with this new type, we can define new objects
# In this case, point1 is the new object
# an object is an instance of a class
# a class simply defines the template for creating objects
# objects are the actual instances based on that blueprint

point1 = Point()
point1.draw()
point1.move()

# objects can also have attributes
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
#print(point2.x)
# Returns an error since point2 does not have the .x attribute.

# Each object is a difference instance, of the Point class

# Quick Recap:
# Classes define new types
# In these classes we can define methods for the types
# The objects created using the class can have attributes


