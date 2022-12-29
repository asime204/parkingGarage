class ParkingGarage:
    def __init__(self, size):
        self.tickets = [{"paid": False} for i in range(size)]
        self.parkingSpaces = [{} for i in range(size)]
        self.currentTicket = {}

    def take_ticket(self):
        if self.tickets:
            self.currentTicket = self.tickets.pop()
            self.parkingSpaces.pop()

    def payForParking(self):
        payment = input("Please insert cash here: ")
        if payment:
            print("ticket has been paid leave within 15 minutes or we will tow your car!")
            self.currentTicket["paid"] = True

    def leaveGarage(self):
         if self.currentTicket:               
            if self.currentTicket["paid"] == True:
                print("Thank you for your money please come again!")
                self.parkingSpaces.append({})
                self.tickets.append({"paid": False})
                self.currentTicket = {}
            else:
                print("You are broke cough some money up before you leave!")
                self.payForParking()
                self.parkingSpaces.append({})
                self.tickets.append({"paid": False})
                self.currentTicket = {}
                print("Thank you for your money please come again!")
                
    def printStatus(self):
        print(f"Tickets: {self.tickets}, Spaces: {self.parkingSpaces}, CurrentTicket: {self.currentTicket}")
                
def playGarage():
    size = int(input("How many spaces in your garage? "))
    myGarage = ParkingGarage(size)
    playing = True
    
    while playing == True:
        choice = input("Please enter 'T' to take ticket, 'P' to pay, 'L' to leave garage, 'S' to print status, or 'Q' to quit: ").lower()
        if choice == 't':
            myGarage.take_ticket()
        elif choice == 'p':
            myGarage.payForParking()
        elif choice == 'l':
            myGarage.leaveGarage()
        elif choice == 's':
            myGarage.printStatus()
        elif choice == 'q':
            playing = False
        
playGarage()