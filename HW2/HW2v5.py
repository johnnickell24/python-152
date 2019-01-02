"""
Description: This is a program that will ask for a person's information such as
their name, ssn, payrate, and hours. The program will then process this info and
give back a report detailing what the person gave plus their grosspay, deductions,
and their net pay.
"""
_author_="John Nickell"
_date_="9/4/14"

#gathering the info
ssn = input("Please enter your SSN: ")
first_name = input("Please enter first name: ")
last_name = input("Please enter last name: ")
str_hours = input("Please enter hours: ")
hours = int(str_hours)
str_payrate = input("Please enter payrate: ")
payrate = float(str_payrate)

#calculations
grosspay = hours * payrate
SS_TAX = .05
SS_TAXRATE = grosspay * SS_TAX
FED_TAX = .15
FED_TAXRATE = grosspay * FED_TAX
total_deduction = FED_TAXRATE + SS_TAXRATE
net_pay = grosspay - total_deduction

#printing report of info
print("Social Security Number:", ssn)
print("First Name:", first_name)
print("Last Name:", last_name)
print("Hours:", hours)
print("Pay Rate:$", round(payrate,2))
print("Gross Pay:$", grosspay)
print("SS Tax Withheld:$", SS_TAXRATE)
print("Federal Tax Withheld:$", FED_TAXRATE)
print("Total Deductions:$", total_deduction)
print("Net Pay:$", net_pay)
