from random_word import RandomWords
import logging
logging.basicConfig(filename="python.log", level=logging.DEBUG, format = "%(levelname)s - %(message)s")
logging.debug("Program start ========================================================================")
# load list of words
r = RandomWords()

# Return a single random word
word = r.get_random_word()
print(word)
logging.debug("The word selected was: " + word)
# randomly select a word

# build an empty holder (list?) for the word
word_guess_list = len(word) * [" _ "]
logging.debug("Getting ready: " + ''.join(word_guess_list))
#print(word_guess_list)
# display the empty word
#print(''.join(word_guess))
#word_guess_list[2]='X'
#print(word_guess_list)
word_guess = ''.join(word_guess_list)
#print(word_guess)
already_guessed = set([])
counter = 0
for j in range(10):
    letter_guess = input("Enter a new letter:      \n>> ")
  #  print("already guessed:" + ','.join(already_guessed))
    #print(letter_guess)
    logging.debug("User guessed: " + letter_guess)

    if letter_guess in already_guessed:
        print("You have already guessed:" + ','.join(already_guessed))
        print("counter: " + str(counter))
        logging.debug(letter_guess + " had already been guessed. This does not count as a guess.")

    else:
        counter += 1
        print("counter: " + str(counter))
        logging.debug(letter_guess + " had not been guessed. This counts as a guess.")
        if letter_guess in word:
            logging.debug(letter_guess + " is in the word. (GOOD GUESS)")
            index_letter = [i for i in range(0, len (word)) if word[i] == letter_guess]
            for x in index_letter:
                logging.debug(''.join(word_guess_list) + " is the word before replacing the good guess.")
                word_guess_list[x] = letter_guess
                logging.debug(''.join(word_guess_list) + " is the word after replacing the good guess.")
        else:
            print("bad guess")
            logging.debug(letter_guess + " is not in the word. (BAD GUESS)")
    already_guessed.add(letter_guess)
    print(''.join(word_guess_list))

    #TODO
    # message when you get the word
    # message when you run out of guesses