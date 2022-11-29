class bcolors:
    ResetAll = "\033[0m"

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def sth(phoneNumber=input('Enter your Phone Number : '), starCount=3):
    if len(phoneNumber) != 11:
        while len(phoneNumber) != 11:
            print(f"{bcolors.FAIL}this is wrong, please enter a correct number \n Your number must contained "
                  f"11 digits \n {bcolors.BOLD}Do it again: {bcolors.ResetAll} ")
            phoneNumber = input("Enter your CORRECT phone number: ")

            if len(phoneNumber) == 11:
                # break
                prefix = phoneNumber[0:4]
                suffix = phoneNumber[-4::1]
                starForm = f'{prefix}{bcolors.WARNING}{starCount * "*"}{bcolors.ResetAll}{suffix}'
                return starForm
            continue


print(sth())
