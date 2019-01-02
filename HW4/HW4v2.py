"""
Description: This program will double and add together a input, reverse an input
, and give a report about a input, including the average, max, min, and total.
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
print(str_reverse[::-1])
#http://stackoverflow.com/questions/931092/reverse-a-string-in-python

#this function reverses the entire input with an extended slice

#part three, print report about an input
str_report = input("Please enter a four digit number: ")
dOne = str_report[0]
dTwo = str_report[1]
dThree = str_report[2]
dFour = str_report[3]

dTotal = dOne + dTwo + dThree + dFour

dAverage = (dOne + dTwo + dThree + dFour) / 4

dMax = max(str_report)

dMin = min(str_report)

print("Average", /t "Minimum", /t "Maximum") 
