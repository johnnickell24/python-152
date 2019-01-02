"""
Description: This program reads a text file then writes a text file using
employee names and pay rate and hours.
"""
_author_="John Nickell"
_date_="11/21/14"

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
def writeInfotoFile(tmpFileName,tmpGrossRoster):
    tmpFile = open(tmpFileName,"w")
    for tmpOneEmp in tmpGrossRoster:
        tmpFile.write(tmpOneEmp[0])+\
        tmpFile.write(tmpOneEmp[1])+\
        tmpFile.write(tmpOneEmp[2])
    tmpFile.close()
#main
empRoster = []
fileName = input("Name of file to be read: ")
while not os.path.isfile(fileName):
    fileName = input("Name of file to be read: ")
readInfo(fileName)
grossPayRoster = []
for oneEmp in empRoster:
    oneEmpList = []
    oneEmpList.append(oneEmp[0])
    oneEmpList.append(oneEmp[1])
    grossPay = calcGrossPay(oneEmp[2],oneEmp[3])
    oneEmpList.append(grossPay)
    grossPayRoster.append(oneEmpList) 
fileName = input("Name of file to be written on: ")
while not os.path.isfile(fileName):
    fileName = input("Name of file to be written on: ")
writeInfotoFile(fileName,grossPayRoster)

