"""
Description:
"""
_author_="John Nickell"
_date_="10/30/14"
#functions
"""
pre-condition:
Description:
"""
def printMenu():
    print("1) Number of Vowels")
    print("2) Number of Consonants")
    print("3) Number of Spaces")
    print("4) Number of punctuation Marks")
    print("5) List of Words")
    print("6) Quit")
    choice = int(input("Please enter your choice: "))
    return choice
"""
pre-condition:
Description:
"""
def countNumVowels(tmpStr):

"""
pre-condition:
Description:
"""
def countNumConsonants(tmpStr):

"""
pre-condition:
Description:
"""
def countNumSpaces(tmpStr):

"""
pre-condition:
Description:
"""
def countNumPunctuation(tmpStr):

"""
pre-condition:
Description:
"""
def getWords(tmpStr):

"""
pre-condition:
Description:
"""
def getSentence():
    sentence = input("Please enter a sentence: ")
    return sentence
#main
choice = printMenu()
while choice != 6:
    if choice == 1:
        sentence = getSentence()
        #number of vowels function
        print("1")
    elif choice == 2:
        sentence = getSentence()
        #consonants function
        print("2")
    elif choice == 3:
        sentence = getSentence()
        #spaces function
        print("3")
    elif choice == 4:
        sentence = getSentence()
        #punctuation mark function
        print("4")
    elif choice == 5:
        sentence = getSentence()
        #list of words function
        print("5")
    else:
        print("Invalid Choice")
    choice = printMenu()
