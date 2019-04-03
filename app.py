from flask import Flask
from flask import render_template, request, url_for, redirect

from hangman import Hangman


app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

#     UNTOGGLE BELOW AND FINISH THE FUNCTION
@app.route("/game/guess/", methods=['POST'])
def guess_text():
	text = request.form["guess"]
	hangman = Hangman()
	hangman.guess(text)
	hangman.save()
	# prediction = guess()
	# text = show_game()
	# if prediction is None:
	# 	game.append(text)
	# pass
	#...When you make a guess on a game. Not when you start a new game. Separate URL for that
	return redirect(url_for('show_game'))
	# remove the following line when you implement this function:

@app.route("/stats/")
def show_stats():
	# cart = get_stats() Later on below you may need to say stats = stats
	return render_template('stats.html')

@app.route("/game/")
def show_game():
	hangman = Hangman()

	# game = get_game() Later on below you may need to say game = game
	# below comma something add in template. we can docreative stuff below
	return render_template('game.html', game=hangman)

@app.route("/game/new")
def new_game():
	hangman = Hangman()
	hangman.new_game()
	hangman.save()
	return redirect(url_for("show_game"))


# @app.route('/game/add_pet/<id>/')
# def add_to_game(id):
# 	pet = find_pet(id)
# 	cart = get_cart()
# 	if pet is not None:
# 		cart.append(pet)
# 	save_cart(cart)	
# 	return redirect(url_for("show_game"))


# issues
# 1. don't allow guessing once the word is guessed
# 2. don't allow guesses of length > 1
# 3. don't allow guesses beyond the allowed amount
