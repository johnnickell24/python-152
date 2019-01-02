"""
Description: A user will enter the amount of years money is compoounded and then
will be given how much money is in after interest.
"""
_author_="John Nickell"
_date_="9/8/14"

#part one
princAmount = 10000
interestRate = .08
numberCompunded = 12
str_numberYears = input("Please state number of years money is compounded: ")
numberYears = int(str_numberYears)
if numberYears>=0:
    print("Yay")

else :
    print("nope")
