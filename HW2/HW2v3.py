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
payrate = int(str_payrate)

#calculations
grosspay = hours * payrate
print(grosspay)
