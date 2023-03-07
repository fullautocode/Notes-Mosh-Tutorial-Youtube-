message = input("> ")

# Use the split(' ') method to spit up words by spaces
words = message.split(' ')
# print(words)
# returns a list of the words that the user entered.
# Example: good morning would returns good, morning.

emoji = {
	":)": "(Insert Smily Emoji",
	":(": "(Insert Sad Emoji)"
}

output = ""

for word in words:
	output += emoji.get(word, word) + " "
	
print(output)

