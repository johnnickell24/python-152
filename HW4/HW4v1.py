"""
Description:
"""
_author_="John Nickell"
_date_="9/21/14"

#part one, double digits
str_doub = input("Please enter a five digit number: ")
digitOne = int(str_doub[0]) * 2
digitTwo = int(str_doub[1]) * 2
digitThree = int(str_doub[2]) * 2
digitFour = int(str_doub[3]) * 2
digitFive = int(str_doub[4]) * 2
sumDigits = digitOne + digitTwo + digitThree + digitFour + digitFive
print(sumDigits)



#part two, reverse digits
str_reverse = input("Please enter a five digit number: ")
reverse = int(str_reverse)
