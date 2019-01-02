_author_="John Nickell"
_date_="9/29/14"
"""
pre-condition: string contains a first
		and last name separated
		by a space.
Description: accepts a string and
	     returns 2 strings --
	     first name and last name
"""
#function 1
def getFirstLastName(tmpFullName):
    tmpFullName = tmpFullName.lower()
    tmpFullName = tmpFullName.title()
    if ',' in tmpFullName:
        fullNameList = tmpFullName.split(', ')
    elif 'Mrs.' or 'Mr.' in tmpFullName:
        fullNameList = tmpFullName.split()
        fullNameList[0] = fullNameList[1]
        fullNameList[1] = fullNameList[2]
    else:
        fullNameList = tmpFullName.split()
    return fullNameList
#function 2
def getPhoneNum(tmpPhoneNum):
    if len(tmpPhoneNum) == 13 and tmpPhoneNum[0] == '(' and tmpPhoneNum[4] == ')' and tmpPhoneNum[8] == '-' and tmpPhoneNum[1:4].isdigit() and tmpPhoneNum[5:8].isdigit() and tmpPhoneNum[9:13].isdigit():
        return("True")
    else:
        return("False")
#function 3

    
#main part
fullName = input("Please enter your name: ")
fullNameList = getFirstLastName(fullName)
firstName = fullNameList[0]
lastName = fullNameList[1]
print(firstName, lastName)
