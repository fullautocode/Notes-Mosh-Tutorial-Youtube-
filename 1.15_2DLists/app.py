# 2:01:54

# 2D lists are based on a concept in math called matrix

#[
#	1 2 3
#	4 5 6
#	7 8 9
#]

# Rectangular Array of numbers
# 3x3 Matrix in math

matrix = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

# Each item in a list is another list
# 1st item is [1, 2, 3] (0th Index)
# 2nd item is [4, 5, 6] (1st Index)
# 3rd item is [7, 8, 9] (2nd Index)

#print (matrix[0][1])
# Returns the 1st index in the list of the 0th index
# Returns the number 2

# Changing the value in a matrix
#matrix[0][1] = 20
#print(matrix[0][1])


# Nested Loops in Matrix
for row in matrix:
	for item in row:
		print(item)
	
