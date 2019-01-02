"""
Description: This program uses a menu function let the user work with a
company roster. They can add, delete, change, and find employees using
functions as well as print a reort with the entire roster.
"""
_author_="John Nickell"
_date_="11/7/14"
"""
pre-condition: None
Description: This is the menu where the user will pick what function is used to
alter or print the company roster.
"""
def printMenu():
    print("1) Add Employee")
    print("2) Delete Employee")
    print("3) Change Employee Info")
    print("4) Find Employee")
    print("5) Print Report-All Employees")
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
"""
pre-condition: A ID,name,payrate,and hours
Description: This adds an employees info to a list that is then added to a
larger company roster.
"""
def addEmp(tmpCompanyRoster,tmpID,tmpFirstName,tmpLastName,tmpPay,tmpHours):
    for oneEmp in tmpCompanyRoster:
        if tmpID == oneEmp[0]:
            return "Duplicate"
    tmpFirstName = tmpFistName.title()
    tmpLastName = tmpLastName.title()
    tmpEmp = [tmpID,tmpFirstName,tmpLastName,tmpPay,tmpHours]
    tmpCompanyRoster.append(tmpEmp)
    return "Successful"
"""
pre-condition: The Company Roster as a list, and a numeric id
Description: This deletes an employee from the company roster if found by
company id.
"""
def delEmp(tmpCompanyRoster,tmpID):
    if not tmpCompanyRoster:
        return "Employee not found"
    for oneEmp in tmpCompanyRoster:
        if tmpID == oneEmp[0]:
            oneEmp.remove()
            return "Successful"
        
            

#main
choice = printMenu()
companyRoster = []                     
while choice != 6:
    if choice == 1:
        compID = input("Company ID: ")
        firstName = input("First Name: ")
        lastName = input("Last Name: ")
        payRate = input("Payrate: ")
        hours = input("Hours: ")
        result = addEmp(companyRoster,compID,firstName,lastName,payRate,hours)
        if result == "Successful":
            print("Employee successfully added")
        if result == "Duplicate":
            print("Error: ID was a duplicate")
    elif choice == 2:
        compID = input("Company ID: ")
        result =  delEmp(companyRoster,compID)
        if result == "Successful":
            print("Employee successfully deleted")
        if result == "Employee not found":
            print("Error: Employee not found")
    elif choice == 3:
        print("3")
    elif choice == 4:
        print("4")
    elif choice == 5:
        print("5")
    choice = printMenu()
print("Thanks for using my program!")
