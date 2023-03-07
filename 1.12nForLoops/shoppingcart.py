# Use a for loop to add all the prices in our shopping cart

shopping_cart = [10, 20, 30]
total_price = 0

for item in shopping_cart:
	total_price += item

print(f"Total: ${total_price}")
