# ALLOWED_GUESSES = 10
import json
import random
# Hint: for testing, use a text file with your own words in it
WORDS_LIST_PATH = 'data/abdomen.txt'


class Hangman:
	def __init__(self):
		self.words = []
		'''Load words from file, and load the game state from the json file'''
		# self.private_word = ' '
		# self.public_word = list('_______')
		# self.guesses = 'e'
#                 You should replace the below file with a txt file change to one word text file
		with open('data/abdomen.txt') as f:
			raw_words = f.readlines()
			# words = []
			for word in raw_words:
				self.words.append(word.strip())
			# self.words = words

		self.load()



	def new_game(self, word=None):
		'''Reset/set appropriate values to self's properties'''
		if word is not None:
			self.private_word = word
		else:
			print("JGSIUGILYVKUYVK")
			self.private_word = random.choice(self.words)

		# self.private_word = word
		self.public_word = list('_' * len(self.private_word))
		self.guesses = []


	def guess(self, text):
		# self.guesses.append(text)
		if text not in self.guesses:
			self.guesses.append(text)
		if text == self.private_word:
			self.public_word = list(self.private_word)
		# 	print("!!!!!!!")
		index = 0
		for letter in self.private_word:
			if letter == text:
				self.public_word[index] = letter
			index += 1

		'''Examine text, and set appropriate values to self's properties
		based on text'''
		# for figure in self.words:
		#     if figure == text:
		#         return True

		#     else:
		#         False

		# pass



	def has_guessed_word(self):
		if "_" in self.public_word:
			return False
		else:
			return True
		# for figure in self.words:
		# 	if figure == text:
		# 		return True

		# 	else:
		# 		False
		'''Return boolean: True if user has guessed the word, False if not'''
		# pass

	def load(self):
		'''Load game state from json file. Set appropriate values to self's properties'''
		# game = [{"private_word": [], "public_word": [], "guesses": []}]
		with open('data/game-state.json') as f:
			game = json.load(f)
			self.private_word = game["private_word"]
			self.public_word = game["public_word"]
			self.guesses = game["guesses"]

		# self.save()
		# is self.public_word = to guessed.json?
		# should list('________') go into self.public_word???
		# self.guesses =

		# pass

	def save(self):

		data = {
			"private_word": self.private_word,
			"public_word": self.public_word,
			"guesses": self.guesses
		}
		with open("data/game-state.json", "w") as f:
			json.dump(data, f)
			# data['private_word'] = self.private_word
			# data['public_word'] = self.public_word
			# json.dump(data, f)

		'''Save game state to json file.'''



#  Milestones
	# 1.) Hangman class must create a new game 
	#      a.)_ Fetch a new random word an d save it somewhere
	#      b.) Then it must handle multiple guesses
						# i.) line 16 should be .guess
						# ii.) Hangman class should give unguessed word as well.
