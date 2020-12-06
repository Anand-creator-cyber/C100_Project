class atm(object):
    def __init__(self, cardnumber, cardholdername, expirydate, pin):
        self.cardholdername = cardholdername
        self.cardnumber = cardnumber
        self.pin = pin
        self.expirydate = expirydate

    def crdnumber(self):
        print("4231 **** **** 1432")

    def checkbalance(self):
        print("Press 1 to check your account's balance")
        activity = input("Activity number :")
        if(activity == 1) :
            print(user.checkbalance)
        
        print("Your Balance is : $50,000")
        
       

    def withdrawl(self):
        print("Press 2 to withdraw")
        act = input("Activity Number :")
        if(act == 2):
            print(user.withdrawl)
        print("You have withdrawn $100")

user = atm("4231 **** **** 1432", "***** X", "4/77", "****")
print(user.crdnumber())
print(user.checkbalance())
print(user.withdrawl())
    
    

