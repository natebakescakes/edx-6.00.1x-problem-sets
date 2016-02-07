from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    max_score = 0
    best_word = None
    
    def is_valid_word(word):
        display_hand = []
        count = 0
        
        for letter in hand.keys():
            for j in range(hand[letter]):
                display_hand.append(letter)
                
        for char in word:                
            if char in display_hand:
                display_hand.remove(char)
                count += 1
                
        if count == len(word):
            return True
        return False
    
    for word in wordList:

        if is_valid_word(word):
            current_score = getWordScore(word, n)
            
            if current_score > max_score:
                max_score = current_score
                best_word = word
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    
    while calculateHandlen(hand) > 0:
    
        print 'Current Hand: ', 
        displayHand(hand)
        
        computer_input = compChooseWord(hand, wordList, n)
        
        if computer_input == None:
            break
        else:
            score += getWordScore(computer_input, n)
            
            print ('"%s" earned %d points. Total: %d points' % (computer_input, getWordScore(computer_input, n), score))
            print

            hand = updateHand(hand, computer_input)
                
    if calculateHandlen(hand) == 0:
        print ('\nRun out of letters. Total score: %d points' % score)
    else:
        print ('\nTotal score: %d points' % score)
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    #print "playGame not yet implemented." # <-- Remove this when you code this function
    HAND_SIZE = 10
    hand = {}
    
    while True:
        command = str(raw_input('Enter n to deal a new hand, r to reply the last hand, or e to end game: '))
        if command == 'n':
            hand = dealHand(HAND_SIZE)
            while True:
                comp_player = str(raw_input('Enter u to have yourself play, c to have the computer play: '))
                if comp_player == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)
                    break
                elif comp_player == 'u':
                    playHand(hand, wordList, HAND_SIZE)
                    break
                else:
                    print ('Invalid command.')                    
            
        elif command == 'r':
            if hand == {}:
                print ('You have not played a hand yet. Please play a new hand first!')
            else:
                while True:
                    comp_player = str(raw_input('Enter u to have yourself play, c to have the computer play: '))
                    if comp_player == 'c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    elif comp_player == 'u':
                        playHand(hand, wordList, HAND_SIZE)
                        break  
                    else:
                        print ('Invalid command.')
        elif command == 'e':
            break
        else:
            print ('Invalid command.')
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


