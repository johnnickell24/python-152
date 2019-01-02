"""
Description:
"""
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
    else:
        if tmpFullName.count(' ') == 2:
            fullNameList = tmpFullName.split()
            fullNameList[0] = fullNameList[1]
            fullNameList[1] = fullNameList[2]
        else:
            fullNameList = tmpFullName.split()
        
    return fullNameList
"""
pre-condition: if string contains (xxx)xxx-xxxx
where 'x' are numbers
"""
#function 2
def getPhoneNum(tmpPhoneNum):
    if len(tmpPhoneNum) == 13 and tmpPhoneNum[0] == '(' and tmpPhoneNum[4] == ')' and tmpPhoneNum[8] == '-' and tmpPhoneNum[1:4].isdigit() and tmpPhoneNum[5:8].isdigit() and tmpPhoneNum[9:13].isdigit():
        return("Valid")
    else:
        return("Invalid")
"""
pre-condition: if string contains a valid
xxx-xx-xxxx ssn where 'x' are numbers
"""
#function 3
def getSSN(tmpSSN):
    if len(tmpSSN) == 10 and tmpSSN[3] == '-' and tmpSSN[6] == '-' and tmpSSN[0:3].isdigit() and tmpSSN[4:6].isdigit() and tmpSSN[7:].isdigit():
        return("Valid")
    else:
        return("Invalid")
    
#main part
fullName = input("Please enter your name: ")
if fullname != "END":
    
fullNameList = getFirstLastName(fullName)
firstName = fullNameList[0]
lastName = fullNameList[1]
firstLine = format("Last","20s"), format("First","20s"), format("Social","13s"), format("Home","13s"))
secondLine = format("Name","20s"), format("Name","20s"), format("Security #","13s"), format("Phone","13s"))
print(format(lastName,"20s"), format(firstName,"20s"))
