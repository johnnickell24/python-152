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
    for ingredient in tmpRecipeDict[tmpRecipeChoice]:
        ingredient = ingredient.title()
        print(ingredient)
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
    if sharedList != []:
        for ingredient in sharedList:
            ingredient = ingredient.title()
            print(ingredient)
    else:
        print("No shared Ingredients")
#3 function
"""
pre-condition: tmpIngredients, recipeDict
Description: This searches for a recipe based off ingredients.
"""
def printRelevantRecipes(tmpIngredients, tmpRecipeDict):
    tmpRecipeList = []
    tmpIngredient = 0
    for tmpRecipe in tmpRecipeDict:
        tmpIngredient = tmpRecipeDict[tmpRecipe]
        if set(tmpIngredients) < set(tmpIngredient):
            tmpRecipeList.append(tmpRecipe)
    if tmpRecipeList != []:
        for recipe in tmpRecipeList:
            print(recipe)
    else:
        print("No recipes with those ingredients")
#4 function
"""
pre-condition: recipeName, recipeDict
Description: This adds a recipe to the dictionary.
"""
def addRecipe(tmpRecipeToAdd, tmpRecipeDict):
    tmpIngredientList = []
    tmpInputIngredient = 0
    while tmpInputIngredient != "END":
        tmpInputIngredient = input("Ingredient to add to recipe(END to stop: ")
        if tmpInputIngredient != "END":
            tmpIngredientList.append(tmpInputIngredient)
    tmpRecipeDict[tmpRecipeToAdd] = tmpIngredientList
#5 Function
"""
pre-condition: recipeDict
Description: This prints the dictionary nicely formatted.
"""
def printDictionary(tmpRecipeDict):
    for recipe in tmpRecipeDict:
        print("Recipe:",recipe)
        print("Ingredients Needed:")
        for ingredient in tmpRecipeDict[recipe]:
            ingredient = ingredient.title()
            print(""*12,ingredient)
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
        inputIngredient = 0
        while inputIngredient != "END":
            inputIngredient = input("Ingredient to add to search(END to stop: ")
            if inputIngredient != "END":
                ingredientList.append(inputIngredient)
        printRelevantRecipes(ingredientList,recipeDict)
    elif choice == 4:
        recipeToAdd = input("What Recipe to Add: ")
        while recipeToAdd in recipeDict:
            print("Recipe already in Dictionary")
            recipeToAdd = input("What Recipe to Add: ")
        addRecipe(recipeToAdd, recipeDict)
    elif choice == 5:
        printDictionary(recipeDict)
    choice = printMenu()
print("Thanks for using my program!")
