"""
Description:
"""
_author_="John Nickell"
_date_="10/30/14"
#functions
"""
pre-condition: None
Description: This is the menu where the user will pick what function is used to
count parts of the sentence inputed.
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
pre-condition: A sentence in string format/
Description: This counts the number of the vowels in the sentence.
"""
def countNumVowels(tmpStr):
    tmpStr.lower()
    num1 = tmpStr.count("a")
    num2 = tmpStr.count("e")
    num3 = tmpStr.count("i")
    num4 = tmpStr.count("o")
    num5 = tmpStr.count("u")
    vowelTotal = num1 + num2 + num3 + num4 + num5
    return vowelTotal
"""
pre-condition: A sentence in string format.
Description: This counts the number of consonants in the sentence.
"""
def countNumConsonants(tmpStr):

"""
pre-condition: A sentence in string format.
Description: This counts the number of spaces in the user sentence.
"""
def countNumSpaces(tmpStr):
    spaceTotal = tmpStr.count(" ")
    return spaceTotal
"""
pre-condition: A sentence in string format.
Description: This counts the number of punctuation marks in the sentence.
"""
def countNumPunctuation(tmpStr):
    num1 = tmpStr.count("!")
    num2 = tmpStr.count("?")
    num3 = tmpStr.count(".")
    num4 = tmpStr.count(",")
    punctTotal = num1 + num2 + num3 + num4
    return punctTotal
"""
pre-condition: A sentence in string format.
Description: This makes a list of the words in the user sentence.
"""
def getWords(tmpStr):

"""
pre-condition: None
Description: Getting the sentence for the main part of the program.
"""
def getSentence():
    sentence = input("Please enter a sentence: ")
    return sentence
#main
choice = printMenu()
while choice != 6:
    if choice == 1:
        sentence = getSentence()
        numVowels = countNumVowels(sentence)
        print("Total number of vowels: ",numVowels)
    elif choice == 2:
        sentence = getSentence()
        #consonants function
        print("2")
    elif choice == 3:
        sentence = getSentence()
        numSpaces = countNumSpaces(sentence)
        print("Total number of spaces: ",numSpaces)
    elif choice == 4:
        sentence = getSentence()
        numPunctuation = countNumPunctuation(sentence)
        print("Total number of punctuation marks: ",numPunctuation)
    elif choice == 5:
        sentence = getSentence()
        #list of words function
        print("5")
    else:
        print("Invalid Choice")
    choice = printMenu()
