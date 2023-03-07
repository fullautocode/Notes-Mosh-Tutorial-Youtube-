# if applicant has high income AND good credit, then applicant is Eligible for loan

high_income = ""
good_credit = ""
criminal_record = ""
income = ""
credit = ""


while True:

	while True:
		income = input("Enter your yearly income: $")	

		try:
			income = int(income)
			break

		except ValueError:
			print("Pick a valid income")
	

	if int(income) >= 100000:
		high_income = True
		break
	elif int(income) < 100000:
		high_income = False
		break
	else:
		print("Please enter a valid number")
	
while True:
	
	while True:
		credit = input("What is your credit score: ")

		try:
			credit = int(credit)
			break
	
		except ValueError:
			print("Pick a valid credit score")

	if int(credit) >= 600 and int(credit) <= 800:
		good_credit = True
		break
	elif int(credit) < 600 and int(credit) >= 0:
		good_credit = False
		break
	else:
		print("Enter a valid credit score")

while True:

	
	has_record = input("Do you have a criminal record, yes (Y) or no (N): ")

	if has_record.upper() == "Y":
		criminal_record = True
		break
				
	elif has_record.upper() == "N":
		criminal_record = False
		break

	else:
		print("Please enter 'Y' for yes and 'N' for no")

if (high_income or good_credit) and not criminal_record:
	print("You are eligable for a loan")
else:
	print("You are not eligable for a loan")
	
