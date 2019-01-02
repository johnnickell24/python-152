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
hours = float(str_hours)
str_payrate = input("Please enter payrate: ")
payrate = float(str_payrate)

#overtime calculations
if hours > 40:
    otHours = hours - 40
    otPayrate = payrate * 1.5
    otGrossPay = otHours * otPayrate
    grosspay = (40 * payrate) + otGrossPay
else :
    grosspay = hours * payrate
#calculations
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
print("Hours:", "%.2f" % hours)
print("Pay Rate:$", "%.2f" % payrate)
print("Gross Pay:$", "%.2f" % grosspay)
print(/t"SS Tax Withheld:$", "%.2f" % SS_TAXRATE)
print("Federal Tax Withheld:$", "%.2f" % FED_TAXRATE)
print("Total Deductions:$", "%.2f" % total_deduction)
print("Net Pay:$", "%.2f" % net_pay)
