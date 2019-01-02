"""
Description: A user will enter the amount of years money is compoounded and then
will be given how much money is in after interest.
"""
_author_="John Nickell"
_date_="9/8/14"

#variables and input
p = 10000
r = .08
n = 12
str_t = input("Please state number of years money is compounded: ")
t = int(str_t)

#if then calculation
if t>=0 :
    variableOne = 1 + (r / n)
    variableExponent = n * t
    variableTwo = variableOne ** variableExponent
    finalAmount = p * variableTwo
    print("$" "%.2f" % finalAmount)

elif ValueError :
    print("Please enter a valid digit")
else :
    print("Please enter a positive number")
   
