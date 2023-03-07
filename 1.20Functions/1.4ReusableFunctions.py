# 2:49:07
# Program the emoji converter to a reusable function

def emoji_converter(x):
	words = x.split(" ")
	emojis = {
		":)": "🙂",
		"(:": "🙂",
		":(": "🙁",
		"):": "🙁"
	}
	output = ""
	for word in words:
		output += emojis.get(word, word) + " "
	return output


# Add two blank lines after you define a function
message = input("> ")
text = emoji_converter(message)
print(text)



