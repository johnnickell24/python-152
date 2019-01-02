"""
Description: This program is used to find a variety of things from a user \
made sentence including counting vowels, consonants, punctuation, spaces, \
and making a list of words from it all from a menu printed to the user.
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
    strChoice = input("Please enter your choice: ")
    choice = 0
    if strChoice.isdigit():
        choice = int(strChoice)
    while strChoice.isdigit() == False:
        print("Invalid Choice")
        strChoice = input("Please enter your choice: ")
        choice = 0
        if strChoice.isdigit():
            choice = int(strChoice)
    return choice
"""
pre-condition: A sentence in string format/
Description: This counts the number of the vowels in the sentence.
"""
def countNumVowels(tmpStr):
    tmpStr = tmpStr.lower()
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
    tmpStr = tmpStr.lower()
    num1 = tmpStr.count("b")
    num2 = tmpStr.count("c")
    num3 = tmpStr.count("d")
    num4 = tmpStr.count("f")
    num5 = tmpStr.count("g")
    num6 = tmpStr.count("h")
    num7 = tmpStr.count("j")
    num8 = tmpStr.count("k")
    num9 = tmpStr.count("l")
    num10 = tmpStr.count("m")
    num11 = tmpStr.count("n")
    num12 = tmpStr.count("p")
    num13 = tmpStr.count("q")
    num14 = tmpStr.count("r")
    num15 = tmpStr.count("s")
    num16 = tmpStr.count("t")
    num17 = tmpStr.count("v")
    num18 = tmpStr.count("w")
    num19 = tmpStr.count("x")
    num20 = tmpStr.count("y")
    num21 = tmpStr.count("z")
    tmpConsonantTotal = num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
    tmpConsonantTotal2 = num11+num12+num13+num14+num15+num16+num17+num18+num19+num20+num21
    consonantTotal = tmpConsonantTotal + tmpConsonantTotal2
    return consonantTotal

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
    tmpList = tmpStr.replace(",","")
    tmpList2 = tmpList.replace("!","")
    tmpList3 = tmpList2.replace("?","")
    tmpList4 = tmpList3.replace(".","")
    tmpListWords = tmpList4.split(" ")
    return tmpListWords
"""
pre-condition: None
Description: Getting the sentence for the main part of the program.
"""
def getSentence():
    sentence = input("Please enter a sentence: ")
    return sentence
#main
"""
Description: This is the main part of the function where the functions are \
called down after a menu choice is made.
"""
choice = printMenu()
while choice != 6:
    if choice == 1:
        sentence = getSentence()
        numVowels = countNumVowels(sentence)
        print("Total number of vowels: ",numVowels)
    elif choice == 2:
        sentence = getSentence()
        numConsonants = countNumConsonants(sentence)
        print("The total number of consonants: ",numConsonants)
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
        listWords = getWords(sentence)
        print("List of words are: ",listWords)
    else:
        print("Invalid Choice")
    choice = printMenu()
print("Thanks for using my program!")
