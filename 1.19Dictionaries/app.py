# 2:18:31

# These are called Key Value Pairs
# Name: John Smith
# Email: john@gmail.com
# Phone: 1234

customer = {
	"name": "John Smith",
	"age": 30,
	"is_verified": True
	# Duplicate key value pairs aren't allowed
	# For example you can't have two "age"
}

print(customer["name"])
# if you try to use a key that doesn't exist you will get a KeyError
# for example customer["birthdate"] will return KeyError

# You can use the .get() method to avoid the Error
print(customer.get("birthdate"))
# This will return "None" since the key doesn't exist

# To avoid getting none, you can supply a default value instead
print(customer.get("birthdate", "No birthdate saved in record"))

# Key values can also be changed
customer["name"] = "Michael Smith"
print(customer["name"])

# And new key value pairs can be added to the dictionary
customer["birthdate"] = "20001213"
print(customer["birthdate"])


