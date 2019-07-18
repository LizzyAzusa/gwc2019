import random

# A list of words that
potential_words = ["example", "words", "someone", "can", "guess"]
word = random.choice(potential_words)
# Use to test your code:
print(word)
# Converts the word to lowercase
word = word.lower()

# Make it a list of letters for someone to guess
current_word=["_",]*len(word)
# for i in range(len(word)):
# Some useful variables
guesses = []
maxfails = 7
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
	# check if the guess is valid: Is it one letter? Have they already guessed it?
	if (guess in guesses) or (len(guess)>1) or (guess.isdigit()):
		print("Enter again")
	# check if the guess is correct: Is it in the word? If so, reveal the letters!
	elif guess in word:
		for i in range(len(word)):
			if word[i]==guess:
				current_word[i]=guess

		guesses.extend([guess])
		print(current_word)

		if not "_" in current_word:
			print("You win!")
			break
	else:
		fails = fails+1
		print("You have " + str(maxfails - fails) + " tries left!")

if fails == maxfails:
	print("You lost.")
