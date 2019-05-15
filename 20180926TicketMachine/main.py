import datetime
import hashlib

class TicketMachine:
    def __init__ (self, price):
        self.costprice = price
        self.balance = 0
        self.total = 0
        self.printedTickets = 0
        self.password = ""
    
    def insertMoney(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("\nPlease insert a positive amount! " + repr(amount) + " is not valid!\n")

    def printTicket(self):
        if self.balance >= self.costprice:
            print("\n-xx-")   
            print("-Ticket Machine Ticket-")    
            print(repr(self.costprice) + " cents")    
            print("-xx-\n")  
            self.total += self.costprice - self.balance
            self.balance -= self.costprice
            self.printedTickets += 1
        else:
            print("\nThe price of this machine is " + repr(self.costprice) + " cents! Insert " + repr(self.costprice-self.balance) + " more please!\n")

    def refundMoney(self):
        self.balance = 0

    def setAdminPassword(self):
        self.password = input()

    def printAdminTicket(self):
        inputpass = input()
        if inputpass == self.password:           
            date = datetime.datetime.now()
            print("\n-xx-")           
            print("-Administrator Ticket-")
            print(date)
            print(self.printedTickets)
            print("-xx-\n")     
        else:
            print("\nWrong password!\n")

__name__ == "__main__"
t1 = TicketMachine(100)
