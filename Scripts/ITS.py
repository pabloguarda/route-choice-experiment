import copy #To copy objects

from Scripts.Functions import * #Import py file with my own functions
from Scripts.TimeSpace import * #Import py file with my own functions


#ITS: Intelligent Transportation Systems. This class is the brain of the program. Most of methods in this class are heuristics invented by me so not necessarily are the optimal ones.

class ITS:

    def __init__(self, networks,busStops,buses, virtualNetwork, realNetwork, timeInterval):
        self.networks = networks
        self.busStops = busStops
        self.buses = buses #The entire buses of the network
        self.realNetwork = realNetwork
        self.virtualNetwork = virtualNetwork
        self.timeInterval = timeInterval  # timeInterval to build the trajectories

    #This method converts a point from the real network to the virtual network (i.e. the map)
    def getVirtualPosition(self,position):
        return reMapping(position,virtualNetwork = self.virtualNetwork,realNetwork = self.realNetwork)

    #This method update the position of the vehicle icon shown in virtual network (i.e. the map)
    def updateVehicleMapPosition(self,vehicle,icon):
       virtualPosition =  self.getVirtualPosition(position = vehicle.position)
       icon.setGeometry(virtualPosition.x - icon.width() / 2,
                        virtualPosition.y - icon.height() / 2, icon.width(), icon.height())

    def moveBus(self,bus,trajectory):
        #Now, we calculate a new trajectory from the current position of the bus

        if self.equalPositions(bus.position,trajectory.destination) == False:
            bus.moving = True
            trajectory = self.createTrajectory(origin = bus.position,destination = trajectory.destination, clockwise = trajectory.direction.isClockwise(),speed = trajectory.speed)['trajectory']
            bus.move(trajectory=trajectory)  # if the bus is already moving there will be a trajectory and direction previously defined
            self.updateVehicleMapPosition(vehicle=bus, icon=bus.icon)

        else:  # if the destination is equal to the origin
            bus.moving = False

    def movePerson(self,person,trajectory,isWalking):
        #Now, we calculate a new trajectory from the current position of the bus
        if self.equalPositions(person.position,trajectory.destination) == False:
            person.moving = True
            trajectory = self.createTrajectory(origin = person.position,destination = trajectory.destination, clockwise = trajectory.direction.isClockwise(),speed = trajectory.speed)['trajectory']
            person.move(trajectory=trajectory,isWalking = isWalking)  # if the bus is already moving there will be a trajectory and direction previously defined
            self.updatePersonMapPosition(person=person, icon=person.icon)

        else: #if the destination is equal to the origin
            person.moving = False

    def updatePersonMapPosition(self,person,icon):
       virtualPosition =  self.getVirtualPosition(position = person.position)
       icon.setGeometry(virtualPosition.x - icon.width / 2,
                        virtualPosition.y - icon.height / 2, icon.width, icon.height)

    def setPositionPerson(self,person, position):
        person.position = position
        self.updatePersonMapPosition(person = person, icon = person.icon)

    # Note that this is not the path the lowest euclidean distance, which is easy to calculate. The geodesic distance depends on the shape of the network and even for the case of a square network is complex.
    def pathDistance(self,origin,destination,clockwise):

        realNetwork = self.realNetwork
        sideOrigin = self.sideDetection(origin)
        sideDestination = self.sideDetection(destination)
        distance = 0
        distanceClockWise = 0

        #We perform the calculation assuming the direction is clockwise. If it is not clockwise, the distance its the total length minus the accumulated distance in clockwise
        #There are 16 possible cases. The combinations between origin in North, West, South, East and the destination in North, West, South, East

        #The following 8 cases has the same calculation (4 when points are in adjacent side of the rectangule and 4 when are in the same side)
        if (sideOrigin == "west" and sideDestination == "north") or (sideOrigin == "north" and sideDestination == "east") \
                or (sideOrigin == "east" and sideDestination == "south") or (sideOrigin == "south" and sideDestination == "west"):
            distanceClockWise = abs(destination.y-origin.y)+abs(destination.x-origin.x)

        if sideOrigin in ["west","northWestCorner","southWestCorner"] and sideDestination in ["east","northEastCorner","southEastCorner"]:
            distanceClockWise = (realNetwork.height-origin.y)+realNetwork.width+(realNetwork.height-destination.y)

        if sideOrigin in ["west","northWestCorner","southWestCorner"] and sideDestination in ["south","southWestCorner","southEastCorner"]:
            distanceClockWise = (realNetwork.height-origin.y)+realNetwork.width+realNetwork.height+(realNetwork.width-destination.x)

        if sideOrigin in ["north","northWestCorner","northEastCorner"] and sideDestination in ["south","southWestCorner","southEastCorner"]:
            distanceClockWise = (realNetwork.width - origin.x) + realNetwork.height + (realNetwork.width - destination.x)

        if sideOrigin in ["north","northWestCorner","northEastCorner"] and sideDestination in ["west","northWestCorner","southWestCorner"]:
            distanceClockWise = (realNetwork.width - origin.x) + realNetwork.height +realNetwork.width+ (destination.y)

        if sideOrigin in ["east","northEastCorner","southEastCorner"] and sideDestination in ["west","northWestCorner","southWestCorner"]:
            distanceClockWise = origin.y + realNetwork.width+destination.y

        if sideOrigin in ["east","northEastCorner","southEastCorner"] and sideDestination in ["north","northWestCorner","northEastCorner"]:
            distanceClockWise = origin.y + realNetwork.width + realNetwork.height + destination.x

        if sideOrigin in ["south","southWestCorner","southEastCorner"] and sideDestination in ["north","northWestCorner","northEastCorner"]:
            distanceClockWise = origin.x + realNetwork.height + destination.x

        if sideOrigin in ["south","southWestCorner","southEastCorner"] and sideDestination in ["east","northEastCorner","southEastCorner"]:
            distanceClockWise = origin.x + realNetwork.height + realNetwork.width + (realNetwork.height-destination.y)

        #These are the cases where the points are in the same segment
        if sideOrigin in ["west","southWestCorner","northWestCorner"] and sideDestination in ["west","southWestCorner","northWestCorner"]:
            if origin.y>destination.y:
                distanceClockWise = (realNetwork.height-origin.y)+realNetwork.width+realNetwork.height+realNetwork.width+destination.y
            else:
                distanceClockWise = destination.y-origin.y

        if sideOrigin in ["north","northWestCorner","northEastCorner"] and sideDestination in ["north","northWestCorner","northEastCorner"]:
            if origin.x > destination.x:
                distanceClockWise = (realNetwork.width - origin.x) + realNetwork.height + realNetwork.width + realNetwork.height + destination.x
            else:
                distanceClockWise = destination.x-origin.x

        if sideOrigin in ["east","northEastCorner","southEastCorner"] and sideDestination in ["east","northEastCorner","southEastCorner"]:
            if origin.y < destination.y:
                distanceClockWise = origin.y + realNetwork.width + realNetwork.height + realNetwork.width + (realNetwork.height-destination.y)
            else:
                distanceClockWise =origin.y-destination.y

        if sideOrigin in ["south","southEastCorner","southWestCorner"] and sideDestination in ["south","southEastCorner","southWestCorner"]:
            if origin.x < destination.x:
                distanceClockWise = origin.x + realNetwork.height + realNetwork.width + realNetwork.height + (realNetwork.width-destination.x)
            else:
                distanceClockWise =origin.x-destination.x

        if clockwise == True:
            distance = distanceClockWise
        else:
            distance = realNetwork.length-distanceClockWise

        return distance

    #Return a vector of positions that are within the network shape and accumulated distance.
    #Speed in metres (unit of distance) per second meanwhile
    #Time interval in seconds
    #Distance: "metres" or units of distane.

    def createTrajectory(self,origin,destination,clockwise,speed):

        timeInterval = self.timeInterval #We fix the same timeinterval for all trajectories

        #Create a copy of the objects to avoid any reference problems if I modify attributes of the object.

        origin = copy.copy(origin)
        destination = copy.copy(destination)
        realNetwork = copy.copy(self.realNetwork)

        positions = []
        #If the origin or the destination are higher than either the width or height of the network, it will make them equal
        if origin.x>realNetwork.width:
            origin.x = realNetwork.width

        if origin.y>realNetwork.height:
            origin.y = realNetwork.height

        #Points: Number of points to divide the shape of the network

        sideOrigin = self.sideDetection(origin)
        accDistance = 0
        accTime = 0
        accOrder = 0
        distance = self.pathDistance(origin=origin,destination=destination,clockwise=clockwise)
        xts = [] #List with states of position-time
        segmentLength = timeInterval*speed
        # clockwise = None

        while accDistance < distance:
            xt = XT(order = accOrder,position = Position(origin.x, origin.y),time = accTime)
            xts.append(xt)

            positions.append({'position':Position(origin.x, origin.y),'accDistance':accDistance})

            if clockwise == True:
                if sideOrigin in ["southWestCorner","west"]: #Bus needs to go North
                    origin.y += segmentLength
                    difference = realNetwork.height-origin.y  #If the position is higher than the limit of the vertical position of the realNetwork, the dif will be lower than 0
                    if difference < 0:
                        origin.x = abs(difference)
                        origin.y = realNetwork.height

                elif sideOrigin in ["northWestCorner", "north"]: #Bus needs to go East
                    origin.x += segmentLength
                    difference = realNetwork.width-origin.x
                    if difference < 0:
                        origin.y = origin.y-abs(difference)
                        origin.x = realNetwork.width

                elif sideOrigin in ["northEastCorner", "east"]: #Bus needs to go South
                    origin.y -= segmentLength
                    difference = origin.y-0
                    if difference < 0:
                        origin.x = origin.x-abs(difference) #the value of y is negative so x position will decease
                        origin.y = 0

                elif sideOrigin in ["southEastCorner", "south"]: #Bus needs to go West
                    origin.x -= segmentLength
                    difference = origin.x-0
                    if difference < 0:
                        origin.y = abs(difference)  # the value of x is negative so y position will increase
                        origin.x = 0

            else: #clockwise == False
                if sideOrigin in ["southWestCorner","south"]: #Bus needs to go east
                    origin.x += segmentLength
                    difference = realNetwork.width - origin.x
                    if difference < 0:
                        origin.y = origin.y + abs(difference)
                        origin.x = realNetwork.width

                elif sideOrigin in ["southEastCorner", "east"]: #Bus needs to go West
                    origin.y += segmentLength
                    difference = realNetwork.height - origin.y
                    if difference < 0:
                        origin.x = origin.x - abs(difference)
                        origin.y = realNetwork.height

                elif sideOrigin in ["northEastCorner", "north"]: #Bus needs to go South
                    origin.x -= segmentLength
                    difference = origin.x-0
                    if difference < 0:
                        origin.y = origin.y-abs(difference)
                        origin.x = 0

                elif sideOrigin in ["northWestCorner", "west"]: #Bus needs to go East
                    origin.y -= segmentLength
                    difference = origin.y-0
                    if difference < 0:
                        origin.x = origin.x + abs(difference)
                        origin.y = 0

            sideOrigin = self.sideDetection(origin)
            accDistance += segmentLength
            accOrder += 1
            accTime += timeInterval

        #Adding the last point (the destination)
        positions.append({'position': destination, 'accDistance': distance})
        xts.append(XT(order = accOrder,position = destination,time = accTime))

        direction = None
        if clockwise == True:
            direction = Direction("clockwise")

        else:
            direction = Direction("counterclockwise")

        trajectory = Trajectory(origin = origin, destination = destination, xts = xts, speed = speed,direction = direction)

        return {'positions':positions, 'xts':xts, 'trajectory':trajectory}

    def isNextPositionAhead(self,trajectory, currentPosition, nextPosition):

        distanceSameDirection = self.pathDistance(origin = currentPosition,destination = nextPosition,clockwise = trajectory.direction.isClockwise())
        distanceOppositeDirection = self.pathDistance(origin = currentPosition,destination = nextPosition, clockwise = not trajectory.direction.isClockwise())

        if distanceSameDirection == 0:
            return None  # This include the case when the currentPosition is the same than the nextPosition

        elif distanceSameDirection < distanceOppositeDirection: #This means poitn B is in a position ahead the trajectory
            return True

        else: # distanceSameDirection > distanceOppositeDirection:
            return False



    #Note that this is not the path the lowest euclidean distance, which is easy to calculate
    def shortestPathTrajectory(self, origin, destination,speed):

        shortestTrajectory = None
        distanceCounterClockwise = self.pathDistance(origin, destination, clockwise=True)
        distanceClockwise = self.pathDistance(origin, destination, clockwise=False)

        if distanceClockwise<distanceCounterClockwise:
            shortestTrajectory = self.createTrajectory(origin, destination, clockwise=True,speed = speed)
            direction = Direction("clockwise")
        else:
            shortestTrajectory = self.createTrajectory(origin, destination, clockwise=False, speed = speed)
            direction = Direction("counterClockwise")

        xts = shortestTrajectory['xts']

        trajectory = Trajectory(origin = origin, destination = destination, direction = direction, xts = xts, speed = speed)

        return trajectory #Return an object of type 'Trajectory'

    # Note that this is not the euclidean distance, which is easy to calculate
    def shortestPathDistance(self, origin, destination):

        distanceCounterClockwise = self.pathDistance(origin, destination, clockwise=True)
        distanceClockwise = self.pathDistance(origin, destination, clockwise=False)

        return min(distanceCounterClockwise,distanceClockwise)


    def calculateTravelTime(self,origin,destination,clockwise,speed):
        return self.pathDistance(origin,destination,clockwise)/speed

    def calculateSpeed(self,origin,destination,clockwise,travelTime):
        return self.pathDistance(origin,destination,clockwise)/travelTime


    # Arrival times of all buses in the network to the bus stops
    def arrivalTimes(self,busStop):

        arrivalTimes = {} #A dictionary containing the id of the buses and the expected arrival times
        for busId in self.realNetwork.buses.keys():
            bus = self.realNetwork.buses[busId]
            arrivalTime = self.travelTime(origin = bus.position,destination = busStop.position,clockwise = bus.clockwise,speed = bus.speed)
            arrivalTimes[bus.id] = arrivalTime

        return arrivalTimes

    def equalPositions(self, positionA, positionB):
        if positionA.x == positionB.x and positionA.y == positionB.y:
            return True
        else:
            return False


    #This function calculate the delay in the bus departure for the targeted waiting time (i.e. calculate the 'delay" to dispatch the bus from its departure terminal).
    # With this delay, the bus will arrive at the bus stop and the passenger will experience the targeted waiting time
    def calculateDispatchingDelay(self,targetedWaitingTime, busRoute, person, busStop):

        distancePersonToStop = self.shortestPathDistance(origin = person.position, destination = busStop.position)
        distanceBusToStop = self.shortestPathDistance(origin = busRoute.departureTerminal.position, destination = busStop.position)

        # Based on the structure of our network, the following equations allows to calculate the delay
        dispathchingDelay = targetedWaitingTime-distanceBusToStop/busRoute.speed + distancePersonToStop/person.walkingSpeed

        return dispathchingDelay

    #Reveal positions of the buses for a given bus route
    def revealBusRoutePosition(self, busRoute):
        for busKey in busRoute.buses.keys():
            busRoute.buses[busKey].icon.show()

    def sideDetection(self, position):
        # First needs to check in what side of the square are both the origin and the destination (North, South, West or East)
        side = None

        if position.x == 0 and position.y == 0:
            side = "southWestCorner"

        elif position.x == self.realNetwork.width and position.y == 0:
            side = "southEastCorner"

        elif position.x == 0 and position.y == self.realNetwork.height:
            side = "northWestCorner"

        elif position.x == self.realNetwork.width and position.y == self.realNetwork.height:
            side = "northEastCorner"

        elif position.x == 0:
            side = "west"

        elif position.x == self.realNetwork.width:
            side = "east"

        elif position.y == self.realNetwork.height:
            side = "north"

        elif position.y == 0:
            side = "south"

        return side


