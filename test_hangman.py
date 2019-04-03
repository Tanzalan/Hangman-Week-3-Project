from hangman import Hangman

# h = Hangman()
# h.new_game()
# h.guess('h')

# "__ _ _ _ _ _e_"

# class MiniHangman
# 	def__



# def test1():
#     h = Hangman()
#     h.new_game('beehive')
#     assert h.secret_text == 'beehive'
#     assert h.public_word == list('_______')
#     print('test1 passed!')


# def test2():
#     h1 = Hangman()
#     h1.new_game('beehive')
#     h1.save()

#     h2 = Hangman()
#     assert h2.secret_text == 'beehive'
#     assert h2.public_word == list('_______')
#     print('test2 passed!')



def test_public_and_private_words():
    h = Hangman()
    h.new_game('beehive')
    assert h.private_word == 'beehive'
    assert h.public_word == list('_______')
    print('test_public_and_private_words passed!')


def test_load_and_save_public_and_private_words():
    h1 = Hangman()
    h1.new_game('cheerful')
    h1.save()

    h2 = Hangman()
    assert h2.private_word == 'cheerful'
    assert h2.public_word == list('________')
    print('test_load_and_save_public_and_private_words passed!')


def test_basic_guesses():
    h = Hangman()
    h.new_game('conscientious')
    h.guess('e')
    assert h.guesses == ['e']
    h.guess('f')
    assert h.guesses == ['e', 'f']
    print('test_basic_guesses passed!')


def test_guesses_changing_public_word():
    h = Hangman()
    h.new_game('encyclopedia')
    assert h.public_word == list('____________')

    h.guess('e')
    assert h.public_word == list('e_______e___')

    h.guess('c')
    assert h.public_word == list('e_c_c___e___')

    h.guess('n')
    assert h.public_word == list('enc_c___e___')

    h.guess('a')
    assert h.public_word == list('enc_c___e__a')

    print('test_guesses_changing_public_word passed!')


def test_multiple_same_guesses():
    h = Hangman()
    h.new_game('defenestrate')
    h.guess('e')
    h.guess('e')
    assert h.guesses == ['e']
    print('test_multiple_same_guesses passed!')


def test_guessing_word():
    h = Hangman()
    h.new_game('cat')

    h.guess('c')
    assert h.has_guessed_word() is False
    h.guess('a')
    assert h.has_guessed_word() is False
    h.guess('t')
    assert h.has_guessed_word() is True
    print('test_guessing_word passed!')


def test_guessing_entire_word():
    h = Hangman()
    h.new_game('batman')
    h.guess('batman')
    assert h.has_guessed_word() is True
    assert h.guesses == ['batman']

    print('test_guessing_entire_word passed!')


test_public_and_private_words()
test_load_and_save_public_and_private_words()
test_basic_guesses()
test_guesses_changing_public_word()
test_multiple_same_guesses()
test_guessing_word()
test_guessing_entire_word()