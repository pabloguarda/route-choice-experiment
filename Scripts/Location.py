from Scripts.TimeSpace import *

class Location(Position):
    def __init__(self, x,y,id):
        self.id = id  # Home, Work, Stop1, Stop2, Stop3, Stop4, etc...
        self.position = Position(x, y)
        super().__init__(x = x , y = y)

class BusStop(Location):
    def __init__(self, id, x,y,dwellTime, icon = None):
        self.id = id
        self.position = Position(x, y)  # Position in x and y
        super().__init__(x=x, y=y, id = id)
        self.visited = False
        self.dwellTime = dwellTime
        self.treatmentStop = False
        self.nextBusTime = None

        self.icon = icon

    # def numberPassenger(self):
    #     a = 0

    def setNextBusTime(self, nextBusTime):
        self.nextBusTime = nextBusTime

    def getNextBusTime(self):
        return self.nextBusTime

    def isTreatmentStop(self):

        if self.treatmentStop == True:
            return True
        else:
            return False

    #In transportation, dwell time or terminal dwell time refers to the time a vehicle such as a public transit bus or train spends at a scheduled stop without moving.
    def getDwellTime(self):
        return self.dwellTime #Fo the moment, we asume the Dwell time is constant (equal to 1 second), regardless the numebr of passenger at the bus stop
    def setDwellTime(self,dwellTime):
        self.dwellTime = dwellTime

class BusTerminal (Location):
    def __init__(self, id, x,y,icon):
        self.id = id
        self.position = Position(x, y)  # Position in x and y
        super().__init__(x=x, y=y, id = id)

        self.icon = icon