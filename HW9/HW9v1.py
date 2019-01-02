"""
Description: This program uses a menu function let the user work with a recipes
in a dictionary using various functions.
"""
_author_="John Nickell"
_date_="12/4/14"
import os.path
#menu function
"""
pre-condition: None
Description: This is the menu where the user will pick what function is used to
alter the recipes, print them, or search them.
"""
def printMenu():
    print("1) Print Ingredients for One Recipe")
    print("2) Shared Ingredients")
    print("3) Search for Recipes with Ingredients")
    print("4) Add a Recipe")
    print("5) Print Dictionary")
    print("6) Quit")
    strChoice = (input("Please enter your choice: "))
    choice = 0
    if strChoice.isdigit():
        choice = int(strChoice)
    while choice > 6 or choice < 1 or strChoice.isdigit() == False:
        print("Invalid Choice")
        strChoice = input("Please enter your choice: ")
        choice = 0
        if strChoice.isdigit():
            choice = int(strChoice)
    return choice
#1 function
"""
pre-condition:recipeChoice, recipeDict
Description: This prints the ingredients for one recipe.
"""
def printIngredients(tmpRecipeChoice,tmpRecipeDict):
    print(tmpRecipeDict[tmpRecipeChoice])
#2 function
"""
pre-condition: firstRecipe, secondRecipe, recipeDict
Description: This finds the shared ingredients between two recipes and
prints them.
"""
def printSharedIngredients(tmpRecipeOne,tmpRecipeTwo,tmpRecipeDict):
    sharedList = []
    for ingredient in tmpRecipeDict[tmpRecipeOne]:
        if ingredient in tmpRecipeDict[tmpRecipeTwo]:
            sharedList.append(ingredient)
    print(sharedList)
#3 function
"""
pre-condition: tmpIngredients, recipeDict
Description: This searches for a recipe based off ingredients.
"""
def printRelevantRecipes(tmpIngredients, tmpRecipeDict):
    print("Under Construction")
#4 function
"""
pre-condition: recipeName, recipeDict
Description: This adds a recipe to the dictionary.
"""
def addRecipe(tmpRecipeName, tmpRecipeDict):
    print("Under Construction")
#5 Function
"""
pre-condition: recipeDict
Description: This prints the dictionary nicely formatted.
"""
def printDictionary(tmpRecipeDict):
    print("Under Construction")
#file dialog box and set up
from tkinter import*
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
window = Tk()
window.title("Reading from a Text File")
infileName = askopenfilename()
inFile = open(infileName,"r")
#adding text file to empty dict
recipeDict = {}
for line in inFile:
    line = line.rstrip("\n")
    wordList = line.split(" ")
    recipeKey = wordList.pop(0)
    for word in wordList:
        recipeDict[recipeKey] = wordList
print(recipeDict)
#menu choices
choice = printMenu()
while choice != 6:
    if choice == 1:
        recipeChoice = input("What recipe do you want to see: ")
        while recipeChoice not in recipeDict:
            print("Recipe not in Dictionary")
            recipeChoice = input("What recipe do you want to see: ")
        printIngredients(recipeChoice,recipeDict)
    elif choice == 2:
        recipeOne = input("First Recipe: ")
        while recipeOne not in recipeDict:
            print("Recipe not in Dictionary")
            recipeOne = input("First Recipe: ")
        recipeTwo = input("Second Recipe: ")
        while recipeTwo not in recipeDict:
            print("Recipe not in Dictionary")
            recipeTwo = input("Second Recipe: ")
        printSharedIngredients(recipeOne,recipeTwo,recipeDict)
    elif choice == 3:
        ingredientList = []
        while inputIngredient != "END":
            inputIngredient = input("Ingredient to add to search(END to stop: ")
            ingredientList.append(inputIngredient)
        printRelevantRecipes(ingredientList,recipeDict)
    elif choice == 4:
        print("Function under Construction")
    elif choice == 5:
        print("Function under Construction")
    choice = printMenu()
