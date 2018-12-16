class Mode:

    def __init__(self, speed, id=None, variableCost=None, fixedCost=None):

        self.speed = speed
        self.id = id #Bus", "Car", "Walking", "Biking"

        # We are not working with cost information for the moment.
        self.variableCost = variableCost
        self.fixedCost = fixedCost

class Vehicle:
    def __init__(self, id, position, speed, icon):
        self.id = id
        self.position = position
        self.speed = speed
        self.icon = icon

    def setIcon(self,vehicleIcon):
        self.icon = vehicleIcon

class Car(Vehicle):
    def driving(self):
        a = 0

class Bike(Vehicle):
    def driving(self):
        a = 0

class Bus(Vehicle):
    def __init__(self, id, position, speed,route,icon):
        self.passengers = [] #List of objects type passenger
        self.id = id
        self.position = position
        self.speed = speed
        self.route = route
        self.icon = icon #It is a vehicleIcon

        self.moving = False #Bus is not initially moving
        self.trajectory = None #The current trajectory of ths bus
        self.clockwise = None  # Boolean saying whether the bus is moving in clockwise direction
        self.positionTrajectory = 0

        super().__init__(id = id, position = position, speed = speed, icon = icon)


    def loadPassenger(self,passenger):
        self.passengers.append(passenger)

    # def moveBus(self):
    #     for passenger in self.passengers:
    #         passenger.position = self.position

    # def newPosition(self,position):
    #     self.position = position

    def move(self,trajectory):
        self.trajectory = trajectory
        xts = trajectory.xts

        if self.trajectory.nPositions > 1:
            self.moving = True
            self.stop = False

            self.clockwise = trajectory.direction.isClockwise()
            # self.positionTrajectory += 1
            self.position = xts[self.positionTrajectory+1].position

            if self.trajectory.nPositions == 2: #If the trajectory have two points is because in the next move the bus will have arrived to the destination
                self.moving = False

    def stop(self):
        self.moving = False
        self.trajectory = None
        # self.positionTrajectory = 0
