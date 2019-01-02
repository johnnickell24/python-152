import os.path
"""
pre-condition: Hours and Payrate
Description: This calculates the gross pay of an employee in a text file.
"""
def calcGrossPay(tmpHours,tmpPay):
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
pre-condition: name of text file
description: this reads the textfile and puts the info into a list
"""
def readInfo(tmpFileName):
    tmpFile = open(tmpFileName,"r")
    for tmpLine in tmpFile:
        oneEmp = tmpLine.split()
        empRoster.append(oneEmp)
    tmpFile.close()
"""
pre-condition: name of text file
description: this writes gross pay to a text file with
the names of employees
"""
def writeInfotoFile(tmpFileName,tmpEmpRoster):
    tmpFile = open(tmpFileName,"r")
    for tmpLine in tmpFile:
        
        






empRoster = []
fileName = input("Name of file to be read: ")
while not os.path.isfile(fileName):
    fileName = input("Name of file to be read: ")
readInfo(fileName)
print(empRoster)
