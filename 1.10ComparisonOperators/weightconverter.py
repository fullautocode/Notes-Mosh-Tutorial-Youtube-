def weight_converter():

	while True:	

		weight = input("Weight: ")
		
		try:
			weight = float(weight)
			break

		except ValueError:
			print("Enter a valid weight")

	while True:
		
		lbs_or_kgs = input("(L)bs or (K)gs: ")

		if lbs_or_kgs.upper() == "L":
			weight = weight * 1/2.2
			print(f"You weigh {weight} kilos")
			break

		elif lbs_or_kgs.upper() == "K":
			weight = weight * 2.2
			print(f"You weigh {weight} pounds")
			break

		else:
			print("Type 'L' for lbs and 'K' for kilos")

# Program Begins

weight_converter()
