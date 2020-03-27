import json
import random
import urllib.request

url = urllib.request.urlopen("https://raw.githubusercontent.com/sindresorhus/mnemonic-words/master/words.json")
words = json.loads(url.read())
word = random.choice(words)

import logging
logging.basicConfig(filename="python.log", level=logging.DEBUG, format = "%(levelname)s - %(message)s")
logging.debug("Program start ========================================================================")
# load list of words

# Return a single random word
print(word)
logging.debug("The word selected was: " + word)
# randomly select a word
word_guess_list = len(word) * [" _ "]
logging.debug("Getting ready: " + ''.join(word_guess_list))

word_guess = ''.join(word_guess_list)
already_guessed = set([])

counter = 0
for j in range(10):
    letter_guess = input("Enter a new letter:      \n>> ")
    logging.debug("User guessed: " + letter_guess)

    if letter_guess in already_guessed:
        print("You have already guessed:" + letter_guess)
        print("counter: " + str(counter))
        logging.debug(letter_guess + " had already been guessed. This does not count as a guess.")

    else:
        counter += 1
        print("counter: " + str(counter))
        logging.debug(letter_guess + " had not been guessed. This counts as a guess.")
        if letter_guess in word:
            logging.debug(letter_guess + " is in the word. (GOOD GUESS)")
            index_letter = [x for x in range(0, len (word)) if word[x] == letter_guess]
            for i in index_letter:
                logging.debug(''.join(word_guess_list) + " is the word before replacing the good guess.")
                word_guess_list[i] = letter_guess
                logging.debug(''.join(word_guess_list) + " is the word after replacing the good guess.")
        else:
            print("bad guess")
            logging.debug(letter_guess + " is not in the word. (BAD GUESS)")
    already_guessed.add(letter_guess)

    word_guess = ''.join(word_guess_list)
    print(word_guess)

    if word == word_guess:
        print("CONGRATS! You won. You guessed the word: " + word_guess)
        logging.debug("User correctly guessed the word: " + word_guess)
        break
    elif counter < 5:
        print("Keep trying!")
        logging.debug("User has not yet guessed the word " + word + ". Current guess is: " + word_guess)
    else:
        print("Too many tries, sorry!")
        break
    #TODO
    # message when you get the word
    # message when you run out of guesses