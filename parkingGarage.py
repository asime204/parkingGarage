# makes a class ParkingGarage which takes one argument for the size of the garage and then instantiates a parking garage with 4 attributes and 4 methods.
# Uses the size parameter to determine the number of tickets and parking spaces available.
# Below the class, a function called playGarage() instantiates a ParkingGarage and allows the user to manipulate the object with its methods.

class ParkingGarage:
    def __init__(self, size): # init main contributor: Aziel.
        self.tickets = [{"paid": False} for i in range(size)] # a list of all available tickets, number determined by user input. ticket structure is a dictionary with "paid" key and boolean value.
        self.parkingSpaces = [{} for i in range(size)] # a list of all available parking spaces, number determined by user input. space structure is an empty dictionary for possible later functionality of tracking individual spaces.
        self.currentTicket = {} # user can hold and use one ticket at a time
        self.paidTicket = [] # added this list of paid tickets so that user can pay more than one ticket at a time

    def take_ticket(self): # take_ticket main contributor: Aziel.
        if self.tickets: # checks whether there are tickets available. if not, does nothing.
            self.currentTicket = self.tickets.pop() # if there are tickets available, takes one off the list and makes it the current ticket
            self.parkingSpaces.pop() # removes one parking space.

    def payForParking(self): # payForParking main contributor: Uriel.
        payment = input("Please insert cash here: ") #prompts the user to enter a payment. will take any truthy value as valid payment.
        if payment: # checks whether user has entered a valid payment.
            print("ticket has been paid leave within 15 minutes or we will tow your car!")
            if self.currentTicket["paid"] == False: # checks whether the current ticket is still unpaid.
                self.currentTicket["paid"] = True # changes the current ticket to paid.
            else:
                    self.paidTicket.append({"paid": True}) # if the current ticket is already paid, allows user to pay another ticket and adds it to the paid ticket list.

    def leaveGarage(self): # leaveGarage main contributor: Uriel.
         if self.currentTicket: # checks if the user has a current ticket.          
            if self.currentTicket["paid"] == True: # checks if the current ticket is paid.
                print("Thank you for your money please come again!")
                self.parkingSpaces.append({}) # adds the vacated spot back onto the parking spaces list.
                self.tickets.append({"paid": False}) # adds a new ticket to the available tickets list.
                if self.paidTicket: # checks whether there are any tickets in the paid tickets list.
                    self.currentTicket = self.paidTicket.pop() # takes one of the previously paid tickets and makes it the current ticket.
                else:
                    self.currentTicket = {"paid": False} # makes the current ticket an unpaid ticket.
            else:
                print("You are broke cough some money up before you leave!")
                self.payForParking() # runs the payForParking method to allow user to pay current ticket in order to leave.
                self.parkingSpaces.append({})
                self.tickets.append({"paid": False})
                if self.paidTicket:
                    self.currentTicket = self.paidTicket.pop()
                else:
                    self.currentTicket = {"paid": False}
                print("Thank you for your money please come again!")
                
    def printStatus(self): # main contributor: todd.
        print(f"Tickets: {self.tickets}, Spaces: {self.parkingSpaces}, CurrentTicket: {self.currentTicket}") # allows the user to see the lists of available tickets, spaces, and the current ticket.
                
def playGarage(): # main contributor: todd
    size = int(input("How many spaces in your garage? ")) # saves user input of desired size into size variable
    myGarage = ParkingGarage(size) # instantiates a parking garage using the size variable as an argument
    playing = True # sets a variable which allows the user to continue interacting until they enter the quit command which changes this variable to False and ends the program.
    
    while playing == True: # continues prompting the user to run class methods until they choose quit and the loop ends.
        choice = input("Please enter 'T' to take ticket, 'P' to pay, 'L' to leave garage, 'S' to print status, or 'Q' to quit: ").lower() # main prompt allows user to enter one of 5 commands and changes case to lower.
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
        
playGarage() # runs playGarage which prompts the user to enter the size of their garage and allows them to run all the methods and play with an instance of a ParkingGarage.