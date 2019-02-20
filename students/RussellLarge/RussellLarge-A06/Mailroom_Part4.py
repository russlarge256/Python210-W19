#!/usr/bin/env python

# -------------------------------------------------#
# Title: Mailroom part 2
# Dev:   Rlarge
# Date:  2/13/2019
# ChangeL/og: (Who, When, What)
#   RLarge, 01/31/2019, Created Script
#   RLarge, 02/13/2019, Modified script with
#   Exceptions and Comprehensions
#   RLarge, 2/18/2019, used refactoring and set
#   up unit testing
# -------------------------------------------------#


# Import Modules
import tempfile
import sys
from collections import defaultdict
# Variables

Names = ["William Gates III", "Jeff Bezos", "Paul Allen", "Mark Zuckerberg"]
Donations = ([65332543, 377.32], [200.34, 9337.393], [8394.23, 777.2, 1.32], [273, 337692.15, 737361.23])
DictDonor = dict(zip(Names, Donations))

prompt = "\n".join(("Welcome to the Mail Room Program.",
                    "1 - View Donor List",
                    "2 - Update/Add Donor Data",
                    "3 - View Donor report",
                    "4 - Email draft to all donors",
                    "5 - Exit Program",
                    "\n\nPlease choose from the above options:"))

# Functions

# Main Functions
def Main():
    while True:
        try:
            response = input(prompt)
            UserResponse(response)
        except TypeError:
            print("ERROR: Please enter a value from 1 to 4...."'\n')

def UserResponse(choice):
    UserOptions = {'1': ViewDonorList, '2': ThankYouResponse, '3': ViewReport, '4': EmailToFile, '5': ExitProgram}
    return UserOptions.get(choice)()

# Option 1
def ThankYouResponse():
    try:
        NameUser = input('\n'"Please enter a Donor Name to update ('exit' returns to main): ")
        if NameUser.lower() == 'exit':
            return Main()
        elif NameUser in DictDonor:
            UpdateDonation = float(input("What is the new value(s) for {}?".format(NameUser)))
            return UpdateDonorData(NameUser, UpdateDonation)
        elif NameUser not in DictDonor:
            NewDonation = float(input("New Name entered. please add donation amount: "))
            return NewDonor(NameUser, NewDonation)
    except TypeError as e:
        print(e)


def UpdateDonorData(name, donation):
    # if user types a name not in the list, add that name to the data structure and use it
    print("Updating {}'s information".format(name))
    DictDonor[name] += donation
    print(DictDonor.get(name, donation))
    print(DictDonor.keys())
    return Main()

def NewDonor(name, donation):
    NewDict = dict.fromkeys([name])
    NewDict[name] = [donation]
    DictDonor.update(NewDict)
    print("New entry successful! Here is the AutoGen Email: \n")
    print(EmailTemplate(name, donation))
    return Main()

# Option 2
def CreateReport(db):
    Reporting = "{:<25}| {:<10} | {:<10} | {:<10}\n".format('Donor Name', 'Total Given','Num Gifts', 'Average Gift')
    Reporting += "-" * 67 + '\n'
    for names, donations in db.items():
        DonorSum = sum(donations)
        DonorLen = len(donations)
        DonorAvg = DonorSum/DonorLen
        Reporting += "{:<25} ${:<15.0f}  {:<10} ${:<2.2f}\n".format(names, DonorSum, DonorLen, DonorAvg)
    Reporting += "-"*67
    return Reporting

def ViewReport():
    print(CreateReport(DictDonor))

# Option 3
def EmailTemplate(name, donation):
    note = ('Dear {},\n\nWe want to thank you for your generous donations(s) of ${}.\n\n'
              'Sincerely,\n'
              'The RussLarge Donation Center.'.format(name, donation))
    return note

def EmailToFile():
    try:
        tempdir = tempfile.gettempdir()
        for name, donation in DictDonor.items():
            with open("{}\{}.txt".format(tempdir, name), "w") as f:
                f.write(EmailTemplate(name, str(donation)))
                f.close()
        print("\nEmail drafts generated and saved to text files using the Donor name."
              " Text Files are saved here: \n({}) \n".format(tempdir))
    except TypeError:
        print("operation/function applied to an object of inappropriate type.\n")
    except NameError:
        print("local/global name not found. applies only to unqualified names")

# Option 4
def ViewDonorList():
    count = 1
    print('\n')
    for item in DictDonor.keys():
        print("Donor {}. {}".format(count, item))
        count += 1
    print('\n')
    return Main()

# Option 5
def ExitProgram():
    print("Thank you for using the Mailroom program.")
    return sys.exit()


if __name__ == "__main__":
    Main()