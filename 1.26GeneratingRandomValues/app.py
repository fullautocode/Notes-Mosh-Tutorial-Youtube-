# 3:36:38

import random
# Python comes with many built in modules
# Search for python3 module index on googlefor the full list

for i in range(3):
	print(random.random())
	# .random() method picks a random float between 0 and 1

for i in range(3):
	print(random.randint(10, 20))
	# .randint(min value, max value) picks a random integer in the given range.

members = ['Name1', 'Name2', 'Name3']
print(random.choice(members))
# .choice() picks a random string from the list

