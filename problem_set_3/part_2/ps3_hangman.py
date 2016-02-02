# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "C:/Users/Nate/Documents/edx-6.00.1x-problem-sets/problem_set_3/part_2/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if all(x in lettersGuessed for x in secretWord):
        return True
    
    return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    ans = ''
    
    for char in secretWord:
        if char in lettersGuessed:
            ans += char
        else:
            ans += '_ '
            
    return ans


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    alphabet = string.ascii_lowercase
    
    for letter in lettersGuessed:
        if letter in alphabet:
            alphabet = alphabet.replace(letter, '')
            
    return alphabet
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    WELCOME_MESSAGE = 'Welcome to the game, Hangman!\nI am thinking of a word that is %d letters long.' % len(secretWord)
    GUESS_COUNT = 8
    LETTERS_GUESSED = []
    
    print(WELCOME_MESSAGE)
    print('-' * 13)
    
    while GUESS_COUNT > 0 and not isWordGuessed(secretWord,LETTERS_GUESSED):
        print ('You have %d guesses left.' % GUESS_COUNT)
        print ('Available letters: %s' % getAvailableLetters(LETTERS_GUESSED))
        
        guessed_letter = raw_input('Please guess a letter: ').lower()
        
        if guessed_letter in LETTERS_GUESSED:
            print ('Oops! You\'ve already guessed that letter: %s' % getGuessedWord(secretWord, LETTERS_GUESSED))
        elif guessed_letter in secretWord:
            LETTERS_GUESSED.append(guessed_letter)
            print ('Good guess: %s' % getGuessedWord(secretWord, LETTERS_GUESSED))
        else:
            LETTERS_GUESSED.append(guessed_letter)
            print ('Oops! That letter is not in my word: %s' % getGuessedWord(secretWord, LETTERS_GUESSED))
            GUESS_COUNT -= 1        
            
        print('-' * 13)        
        
    if GUESS_COUNT == 0:
        print ('Sorry, you ran out of guesses. The word was %s' % secretWord)
    else:
        print ('Congratulations, you won!')

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
