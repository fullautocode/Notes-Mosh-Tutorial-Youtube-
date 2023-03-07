# Price of a house is 1 000 000 $
# If buyer has good credit, they put down 10%
# otherwise, they put down 20%
# print the down payment

house_price = 1000000

x = ""

while True: 
	x = input("Is your credit good, type (Y) for yes and (N) for no: ")
	if x.upper() == "Y" or "N":
		break
	else:
		print("Plese enter 'Y' or 'N'" 13 
)


if x.upper() == "Y":
	good_credit = True
if x.upper() == "N":
	good_credit = False


if good_credit:
	down_payment = house_price * .1
else:
	down_payment = house_price * .2

print(f"Down Payment = ${down_payment}")

