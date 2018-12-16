#This class contains all attributes related to the participant, which are asked in the Demographic window.
#The constructor of the class Trial received a participant, as each Trial contains information on the participant itself but also about the urn chosen, picked marble, etc.

from Scripts.Journey import * #TimeSpace
from collections import OrderedDict
from Scripts.Functions import * #Import py file with my own functions

class Participant:

    def __init__(self, id, startDate, startTime
                 , name = None, lastName = None, age = None, gender = None, educationLevel= None, countryOfResidence= None):

        self.id = id
        self.endingTime = None #Time when participant finishes the experiment
        self.startTime = startTime #Time when the participant started the experiment
        self.startDate= startDate  # Time when the participant started the experiment
        self.computerId = None
        self.experimentalSession = None
        self.age = age
        self.name = name
        self.lastName = lastName
        self.gender = gender
        self.educationLevel = educationLevel
        self.countryOfResidence = countryOfResidence
        self.cityOfResidence = None

        #Trips per week
        self.busTripsPerWeek = None
        self.metroTripsPerWeek = None
        self.carTripsPerWeek = None
        self.bikeTripsPerWeek = None

        #Proxies for income
        self.familyMonthlyIncome = None
        self.neighbourhood = None #Municipality for Chileans, Neighbourhood in London
        self.ownCar = None


        self.trips = [] #Each participant holds a list with trips

        #Object with information on travel behaviour
        self.travelBehaviourInformation = None
        # Object with experiment debrief responses
        self.experimentDebriefInformation = None

    def setTravelBehaviourInformation(self,travelBehaviourInformation):
        self.travelBehaviourInformation = travelBehaviourInformation

    def setExperimentDebriefInformation(self,experimentDebriefInformation):
        self.experimentDebriefInformation = experimentDebriefInformation

    def setComputerId(self,computerId):
        self.computerId = computerId

    def setExperimentalSession(self,experimentalSession):
        self.experimentalSession = experimentalSession

    def setEndingTime(self,endingTime):
        self.endingTime = endingTime

    def setAge(self, age):
        self.age = age

    def setGender(self, gender):
        self.gender = gender

    def setEducationLevel(self, educationLevel):
        self.educationLevel = educationLevel

    def setCountryOfResidence(self,countryOfResidence):
        self.countryOfResidence = countryOfResidence
        self.setCityOfResidence(countryOfResidence = countryOfResidence)

    def setCityOfResidence(self,countryOfResidence):

        if countryOfResidence == "Chile":
            self.cityOfResidence = "Santiago"

        if countryOfResidence == "UK":
            self.cityOfResidence = "London"

    def addTrip(self, trip):
        self.trips.add(trip)

class TravelBehaviourInformation:
    def __init__(self,filePath, participantId
                 , originPlace, otherOriginPlace, originBorough, otherOriginBorough
                 , destinationPlace, otherDestinationPlace,destinationBorough, otherDestinationBorough
                 , busRoute, tripsPerWeekBuses,tripsPerWeekMostFreqBusRoute
                 , departureTime, waitingTime,inVehicleTime, walkingTime, journeyTime, realTimeInformation
                 , realWaitingTimeImportance, realWaitingTimeReliabilityImportance
                 , realInVehicleTimeImportance, realInVehicleTimeReliabilityImportance
                 , realJourneyTimeImportance):

        # Participant id
        self.participantId=participantId

        # File path
        self.filePath = filePath

        # Questions Page 1
        self.tripsPerWeekBuses = tripsPerWeekBuses
        self.departureTime = departureTime
        self.waitingTime = waitingTime
        self.inVehicleTime = inVehicleTime
        self.walkingTime = walkingTime
        self.journeyTime = journeyTime
        self.realTimeInformation = realTimeInformation

        #Questions Page 2
        self.originPlace = originPlace
        self.otherOriginPlace = otherOriginPlace
        self.originBorough = originBorough
        self.otherOriginBorough = otherOriginBorough
        self.destinationPlace = destinationPlace
        self.otherDestinationPlace = otherDestinationPlace
        self.destinationBorough = destinationBorough
        self.otherDestinationBorough = otherDestinationBorough
        self.busRoute = busRoute
        self.tripsPerWeekMostFreqBusRoute = tripsPerWeekMostFreqBusRoute

        # Questions Page 3 (Evaluation about time attributes with slider bars)
        self.realWaitingTimeImportance = realWaitingTimeImportance
        self.realWaitingTimeReliabilityImportance = realWaitingTimeReliabilityImportance
        self.realInVehicleTimeImportance = realInVehicleTimeImportance
        self.realInVehicleTimeReliabilityImportance = realInVehicleTimeReliabilityImportance
        self.realJourneyTimeImportance = realJourneyTimeImportance

    def createLineTravelBehaviourInformationCsv(self, colLabels=False):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        dictCsv = OrderedDict(
                [('participantId', self.participantId)

                , ('originPlace', self.originPlace)
                , ('otherOriginPlace', self.otherOriginPlace)
                , ('originBorough', self.originBorough)
                , ('otherOriginBorough', self.otherOriginBorough)

                , ('destinationPlace', self.destinationPlace)
                , ('otherDestinationPlace', self.otherDestinationPlace)
                , ('destinationBorough', self.destinationBorough)
                , ('otherDestinationBorough', self.otherDestinationBorough)

                , ('busRoute', self.busRoute)
                , ('tripsPerWeekBuses', self.tripsPerWeekBuses)

                , ('departureTime', self.departureTime)
                , ('walkingTime', self.walkingTime)
                , ('waitingTime', self.waitingTime)
                , ('inVehicleTime', self.inVehicleTime)
                , ('journeyTime', self.journeyTime)
                , ('realTimeInformation', self.realTimeInformation)

                , ('tripsPerWeekMostFreqBusRoute', self.tripsPerWeekMostFreqBusRoute)

                , ('realWaitingTimeImportance', self.realWaitingTimeImportance)
                , ('realWaitingTimeReliabilityImportance', self.realWaitingTimeReliabilityImportance)
                , ('realInVehicleTimeImportance', self.realInVehicleTimeImportance)
                , ('realInVehicleTimeReliabilityImportance', self.realInVehicleTimeReliabilityImportance)
                , ('realJourneyTimeImportance', self.realJourneyTimeImportance)
             ])

        # This is helpful to define the order in which the columns will be printed in the file
        # self.orderAttributesCsv = ['age', 'gender','eduLevel']

        if not colLabels:
            valuesCsv = []
            for attribute in dictCsv.keys():
                valuesCsv.append(dictCsv[attribute])

            return valuesCsv

        else:
            return list(dictCsv.keys())

    def writeTravelBehaviourInformationCsv(self):
        fileExperiment = open(self.filePath, 'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = self.createLineTravelBehaviourInformationCsv(colLabels=True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileTravelBehaviourResponses = open(self.filePath, 'a')
            fileTravelBehaviourResponses.write(lineFormattedCsv)
            fileTravelBehaviourResponses.close()

            self.writeTravelBehaviourInformationCsv()

        else:
            lineCsv = self.createLineTravelBehaviourInformationCsv(colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileTravelBehaviourResponses = open(self.filePath, 'a')
            fileTravelBehaviourResponses.write(lineFormattedCsv)
            fileTravelBehaviourResponses.close()

class ExperimentDebriefInformation:
    def __init__(self, filePath, participantId
                 , experiencedExperimentTimeCounting
                 , experiencedExperimentIdentificationLevel
                 , descriptiveExperimentIdentificationLevel
                 , experiencedExperimentWalkingTime,experiencedExperimentWaitingTime
                 , experiencedExperimentInVehicleTime, experiencedExperimentJourneyTime
                 , experiencedExperimentOpenQuestion
                 # , descriptiveExperimentOpenQuestion
                 ):

        # , experiencedExperimentWaitingTimeImportance, experiencedExperimentWaitingTimeReliabilityImportance
        # , experiencedExperimentInVehicleTimeImportance, experiencedExperimentInVehicleTimeReliabilityImportance
        # , experiencedExperimentJourneyTimeImportance
        # , descriptiveExperimentWaitingTimeImportance, descriptiveExperimentWaitingTimeReliabilityImportance
        # , descriptiveExperimentInVehicleTimeImportance, descriptiveExperimentInVehicleTimeReliabilityImportance
        # , descriptiveExperimentJourneyTimeImportance

        #Participant id
        self.participantId = participantId

        #File path
        self.filePath = filePath

        #Questions Pages 1
        self.experiencedExperimentIdentificationLevel = experiencedExperimentIdentificationLevel
        self.descriptiveExperimentIdentificationLevel = descriptiveExperimentIdentificationLevel

        # #Questions aboout the experienced experiment
        # self.experiencedExperimentWaitingTimeImportance = experiencedExperimentWaitingTimeImportance
        # self.experiencedExperimentWaitingTimeReliabilityImportance = experiencedExperimentWaitingTimeReliabilityImportance
        # self.experiencedExperimentInVehicleTimeImportance = experiencedExperimentInVehicleTimeImportance
        # self.experiencedExperimentInVehicleTimeReliabilityImportance = experiencedExperimentInVehicleTimeReliabilityImportance
        # self.experiencedExperimentJourneyTimeImportance = experiencedExperimentJourneyTimeImportance
        #
        # #Questions about the descriptive Experiment
        # self.descriptiveExperimentWaitingTimeImportance = descriptiveExperimentWaitingTimeImportance
        # self.descriptiveExperimentWaitingTimeReliabilityImportance = descriptiveExperimentWaitingTimeReliabilityImportance
        # self.descriptiveExperimentInVehicleTimeImportance = descriptiveExperimentInVehicleTimeImportance
        # self.descriptiveExperimentInVehicleTimeReliabilityImportance = descriptiveExperimentInVehicleTimeReliabilityImportance
        # self.descriptiveExperimentJourneyTimeImportance = descriptiveExperimentJourneyTimeImportance

        #General questions (second page)
        self.experiencedExperimentTimeCounting = experiencedExperimentTimeCounting
        self.experiencedExperimentWalkingTime = experiencedExperimentWalkingTime
        self.experiencedExperimentWaitingTime = experiencedExperimentWaitingTime
        self.experiencedExperimentInVehicleTime = experiencedExperimentInVehicleTime
        self.experiencedExperimentJourneyTime = experiencedExperimentJourneyTime

        self.experiencedExperimentOpenQuestion = experiencedExperimentOpenQuestion
        # self.descriptiveExperimentOpenQuestion = descriptiveExperimentOpenQuestion

    def writeTravelBehaviourInformationCsv(self):

        fileExperiment = open(self.filePath, 'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = self.createLineExperimentDebriefInformationCsv(colLabels = True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileExperimentDebriefResponses = open(self.filePath, 'a')
            fileExperimentDebriefResponses.write(lineFormattedCsv)
            fileExperimentDebriefResponses.close()

            self.writeExperimentDebriefInformationCsv()

        else:
            lineCsv = self.createLineExperimentDebriefInformationCsv(colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileExperimentDebriefResponses = open(self.filePath, 'a')
            fileExperimentDebriefResponses.write(lineFormattedCsv)
            fileExperimentDebriefResponses.close()

    def createLineExperimentDebriefInformationCsv(self, colLabels=False):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        dictCsv = OrderedDict(
                [('participantId', self.participantId)

                    , ('experiencedExperimentIdentificationLevel', self.experiencedExperimentIdentificationLevel)
                    , ('descriptiveExperimentIdentificationLevel', self.descriptiveExperimentIdentificationLevel)

                # , ('experiencedExperimentWaitingTimeImportance', self.experiencedExperimentWaitingTimeImportance)
                # , ('experiencedExperimentWaitingTimeReliabilityImportance', self.experiencedExperimentWaitingTimeReliabilityImportance)
                # , ('experiencedExperimentInVehicleTimeImportance', self.experiencedExperimentInVehicleTimeImportance)
                # , ('experiencedExperimentInVehicleTimeReliabilityImportance', self.experiencedExperimentInVehicleTimeReliabilityImportance)
                # , ('experiencedExperimentJourneyTimeImportance', self.experiencedExperimentJourneyTimeImportance)
                #
                # , ('descriptiveExperimentWaitingTimeImportance', self.descriptiveExperimentWaitingTimeImportance)
                # , ('descriptiveExperimentWaitingTimeReliabilityImportance', self.descriptiveExperimentWaitingTimeReliabilityImportance)
                # , ('descriptiveExperimentInVehicleTimeImportance', self.descriptiveExperimentInVehicleTimeImportance)
                # , ('descriptiveExperimentInVehicleTimeReliabilityImportance', self.descriptiveExperimentInVehicleTimeReliabilityImportance)
                # , ('descriptiveExperimentJourneyTimeImportance', self.descriptiveExperimentJourneyTimeImportance)

                , ('experiencedExperimentTimeCounting', self.experiencedExperimentTimeCounting)
                    , ('experiencedExperimentWalkingTime', self.experiencedExperimentWalkingTime)
                    , ('experiencedExperimentWaitingTime', self.experiencedExperimentWaitingTime)
                    , ('experiencedExperimentInVehicleTime', self.experiencedExperimentInVehicleTime)
                    , ('experiencedExperimentJourneyTime', self.experiencedExperimentJourneyTime)

                , ('experiencedExperimentOpenQuestion', self.experiencedExperimentOpenQuestion) #It will be written in a different file
                # , ('descriptiveExperimentOpenQuestion', self.descriptiveExperimentOpenQuestion)

             ])

        # This is helpful to define the order in which the columns will be printed in the file
        # self.orderAttributesCsv = ['age', 'gender','eduLevel']

        if not colLabels:
            valuesCsv = []
            for attribute in dictCsv.keys():
                valuesCsv.append(dictCsv[attribute])

            return valuesCsv

        else:
            return list(dictCsv.keys())

    def writeExperimentDebriefInformationCsv(self):

        fileExperiment = open(self.filePath, 'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = self.createLineExperimentDebriefInformationCsv(colLabels = True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileExperimentDebriefResponses = open(self.filePath, 'a')
            fileExperimentDebriefResponses.write(lineFormattedCsv)
            fileExperimentDebriefResponses.close()

            self.writeExperimentDebriefInformationCsv()

        else:
            lineCsv = self.createLineExperimentDebriefInformationCsv(colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileExperimentDebriefResponses = open(self.filePath, 'a')
            fileExperimentDebriefResponses.write(lineFormattedCsv)
            fileExperimentDebriefResponses.close()

    # def writeExperimentDebriefExperiencedOpenQuestion(self):
