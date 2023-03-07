# 3:07:58

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y
# A constructor is a function that gets called at the time of creatingan object.
# __init__ is short for initialize
# __init__ is the function that gets called when we create a new Point object.
# This method is called a constructor because it is used to construct an object.

	def move(self):
		print("move")
	
	def draw(self):
		print("draw")
	
point = Point(10, 20)
print(point.x)

