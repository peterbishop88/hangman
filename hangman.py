from random_word import RandomWords
# load list of words
r = RandomWords()

# Return a single random word
word = r.get_random_word()
print(word)
# randomly select a word

# build an empty holder (list?) for the word
word_guess_list = len(word) * [" _ "]
print(word_guess_list)
# display the empty word
#print(''.join(word_guess))
#word_guess_list[2]='X'
print(word_guess_list)
word_guess = ''.join(word_guess_list)
print(word_guess)

already_guessed = set([])
counter = 0
for j in range(10):
    letter_guess = input("Enter a new letter:      \n>> ")
  #  print("already guessed:" + ','.join(already_guessed))
    print(letter_guess)

    if letter_guess in already_guessed:
        print("You have already guessed:" + ','.join(already_guessed))
        print("counter: " + str(counter))
    else:
        counter += 1
        print("counter: " + str(counter))

        if letter_guess in word:
            print("good guess")
            index_letter = [i for i in range(0, len (word)) if word[i] == letter_guess]
            for x in index_letter:
                word_guess_list[x] = letter_guess
        else:
            print("bad guess")

    already_guessed.add(letter_guess)

    print(word_guess_list)


