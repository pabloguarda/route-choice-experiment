from random import * #Library to generate random numbers

#Route id allows to link two bus routes that stops in the same bus stops but has different directions
class BusRoute():
    #Headway are the time intervals between bus arrivals at a given point of the network

    def __init__(self, headway, busStops, maxSpeed, id, routeId, departureTerminal, arrivalTerminal, direction, icon = None):
        self.headway = headway
        self.direction = direction
        self.icon = icon #Icon will be the same for all buses that operate in a given route
        self.maxSpeed = maxSpeed
        self.speed = maxSpeed
        self.busStops = busStops  # Bus stops where buses in the route stop. It is a dictionary where the key is the order of the bus stop, and the value the object of the bus stop
        self.routeId = routeId  # E.g. Red route, blue route
        self.id = id #E.g. 'Red route clockwise' and 'Red route counterclockwise'. Both bus routes will have the routeId 'Red route'
        self.buses = {} #Dictionary where the key is the id of the bus and the value an object type 'bus'
        self.nBuses = 0
        # This are the terminals where the buses start and end their runs (arrival, departure)
        self.departureTerminal = departureTerminal
        self.arrivalTerminal = arrivalTerminal
        # self.nBuses = len(buses)

    #Add a bus in the bus fleet
    def addBus(self,bus):
        # self.buses.append(bus)
        self.buses[bus.id] = bus
        self.nBuses = len(self.buses)
        bus.setIcon(self.icon)  # Add the icon of the route to the bus. I need to make a copy of the icon, otherwise all buses will be referencing the same vehicleIcon object

    def setBusIcon(self,icon):
        self.icon = icon

# What is a stage? Trips consist of one or more stages. A new stage is defined when there is a change in the mode of transport
# Source: https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/457752/nts2014-01.pdf

class TripStage:

    def __init__(self, origin, destination, mode, direction, waitingTime, travelTime, walkingTime, dwellTime, walkingDistance, travelDistance, walkingSpeed, travelSpeed):
        self.origin = origin #The origin of the chain
        self.destination = destination  # The end of the chain
        self.mode = mode #Mode of transportation
        self.direction = direction
        self.waitingTime = waitingTime
        self.travelTime = travelTime
        self.walkingTime = walkingTime
        self.walkingDistance = walkingDistance
        self.travelDistance = travelDistance
        self.walkingSpeed = walkingSpeed
        self.travelSpeed = travelSpeed
        self.dwellTime = dwellTime

# A trip has a set of stages. A new stage is defined when there is a change in the mode of transport

class Trip():

    def __init__(self,tripStages = []):
        self.tripStages = tripStages #List of trip stages

        self.travelTime = self.getTravelTime(tripStages = self.tripStages)
        self.walkingTime = self.getWalkingTime(tripStages = self.tripStages)
        self.waitingTime = self.getWaitingTime(tripStages = self.tripStages)
        self.journeyTime = self.getJourney(tripStages=self.tripStages)
        self.dwellTime = self.getDwellTime(tripStages=self.tripStages)

        self.walkingDistance = self.getWalkingDistance(tripStages = self.tripStages)
        self.travelDistance = self.getTravelDistance(tripStages = self.tripStages)
        self.journeyDistance = self.getJourneyDistance(tripStages=self.tripStages)

        self.travelSpeed = self.getMaxVehicleSpeed(tripStages = self.tripStages)
        self.walkingSpeed = self.getWalkingSpeed(tripStages = self.tripStages)


    def addTripStage(self, tripStage):
        self.tripStages.append(tripStage)

    def getWalkingDistance(self, tripStages):

        walkingDistance = 0
        for tripStage in tripStages:
            walkingDistance += tripStage.walkingDistance
        return walkingDistance


    def getTravelDistance(self, tripStages):
        travelDistance = 0
        for tripStage in tripStages:
            travelDistance += tripStage.travelDistance
        return travelDistance


    def getMaxVehicleSpeed(self, tripStages):
        maxVehicleSpeed = 0
        for tripStage in tripStages:
            if tripStage.mode.id != "walking":
                if tripStage.mode.speed > maxVehicleSpeed:
                    maxVehicleSpeed = tripStage.mode.speed
        return maxVehicleSpeed

    def getWalkingSpeed(self, tripStages):
        walkingSpeed = 0
        for tripStage in tripStages:
            if tripStage.mode.id == "walking":
                walkingSpeed = tripStage.mode.speed

    def getTravelTime(self, tripStages):
        travelTime = 0
        for tripStage in tripStages:
            travelTime += tripStage.travelTime
        return travelTime

    def getWaitingTime(self, tripStages):
        waitingTime = 0
        for tripStage in tripStages:
            waitingTime += tripStage.waitingTime
        return waitingTime

    def getWalkingTime(self, tripStages):
        walkingTime = 0
        for tripStage in tripStages:
            walkingTime += tripStage.walkingTime
        return walkingTime

    def getDwellTime(self, tripStages):
        dwellTime = 0
        for tripStage in tripStages:
            dwellTime += tripStage.dwellTime
        return dwellTime


    def getJourney(self, tripStages):
        journeyTime = 0
        for tripStage in tripStages:
            journeyTime += tripStage.walkingTime + tripStage.travelTime + tripStage.waitingTime  + tripStage.dwellTime
        return journeyTime

    def getJourneyDistance(self, tripStages):
        journeyDistance = 0
        for tripStage in tripStages:
            journeyDistance += tripStage.walkingDistance + tripStage.travelDistance
        return journeyDistance

class Journey:
    def __init__(self, travel, waiting, treatment = None, direction = None):
        self.travel = travel
        self.waiting = waiting

        self.detJourney = None # The journey time is generated when the user execute the method generateJourney()
        self.randJourney = None
        self.journeyTime = None

        self.detTravelTime = None
        self.randTravelTime = None
        self.travelTime = None

        self.detWaitingTime = None
        self.randWaitingTime = None
        self.waitingTime = None

        self.randomWait = None
        self.randomTravel = None

        self.treatment = treatment #Boolean that says whether the journey is the treatment condition
        self.direction = direction #"counterclockwise" or "clockwise"

    def generateJourneyTimes(self, randomWait = True, randomTravel = True):

        self.randomWait = randomWait
        self.randomTravel = randomTravel

        self.waiting.generateWaitingTime(random = randomWait)
        self.detWaitingTime = self.waiting.detWaitingTime
        self.randWaitingTime = self.waiting.randWaitingTime
        self.waitingTime = self.waiting.waitingTime

        self.travel.generateTravelTime(random = randomTravel)
        self.detTravelTime = self.travel.detTravelTime
        self.randTravelTime = self.travel.randTravelTime
        self.travelTime = self.travel.travelTime

        self.detJourneyTime = self.detWaitingTime + self.detTravelTime
        self.randJourneyTime = self.randWaitingTime + self.randTravelTime
        self.journeyTime = self.detJourneyTime + self.randJourneyTime

    def updateJourneyTimes(self):

        self.waiting.generateWaitingTime(random = self.randomWait)
        self.detWaitingTime = self.waiting.detWaitingTime
        self.randWaitingTime = self.waiting.randWaitingTime
        self.waitingTime = self.waiting.waitingTime

        self.travel.generateTravelTime(random = self.randomTravel)
        self.detTravelTime = self.travel.detTravelTime
        self.randTravelTime = self.travel.randTravelTime
        self.travelTime = self.travel.travelTime

        self.detJourneyTime = self.detWaitingTime + self.detTravelTime
        self.randJourneyTime = self.randWaitingTime + self.randTravelTime
        self.journeyTime = self.detJourneyTime + self.randJourneyTime

class Waiting:

    def __init__(self, meanWaitingTime = "", sdWaitingTime = "", minWaitingTime = "", maxWaitingTime=""):
        self.minWaitingTime = minWaitingTime
        self.maxWaitingTime = maxWaitingTime
        self.meanWaitingTime = meanWaitingTime
        self.sdWaitingTime = sdWaitingTime

        if self.minWaitingTime == "":
            self.minWaitingTime = meanWaitingTime

        if self.maxWaitingTime == "":
            self.maxWaitingTime = meanWaitingTime

        if self.sdWaitingTime == "":
            self.sdWaitingTime = 0

        self.detWaitingTime = None  # The waiting time is generated when the user execute the method generateWaitingTime()
        self.randWaitingTime = None #Non-deterministic portion of the waiting time.
        self.waitingTime = None

        self.generateWaitingTime(random=False) #The default is to generate a non-random waiting time

    def generateWaitingTime(self, random=True):

        if random == True:
            self.detWaitingTime = uniform(self.minWaitingTime, self.maxWaitingTime)
            self.randWaitingTime = uniform(0,self.sdWaitingTime)
        else:
            self.detWaitingTime = uniform(self.minWaitingTime, self.maxWaitingTime)
            self.randWaitingTime = 0

        self.waitingTime = self.detWaitingTime + self.randWaitingTime

class Travel:

    def __init__(self, meanTravelTime = "", sdTravelTime = "", minTravelTime = "", maxTravelTime = ""):

        self.minTravelTime = minTravelTime
        self.maxTravelTime = maxTravelTime
        self.meanTravelTime = meanTravelTime
        self.sdTravelTime = sdTravelTime

        if self.minTravelTime == "":
            self.minTravelTime = meanTravelTime

        if self.maxTravelTime == "":
            self.maxTravelTime = meanTravelTime

        if self.sdTravelTime == "":
            self.sdTravelTime = 0

        self.detTravelTime = None #The travel time is generated when the user execute the method generateTravelTime()
        self.randTravelTime = None
        self.travelTime = None

        self.generateTravelTime(random=False)  # The default is to generate a non-random waiting time

    def generateTravelTime(self, random = True):

        if random == True:
            self.detTravelTime = randint(self.minTravelTime, self.maxTravelTime)
            self.randTravelTime = randint(0, self.sdTravelTime)
        else:
            # self.detTravelTime = (self.minTravelTime + self.maxTravelTime)/2
            # self.randTravelTime = 0
            self.detTravelTime = uniform(self.minTravelTime, self.maxTravelTime)
            self.randTravelTime = 0

        self.travelTime = self.detTravelTime + self.randTravelTime


# These two classes are used for the experiments that present alternatives with no variability
class TimeAlternative():
    def __init__(self, waiting, travel):
        self.waitingTime = waiting.waitingTime
        self.travelTime = travel.travelTime
        self.journeyTime = self.waitingTime + self.travelTime

        self.xWaitingTime = self.waitingTime/self.journeyTime
        self.xTravelTime = self.travelTime / self.journeyTime

class TimeChoiceSet():
    def __init__(self, timeAlternatives):
        self.choiceSet = timeAlternatives

    def addTimeAlternative(self,timeChoice):
        self.choiceSet.append(timeChoice)

    def getTimeAlternative(self,index):
        return self.choiceSet[index]


class JourneyProspect:
    def __init__(self, travelProspect, waitingProspect, treatment=None, direction=None):

        self.waitingProspect = waitingProspect
        self.travelProspect = travelProspect


        self.p1 = ""
        self.p2 = ""

        self.journeyTime1 = ""
        self.journeyTime2 = ""

        self.setTimeConsequencesAndProbabilities()

        self.treatment = treatment  # Boolean that says whether the journey is the treatment condition
        self.direction = direction  # "counterclockwise" or "clockwise"

        self.waitingTime  = ""
        self.travelTime = ""
        self.journeyTime = ""

        self.expectedJourneyTime = self.getExpectedJourneyTime()

    def setTimeConsequencesAndProbabilities(self):

        self.journeyTime1 = self.waitingProspect.waitingTime1 + self.travelProspect.travelTime1

        #If the probability of the consequence of the waiting or trvel time prosepcts are equal to 1, then the time2 will be none

        if self.waitingProspect.p1 == 1 and self.travelProspect.p1 == 1:
            self.journeyTime2 = ""
            self.p1 = self.waitingProspect.p1 #The probabilities of waiting and travel are the same and equal to 1

        if self.waitingProspect.p1 == 1 and self.travelProspect.p1 != 1:
            self.journeyTime2 = self.waitingProspect.waitingTime1 + self.travelProspect.travelTime2
            self.p1 = self.travelProspect.p1

        if self.waitingProspect.p1 != 1 and self.travelProspect.p1 == 1:
            self.journeyTime2 = self.waitingProspect.waitingTime2 + self.travelProspect.travelTime1
            self.p1 = self.waitingProspect.p1

        if self.waitingProspect.p1 != 1 and self.travelProspect.p1 != 1:
            self.journeyTime2 = self.waitingProspect.waitingTime2 + self.travelProspect.travelTime2
            self.p1 = self.waitingProspect.p1 #The probabilities of waiting and travel are the same

        self.p2 = 1-self.waitingProspect.p1

    def generateJourneyTimes(self):
        self.waitingProspect.generateWaitingTime()
        self.waitingTime = self.waitingProspect.waitingTime

        self.travelProspect.generateTravelTime()
        self.travelTime = self.travelProspect.travelTime

        self.journeyTime = self.waitingTime + self.travelTime

    def getExpectedJourneyTime(self):
        return self.waitingProspect.expectedWaitingTime + self.travelProspect.expectedTravelTime

    def maxJourneyTime(self):
        return self.waitingProspect.maxWaitingTime() +self.travelProspect.maxTravelTime()

    def minJourneyTime(self):
        return self.waitingProspect.minWaitingTime() + self.travelProspect.minTravelTime()

class WaitingProspect:
    def __init__(self, waitingTime1, p1, waitingTime2 = "", p2 = ""):
        self.waitingTime1 = waitingTime1
        self.waitingTime2 = waitingTime2
        self.p1 = p1
        self.p2 = p2

        if p2 == "":
            self.p2 = 1-self.p1

        self.waitingTime = ""
        self.minWaitingTime = self.getMinWaitingTime()
        self.maxWaitingTime = self.getMaxWaitingTime()
        self.expectedWaitingTime = self.getExpectedWaitingTime()

        # self.generateWaitingTime()

    def getNOutcomes(self):
        if self.waitingTime2 == "":
            return 1
        else:
            return 2

    def getExpectedWaitingTime(self):

        if self.waitingTime2 != "":
            return self.p1*self.waitingTime1+self.p2*self.waitingTime2
        else:
            return self.waitingTime1

    def generateWaitingTime(self):

        randomNumber = uniform(0, 1)

        if randomNumber<=self.p1:
            self.waitingTime = self.waitingTime1

        else:
            self.waitingTime = self.waitingTime2

    def getMaxWaitingTime(self):
        if self.waitingTime2 != "":
            if self.waitingTime1>self.waitingTime2:
                return self.waitingTime1
            else:
                return self.waitingTime2

        else:
            return self.waitingTime1


    def getMinWaitingTime(self):
        if self.waitingTime2 != "":
            if self.getMaxWaitingTime == self.waitingTime1:
                return self.waitingTime2

            else:
                return self.waitingTime1
        else:
            return self.waitingTime1

class TravelProspect:
    def __init__(self, travelTime1, p1, travelTime2 = "", p2=""):
        self.travelTime1 = travelTime1
        self.travelTime2 = travelTime2
        self.p1 = p1
        self.p2 = p2

        if p2 == "":
            self.p2 = 1 - self.p1

        self.travelTime = ""
        self.minTravelTime = self.getMinTravelTime()
        self.maxTravelTime = self.getMaxTravelTime()
        self.expectedTravelTime = self.getExpectedTravelTime()

        # self.generateTravelTime()


    def getNOutcomes(self):
        if self.travelTime2 == "":
            return 1
        else:
            return 2

    def getExpectedTravelTime(self):
        if self.travelTime2 != "":
            return self.p1*self.travelTime1+self.p2*self.travelTime2
        else:
            return self.travelTime1

    def generateTravelTime(self):

        randomNumber = uniform(0, 1)

        if randomNumber <= self.p1:
            self.travelTime = self.travelTime1

        else:
            self.travelTime = self.travelTime2

    def getMaxTravelTime(self):

        if self.travelTime2 != "":
            if self.travelTime1 > self.travelTime2:
                return self.travelTime1
            else:
                return self.travelTime2

        else:
            return self.travelTime1

    def getMinTravelTime(self):

        if self.travelTime2 != "":
            if self.getMaxTravelTime() == self.travelTime1:
                return self.travelTime2

            else:
                return self.travelTime1
        else:
            return self.travelTime1


# These two classes are used for the experiments that present alternatives with variability
class TimeProspect:
    def __init__(self, waitingProspect, travelProspect):

        self.waitingProspect = waitingProspect
        self.travelProspect = travelProspect
        self.journeyProspect = JourneyProspect(waitingProspect= self.waitingProspect,travelProspect = self.travelProspect)

        self.expectedWaitingTime = self.journeyProspect.waitingProspect.expectedWaitingTime
        self.expectedTravelTime = self.journeyProspect.travelProspect.expectedTravelTime
        self.expectedJourneyTime = self.journeyProspect.expectedJourneyTime

        self.journeys = [] #List of possible journeys that can be generated with this prospect

    #Generate all possible outcomes of the prospect
    def getTimeConsequences(self):

        journeys = []

        if self.waitingProspect.getNOutcomes() == 1:
            if self.travelProspect.getNOutcomes() == 1:
                journeys.append(Journey(waiting = Waiting(meanWaitingTime=self.waitingProspect.expectedWaitingTime), travel = Travel(meanTravelTime=self.travelProspect.expectedTravelTime)))

            if self.travelProspect.getNOutcomes() == 2:
                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.expectedWaitingTime)
                                             , travel = Travel(meanTravelTime=self.travelProspect.minTravelTime)))
                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.expectedWaitingTime),
                                   travel=Travel(meanTravelTime=self.travelProspect.maxTravelTime)))

        if self.waitingProspect.getNOutcomes() == 2:
            if self.travelProspect.getNOutcomes() == 1:
                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.minWaitingTime)
                                             , travel = Travel(meanTravelTime=self.travelProspect.expectedTravelTime)))

                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.maxWaitingTime),
                                   travel=Travel(meanTravelTime=self.travelProspect.expectedTravelTime)))


            if self.travelProspect.getNOutcomes() == 2:
                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.minWaitingTime),
                                   travel=Travel(meanTravelTime=self.travelProspect.minTravelTime)))
                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.maxWaitingTime),
                                   travel=Travel(meanTravelTime=self.travelProspect.maxTravelTime)))
                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.minWaitingTime),
                                   travel=Travel(meanTravelTime=self.travelProspect.minTravelTime)))
                journeys.append(Journey(waiting=Waiting(meanWaitingTime=self.waitingProspect.maxWaitingTime),
                                   travel=Travel(meanTravelTime=self.travelProspect.maxTravelTime)))




        return journeys

class TimeProspectSet:
    def __init__(self, timeProspects):
        self.prospectSet = timeProspects

    def addTimeProspect(self, timeProspect):
        self.prospectSet.append(timeProspect)

    def getTimeProspect(self, index):
        return self.prospectSet[index]

class Speed:
    def __init__(self, mean, sd, distribution):
        self.mean = mean
        self.sd = sd
        self.distribution = distribution

    # This method pick a certain value of speed from a normal distribution
    def NormalSpeed(self):
        a = 0 #Complete this function

    #Return the mean value of the speed
    def MeanSpeed(self):
        return self.mean

class Choice:
    def __init__(self, waitingTime, varWaitingTime, meanTravelTime, varTravelTime):
        self.waitingTime = waitingTime
        self.varWaitingTime = varWaitingTime
        self.travelTime = meanTravelTime
        self.varTravelTime = varTravelTime

