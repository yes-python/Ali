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


def sth(phoneNumber=input('Enter your Phone Number : '), starCount='*'):

    if len(phoneNumber) != 11:
        while len(phoneNumber) != 11:
            print(f"{bcolors.FAIL}this is wrong, please enter a correct number \n Your number must contained "
                  f"11 digits \n {bcolors.BOLD}Do it again: {bcolors.ResetAll} ")
            phoneNumber = input("Enter your CORRECT phone number: ")

            if len(phoneNumber) == 11:
                plus_star = int(input("how many stars do you want: "))
                if plus_star == 3:
                    return (phoneNumber.replace(phoneNumber[4:7], starCount * plus_star))
                elif plus_star == 4:
                    return (phoneNumber.replace(phoneNumber[4:8], starCount * plus_star))
                elif plus_star == 5:
                    return (phoneNumber.replace(phoneNumber[4:9], starCount * plus_star))
                elif plus_star == 6:
                    return (phoneNumber.replace(phoneNumber[4:10], starCount * plus_star))
                elif plus_star == 7:
                    return (phoneNumber.replace(phoneNumber[4:11], starCount * plus_star))
                else:
                    print(f'{bcolors.WARNING}You`ve chosen wrong!!! CHOOSE FROM NUMBERS FROM 3 TO 7.{bcolors.ResetAll}')
                    return sth()

            continue

    else:
        plus_star = int(input("how many stars do you want: "))
        if plus_star == 3:
            return (phoneNumber.replace(phoneNumber[4:7], starCount * plus_star))
        elif plus_star == 4:
            return (phoneNumber.replace(phoneNumber[4:8], starCount * plus_star))
        elif plus_star == 5:
            return (phoneNumber.replace(phoneNumber[4:9], starCount * plus_star))
        elif plus_star == 6:
            return (phoneNumber.replace(phoneNumber[4:10], starCount * plus_star))
        elif plus_star == 7:
            return (phoneNumber.replace(phoneNumber[4:11], starCount * plus_star))
        else:
            print(f'{bcolors.WARNING}You`ve chosen wrong!!! CHOOSE FROM NUMBERS FROM 3 TO 7.{bcolors.ResetAll}')
            return sth()



print(sth())
