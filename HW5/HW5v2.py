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
def getFirstLastName(tmpFullName):
    tmpFullName = tmpFullName.lower()
    tmpFullName = tmpFullName.title()
    if ',' in tmpFullName:
        fullNameList = tmpFullName.split(',')
    else:
        fullNameList = tmpFullName.split()
    return fullNameList

#main part
fullName = input("Please enter your name: ")
fullNameList = getFirstLastName(fullName)
firstName = fullNameList[0]
lastName = fullNameList[1]
print(firstName, lastName)
