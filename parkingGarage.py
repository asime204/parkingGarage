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
        pass

    def leaveGarage(self):
        pass

myGarage = ParkingGarage(3)

print(myGarage.tickets)