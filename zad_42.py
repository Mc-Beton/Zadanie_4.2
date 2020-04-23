#funkcja zwracająca czy dane słowo jest polindromem
def check_word_backwards(word):
    new_word=word[::-1]
    if new_word == word:
        True
    else:
        False

