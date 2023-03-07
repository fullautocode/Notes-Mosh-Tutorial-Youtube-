# write a program to remove the duplicates in a list


list1 = [1, 4, 1, 7, 7, 4, 2, 3, 3, 7, 2]
list2 = []

for item in list1:
	if item not in list2:
		list2.append(item)
list2.sort()
print(list2)
