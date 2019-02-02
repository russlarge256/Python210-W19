#-------------------------------------------------#
# Title: MailRoom Lab
# Dev:   Rlarge
# Date:  1/31/2019
# ChangeLog: (Who, When, What)
#   RLarge, 01/31/2019, Created Script

#-------------------------------------------------#

# Import Modules
import sys


# Variables
Donor1 = ["William Gates III", 65332543, 377.32]
Donor2 = ["Jeff Bezos",  200.34, 9337.393]
Donor3 = ["Paul Allen",  8394.23, 777.2, 1.32]
Donor4 = ["Mark Zuckerberg", 273, 337692.15, 737361.23]

DonorList = [Donor1, Donor2, Donor3, Donor4]


prompt = "\n".join(("Welcome to the Mail Room Program.",
                    "Please choose from below options:",
                    "1 - Send a Thank you",
                    "2 - Create a Report",
                    "3 - Exit",
                    ">>> "))

# Functions
def MainMenu():
    print(prompt)


def ViewDonorList():
    # if user types 'list', show them a list of the donor names and reprompt.
    ShowList = input("enter 'list' to view current Donor List: ")
    if ShowList.lower() == 'list':
        for x in DonorList:
            print(x[0])

def SendThankYou():
    # if user types a name not in the list, add that name to the data structure and use it
    while True:
        StrDonorList = str(DonorList)
        DonorNameInput = input("Please enter a Donor Name to update: ")
        if DonorNameInput in StrDonorList:
            print("Updating {}'s information".format(DonorNameInput))
            # Struggled to figure out how to update an associated item in the tuple.
        elif DonorNameInput not in StrDonorList:
            NewList = DonorList
            NewEntry = float(input("New Name entered. please add donation amount: "))
            AppendList = (str(DonorNameInput), [NewEntry])
            NewList += AppendList
            AutoPrompt = ("AutoGen Email Response:")
            EmailMes = ("Hello {}, {}On behalf of the Russ Large Donation center, we thank"
                        " you for your generous donation.".format(DonorNameInput, '\n'))
            print("{} Has now been added to the donation history.".format(AppendList))
            print("{}{}{}{}{}".format(AutoPrompt, '\n', '\n', EmailMes, '\n'))
            break


def CreateReport():
    # Generate a report showing formatted items in the DonorList
    Header = "{:<25}| {:<10} | {:<10} | {:<10}".format('DonorName', 'Total Given','Num Gifts', 'Average Gift')
    print('\n')
    print(Header)
    print("-"*67)

    for x in DonorList:
        print('{:<25} ${:<15.0f}  {:<10} ${:<2.2f}'.format(x[0], sum(x[1:]), len(x[1:]), sum(x[1:]) / len(x[1:])))
    print("-"*67)
    print('\n')


# Presentation
def main():
    while True:
        response = input(prompt)
        if response == "1":
            ViewDonorList()
            SendThankYou()
        elif response == "2":
            CreateReport()
        elif response == "3":
            print("Thank you for using the Mailroom program.")
            break
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    # This guard blocks against code running automatically if module is imported
    main()