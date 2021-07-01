class ATM:
    def __init__(self,cardNo,pin):
        self.card = cardNo
        self.pin = pin

    def CashWithdrawl(self,amount):
        print("Withdrawn Rs. " , amount , " From Your account " , self.card)

    def Enquiry(self):
        print("Rs. 300 Currently available in your account")



def loggedIn(acc):
    print(" Enter [1] for cash withdrawl \n Enter [2] for balance inquiry")

    wtd = input("Your Input: ")

    if wtd == "1" or wtd == "2":
        if wtd == "1":
            amnt = input("Amount to be withdrawn: ")
            acc.CashWithdrawl(amnt)
        else:
            acc.Enquiry()

    else: 
        print("Please try again")
        loggedIn(acc)
    
    ag = input(" Would you like to Do something else? \n Enter [Y] for YES or any other key for NO: ")

    if(ag == "Y" or ag == "y"):
        loggedIn(acc)
    else:
        print("Thank you for banking with us.")

def login(c,p):
    acc = ATM(c,p)
    loggedIn(acc)


def start():
    print("Please log in to your account")
    cardno = input("Card Number: ")

    pin = input("Pin for account " + cardno + ": ")

    if cardno != '' and pin != '':
        login(cardno,pin)

    else:
        print("Invalid Inputs. Please Try again.")
        start()


start()