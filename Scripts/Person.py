#Maybe this class should be called "Person" as passenger is only limited for buses

class Person:
    #Picture is
    def __init__(self, id, position, walkingSpeed, westLocation, eastLocation, icon = None):
        self.id = id
        self.position = position
        self.icon = icon
        self.westLocation = westLocation
        self.eastLocation = eastLocation
        self.moving = True

        #Dictionary with path of different icons where the key is the name of the icon, and the value its path
        self.icons = {}
        if icon is not None:
            self.icons[icon.id] = icon

        self.trajectory = None
        self.positionTrajectory = 0

        #Walking attributes
        self.walking = False
        self.walkingTime = 0
        self.walkingSpeed = walkingSpeed

        self.speed = self.walkingSpeed #If the person is not riding a vehicle (car, bike, bus)

        #Waiting attributes
        self.waiting = False
        self.waitingTime = 0

        #Travelling attributes
        self.travelling = False
        self.travelTime = 0
        self.travelSpeed = None
        self.destination = None

        self.trips = [] #List of trips

        self.finalLocation = None

    def getWalkingDistance(self):
        return self.walkingDistanceFromOriginToStop +  self.walkingDistanceFromStopToDestination + self.walkingDistanceFromOriginToDestination

    def setWalkingDistanceFromOriginToStop(self, distance):
        self.walkingDistanceFromOriginToStop = distance

    def setWalkingDistanceFromStopToDestinatio(self, distance):
        self.walkingDistanceFromStopToDestination = distance

    def setWalkingDistanceFromOriginToDestination(self, distance):
        self.walkingDistanceFromOriginToDestination = distance

    def addTrip(self,trip):
        self.trips.append(trip)

    def move(self,trajectory, isWalking):
        self.trajectory = trajectory
        xts = trajectory.xts

        if self.trajectory.nPositions > 1:
            self.moving = True
            self.stop = False

            self.clockwise = trajectory.direction.isClockwise()
            # self.positionTrajectory += 1
            initialPosition = self.position
            nextPosition =  xts[self.positionTrajectory+1].position

            self.position = nextPosition #Update person position

            if self.trajectory.nPositions == 2: #If the trajectory have two points is because in the next move the bus will have arrived to the destination
                self.moving = False

            if isWalking == True:
                self.speed = self.walkingSpeed

    def stop(self):
        self.walking = False
        self.trajectory = None
        self.positionTrajectory = -1

    def waitBusStop(self,timeInterval):
        self.waiting = True
        self.waitingTime += timeInterval

    def travel(self,timeInterval,travelSpeed,destination):
        self.travelling = True
        self.destination = destination
        self.travelTime += timeInterval

    def travellingInVehicle(self, vehicle):
        self.speed = vehicle.speed

    def setIcon(self,icon):
        # self.addIcon(icon)
        self.icons[icon.id] = icon
        self.icon = icon

    def addIcon(self,icon, id = None):

        if id is None:
            self.icons[icon.id] = icon
        else:
            # icon.id = id
            self.icons[id] = icon


    def setPictureIcon(self,path):
        self.icon.setPicture(path = path)

    def setFinalLocation(self,location):
        self.finalLocation = location