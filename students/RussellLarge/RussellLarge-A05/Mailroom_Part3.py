#-------------------------------------------------#
# Title: Mailroom part 2
# Dev:   Rlarge
# Date:  2/13/2019
# ChangeL/og: (Who, When, What)
#   RLarge, 01/31/2019, Created Script
#   RLarge, 02/13/2019, Modified script with
#   Exceptions and Comprehensions
#-------------------------------------------------#

# Import Modules
import tempfile

# Variables

# Create variables for dict keys and values
Names = ["William Gates III", "Jeff Bezos", "Paul Allen", "Mark Zuckerberg"]
Donations = ([65332543, 377.32], [200.34, 9337.393], [8394.23, 777.2, 1.32], [273, 337692.15, 737361.23])

# create a dictionary, and 'zip' the keys and associated values together
DictDonor = dict(zip(Names, Donations))


prompt = "\n".join(("Welcome to the Mail Room Program.",
                    "Please choose from below options:",
                    "1 - Send a Thank you",
                    "2 - Create a Report",
                    "3 - Send out Email drafts",
                    "4 - Exit",
                    ">>> "))

# Functions
def MainMenu():
    print(prompt)


def ViewDonorList():
    # if user types 'list', show them a list of the donor names and reprompt.
    ShowList = input("View current donor list? (y/n)")
    if ShowList.lower() == 'y':
        print("Current Donor List:\n")
        [print(donor) for donor in DictDonor]

def SendThankYou():
    # if user types a name not in the list, add that name to the data structure and use it
    while True:
        DonorNameInput = input('\n'"Please enter a Donor Name to update (type 'exit' to quit): ")
        if DonorNameInput.lower() == 'exit':
            break
        elif DonorNameInput in DictDonor:
            print("Updating {}'s information".format(DonorNameInput))
            UpdateDonation = input("What is the new value(s) for {}?".format(DonorNameInput))
            DictDonor[DonorNameInput].append(float(UpdateDonation))
            print(DictDonor)
        else:
            NewDonation = [float(input("New Name entered. please add donation amount: "))]
            InputKey = [DonorNameInput]
            NewDict = dict.fromkeys(InputKey)
            NewDict[DonorNameInput] = NewDonation
            DictDonor.update(NewDict)
            print(NewDict)
            print("New entry successful! Here is the AutoGen Email: \n")
            # key would be the DonorNameInput, Values would be the letter template
            EmailTemplatedict = {"DonorName": DonorNameInput, "Email": "\nWe here at the Donation Center want "
                                                                       "to thank you for your contribution.\n"
                                                                       "Sincerely, \nthe Donation center.\n"}
            print("Dear {DonorName}, {Email}".format(**EmailTemplatedict))


def CreateReport():
    # Generate a report showing formatted items in the DictDonor
    Header = "{:<25}| {:<10} | {:<10} | {:<10}".format('DonorName', 'Total Given','Num Gifts', 'Average Gift')
    print(Header)
    print("-"*67)

    # DonorList = DictDonor[]

    for x in DictDonor:
        DonorSum = sum(DictDonor[x])
        DonorLen = len(DictDonor[x])
        DonorAvg = DonorSum/DonorLen
        print('{:<25} ${:<15.0f}  {:<10} ${:<2.2f}'.format(x, DonorSum, DonorLen, DonorAvg))
    print("-"*67)


def EmailToFile(enterdict):
    tempdir = tempfile.gettempdir()
    print(tempdir)
    name = enterdict.keys()
    for item in name:
        EmailTemplatedict = {"DonorName": item, "Email": "\nWe here at the Donation Center want "
                                                                   "to thank you for your contribution.\n"
                                                                   "Sincerely, \nthe Donation center.\n"}
        with open("{}\{}.txt".format(tempdir, item), "w") as f:
            f.write("Dear {},".format(EmailTemplatedict["DonorName"]))
            f.write(EmailTemplatedict["Email"])
    print("Email drafts generated and saved to text files using the Donor name."
          " Text Files are saved here: \n\n({}) ".format(tempdir))



# Presentation
def main():
    try:
        response = input(prompt)
        if response == "1":
            ViewDonorList()
            SendThankYou()
        elif response == "2":
            CreateReport()
        elif response == "3":
            EmailToFile(DictDonor)
        elif response == "4":
            print("Thank you for using the Mailroom program.")
        else:
            raise TypeError
    except TypeError:
        print("ERROR: Please enter a value from 1 to 4...."'\n')
        return main()

if __name__ == "__main__":
    # This guard blocks against code running automatically if module is imported
    main()