#-------------------------------------------------#
# Title: Mailroom part 2
# Dev:   Rlarge
# Date:  1/31/2019
# ChangeLog: (Who, When, What)
#   RLarge, 01/31/2019, Created Script
#-------------------------------------------------#

# Import Modules
import tempfile

# Variables

# Create dictionary, create keys, add values to keys
NewKeys = ["William Gates III", "Jeff Bezos", "Paul Allen", "Mark Zuckerberg"]
DictDonor = dict.fromkeys(NewKeys)

# Add more data to the dictionary
DictDonor["William Gates III"] = [65332543, 377.32]
DictDonor["Jeff Bezos"] = [200.34, 9337.393]
DictDonor["Paul Allen"] = [8394.23, 777.2, 1.32]
DictDonor["Mark Zuckerberg"] = [273, 337692.15, 737361.23]


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
    ShowList = input("enter 'list' to view current Donor List: ")
    if ShowList.lower() == 'list':
        for x in DictDonor.keys():
            print(x)

def SendThankYou():
    # if user types a name not in the list, add that name to the data structure and use it
    while True:
        DonorNameInput = input("Please enter a Donor Name to update (type 'exit' to quit): ")
        if DonorNameInput.lower() == 'exit':
            break
        elif DonorNameInput in DictDonor:
            print("Updating {}'s information".format(DonorNameInput))
            UpdateDonation = input("What is the new value(s) for {}?".format(DonorNameInput))
            DictDonor[DonorNameInput] = UpdateDonation
            print(DictDonor)
        else:
            NewDonateEntry = [float(input("New Name entered. please add donation amount: "))]
            InputKey = [DonorNameInput]
            NewDict = dict.fromkeys(InputKey)
            NewDict[DonorNameInput] = NewDonateEntry
            DictDonor.update(NewDict)
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
    # print(name)
    for item in name:
        EmailTemplatedict = {"DonorName": item, "Email": "\nWe here at the Donation Center want "
                                                                   "to thank you for your contribution.\n"
                                                                   "Sincerely, \nthe Donation center.\n"}

        with open("{}\{}.txt".format(tempdir, item), "w") as f:
            f.write("Dear {},".format(EmailTemplatedict["DonorName"]))
            f.write(EmailTemplatedict["Email"])
    print("Email drafts generated and saved to text files using the Donor name."
          " Text Files are saved here: \n\n({}) ".format(tempdir))
        # print("Dear {DonorName}, {Email}".format(**EmailTemplatedict))



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
            EmailToFile(DictDonor)
        elif response == "4":
            print("Thank you for using the Mailroom program.")
            break
        else:
            print("Not a valid option!")

if __name__ == "__main__":
    # This guard blocks against code running automatically if module is imported
    main()