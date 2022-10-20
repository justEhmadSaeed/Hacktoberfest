print(">>>>>>>>>>_____HANGMAN_____<<<<<<<<<<")

WORDLIST_FILENAME = "words.txt"
import random
#1 Search Word
def load_words():
    print("Loading word list from file...")
    with open(WORDLIST_FILENAME, 'r') as inFile:
        line = inFile.readline()
        # wordlist: list of strings
        wordlist = line.split()
        print(">>>>>  ", len(wordlist), "words loaded.")
        return wordlist
wordlist=load_words()

#2 Random Word selection
def choose_word(wordlist):
        return random.choice(wordlist)

#3 Return True/False
a=(choose_word(wordlist))
while True:
    if len(a)<=6:
        break
    if len(a)>6:
        a=(choose_word(wordlist))
        
    


def is_word_guessed(secret_word, letters_guessed):
    print()
    sec_set=set([x for x in secret_word])
    guess_set=set([x for x in letters_guessed])
    if sec_set==guess_set:
        return True
    return False


#4 guess missing words
def get_guessed_word(secret_word, letters_guessed):
    for i in secret_word:
        if i in letters_guessed:
            print(i,end=" ")
        else:
            print("_",end=" ")
    print()



#5 letters left
def get_available_letters(ListOfLettersGuessed):
    import string
    stringy=""
    for element in string.ascii_lowercase:
        if element in ListOfLettersGuessed:
            continue
        else:
            stringy=stringy + element
    print("Available letters: ", stringy)
#get_available_letters(list)

#6 Main Function
def hangman(secret_word):
    secword_length=len(set([x for x in secret_word]))
    length=len(secret_word)
    vowels=["a","e","i","o","u"]
    letter=""
    mainlist=[]
    print(f" This word contains: {length} letters in it.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    warning=3
    guess=1
    tinylist=[]
    while guess<=6 and guess>0 and warning>=0 and warning<=3:
        print("-------------------------")
        left=7-guess
        left2=warning
        print("Guesses left: ",left)
        print("Warning Left: ",left2)
        guess_input=str(input("Enter Letter: ")).lower()
        mainlist.append(guess_input)
        get_available_letters(mainlist)
        # get_guessed_word(a, letter)
        if guess_input in letter:
            pass
        if guess_input not in letter:
            tinylist.append(guess_input)
        if guess_input.isalpha()==False or guess_input in letter:
            if guess_input.isalpha()==False:
                print("Invalid Input!")
            if guess_input in letter:
                print("Oops you've already entered that letter!")
            warning=warning-1
        if guess_input not in secret_word:
            print("Oops that letter is not in my word!")
            print()
        if guess_input in secret_word:
            letter=letter+guess_input
            length_of_guess=len(letter)
            if is_word_guessed(secret_word, letter)==True:
                TotalScore = left*(len(tinylist))
                print("Your Total Score is: ",TotalScore)
                print("True")
                print("---___CONGRATULATIONS___---")
                print("__---<< YOU WON >>---__")
                return True
            if guess_input.isalpha()==False and guess_input not in letter:
                warning=warning-1
                print()
        get_guessed_word(secret_word, letter)
        
        if guess_input not in vowels and guess_input not in letter and guess_input not in secret_word:
            guess=guess+0
        if guess_input in vowels and guess_input not in letter and guess_input not in secret_word:
            guess=guess+1
        guess=guess+1
        warning=warning-0
    if secret_word==letter:
        tinylist.append(guess_input)
        TotalScore = left*tiny_length
        print("Your Total Score is: ",TotalScore)
        print("True")
        print("---___CONGRATULATIONS___---")
        print("__---<< YOU WON >>---__")
    if secret_word!=letter:
        print("False")
        print("---___OOPS___---")
        print("__---<< YOU LOSE >>---__")
        print("Try Again Later...")
    

hangman(a)
print("Secret Word: ",a)


