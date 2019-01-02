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
    tmpFirstName = tmpFirstName.title()
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
            tmpCompanyRoster.remove(oneEmp)
            return "Successful"
    return "Employee not found"    
"""
pre-condition: Company Roster, Company ID, new payrate, new hours
Description: This changes an employees hours and rate to a new rate, but 0
by default.
"""           
def changeEmp(tmpCompanyRoster,tmpID,tmpNewPay=0,tmpNewHours=0):
    for oneEmp in tmpCompanyRoster:
        if tmpID == oneEmp[0]:
            oneEmp[3] = tmpNewPay
            oneEmp[4] = tmpNewHours
            return "Successful"
    return "Employee not found"
"""
pre-condition: The Company Roster as a list, and a last name
Description: This finds an employee or employees matching a last name in the
company roster and printing their info
"""
def findEmp(tmpCompanyRoster,tmpLastName):
    tmpList = []
    tmpLastName = tmpLastName.title()
    for oneEmp in tmpCompanyRoster:
        if oneEmp[2] == tmpLastName:
            tmpList.append(oneEmp)
    tmpTuple = tuple(tmpList)
    if not tmpTuple:
        return "Employee not found"
    return tmpTuple
"""
pre-condition: Company Roster and Employee ID
Description: This calculates the gross pay of an employee to be used in a
report.
"""
def calcGrossPay(tmpCompanyRoster,tmpID):
    for oneEmp in tmpCompanyRoster:
        if oneEmp[0] == tmpID:
            tmpHours = oneEmp[4]
            tmpPay = oneEmp[3]
    tmpHours = float(tmpHours)
    tmpPay = float(tmpPay)
    if tmpHours > 40:
        tmpOverHours = tmpHours - 40
        tmpOverPay = tmpPay * 1.5
        tmpOverGrossPay = tmpOverHours * tmpOverPay
        tmpGrossPay = (40 * tmpPay) + tmpOverGrossPay
    else:
        tmpGrossPay = tmpHours * tmpPay
    tmpGrossPay = str(tmpGrossPay)
    return tmpGrossPay
"""
pre-condition: The Company Roster as a list
Description: This prints a report detailing the entire Company Roster with
each employee's id, name, payrate, hours, and grosspay.
"""
def printReport(tmpCompanyRoster):
    firstLine = format("ID","15s")+format("First Name","15s")+format("Last Name","15s")\
    +format("Payrate","10s")+format("Hours","10s")+format("Grosspay","10s")
    secondLine = "-" * 80
    print(firstLine)
    print(secondLine)
    for oneEmp in tmpCompanyRoster:
        print(format(oneEmp[0],"15s")+format(oneEmp[1],"15s")+format(oneEmp[2],"15s")\
        +format(oneEmp[3],"10s")+format(oneEmp[4],"10s")\
        +format(calcGrossPay(tmpCompanyRoster,oneEmp[0]),"10s"))
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
        compID = input("Company ID: ")
        newPay = input("New Pay: ")
        newHours = input("New Hours: ")
        result = changeEmp(companyRoster,compID,newPay,newHours)
        if result == "Successful":
            print("Employee successfully changed")
        if result == "Employee not found":
            print("Error: Employee not found")
    elif choice == 4:
        lastName = input("Last Name: ")
        result = findEmp(companyRoster,lastName)
        if result == "Employee not found":
            print("Error: Employee not found")
        else:
            print(result)
    elif choice == 5:
        printReport(companyRoster)
    print(companyRoster)
    choice = printMenu()
print("Thanks for using my program!")
