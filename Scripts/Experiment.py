import copy
from collections import OrderedDict
from os import listdir # This library has some functions to read the list of files names in a folder

from Scripts.Functions import * #Import py file with my own functions
from Scripts.Journey import *
from Scripts.Participant import Participant #Import class 'Participant'


# **********************************************  Class that control the experiment  ********************************************************** #

#This class contains most of the methods used for running the experiment.

class MainExperiment:

    def __init__(self,currentParticipant, journeyLengthConditions, nameFolderResponses, nameFolderExperimentDescriptions,
                 nameFolderExperiments, languageCondition, descriptiveExperimentCondition, simulatedExperimentCondition
                 , fontFactor, fontLetter, variableWaitingTimer):
        # ,nMarblesConditions,urnA,urnB,prize,colorPrize,randomColor,experimentId = ""):


        self.languageCondition =languageCondition
        self.descriptiveExperimentCondition = descriptiveExperimentCondition
        self.simulatedExperimentCondition = simulatedExperimentCondition
        self.variableWaitingTimer = variableWaitingTimer #True if the counter for waiting time decrease second by second

        # self.csvExperiment = csvExperiment #This should be a file summarizing the results of the other experiments.
        # self.experimentId = experimentId

        self.currentParticipant = currentParticipant

        #Experiment Stages
        self.nStages = 4 #Learning, Decision, Consequences, Confirmation


        self.experiments = [] #List with all the experiments
        self.experiments0 = []  # List with all experiments from Block 1
        self.experiments1 = [] #List with all experiments from Block 1
        self.experiments2 = []#List with all experiments from Block 2
        self.experiments3 = [] #List with all experiments from Block 3
        self.experiments4 = [] #List with all experiments from Block 4

        # self.experiment1 = None
        # self.experiment2 = None
        # self.experiment3 = None
        # self.experiment4 = None

        #Parameters for the size of the elements in the screen
        self.fontFactor = fontFactor
        self.fontLetter = fontLetter


        #Counter to keep track of the current decision problem
        self.nDecisionProblem = 0
        self.nBlockDecisionProblem = 0

        # self.experiments1
        self.currentExperiment = None
        self.currentTrial = None
        # self.nLearningTrials = nLearningTrials

        #Files' paths
        self.nameFolderResponses = nameFolderResponses
        self.nameFolderExperimentDescriptions = nameFolderExperimentDescriptions
        self.nameFolderExperiments = nameFolderExperiments

        #Participant Files
        self.pathParticipantInformation = self.nameFolderResponses + "/" + "Participant" + str(
            self.currentParticipant.id) + ".csv"

        self.pathTravelBehaviourInformation = self.nameFolderResponses + "/" + "TravelBehaviourInformation" + ".csv"

        self.pathExperimentDebriefInformation = self.nameFolderResponses + "/" + "ExperimentDebriefInformation" + ".csv"

        self.createParticipantFiles(participant=self.currentParticipant)

        #Experiment Response FIles
        self.pathAllExperimentsSimulatedLearningResponses = self.nameFolderResponses + "/" + "ExperimentsSimulatedLearningResponses" + ".csv"
        self.pathAllExperimentsSimulatedChoiceResponses = self.nameFolderResponses + "/" + "ExperimentsSimulatedChoiceResponses" + ".csv"
        self.pathAllExperimentsDescriptiveLearningResponses = self.nameFolderResponses + "/" + "ExperimentsDescriptiveLearningResponses" + ".csv"
        self.pathAllExperimentsDescriptiveChoiceResponses = self.nameFolderResponses + "/" + "ExperimentsDescriptiveChoiceResponses" + ".csv"
        self.pathAllExperimentsReactionTimeResponses = self.nameFolderResponses + "/" + "ExperimentsReactionTimeResponses" + ".csv"

        #Counter for the number of the current trial
        # self.nTrial = 1

        #optional attributes
        self.journeyLengthConditions = journeyLengthConditions #conditions is a list that contains the journey lengths used in each condition
        self.nConditions = len(self.journeyLengthConditions) #Number of conditions in the experiment
        # self.participant = None

        #Attributes to be printed in each file
        self.simulatedLearningAttributesCsv = []
        self.simulatedChoiceAttributesCsv = []
        self.descriptiveLearningAttributesCsv = []
        self.descriptiveChoiceAttributesCsv = []
        self.reactionTimeAttributesCsv = []

        #File with condition
        self.existingConditionsAllExperimentsFile = True
        self.existingConditionsExperiment1File = True
        self.existingConditionsExperiment2File = True
        self.existingConditionsExperiment3File = True

        self.pathFileAllExperimentalConditions = self.nameFolderExperiments + "/" + "ExperimentConditions.csv"


    def createLineReactionTimeResponsesCsv(self,participantId, computerId, experimentCountry, experimentalSession,dp, blockDp, order, blockOrder
                                           , experimentBlock, experimentType, experimentalCondition,experimentStage
                                           ,startingTime,endingTime, colLabels=False):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        FMT = '%H%M%S'
        duration =  datetime.strptime(endingTime, FMT) - datetime.strptime(startingTime, FMT)

        dictCsv = OrderedDict(
                [('participantId', participantId)
                , ('expSession',experimentalSession)
                , ('computerId',computerId)
                , ('country', experimentCountry)
                , ('experimentType', experimentType)
                , ('experimentalCondition', experimentalCondition)
                , ('experimentStage', experimentStage)
                , ('experimentBlock', experimentBlock)

                , ('dp', dp)
                , ('blockDp', blockDp)
                , ('order', order)
                , ('blockOrder', blockOrder)

                , ('startingTime', startingTime)
                , ('endingTime', endingTime)
                , ('duration', duration)
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

    def writeReactionTimeResponse(self,participantId, computerId, experimentCountry, experimentalSession
                                  , experimentBlock,experimentalCondition, experimentType,experimentStage
                                  , dp, blockDp, order, blockOrder
                                  ,startingTime,endingTime):

        fileExperiment = open(self.pathAllExperimentsReactionTimeResponses, 'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = self.createLineReactionTimeResponsesCsv(participantId = participantId, computerId = computerId
                                                              , experimentCountry = experimentCountry
                                                              , experimentalSession = experimentalSession
                                                              , experimentBlock = experimentBlock
                                                              , experimentalCondition=experimentalCondition
                                                              , experimentType=experimentType,experimentStage=experimentStage
                                                              , dp=dp, blockDp=blockDp, order=order, blockOrder = blockOrder
                                                              ,startingTime=startingTime,endingTime= endingTime,colLabels=True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileReactionTimeResponses = open(self.pathAllExperimentsReactionTimeResponses, 'a')
            fileReactionTimeResponses.write(lineFormattedCsv)
            fileReactionTimeResponses.close()

            self.writeReactionTimeResponse(participantId = participantId, computerId = computerId
                                                              , experimentCountry=experimentCountry
                                                              , experimentalSession = experimentalSession
                                                              , experimentBlock = experimentBlock
                                                              , experimentalCondition=experimentalCondition
                                                              , experimentType=experimentType,experimentStage=experimentStage
                                                              , dp=dp, blockDp=blockDp, order=order, blockOrder = blockOrder
                                                              , startingTime=startingTime,endingTime= endingTime)

        else:
            lineCsv = self.createLineReactionTimeResponsesCsv(participantId = participantId, computerId = computerId
                                                              , experimentCountry=experimentCountry
                                                              , experimentalSession=experimentalSession
                                                              , experimentBlock=experimentBlock
                                                              , experimentalCondition=experimentalCondition
                                                              , experimentType=experimentType,experimentStage=experimentStage
                                                              , dp=dp, blockDp=blockDp, order=order, blockOrder = blockOrder
                                                              , startingTime=startingTime,endingTime= endingTime, colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileReactionTimeResponses = open(self.pathAllExperimentsReactionTimeResponses, 'a')
            fileReactionTimeResponses.write(lineFormattedCsv)
            fileReactionTimeResponses.close()


    def writeLineParticipantFile(self,label,value):

        fileParticipantInformation = open(self.pathParticipantInformation, 'a')

        fileParticipantInformation.write(printCsvLine([label, str(value)]))

        fileParticipantInformation.close()

    def createParticipantFiles(self, participant):

        # Create file for the participant
        fileParticipantInformation = open(self.pathParticipantInformation, 'w')

        self.writeLineParticipantFile(label = "StartDate", value = participant.startDate)
        self.writeLineParticipantFile(label="StartTime", value=participant.startTime)
        self.writeLineParticipantFile(label="ParticipantId", value=participant.id)
        self.writeLineParticipantFile(label="ParticipantName", value=participant.name)
        self.writeLineParticipantFile(label="ParticipantLastName", value=participant.lastName)
        self.writeLineParticipantFile(label="ComputerId", value=participant.computerId)
        self.writeLineParticipantFile(label="ExperimentalSession", value=participant.experimentalSession)
        self.writeLineParticipantFile(label="ExperiencedCondition", value=self.simulatedExperimentCondition)
        self.writeLineParticipantFile(label="DescriptiveCondition", value=self.descriptiveExperimentCondition)

        fileParticipantInformation.close()

        #Travel Behaviour information
        fileTravelBehaviourInformation = open(self.pathTravelBehaviourInformation, 'w')
        fileTravelBehaviourInformation.close()

        #Experiment Debrief Information
        fileExperimentDebriefInformation = open(self.pathExperimentDebriefInformation, 'w')
        fileExperimentDebriefInformation.close()

    def getExperimentList(self,expType):

        if expType == 0:
            return self.experiments0

        if expType == 1:
            return self.experiments1

        elif expType == 2:
            return self.experiments2

        elif expType == 3:
            return self.experiments3

        elif expType == 4:
            return self.experiments4

        else:
            return self.experiments

    def getExperiment(self,experimentId, descriptive, expType = None, random = True):

        if expType is not None:
            experimentsList = self.getExperimentList(expType)

        else: #If a specific epxierment type is not specified, then the experiment returned may correspond to any block.
            experimentsList = self.experiments

        if expType != 0:

            for experiment in experimentsList:
                if descriptive == False:
                    if random == False:
                        if experiment.id == experimentId:
                            return experiment
                    else:
                        if experiment.orderId == experimentId:
                            return experiment
                else:
                    if random == False:
                        if experiment.id == experimentId:
                            return experiment
                    else:
                        if experiment.descriptionOrderId == experimentId:
                            return experiment

        else:
            return experimentsList[0]

    def setNDecisionProblem(self):

        experimentsList = self.getExperimentList(expType = "all")

        for experiment in experimentsList:

            # if experiment.expType == 0:
            #     experiment.dp

            if experiment.expType == 1:
                experiment.dp = experiment.id

            if experiment.expType == 2:
                experiment.dp = experiment.id + len(self.getExperimentList(expType=1))

            if experiment.expType == 3:
                experiment.dp = experiment.id \
                                        + len(self.getExperimentList(expType=1)) \
                                        + len(self.getExperimentList(expType=2))

            experiment.absoluteDp = experiment.dp

    def setAbsoluteOrderIds(self, descriptive, mode):

        if  descriptive == False:

            if mode == "block": #Randomization within the experimental blocks
                for expType in [1, 2, 3]:
                    experimentsList = self.getExperimentList(expType)

                    if expType == 1:
                        for experiment in experimentsList:
                            experiment.simulationAbsoluteOrderId = experiment.simulationOrderId

                    if expType == 2:
                        for experiment in experimentsList:
                            experiment.simulationAbsoluteOrderId = experiment.simulationOrderId + len(self.getExperimentList(expType=1))

                    if expType == 3:
                        for experiment in experimentsList:
                            experiment.simulationAbsoluteOrderId = experiment.simulationOrderId \
                                                 + len(self.getExperimentList(expType=1))\
                                                 + len(self.getExperimentList(expType=2))

        if descriptive == True:

            completed = False

            # if mode != "block":  # Randomization within the experimental blocks
            #     for expType in [1, 2, 3]:
            #         experimentsList = self.getExperimentList(expType)
            #
            #         if expType == 1:
            #             for experiment in experimentsList:
            #                 experiment.simulationAbsoluteOrderId = experiment.simulationOrderId
            #
            #         if expType == 2:
            #             for experiment in experimentsList:
            #                 experiment.simulationAbsoluteOrderId = experiment.simulationOrderId + len(
            #                     self.getExperimentList(expType=1))
            #
            #         if expType == 3:
            #             for experiment in experimentsList:
            #                 experiment.simulationAbsoluteOrderId = experiment.simulationOrderId \
            #                                                        + len(self.getExperimentList(expType=1)) \
            #                                                        + len(self.getExperimentList(expType=2))

    def setOrderIds(self, descriptive, mode):

        if mode == "block": #Randomization within the experimental blocks
            for expType in [1, 2, 3]:
                self.setOrderByExperimentBlock(expType=expType)
                experimentsList = self.getExperimentList(expType)

                if expType == 1:
                    for experiment in experimentsList:
                        experiment.tempId = experiment.orderBlockId

                if expType == 2:
                    for experiment in experimentsList:
                        experiment.tempId = experiment.orderBlockId + len(self.getExperimentList(expType=1))

                if expType == 3:
                    for experiment in experimentsList:
                        experiment.tempId = experiment.orderBlockId \
                                             + len(self.getExperimentList(expType=1))\
                                             + len(self.getExperimentList(expType=2))

        if mode == "all":  # Randomization within all the experimental blocks
            self.setOrderExperimentBlocks(experimentsList = self.experiments)

        experimentsList = self.getExperimentList(expType="all")

        if not descriptive:
            for experiment in experimentsList:
                experiment.simulationOrderId = experiment.orderId

        else:
            for experiment in experimentsList:
                experiment.descriptionOrderId = experiment.orderId

    def setOrderByExperimentBlock(self,expType):
        # if mode == "block":
        experimentsList = self.getExperimentList(expType)
        randomNumbers = sample(range(1, len(experimentsList)+1), len(experimentsList))

        for number,experiment in zip(randomNumbers,experimentsList):
            experiment.orderBlockId = number
            experiment.orderId = experiment.orderBlockId

    def setOrderExperimentBlocks(self,experimentsList):

        randomNumbers = sample(range(1, len(experimentsList) + 1), len(experimentsList))

        for number,experiment in zip(randomNumbers,experimentsList):
            experiment.orderId = number

    def nExperiments(self):
        return int(len(self.experiments1)+len(self.experiments2)+len(self.experiments3))

    def randomization(self,conditions):
        #Receive an array of conditions (e.g. strings) and return the name of a random condition:
        randomization = randint(0, len(conditions)-1)
        return conditions[randomization]

    #This setup the parameters of all experiments (I can reduce this method removing all conditionals for the type of experiment
    def setup(self, experiment, typeTrials):

        #Randomization of the treatment and contro routes ( "counterclockwise", "clockwise")
        experiment.treatmentDirection = self.randomization(conditions=["counterclockwise", "clockwise"])

        #Randomization of the color of the bus shown in the treatment route (red or blue)
        experiment.treatmentColor = self.randomization(conditions=["red", "blue"])

        #Randomization of the origin and destination of the trip
        experiment.randomOrigin = self.randomization(conditions=["west", "east"])
        experiment.randomDestination = None

        #Randomization of descriptive route
        treatmentDescriptiveOption= self.randomization(conditions=["A", "B"])
        experiment.treatmentDescriptiveOption = treatmentDescriptiveOption

        if experiment.randomOrigin == "west":
            experiment.randomDestination = "east"
        else:
            experiment.randomDestination = "west"

        #Randomization mode of transportation
        experiment.randomMode = self.randomization(conditions=["bus", "metro"])

        experiment.pathExperimentSimulatedLearningResponses = self.nameFolderResponses + "/" + experiment.csvSimulatedLearningResponses
        experiment.pathExperimentSimulatedChoiceResponses = self.nameFolderResponses + "/" + experiment.csvSimulatedChoiceResponses
        experiment.pathExperimentDescriptiveChoiceResponses = self.nameFolderResponses + "/" + experiment.csvDescriptiveChoiceResponses

        # experiment.pathExperimentDescription = self.nameFolderExperimentDescriptions + "/" + experiment.csvDescription
        experiment.pathExperiment = self.nameFolderExperiments+"/"+ experiment.csvExperiment
        experiment.running = True
        self.setExperimentStage(experiment=experiment, stage="learning")



        #Create Learning Trials
        nTotalTrials = experiment.nLearningTrials

        if experiment.expType == 0:

            self.createTrialsExperiment(experiment=experiment, nTrials= nTotalTrials,
                                        typeTrials=typeTrials)

            # For each choice set, there is one object type Experiment 1
            self.experiments0.append(experiment)


        if experiment.expType == 1:

            # moduleNumber = 2
            # moduleCycles = int(nTotalTrials / moduleNumber)
            # remainingTrials = nTotalTrials % moduleNumber
            #
            # for moduleCycle in range(0, moduleCycles):
            #     self.createTrialsExperiment(experiment=experiment, nTrials=moduleNumber,
            #                                 typeTrials=typeTrials)
            #
            # if remainingTrials > 0:
            #     self.createTrialsExperiment(experiment=experiment, nTrials=remainingTrials,
            #                                 typeTrials=typeTrials)

            self.createTrialsExperiment(experiment=experiment, nTrials= nTotalTrials,
                                        typeTrials=typeTrials)

            # For each choice set, there is one object type Experiment 1
            self.experiments1.append(experiment)

            # Create Descriptive Trials
            # self.createDescriptiveTrialsExperiment(experiment=experiment,
            #                                        nDescriptiveTrials=experiment.nDescriptiveTrials)

        if experiment.expType == 2:

            self.createTrialsExperiment(experiment=experiment, nTrials= nTotalTrials,
                                        typeTrials=typeTrials)

            # moduleNumber = 2
            # moduleCycles = int(nTotalTrials / moduleNumber)
            # remainingTrials = nTotalTrials % moduleNumber
            #
            # for moduleCycle in range(0, moduleCycles):
            #     self.createTrialsExperiment(experiment=experiment, nTrials=moduleNumber,
            #                                 typeTrials=typeTrials)
            #
            # if remainingTrials > 0:
            #     self.createTrialsExperiment(experiment=experiment, nTrials=remainingTrials,
            #                                 typeTrials=typeTrials)

            # For each choice set, there is one object type Experiment 2
            self.experiments2.append(experiment)

        if experiment.expType == 3:

            # moduleNumber = 4
            # moduleCycles = int(nTotalTrials  / moduleNumber)
            # remainingTrials = nTotalTrials  % moduleNumber

            # for moduleCycle in range(0, moduleCycles):
            #     self.createTrialsExperiment(experiment=experiment, nTrials=moduleNumber,
            #                                 typeTrials=typeTrials)
            #
            # if remainingTrials > 0:
            #     self.createTrialsExperiment(experiment=experiment, nTrials=remainingTrials,
            #                                 typeTrials=typeTrials)

            self.createTrialsExperiment(experiment=experiment, nTrials=nTotalTrials,
                                                                         typeTrials=typeTrials)

            self.experiments3.append(experiment)


        if experiment.expType == 4:
            self.experiments4.append(experiment)

        #Update the number of trials

        for trial in experiment.trials:
            trial.nTrials = experiment.nTrials


        if experiment.expType != 0:
            self.experiments.append(experiment)

            #Write File Information

            # Create Descriptive Trials
            self.createDescriptiveTrialsExperiment(experiment=experiment,
                                                   nDescriptiveTrials=experiment.nDescriptiveTrials)

            self.createExperimentFiles(experiment)
            self.setNDecisionProblem()
            self.printExperimentConditions(experiment)

            # Randomization of the order of the alternatives shown within the experiment block
            self.setOrderIds(mode="block", descriptive=False)
            self.setAbsoluteOrderIds(mode="block", descriptive=False)


    def createTrialsExperiment(self, experiment, nTrials, typeTrials):

        if experiment.learningMode != "free":
            self.createJourneyDirectionsLearning(experiment=experiment, nTrials=nTrials)

        if typeTrials == "learning":
            experiment.nTrials += nTrials

        # Experiment 1
        if experiment.expType == 1 or experiment.expType == 0:

            for i in range(0, nTrials):
                if i == 0:
                    experiment.setTimeAttributes(treatmentDirection=experiment.treatmentDirection)

                nTrial = ""
                if typeTrials == "descriptive":
                    nTrial = i +1
                else:
                    nTrial = int(len(experiment.trials)) + 1

                experiment.createTrial(nTrial=nTrial, typeTrial = typeTrials
                                       , randomOrigin=experiment.randomOrigin, randomDestination=experiment.randomDestination
                                       , treatmentDirection=experiment.treatmentDirection, treatmentColor=experiment.treatmentColor
                                       , treatmentDescriptiveOption=experiment.treatmentDescriptiveOption
                                       , journeyClockwise=experiment.journeyClockwise
                                       , journeyCounterclockwise=experiment.journeyCounterclockwise)


            # self.trialsExp1 = self.experiment1.trials

        # Experiment 2
        elif experiment.expType == 2:

            # Randomize the order in which the trials are shown to the user

            for i in range(0, nTrials):
                if i == 0:
                    experiment.setTimeAttributes(treatmentDirection=experiment.treatmentDirection)

                nTrial = ""
                if typeTrials == "descriptive":
                    nTrial = i + 1
                else:
                    nTrial = int(len(experiment.trials)) + 1

                experiment.createTrial(nTrial= nTrial, typeTrial = typeTrials
                                       , randomOrigin=experiment.randomOrigin, randomDestination=experiment.randomDestination
                                       , treatmentDirection=experiment.treatmentDirection, treatmentColor=experiment.treatmentColor,
                                       treatmentDescriptiveOption=experiment.treatmentDescriptiveOption
                                       , journeyClockwise=experiment.journeyClockwise
                                       , journeyCounterclockwise=experiment.journeyCounterclockwise)

        # Experiment 3
        elif experiment.expType == 3:

            experiment.createTrials(nTrials = nTrials, typeTrial = typeTrials, randomOrigin=experiment.randomOrigin
                                    , randomDestination=experiment.randomDestination
                                    , treatmentDirection=experiment.treatmentDirection
                                    , treatmentColor=experiment.treatmentColor
                                    , treatmentDescriptiveOption=experiment.treatmentDescriptiveOption)


        # Experiment 4
        elif experiment.expType == 4:
            completed = False
            # self.trialsExp4 = self.experiment4.trials

    def createNewTrialsExperiment(self, experiment, nTrials,typeTrials):

        if typeTrials == "learning" or typeTrials == "extraLearning":
            experiment.nTotalLearningTrials += nTrials

            # if typeTrials == "learning":
            #     experiment.nLearningTrials += nTrials

            if typeTrials == "extraLearning":
                experiment.nTotalExtraLearningTrials += nTrials
        #
        experiment.nTrials += nTrials

        self.createTrialsExperiment(experiment = experiment, nTrials = nTrials, typeTrials= typeTrials)
        self.runNewTrial(experiment)

    def createDescriptiveTrialsExperiment(self, experiment, nDescriptiveTrials):
        # self.createNewTrialsExperiment(experiment = experiment, nTrials = nDescriptiveTrials, typeTrials="descriptive")
        self.createTrialsExperiment(experiment=experiment, nTrials=nDescriptiveTrials, typeTrials="descriptive")

        lenList = int(len(experiment.journeyDirections) - experiment.nDescriptiveTrials)
        journeyDirectionsTemp = {}

        for key in experiment.journeyDirections.keys():
            if key <=lenList:
                journeyDirectionsTemp[key] = experiment.journeyDirections[key]

        experiment.journeyDirections = journeyDirectionsTemp

    def createConsequencesExperiment(self, experiment, nTrials, choiceResponse, typeTrials):

        experiment.nTrials += nTrials
        # experiment.nConsequenceTrials += nTrials

        #We crate the double of trials but then only keep the trials with the same direction of the one chosen
        self.createTrialsExperiment(experiment = experiment, nTrials = nTrials*2, typeTrials = typeTrials)

        #We only pick those trials that has the same colour of the chosen route
        counter = 1
        element = 0
        originalnLearningTrials = len(experiment.trials)-2*nTrials
        preferredTrials = []

        for trial in experiment.trials:
            if trial.nTrial>originalnLearningTrials:
                if trial.direction == choiceResponse.preferredRoute:
                    trial.nTrial = originalnLearningTrials + counter
                    counter += 1
                    preferredTrials.append(trial)


        experiment.trials = experiment.trials[0:originalnLearningTrials]+ preferredTrials

        experiment.nTrials = len(experiment.trials)

        self.runNewTrial(experiment)
        experiment.decisionConsequences = True

    def getTrialsExperiment(self, experiment):
        return experiment.trials

    def getTrialsCurrentExperiment(self, experiment):
        return experiment.trials

    def getCurrentExperimentTrial(self,experiment):
        return experiment.currentTrial

    def isLastTrial(self,experiment):
        if experiment.currentTrial.nTrial == experiment.nTrials:
            return True
        else:
            return False

    def runNewTrial(self,experiment):

        if experiment.currentTrial == None:  # The first trial has not created yet
            self.currentExperiment.currentTrial = experiment.trials[0]
        else:
            self.currentExperiment.currentTrial = experiment.trials[self.currentNTrial(experiment)-1+1]

        self.currentTrial = self.currentExperiment.currentTrial

    def currentNTrial(self,experiment):

        if self.currentExperiment.currentTrial == None:
            return 0
        else:
            return experiment.currentTrial.nTrial

    def endTrial(self, experiment):
        #Register participant response
        a = 0

    def runExperiment(self,experiment):

        self.currentExperiment = experiment

        if experiment.running == False:
            self.setup(experiment=experiment)

        if self.currentNTrial(experiment) == 0: #The first trial has not created yet
            self.runNewTrial(experiment=experiment)

            if experiment.expType is not 0:
                self.nDecisionProblem += 1

                if experiment.expType == 1:
                    self.nBlockDecisionProblem = self.nDecisionProblem - 0

                if experiment.expType == 2:
                    self.nBlockDecisionProblem = self.nDecisionProblem -len(self.getExperimentList(expType=1))

                if experiment.expType == 3:
                    self.nBlockDecisionProblem = self.nDecisionProblem -len(self.getExperimentList(expType=2))-len(self.getExperimentList(expType=1))

        elif self.currentNTrial(experiment) < experiment.nTrials:
            self.runNewTrial(experiment=experiment)

        else:
            self.close(experiment = experiment)
            # if experiment.expType == 1:
            #
            # if experiment.expType == 2:
            # if experiment.expType == 3:
            # if experiment.expType == 4:

        # if expType == 1: self.trialsExp1 = self.runExperimentTrial1
        # if expType == 2: self.trialsExp2 = self.runExperimentTrial2
        # if expType == 3: self.trialsExp3 = self.runExperimentTrial3

    def close(self, experiment):
        self.currentTrial = None
        self.currentExperiment.currentTrial = None

    def setExperimentStage(self,stage, experiment):

        if stage == "learning":
            experiment.learningStage = True
            experiment.currentExperimentStage = "learning"

        if stage == "extraLearning":
            experiment.extraLearningStage = True
            experiment.currentExperimentStage = "extraLearning"
            experiment.decisionStage = False

        if stage == "decision":
            experiment.decisionStage = True
            experiment.currentExperimentStage = "decision"

        if stage == "consequences":
            experiment.simulationStage = True
            experiment.currentExperimentStage = "consequences"

        if stage == "confirmation":
            experiment.confirmationStage = True
            experiment.currentExperimentStage = "confirmation"

    def getCurrentExperimentStage(self):
        return self.currentExperiment.currentExperimentStage

    def getNameCurrentExperimentStage(self, language, short=False, comma = False):

        return self.getNameExperimentStage(experimentStage = self.currentExperiment.currentExperimentStage,language = language, short = short)

    def getNameExperimentStage(self, experimentStage, language, short = False):

        stage = experimentStage

        if short == False:
            if language == "spanish":
                if stage == "learning" or stage == "extraLearning": return "Etapa 1 de 4 (Aprendizaje)"
                elif stage == "decision": return "Etapa 2 de 4 (Decisión)"
                elif stage == "consequences": return "Etapa 3 de 4 (Consecuencias)"
                elif stage == "confirmation": return "Etapa 4 de 4 (Confirmación)"
                else: return ""

            if language == "english":
                if stage == "learning" or stage == "extraLearning": return "Stage 1 out of 4 (Learning)"
                elif stage == "decision": return "Stage 2 out of 4 (Decision)"
                elif stage == "consequences": return "Stage 3 out of 4 (Consequences)"
                elif stage == "confirmation": return "Stage 4 out of 4 (Confirmation)"
                else: return ""

        if short == True:
            if language == "spanish":
                if stage == "learning" or stage == "extraLearning":
                    return "Aprendizaje"
                elif stage == "decision":
                    return "Decisión"
                elif stage == "consequences":
                    return "Consecuencias"
                elif stage == "confirmation":
                    return "Confirmación"
                else:
                    return ""

            if language == "english":
                if stage == "learning" or stage == "extraLearning":
                    return "Learning"
                elif stage == "decision":
                    return "Decision"
                elif stage == "consequences":
                    return "Consequences"
                elif stage == "confirmation":
                    return "Confirmation"
                else:
                    return ""

    def getIdExperimentStage(self, number):

        if number == 1:
            return "learning"

        if number == 2:
            return "decision"

        if number == 3:
            return "consequences"

        if number == 4:
            return "confirmation"

        # nameExperimentStage = self.getNameExperimentStage(number = number-1, language = "english", short=True).lower()
        #
        # return nameExperimentStage

    def isCurrentExperimentStage(self,stage):
        if stage == self.currentExperiment.currentExperimentStage:
            return True
        else:
            return False

    def getNumberCurrentExperimentStage(self):
        currentExperimentStage = self.getCurrentExperimentStage()

        if currentExperimentStage == "learning" or currentExperimentStage == "extraLearning":
            return 1
        elif currentExperimentStage == "decision":
            return 2
        elif currentExperimentStage == "consequences":
            return 3
        elif currentExperimentStage == "confirmation":
            return 4

    def getNameCurrentExperimentBlock(self,language, short):

        expType = self.currentExperiment.expType

        if short == False:
            if language == "spanish":
                if expType == 1: return "Bloque de Entrenamiento"
                elif expType == 2: return "Primer Bloque Experimental"
                elif expType == 3: return "Segundo Bloque Experimental"
                else: return ""

            if language == "english":
                if expType == 1: return "Training Block"
                elif expType == 2: return "First Experimental Block"
                elif expType == 3: return "Second Experimental Block"
                else: return ""

        if short == True:

            if language == "spanish":
                if expType == 1:
                    return "Entrenamiento"
                elif expType == 2:
                    return "Primer Bloque"
                elif expType == 3:
                    return "Segundo Bloque"
                else:
                    return ""

            if language == "english":
                if expType == 1:
                    return "Training"
                elif expType == 2:
                    return "First Block"
                elif expType == 3:
                    return "Second Block"
                else:
                    return ""


    def getSimulatedLearningResponse(self,experiment, directionRouteSelected):

        treatmentDirection = None
        waitingTimeTreatment = None
        travelTimeTreatment = None
        journeyTimeTreatment = None

        controlRoute = None
        waitingTimeControl = None
        travelTimeControl = None
        journeyTimeControl = None


        if experiment.currentTrial.treatmentDirection == "clockwise":

            if experiment.currentTrial.journeyClockwise is not None:
                waitingTimeTreatment = experiment.currentTrial.journeyClockwise.waitingTime
                travelTimeTreatment = experiment.currentTrial.journeyClockwise.travelTime
                journeyTimeTreatment = experiment.currentTrial.journeyClockwise.journeyTime

            else:
                waitingTimeTreatment = "NA"
                travelTimeTreatment = "NA"
                journeyTimeTreatment = "NA"

            if experiment.currentTrial.journeyCounterclockwise is not None:

                waitingTimeControl = experiment.currentTrial.journeyCounterclockwise.waitingTime
                travelTimeControl = experiment.currentTrial.journeyCounterclockwise.travelTime
                journeyTimeControl = experiment.currentTrial.journeyCounterclockwise.journeyTime

            else:
                waitingTimeControl = "NA"
                travelTimeControl = "NA"
                journeyTimeControl = "NA"


        else:

            if experiment.currentTrial.journeyCounterclockwise is not None:
                waitingTimeTreatment = experiment.currentTrial.journeyCounterclockwise.waitingTime
                travelTimeTreatment = experiment.currentTrial.journeyCounterclockwise.travelTime
                journeyTimeTreatment = experiment.currentTrial.journeyCounterclockwise.journeyTime

            else:
                waitingTimeTreatment = "NA"
                travelTimeTreatment = "NA"
                journeyTimeTreatment = "NA"

            if experiment.currentTrial.journeyClockwise is not None:
                waitingTimeControl = experiment.currentTrial.journeyClockwise.waitingTime
                travelTimeControl = experiment.currentTrial.journeyClockwise.travelTime
                journeyTimeControl = experiment.currentTrial.journeyClockwise.journeyTime

            else:
                waitingTimeControl = "NA"
                travelTimeControl = "NA"
                journeyTimeControl = "NA"


        # if directionRouteSelected == experiment.treatmentDirection:
        #     colorRouteShown = experiment.treatmentColor
        # else:
        #     routeColorShown = experiment.treatmentColor


        currentTrial = experiment.currentTrial

        experimentLearningResponse = SimulatedLearningResponse(experiment=experiment
                                                , date = datetime.now().strftime('%d%m%Y')
                                                , time = datetime.now().strftime('%H%M%S')
                                                , trial =  currentTrial
                                                , randomOrigin = currentTrial.randomOrigin
                                                , randomDestination  = currentTrial.randomDestination
                                                , nTrial = currentTrial.nTrial, nLearningTrials = currentTrial.nTrials, learningMode=experiment.learningMode
                                                , participant = experiment.participant
                                                , typeShown = experiment.currentTrial.typeRouteSelected, directionShown = directionRouteSelected, colorShown = experiment.currentTrial.colorRouteSelected
                                                , treatmentDirection = experiment.treatmentDirection, controlRoute = experiment.controlRoute
                                                , waitingTimeShown = currentTrial.waitingTime, travelTimeShown = currentTrial.travelTime, journeyTimeShown = currentTrial.journeyTime
                                                                )
        return experimentLearningResponse

    def getSimulatedChoiceResponse(self, experiment, type):
        experimentChoiceResponse = SimulatedChoiceResponse(experiment=experiment, type = type
                                                            , date=datetime.now().strftime('%d%m%Y')
                                                            , time=datetime.now().strftime('%H%M%S')
                                                        ,  nLearningTrials=experiment.nLearningTrials, learningMode=experiment.learningMode
                                                        , participant = experiment.participant
                                                        , randomOrigin=experiment.currentTrial.randomOrigin
                                                        , randomDestination=experiment.currentTrial.randomDestination
                                                        , preferredRoute=experiment.preferredJourney, treatmentDirection=experiment.treatmentDirection
                                                        , controlRoute=experiment.controlRoute)


        return experimentChoiceResponse

    def getDescriptiveLearningResponse(self, experiment, trial):

        # treatmentDirection = None
        # waitingTimeTreatment = None
        # travelTimeTreatment = None
        # journeyTimeTreatment = None
        #
        # controlRoute = None
        # waitingTimeControl = None
        # travelTimeControl = None
        # journeyTimeControl = None
        #
        #
        # if trial.treatmentDirection == "clockwise":
        #
        #     if trial.journeyClockwise is not None:
        #         waitingTimeTreatment = trial.journeyClockwise.waitingTime
        #         travelTimeTreatment = trial.journeyClockwise.travelTime
        #         journeyTimeTreatment = trial.journeyClockwise.journeyTime
        #
        #     else:
        #         waitingTimeTreatment = "NA"
        #         travelTimeTreatment = "NA"
        #         journeyTimeTreatment = "NA"
        #
        #     if trial.journeyCounterclockwise is not None:
        #
        #         waitingTimeControl = trial.journeyCounterclockwise.waitingTime
        #         travelTimeControl = trial.journeyCounterclockwise.travelTime
        #         journeyTimeControl = trial.journeyCounterclockwise.journeyTime
        #
        #     else:
        #         waitingTimeControl = "NA"
        #         travelTimeControl = "NA"
        #         journeyTimeControl = "NA"
        #
        #
        # else:
        #
        #     if trial.journeyCounterclockwise is not None:
        #         waitingTimeTreatment = trial.journeyCounterclockwise.waitingTime
        #         travelTimeTreatment = trial.journeyCounterclockwise.travelTime
        #         journeyTimeTreatment = trial.journeyCounterclockwise.journeyTime
        #
        #     else:
        #         waitingTimeTreatment = "NA"
        #         travelTimeTreatment = "NA"
        #         journeyTimeTreatment = "NA"
        #
        #     if trial.journeyClockwise is not None:
        #         waitingTimeControl = trial.journeyClockwise.waitingTime
        #         travelTimeControl = trial.journeyClockwise.travelTime
        #         journeyTimeControl = trial.journeyClockwise.journeyTime
        #
        #     else:
        #         waitingTimeControl = "NA"
        #         travelTimeControl = "NA"
        #         journeyTimeControl = "NA"

        descriptiveLearningResponse = DescriptiveLearningResponse(experiment=experiment, learningMode = experiment.learningMode
                                                            , date=datetime.now().strftime('%d%m%Y')
                                                            , time=datetime.now().strftime('%H%M%S')
                                                        , trial = trial
                                                        , nTrial = trial.nTrial
                                                        , waitingTimeShown = trial.waitingTime, travelTimeShown = trial.travelTime, journeyTimeShown = trial.journeyTime
                                                        # , waitingTimeControl = waitingTimeControl, travelTimeControl = travelTimeControl, journeyTimeControl = journeyTimeControl
                                                        # , waitingTimeTreatment = waitingTimeTreatment, travelTimeTreatment = travelTimeTreatment, journeyTimeTreatment = journeyTimeTreatment
                                                        , nLearningTrials=experiment.nLearningTrials
                                                        , participant = experiment.participant
                                                        , treatmentDirection=experiment.treatmentDirection
                                                        , controlRoute=experiment.controlRoute)

        return descriptiveLearningResponse


    def getDescriptiveChoiceResponse(self, experiment):
        descriptiveChoiceResponse = DescriptiveChoiceResponse(experiment=experiment
                                                            , date=datetime.now().strftime('%d%m%Y')
                                                            , time=datetime.now().strftime('%H%M%S')
                                                        ,  nLearningTrials=experiment.nLearningTrials, learningMode=experiment.learningMode
                                                        , participant = experiment.participant
                                                        , preferredRoute=experiment.preferredDescriptiveJourney, treatmentDirection=experiment.treatmentDirection
                                                        , controlRoute=experiment.controlRoute)

        return descriptiveChoiceResponse

    def createJourneyDirectionsLearning(self, experiment, nTrials):
        # It will create a dictionary where the key is the number of each trial and the value is the direction
        # The directions shown are equal, so the participant experience equally the two journeys

        journeyDirections = {}
        learningMode = experiment.learningMode
        randomizationDone = False
        journeyDirection = None
        conditions = ["clockwise","counterclockwise"]
        countClockwise = 0
        countCounterclockwise = 0
        halfTrials = round(nTrials/2)

        for nTrial in range(1,nTrials+1):

            if learningMode == "random": #Directions are randomly

                if countClockwise < halfTrials and countCounterclockwise < halfTrials: #Randomly allocation of trials
                    journeyDirection = self.randomization(conditions)
                    journeyDirections[nTrial] = journeyDirection

                elif countClockwise == halfTrials: #If the clockwise direction are ready
                    journeyDirections[nTrial] = "counterclockwise"

                elif countCounterclockwise == halfTrials: #If the counterclockwise direction are ready
                    journeyDirections[nTrial] = "clockwise"

                #This counts the number of trials in each direction
                if journeyDirections[nTrial] == "clockwise":
                    countClockwise += 1
                else:
                    countCounterclockwise += 1

            if learningMode == "half": #The first half of directions correspond to one type, and the next half to the other

                if randomizationDone == False:
                    journeyDirection = self.randomization(conditions)
                    randomizationDone = True

                if nTrial <= halfTrials:
                    journeyDirections[nTrial] = journeyDirection
                else:
                    if journeyDirection == "clockwise":
                        journeyDirections[nTrial] = "counterclockwise"
                    else:
                        journeyDirections[nTrial] = "clockwise"

            if learningMode == "sequence":#The directions are alternated in each trial

                if randomizationDone == False:
                    journeyDirection = self.randomization(conditions)
                    randomizationDone = True

                    if journeyDirection == "clockwise":
                        journeyDirectionEvenLearningTrials = "clockwise"
                        journeyDirectionOddsTrials = "counterclockwise"
                    else:
                        journeyDirectionEvenLearningTrials = "counterclockwise"
                        journeyDirectionOddsTrials = "clockwise"

                if nTrial % 2 == 0:
                    journeyDirections[nTrial] = journeyDirectionEvenLearningTrials
                else:
                    journeyDirections[nTrial] = journeyDirectionOddsTrials


            #If there are nTrials, n/2 trials are random, the other half follows the same pattern of randomness

            if learningMode =="halfRandom":
                if halfTrials>1:

                    if countCounterclockwise + countClockwise == halfTrials:
                        journeyDirections[nTrial] = journeyDirections[nTrial-halfTrials]

                    else:
                        if countClockwise < halfTrials/2 and countCounterclockwise < halfTrials/2: #Randomly allocation of trials
                            journeyDirection = self.randomization(conditions)
                            journeyDirections[nTrial] = journeyDirection

                        elif countClockwise == halfTrials/2: #If the clockwise direction are ready
                            journeyDirections[nTrial] = "counterclockwise"

                        elif countCounterclockwise == halfTrials/2: #If the counterclockwise direction are ready
                            journeyDirections[nTrial] = "clockwise"

                        #This counts the number of trials in each direction
                        if journeyDirections[nTrial] == "clockwise":
                            countClockwise += 1
                        else:
                            countCounterclockwise += 1




                else:
                    if countClockwise < halfTrials and countCounterclockwise < halfTrials:  # Randomly allocation of trials
                        journeyDirection = self.randomization(conditions)
                        journeyDirections[nTrial] = journeyDirection

                    elif countClockwise == halfTrials:  # If the clockwise direction are ready
                        journeyDirections[nTrial] = "counterclockwise"

                    elif countCounterclockwise == halfTrials:  # If the counterclockwise direction are ready
                        journeyDirections[nTrial] = "clockwise"

                    # This counts the number of trials in each direction
                    if journeyDirections[nTrial] == "clockwise":
                        countClockwise += 1
                    else:
                        countCounterclockwise += 1

        # experiment.journeyDirections = journeyDirections

        # Add this direction to the dictionary of existing directions

        for nTrial in journeyDirections.keys():
            experiment.journeyDirections[len(experiment.journeyDirections)+1] = journeyDirections[nTrial]

    def createExperimentFiles(self, experiment):
        # See whether the file with registries of participant was already created
        if self.existingExperiment(experiment.pathExperiment, experiment) == False: #if the file of the experiment has not been created yet (i.e. the first trial of the experiment)
            # Create a file with the main information about the experiment (id, number of participants, conditions.
            fileExperiment = open(experiment.pathExperiment, 'w')
            # Write the first two lines of the file, with the name of the file with the trials of that experiment and the experiment id
            # fileExperiment.write(printCsvLine(["Experiment", str(experiment.expType)]))
            # writeChoiceResponseCsv
            # The next line will contain the distirbution of marbles in the random urn, since for trials of the same experiment, this distribution keeps the same.
            # This will update it later in the method randomMarbles
            fileExperiment.close()

            ## Create file with participants responses in the learning trial stage (regardless of the experiment)
            fileAllSimulatedLearningResponses = open(self.pathAllExperimentsSimulatedLearningResponses, 'w')
            fileAllSimulatedLearningResponses.write(printCsvLine(self.simulatedLearningAttributesCsv))
            fileAllSimulatedLearningResponses.close()

            # # Create file with participants responses in the learning trial stage for each experiment
            # fileSimulatedLearningResponses = open(experiment.pathExperimentSimulatedLearningResponses, 'w')
            # #Write the columns of this file
            # fileSimulatedLearningResponses.write(printCsvLine(self.simulatedLearningAttributesCsv))
            # fileSimulatedLearningResponses.close()

            # Create file with participants responses in the choice stage (regardless of the experiment)
            fileAllSimulatedChoiceResponses = open(self.pathAllExperimentsSimulatedChoiceResponses, 'w')
            fileAllSimulatedChoiceResponses.write(printCsvLine(self.simulatedChoiceAttributesCsv))
            fileAllSimulatedChoiceResponses.close()

            # # Create file with participants responses in the choice stage for each experiment
            # fileSimulatedChoiceResponses = open(experiment.pathExperimentSimulatedChoiceResponses, 'w')
            # # Write the columns of this file
            # fileSimulatedChoiceResponses.write(printCsvLine(self.simulatedChoiceAttributesCsv))
            # fileSimulatedChoiceResponses.close()

            # Create file with participants responses in the choice stage (regardless of the experiment)
            fileAllDescriptiveLearningResponses = open(self.pathAllExperimentsDescriptiveLearningResponses, 'w')
            fileAllDescriptiveLearningResponses.write(printCsvLine(self.descriptiveLearningAttributesCsv))
            fileAllDescriptiveLearningResponses.close()

            # # Create file with participants responses in the choice stage for each experiment
            # fileSimulatedLearningResponses = open(experiment.pathExperimentSimulatedLearningResponses, 'w')
            # # Write the columns of this file
            # fileSimulatedLearningResponses.write(printCsvLine(self.simulatedLearningAttributesCsv))
            # fileSimulatedLearningResponses.close()

            # Create file with participants responses in the choice stage (regardless of the experiment)
            fileAllDescriptiveChoiceResponses = open(self.pathAllExperimentsDescriptiveChoiceResponses, 'w')
            fileAllDescriptiveChoiceResponses.write(printCsvLine(self.descriptiveChoiceAttributesCsv))
            fileAllDescriptiveChoiceResponses.close()

            # # Create file with participants responses in the choice stage for each experiment
            # fileSimulatedChoiceResponses = open(experiment.pathExperimentSimulatedChoiceResponses, 'w')
            # # Write the columns of this file
            # fileSimulatedChoiceResponses.write(printCsvLine(self.simulatedChoiceAttributesCsv))
            # fileSimulatedChoiceResponses.close()

            #Create file with reaction time responses
            fileAllReactionTimeResponses = open(self.pathAllExperimentsReactionTimeResponses, 'w')
            fileAllReactionTimeResponses.write(printCsvLine(self.reactionTimeAttributesCsv))
            fileAllReactionTimeResponses.close()

            # # Add some rows to the Experiment txt file with the number of the columns
            # fileExperiment = open(experiment.pathExperiment, 'a')
            #
            # # The first line has the label of the columns (red and blue marbles)
            # fileExperiment.write(printCsvLine(["\n "]))  # Blank line
            # fileExperiment.write(
            #     printCsvLine(["DP", "Waiting (T)", "Travel (T)", "Waiting (C)", "Travel (C)"]))

        else:  # If the file exists
            # self.readExistingExperimentFile(experiment)
            completed = False
            # experiment.printExperimentConditions()

    # Return a bool whether the experiment was already created (i.e. True if this is the first trial)
    def existingExperiment(self, pathExperiment,experiment):
        return experiment.csvExperiment in listdir("Experiments")

    #This method review the existing trials of participants. I assumed that the file with the experiment trials in the same
    #folder from where this file is being executed.
    def readExistingExperimentFile(self,experiment):

        pathExperiment = experiment.pathExperiment
        files = listdir()

        # Reading file contents
        fileExperiment = open(pathExperiment, 'r')  # Read the csv file for Experiment
        infoFileExperiment = fileExperiment.readlines()  # infoFile is a list of strings that has all the string lines inside the participant's file
        fileExperiment.close()  # Close the file for this participant as the information is already stored in the variable 'infoFile'

        #The first line of this file has the name of the file with the summary of the participant trials for that experiment
        csvSimulatedLearningResponses = infoFileExperiment[1].split(",")[1].replace("\n","").replace(" ","")
        fileResponses = open(self.nameFolderResponses+"/"+csvSimulatedLearningResponses, 'r')  # Read the csv file for Experiment
        infoFileResponses = fileResponses.readlines()  # infoFile is a list of strings that has all the string lines inside the participant's file
        fileResponses.close()  # Close the file for this participant as the information is already stored in the variable 'infoFile'

        #First row of the file (Name of the columns)
        colNames = infoFileResponses[0].split(",")
        colValues = infoFileResponses[1:]
        for lineParticipantsInfo in colValues:
            lineTrial = lineParticipantsInfo.split(",")
            participant = Participant(age=lineTrial[0],  gender=lineTrial[1],educationLevel=lineTrial[2])
            # trial = ExperimentTrial(journeyLengthCondition=lineTrial[4],urnA=urnA,urnB=urnB,urnsPositions=lineTrial[5],participant=participant
            #               ,urnSelected=lineTrial[6],marblePicked=lineTrial[7],prize=self.prize, colorPrize=self.colorPrize,experimentId=self.experimentId)
            #
            # self.addTrial(trial)

        a = 0
    # Random selection of the condition but constrained to the remaining participants in each experiment.
    # Example with 3 conditions for the randomization process:

    # Iteration 1
    # Step 1: if there are 3 conditions, we picked one randomly (e.g. 2 marbles)
    # Step 2: If there are 3 conditions and there is already one participant in condition 1 (e.g. 2 marbles), we need to pick one of the remaining conditions randomly (e.g. 10 marbles).
    # Step 3: In the next iteration, the selected condition will be the remaining one (100 marbles)
    # Iteration 2:
    # For the 4th participant, we selected randomly one of the three conditions (Step 1).
    # Then for the 5th participant, we picked one of the 2 remaining conditions (Step 2)
    # ... Iteration n:

    def printExperimentConditions(self,experiment):

        # fileExperiment.write(
        #     printCsvLine(["DP", "Waiting (T)", "Travel (T)", "Waiting (C)", "Travel (C)"]))

        #File with all experimental conditions



        if experiment.expType == 1 or experiment.expType == 2:

            dictCsv = OrderedDict([('experiment', round(experiment.expType,0)), ('relDp', experiment.relativeDp), ('absDp', experiment.absoluteDp)
                                      , ('Waiting (C)', round(experiment.waitingTimeControl,0))
                                      , ('Travel (C)', round(experiment.travelTimeControl,0))
                                      , ('Journey (C)', round(experiment.journeyTimeControl,0))
                                      , ('Waiting (T)', round(experiment.waitingTimeTreatment,0))
                                      , ('Travel (T)', round(experiment.travelTimeTreatment,0))
                                      , ('Journey (T)', round(experiment.journeyTimeTreatment,0))
                                   ])

            fileExperiment = open(experiment.pathExperiment, 'r')  # Read the csv file for Experiment
            infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
            lineFormattedCsv = ""


            if infoLineExperiment == "":
                lineCsv = list(dictCsv.keys())
                lineFormattedCsv = printCsvLine(lineCsv)
                fileExperiment.close()

                # This command write the response in a file that contains responses from the 4 experiments.
                fileAllExperimentResponses = open(experiment.pathExperiment, 'a')
                fileAllExperimentResponses.write(lineFormattedCsv)
                fileAllExperimentResponses.close()


                if experiment.expType == 1:

                    # File with all experimental Conditions. Write the column labels only for experiment 1
                    fileAllExperimentalConditions = open(self.pathFileAllExperimentalConditions, 'a')
                    fileAllExperimentalConditions.write(lineFormattedCsv)
                    fileAllExperimentalConditions.close()

                    self.existingConditionsExperiment1File = False

                if experiment.expType == 2:
                    self.existingConditionsExperiment2File = False


            if  experiment.expType == 1:

                if not self.existingConditionsExperiment1File:

                    valuesCsv = []
                    for attribute in dictCsv.keys():
                        valuesCsv.append(dictCsv[attribute])

                    lineFormattedCsv = printCsvLine(valuesCsv)
                    fileExperiment.close()

                    # This command write the response in a file that contains responses from the 4 experiments.
                    fileAllExperimentResponses = open(experiment.pathExperiment, 'a')
                    fileAllExperimentResponses.write(lineFormattedCsv)
                    fileAllExperimentResponses.close()

                    # File with all experimental Conditions
                    fileAllExperimentalConditions = open(self.pathFileAllExperimentalConditions, 'a')
                    fileAllExperimentalConditions.write(lineFormattedCsv)
                    fileAllExperimentalConditions.close()



            if experiment.expType == 2:

                if not self.existingConditionsExperiment2File:

                    valuesCsv = []
                    for attribute in dictCsv.keys():
                        valuesCsv.append(dictCsv[attribute])

                    lineFormattedCsv = printCsvLine(valuesCsv)
                    fileExperiment.close()

                    # This command write the response in a file that contains responses from the 4 experiments.
                    fileAllExperimentResponses = open(experiment.pathExperiment, 'a')
                    fileAllExperimentResponses.write(lineFormattedCsv)
                    fileAllExperimentResponses.close()

                    # File with all experimental Conditions
                    fileAllExperimentalConditions = open(self.pathFileAllExperimentalConditions, 'a')
                    fileAllExperimentalConditions.write(lineFormattedCsv)
                    fileAllExperimentalConditions.close()



        if experiment.expType == 3:

            #Control prospect to be printed
            prospectControlStr = experiment.getProspectToPrint(experiment.timeProspectControl)
            waitingControlProspectStr = prospectControlStr["waiting"]
            travelControlProspectStr = prospectControlStr["travel"]
            journeyControlProspectStr = prospectControlStr["journey"]

            # Treatment prospect to be printed
            prospectTreatmentStr = experiment.getProspectToPrint(experiment.timeProspectTreatment)
            waitingTreatmentProspectStr = prospectTreatmentStr["waiting"]
            travelTreatmentProspectStr = prospectTreatmentStr["travel"]
            journeyTreatmentProspectStr = prospectTreatmentStr["journey"]


            dictCsv = OrderedDict([('experiment', round(experiment.expType,0)), ('relDp', experiment.relativeDp), ('absDp', experiment.absoluteDp)
                                      , ('Waiting (C)', waitingControlProspectStr)
                                      , ('Travel (C)', travelControlProspectStr)
                                      , ('Journey (C)', journeyControlProspectStr)
                                      , ('Waiting (T)', waitingTreatmentProspectStr)
                                      , ('Travel (T)', travelTreatmentProspectStr)
                                      , ('Journey (T)', journeyTreatmentProspectStr)
                                   ])

            fileExperiment = open(experiment.pathExperiment, 'r')  # Read the csv file for Experiment
            infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
            lineFormattedCsv = ""


            if infoLineExperiment == "":
                lineCsv = list(dictCsv.keys())
                lineFormattedCsv = printCsvLine(lineCsv)
                fileExperiment.close()

                # This command write the response in a file that contains responses from the 4 experiments.
                fileAllExperimentResponses = open(experiment.pathExperiment, 'a')
                fileAllExperimentResponses.write(lineFormattedCsv)
                fileAllExperimentResponses.close()


                self.existingConditionsExperiment3File = False


            if not self.existingConditionsExperiment3File:

                valuesCsv = []
                for attribute in dictCsv.keys():
                    valuesCsv.append(dictCsv[attribute])

                lineFormattedCsv = printCsvLine(valuesCsv)
                fileExperiment.close()

                # This command write the response in a file that contains responses from the 4 experiments.
                fileAllExperimentResponses = open(experiment.pathExperiment, 'a')
                fileAllExperimentResponses.write(lineFormattedCsv)
                fileAllExperimentResponses.close()

                # File with all experimental Conditions
                fileAllExperimentalConditions = open(self.pathFileAllExperimentalConditions, 'a')
                fileAllExperimentalConditions.write(lineFormattedCsv)
                fileAllExperimentalConditions.close()

    def randConditions(self):

        #First check if there are enough participants in any of the conditions
        dictConditions = {}
        dictConditionsCompleted = {}

        #Create a dictionary where the keys are the number of marbles per condition (e.g. 2,4 and100) and the values of the dictionary are initilized in 0.
        for condition in self.nMarblesConditions:
            dictConditions[str(condition)] = 0

        conditions = list(dictConditions.keys()) #E.g [2,4,100]
        nConditions = len(conditions)
        nLearningTrials = len(self.trials)
        completeCondition = int(nLearningTrials % nConditions)
        iteration = int(nLearningTrials/nConditions)+1

        for condition in conditions:

            # The values of the dictionary are replaced by the number of participants per condition that participated in the experiment previously
            for trial in self.trials:
                if int(trial.nMarblesCondition) == int(condition):
                    a = dictConditions[condition]
                    dictConditions[condition] = int(dictConditions[condition])+ 1

            if int(dictConditions[condition]) == iteration: #Remove the condition from the dictionary if it has enough participants
                del dictConditions[condition]

        #From the remaining conditions of the dictionary, we select one of those randomly and holds the value of marbles for that condition
        self.nMarbles = int(list(dictConditions.keys())[randint(0, len(dictConditions) - 1)])

    # 1. The positions of the two urns must be randomized in each trial. While the left urn must always be called
    # “urn A” and the right one “urn B” as in the original experiment, whether it is A (left) that contains the
    # 50:50 or the ambiguous distribution should be randomly decided every time the experiment runs. Of course,
    # the instructions should also be changing to reflect this.

    #Write information of the current trial (or participant) in the corresponding csv file of an experiment
    def writeSimulatedLearningResponseCsv(self,experiment, experimentalCondition, simulatedLearningResponse):

        # #Write the response in the file of the corresponding experiment
        # fileExperimentResponses = open(experiment.pathExperimentSimulatedLearningResponses, 'a')
        # fileExperimentResponses.write(lineFormattedCsv)
        # fileExperimentResponses.close()

        fileExperiment = open(self.pathAllExperimentsSimulatedLearningResponses, 'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = simulatedLearningResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels = True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsSimulatedLearningResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()

            self.writeSimulatedLearningResponseCsv(experiment = experiment,experimentalCondition = experimentalCondition, simulatedLearningResponse = simulatedLearningResponse)

        else:
            lineCsv = simulatedLearningResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsSimulatedLearningResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()



        # #This command write the response in a file that contains the responses from the same participant
        # fileParticipants = open("Responses/ExperimentResponses.csv", 'a')

    #Write information of the current trial (or participant) in the corresponding csv file of an experiment
    def writeSimulatedChoiceResponseCsv(self,experiment, experimentalCondition, simulatedChoiceResponse):

        fileExperiment = open(self.pathAllExperimentsSimulatedChoiceResponses, 'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = simulatedChoiceResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels = True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsSimulatedChoiceResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()

            self.writeSimulatedChoiceResponseCsv(experiment = experiment, experimentalCondition = experimentalCondition, simulatedChoiceResponse = simulatedChoiceResponse)

        else:
            lineCsv = simulatedChoiceResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsSimulatedChoiceResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()

    # Write information of the current trial (or participant) in the corresponding csv file of an experiment

    def writeDescriptiveLearningResponseCsv(self, experiment, experimentalCondition, descriptiveLearningResponse):

        # #Write the response in the file of the corresponding experiment
        # fileExperimentResponses = open(experiment.pathsimulatedLearningResponses, 'a')
        # fileExperimentResponses.write(lineFormattedCsv)
        # fileExperimentResponses.close()

        fileExperiment = open(self.pathAllExperimentsDescriptiveLearningResponses,
                              'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = descriptiveLearningResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels=True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsDescriptiveLearningResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()

            self.writeDescriptiveLearningResponseCsv(experiment=experiment,experimentalCondition = experimentalCondition,
                                                   descriptiveLearningResponse=descriptiveLearningResponse)

        else:
            lineCsv = descriptiveLearningResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsDescriptiveLearningResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()

            # #This command write the response in a file that contains the responses from the same participant
            # fileParticipants = open("Responses/ExperimentResponses.csv", 'a')

    #Descriptive Exercise: Write information of the current trial (or participant) in the corresponding csv file of an experiment
    def writeDescriptiveChoiceResponseCsv(self,experiment, descriptiveChoiceResponse,experimentalCondition):

        fileExperiment = open(self.pathAllExperimentsDescriptiveChoiceResponses, 'r')  # Read the csv file for Experiment
        infoLineExperiment = fileExperiment.readline()  # infoFile is a list of strings that has all the string lines inside the participant's file
        lineFormattedCsv = ""

        if infoLineExperiment == "":
            lineCsv = descriptiveChoiceResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels = True)
            lineFormattedCsv = printCsvLine(lineCsv)
            fileExperiment.close()

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsDescriptiveChoiceResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()

            self.writeDescriptiveChoiceResponseCsv(experiment = experiment, experimentalCondition = experimentalCondition, descriptiveChoiceResponse = descriptiveChoiceResponse)

        else:
            lineCsv = descriptiveChoiceResponse.createLineExperimentResponsesCsv(experimentalCondition = experimentalCondition, colLabels=False)
            lineFormattedCsv = printCsvLine(lineCsv)

            # This command write the response in a file that contains responses from the 4 experiments.
            fileAllExperimentResponses = open(self.pathAllExperimentsDescriptiveChoiceResponses, 'a')
            fileAllExperimentResponses.write(lineFormattedCsv)
            fileAllExperimentResponses.close()

    def addTrial(self,trial):
        self.trials.append(trial) #This add the trial to the existing list of trials

# **********************************************  Classes to create an specific experiment  ********************************************************** #

class ExperimentBlock:
    def __init__(self, expType, id, maxId, participant
                 ,nLearningTrials, nExtraLearningTrials, nConsequenceTrials, nDescriptiveTrials
                 , learningMode
                 ,csvExperiment,csvSimulatedLearningResponses,csvDescriptiveLearningResponses
                 ,csvSimulatedChoiceResponses,csvDescriptiveChoiceResponses):

        self.expType = expType
        self.participant = participant

        self.nTrials = 0
        self.nLearningTrials = nLearningTrials
        self.nLearningTrialsByRoute = nLearningTrials/2
        self.nExtraLearningTrials = nExtraLearningTrials
        self.nConsequenceTrials = nConsequenceTrials
        self.nDescriptiveTrials = nDescriptiveTrials

        self.nTotalExtraLearningTrials = 0
        self.nTotalLearningTrials = self.nTotalExtraLearningTrials + self.nLearningTrials



        # self.nTrial = 1 #This is to keep the order of the current trial in the experiment
        self.trials = []
        self.descriptiveTrials = []
        self.id = id #Each experiment have several choice sets. Each id represents each of the choice sets
        self.dp = None #

        self.relativeDp = id #Equal to id
        self.absoluteDp = None #Equal to dp

        self.orderId = None #This random id will be used to randomize the order in which the experiment are shown in the experiential and escriptive experiment.
        self.orderBlockId = None #This is a random id at the block level
        self.descriptionOrderId = None
        self.simulationOrderId = None #Sequential order by block (1,2,1,2,3,4,5,6,1,..,6)
        self.simulationAbsoluteOrderId = None #Absolute order (1,2,3,4,5,6,..., 14)



        self.tempId = None #Temporal id
        self.maxId = maxId #The total number of choice sets.
        self.currentTrial = None

        self.randomOrigin = None
        self.randomDestination = None

        #Experiment Stages
        self.currentExperimentStage = None
        self.learningStage = False
        self.decisionStage = False
        self.consequenceStage = False
        self.confirmationStage = False
        self.defaultCertaintyLevel = True #This boolean allows to detect whether the person have choose a different certainty level

        self.learningMode = learningMode
        # This will be a dictionary where the key is the number of each trial and the value is the direction
        # self.journeyDirections = None

        self.journeyDirections = {}

        self.treatmentDirection = None
        self.treatmentColor = None
        self.controlColor = None
        self.controlAlternative = None #A or B
        self.treatmentAlternative = None  # A or B

        self.treatmentDescriptiveOption = None

        self.controlRoute = None

        self.csvExperiment = csvExperiment

        self.csvSimulatedLearningResponses =csvSimulatedLearningResponses
        self.csvSimulatedChoiceResponses = csvSimulatedChoiceResponses
        self.csvDescriptiveLearningResponses = csvDescriptiveLearningResponses
        self.csvDescriptiveChoiceResponses = csvDescriptiveChoiceResponses

        self.pathExperimentResponses = None
        self.pathExperimentDescription = None
        self.pathExperiment = None

        self.running = False

        self.journeyTimeClockwise = None
        self.journeyCounterclockwise = None

        # self.journeyLength = journeyLength

        self.waitingTimeControl = None
        self.waitingTimeTreatment = None
        self.travelTimeControl = None
        self.travelTimeTreatment = None

        self.preferredJourney = None
        self.preferredColor = None
        self.certaintyLevel = "NA" #Number between 0 and 100.

        self.preferredType = None

        self.preferredDescriptiveJourney = None
        self.preferredDescriptiveAlternative = None
        self.preferredDescriptiveType = None

        self.preferredProspectJourney = None


    def getCardinalDirection(self, color, origin):
        if origin == "west":
            if self.getColorDirection(color) =="clockwise":
                return "north"
            else:
                return "south"

        if origin == "east":
            if self.getColorDirection(color) =="clockwise":
                return "south"
            else:
                return "north"

    def getColorDirection(self,color):

        if color == "blue" or color == "red":

            if self.treatmentColor == color:
                return self.treatmentDirection
            else:
                return self.controlDirection

    def randomization(self,conditions):
        #Receive an array of conditions (e.g. strings) and return the name of a random condition:
        randomization = randint(0, len(conditions)-1)
        return conditions[randomization]

    def getJourneyDirection(self, nTrial):
        # 'journeyDirections' dictionary where the key is the number of each trial and the value is the direction
        return self.journeyDirections[nTrial]

    def getCurrentTrial(self):
        return self.trials[self.nTrial-1]

    def getId(self, block = True, random=False):

        if block == False:
            if random == True:
                return self.orderId
            else:
                return self.id

        if block == True:
            if random == True:
                return self.orderBlockId
            else:
                return self.id

    def setPreferredJourney(self, preferredJourney):
        self.preferredJourney = preferredJourney #'clockwise' or 'counterclockwise'

        if preferredJourney == self.treatmentDirection:
            self.preferredColor = self.treatmentColor
            self.preferredType = "treatment"
        else:
            self.preferredColor = self.controlColor
            self.preferredType = "control"

    def setPreferredDescriptiveJourney(self, preferredDescriptiveAlternative):

        self.preferredDescriptiveAlternative = preferredDescriptiveAlternative
        # self.preferredDescriptiveJourney = preferredDescriptiveJourney #'clockwise' or 'counterclockwise'

        if preferredDescriptiveAlternative == self.treatmentDescriptiveOption:
            self.preferredDescriptiveJourney = self.treatmentDirection
            self.preferredDescriptiveType = "treatment"
        else:
            self.preferredDescriptiveJourney = self.controlDirection
            self.preferredDescriptiveType = "control"

    def setCertaintyLevel(self, certaintyLevel):
        self.certaintyLevel = certaintyLevel



    def setExpAlternatives(self, treatmentAlternative):

        self.treatmentAlternative = treatmentAlternative

        if treatmentAlternative == "A":
            self.controlAlternative = "B"
        else:
            self.controlAlternative = "A"

    def setExpColors(self, treatmentColor):

        self.treatmentColor = treatmentColor

        if treatmentColor == "blue":
            self.controlColor = "red"
        else:
            self.controlColor = "blue"

class ExperimentBlock1(ExperimentBlock):

    def __init__(self, expType, participant,nLearningTrials, nExtraLearningTrials, nConsequenceTrials, nDescriptiveTrials
                 , learningMode, timeAlternativeControl, timeAlternativeTreatment
                 , csvExperiment, csvSimulatedLearningResponses,csvSimulatedChoiceResponses,csvDescriptiveLearningResponses, csvDescriptiveChoiceResponses, id, maxId):

        super().__init__(participant = participant, expType = expType
                         , nLearningTrials = nLearningTrials, nExtraLearningTrials = nExtraLearningTrials, nConsequenceTrials = nConsequenceTrials
                         , nDescriptiveTrials = nDescriptiveTrials
                         , learningMode = learningMode, id = id, maxId = maxId
                         , csvExperiment = csvExperiment
                         , csvSimulatedLearningResponses = csvSimulatedLearningResponses, csvSimulatedChoiceResponses = csvSimulatedChoiceResponses
                         ,csvDescriptiveLearningResponses = csvDescriptiveLearningResponses, csvDescriptiveChoiceResponses = csvDescriptiveChoiceResponses)

        self.waitingCounterclockwise = None
        self.travelCounterclockwise = None
        self.waitingClockwise = None
        self.travelClockwise = None
        # self.journeyTime = None #The journey time is fixed in both scenarios, but there might be many journey length conditions

        self.waitingTimeControl = timeAlternativeControl.waitingTime
        self.travelTimeControl = timeAlternativeControl.travelTime
        self.journeyTimeControl = timeAlternativeControl.journeyTime

        self.waitingTimeTreatment = timeAlternativeTreatment.waitingTime
        self.travelTimeTreatment = timeAlternativeTreatment.travelTime
        self.journeyTimeTreatment = timeAlternativeTreatment.journeyTime

        self.treatmentDirection = None

    def setTimeAttributes(self, treatmentDirection):

        self.treatmentDirection = treatmentDirection

        if self.treatmentDirection == "clockwise":
            self.controlDirection = "counterclockwise"

        else:
            self.controlDirection = "clockwise"


        waitingCounterclockwise = None
        waitingClockwise = None
        travelClockwise = None
        travelCounterclockwise = None
        # self.journeyTime = journeyTime

        # self.journeyTimeControl = self.journeyTimeControl
        # self.waitingTimeControl = round(self.xWaitingTimeControl * self.journeyTimeControl, 2)
        # self.travelTimeControl = round(self.journeyTimeControl - self.waitingTimeControl, 2)
        #
        # self.journeyTimeTreatment = self.journeyTimeTreatment
        # self.waitingTimeTreatment = round(self.xWaitingTimeTreatment * self.journeyTimeTreatment, 2)
        # self.travelTimeTreatment = round(self.journeyTimeTreatment - self.waitingTimeTreatment, 2)

        if treatmentDirection == "counterclockwise":
            treatmentClockwise = False
            self.controlRoute = "clockwise"
            waitingCounterclockwise = self.waitingTimeTreatment
            waitingClockwise = self.waitingTimeControl
            travelClockwise = self.journeyTimeControl - waitingClockwise
            travelCounterclockwise = self.journeyTimeTreatment - waitingCounterclockwise

        else: #Clockwise route is the treatment condition
            treatmentClockwise = True
            self.controlRoute = "counterclockwise"
            waitingCounterclockwise = self.waitingTimeControl
            waitingClockwise = self.waitingTimeTreatment
            travelClockwise = self.journeyTimeTreatment - waitingClockwise
            travelCounterclockwise = self.journeyTimeControl - waitingCounterclockwise

        #Set waiting, travel and journey times for clockwise Route
        self.waitingClockwise = Waiting(meanWaitingTime=waitingClockwise)

        self.travelClockwise = Travel(meanTravelTime=travelClockwise)
        self.journeyClockwise = Journey(travel=self.travelClockwise, waiting=self.waitingClockwise,
                                        direction="clockwise", treatment=treatmentClockwise)

        # Set waiting, travel and journey times for counterclockwise Route
        self.waitingCounterclockwise = Waiting(meanWaitingTime=waitingCounterclockwise)

        self.travelCounterclockwise = Travel(meanTravelTime=travelCounterclockwise)
        self.journeyCounterclockwise = Journey(travel=self.travelCounterclockwise,
                                               waiting=self.waitingCounterclockwise,
                                               direction="counterclockwise", treatment = not treatmentClockwise)

        #This generate deterministic waiting and travel times according to the mean values given before
        self.journeyClockwise.generateJourneyTimes(randomTravel=False,randomWait=False)
        self.journeyCounterclockwise.generateJourneyTimes(randomTravel=False, randomWait=False)

    def createTrial(self, nTrial, typeTrial, treatmentDirection, treatmentColor,treatmentDescriptiveOption
                    , randomOrigin, randomDestination, journeyClockwise, journeyCounterclockwise):

        # This generate deterministic waiting and travel times according to the mean values given before
        journeyClockwiseTemp = copy.copy(journeyClockwise)
        journeyCounterclockwiseTemp = copy.copy(journeyCounterclockwise)

        journeyClockwiseTemp.updateJourneyTimes() #This generate new waiting and travel times if the random modes were activated
        journeyCounterclockwiseTemp.updateJourneyTimes() #This generate new waiting and travel times if the random modes were activated

        trial = ExperimentTrial(expType=self.expType, nTrials=self.nTrials, type = typeTrial
                                , learningMode = self.learningMode, participant=self.participant
                                , nTrial=nTrial
                                , randomOrigin=randomOrigin
                                , randomDestination = randomDestination
                                , journeyClockwise=journeyClockwiseTemp
                                , journeyCounterclockwise=journeyCounterclockwiseTemp
                                , treatmentDirection=treatmentDirection
                                , treatmentDescriptiveOption = treatmentDescriptiveOption
                                , treatmentColor = treatmentColor)



        if trial.learningMode != "free":

            if trial.type == "descriptive":
                self.setExpAlternatives(treatmentAlternative=treatmentDescriptiveOption)
                trialDirection = self.getJourneyDirection(nTrial=len(self.journeyDirections) - self.nDescriptiveTrials + nTrial)
                trial.setDirection(trialDirection)
                trial.setColors(treatmentColor = treatmentColor)
                self.descriptiveTrials.append(trial)

            else:
                self.setExpColors(treatmentColor=treatmentColor)
                trialDirection = self.getJourneyDirection(nTrial=nTrial)
                trial.setDirection(trialDirection)
                trial.setColors(treatmentColor = treatmentColor)
                self.trials.append(trial)


class ExperimentBlock2(ExperimentBlock):

    def __init__(self, expType, participant,nLearningTrials, nExtraLearningTrials, nConsequenceTrials, nDescriptiveTrials
                 , learningMode, timeAlternativeControl
                 , timeAlternativeTreatment
                 , csvExperiment, csvSimulatedLearningResponses, csvSimulatedChoiceResponses,csvDescriptiveLearningResponses, csvDescriptiveChoiceResponses, id, maxId):

        super().__init__(participant=participant, expType=expType
                         , nLearningTrials=nLearningTrials, nExtraLearningTrials=nExtraLearningTrials,
                         nConsequenceTrials=nConsequenceTrials, nDescriptiveTrials = nDescriptiveTrials
                         , learningMode=learningMode, id=id, maxId = maxId
                         , csvExperiment=csvExperiment
                         , csvSimulatedLearningResponses=csvSimulatedLearningResponses, csvSimulatedChoiceResponses=csvSimulatedChoiceResponses
                         , csvDescriptiveLearningResponses = csvDescriptiveLearningResponses,csvDescriptiveChoiceResponses = csvDescriptiveChoiceResponses)

        self.waitingCounterclockwise = None
        self.travelCounterclockwise = None
        self.waitingClockwise = None
        self.travelClockwise = None
        # self.journeyTime = None #The journey time is fixed in both scenarios, but there might be many journey length conditions

        self.waitingTimeControl = timeAlternativeControl.waitingTime
        self.travelTimeControl = timeAlternativeControl.travelTime
        self.journeyTimeControl = timeAlternativeControl.journeyTime

        self.waitingTimeTreatment = timeAlternativeTreatment.waitingTime
        self.travelTimeTreatment = timeAlternativeTreatment.travelTime
        self.journeyTimeTreatment = timeAlternativeTreatment.journeyTime

        self.treatmentDirection = None

    def setTimeAttributes(self, treatmentDirection):

        self.treatmentDirection = treatmentDirection

        if self.treatmentDirection == "clockwise":
            self.controlDirection = "counterclockwise"

        else:
            self.controlDirection = "clockwise"

        waitingCounterclockwise = None
        waitingClockwise = None
        travelClockwise = None
        travelCounterclockwise = None
        # self.journeyTime = journeyTime

        # self.journeyTimeControl = self.journeyTimeControl
        # self.waitingTimeControl = self.xWaitingTimeControl * self.journeyTimeControl, 2)
        # self.travelTimeControl = self.journeyTimeControl - self.waitingTimeControl, 2)
        #
        # self.journeyTimeTreatment = self.journeyTimeTreatment
        # self.waitingTimeTreatment = self.xWaitingTimeTreatment * self.journeyTimeTreatment, 2)
        # self.travelTimeTreatment = self.journeyTimeTreatment - self.waitingTimeTreatment, 2)

        if treatmentDirection == "counterclockwise":
            treatmentClockwise = False
            self.controlRoute = "clockwise"
            waitingCounterclockwise = self.waitingTimeTreatment
            waitingClockwise = self.waitingTimeControl
            travelClockwise = self.journeyTimeControl - waitingClockwise
            travelCounterclockwise = self.journeyTimeTreatment - waitingCounterclockwise

        else:  # Clockwise route is the treatment condition
            treatmentClockwise = True
            self.controlRoute = "counterclockwise"
            waitingCounterclockwise = self.waitingTimeControl
            waitingClockwise = self.waitingTimeTreatment
            travelClockwise = self.journeyTimeTreatment - waitingClockwise
            travelCounterclockwise = self.journeyTimeControl - waitingCounterclockwise

        # Set waiting, travel and journey times for clockwise Route
        self.waitingClockwise = Waiting(meanWaitingTime=waitingClockwise)

        self.travelClockwise = Travel(meanTravelTime=travelClockwise)
        self.journeyClockwise = Journey(travel=self.travelClockwise, waiting=self.waitingClockwise,
                                        direction="clockwise", treatment=treatmentClockwise)

        # Set waiting, travel and journey times for counterclockwise Route
        self.waitingCounterclockwise = Waiting(meanWaitingTime=waitingCounterclockwise)

        self.travelCounterclockwise = Travel(meanTravelTime=travelCounterclockwise)
        self.journeyCounterclockwise = Journey(travel=self.travelCounterclockwise,
                                               waiting=self.waitingCounterclockwise,
                                               direction="counterclockwise", treatment=not treatmentClockwise)

        # This generate deterministic waiting and travel times according to the mean values given before
        self.journeyClockwise.generateJourneyTimes(randomTravel=False, randomWait=False)
        self.journeyCounterclockwise.generateJourneyTimes(randomTravel=False, randomWait=False)

    def createTrial(self, nTrial, typeTrial, treatmentDirection, treatmentColor,treatmentDescriptiveOption
                    , randomOrigin, randomDestination, journeyClockwise, journeyCounterclockwise):

        # This generate deterministic waiting and travel times according to the mean values given before
        journeyClockwiseTemp = copy.copy(journeyClockwise)
        journeyCounterclockwiseTemp = copy.copy(journeyCounterclockwise)

        journeyClockwiseTemp.updateJourneyTimes() #This generate new waiting and travel times if the random modes were activated
        journeyCounterclockwiseTemp.updateJourneyTimes() #This generate new waiting and travel times if the random modes were activated

        trial = ExperimentTrial(expType=self.expType, nTrials=self.nTrials, type = typeTrial
                                , learningMode = self.learningMode, participant=self.participant
                                , nTrial=nTrial
                                , randomOrigin=randomOrigin
                                , randomDestination = randomDestination
                                , journeyClockwise=journeyClockwiseTemp
                                , journeyCounterclockwise=journeyCounterclockwiseTemp
                                , treatmentDirection=treatmentDirection
                                , treatmentDescriptiveOption = treatmentDescriptiveOption
                                , treatmentColor = treatmentColor)


        if trial.learningMode != "free":

            if trial.type == "descriptive":
                self.setExpAlternatives(treatmentAlternative=treatmentDescriptiveOption)
                trialDirection = self.getJourneyDirection(nTrial=len(self.journeyDirections) - self.nDescriptiveTrials + nTrial)
                trial.setDirection(trialDirection)
                trial.setColors(treatmentColor)
                self.descriptiveTrials.append(trial)

            else:
                self.setExpColors(treatmentColor=treatmentColor)
                trialDirection = self.getJourneyDirection(nTrial=nTrial)
                trial.setDirection(trialDirection)
                trial.setColors(treatmentColor)
                self.trials.append(trial)

# Experiment 3: xDeterministicWaitingTime must be greater or equal than xWaitingTimeVariability
class ExperimentBlock3(ExperimentBlock):
    def __init__(self, expType, participant
                 , nLearningTrials, nExtraLearningTrials, nConsequenceTrials, nDescriptiveTrials
                 , learningMode,id, maxId
                 , timeProspectControl, timeProspectTreatment
                 , csvExperiment, csvSimulatedLearningResponses, csvSimulatedChoiceResponses
                 , csvDescriptiveLearningResponses,csvDescriptiveChoiceResponses):

        super().__init__(participant = participant, expType = expType
                         , nLearningTrials=nLearningTrials, nExtraLearningTrials=nExtraLearningTrials,
                         nConsequenceTrials=nConsequenceTrials, nDescriptiveTrials = nDescriptiveTrials
                         ,csvExperiment = csvExperiment, csvSimulatedLearningResponses = csvSimulatedLearningResponses,id = id, maxId = maxId
                         , csvSimulatedChoiceResponses = csvSimulatedChoiceResponses
                         , csvDescriptiveLearningResponses = csvDescriptiveLearningResponses,csvDescriptiveChoiceResponses = csvDescriptiveChoiceResponses
                         ,learningMode = learningMode)

        # The amount of variability in the waiting time as a proportion of the mean journey time (Control and TreatmentRoute)
        self.timeProspectControl = timeProspectControl
        self.timeProspectTreatment = timeProspectTreatment

        self.treatmentDirection = None

    def createTrials(self, nTrials, typeTrial, treatmentDirection, treatmentColor,treatmentDescriptiveOption, randomOrigin, randomDestination):

        self.treatmentDirection = treatmentDirection

        if self.treatmentDirection == "clockwise":
            self.controlDirection = "counterclockwise"

        else:
            self.controlDirection = "clockwise"

        journeysControl = self.timeProspectControl.getTimeConsequences()
        journeysTreatment = self.timeProspectTreatment.getTimeConsequences()

        #Create lists of journeys following the same sequences of the journeys generate for the prospect.
        # This is done until the lists have a number of journeys equals to the number of trials
        journeysTrialsControl = []
        journeysTrialsTreatment = []
        counterControl = -1
        counterTreatment = -1

        for i in range(0,int(nTrials/2)):

            counterControl += 1
            counterTreatment += 1

            journeysTrialsControl.append(journeysControl[counterControl])
            journeysTrialsTreatment.append(journeysTreatment[counterTreatment])

            if counterControl == len(journeysControl)-1:
                counterControl = -1

            if counterTreatment == len(journeysTreatment)-1:
                counterTreatment = -1

        #Randomization of direction

        journeysTrialsClockwise = []
        journeysTrialsCounterclockwise = []

        if treatmentDirection == "counterclockwise":
            self.treatmentRoute = "counterclockwise"
            self.controlRoute = "clockwise"
            journeysTrialsCounterclockwise = copy.copy(journeysTrialsTreatment)
            journeysTrialsClockwise = copy.copy(journeysTrialsControl)
        else:

            self.treatmentRoute = "clockwise"
            self.controlRoute = "counterclockwise"
            journeysTrialsClockwise = copy.copy(journeysTrialsTreatment)
            journeysTrialsCounterclockwise = copy.copy(journeysTrialsControl)

        counterClockwiseList = 0
        counterCounterclockwiseList = 0

        temp =  self.journeyDirections

        for nTrial in range(0,nTrials):

            journeyClockwiseTemp = None
            journeyCounterclockwiseTemp = None

            if self.learningMode != "free":

                if nTrials == len(self.journeyDirections):
                    trialDirection = self.getJourneyDirection(nTrial=nTrial + 1)

                else:
                    trialDirection = self.getJourneyDirection(nTrial=len(self.journeyDirections)-nTrials+nTrial+1)

                if trialDirection == "clockwise":

                    if len(journeysTrialsClockwise) > 1:
                        randomIndexClockwise = randint(0, int(len(journeysTrialsClockwise))-1)
                    else:
                        randomIndexClockwise = 0

                    journeyClockwise = journeysTrialsClockwise[randomIndexClockwise]
                    journeyClockwiseTemp = copy.copy(journeyClockwise)
                    journeyClockwiseTemp.updateJourneyTimes()  # This generate new waiting and travel times if the random modes were activated

                    del journeysTrialsClockwise[randomIndexClockwise]


                if trialDirection == "counterclockwise":

                    if len(journeysTrialsCounterclockwise) > 1:
                        randomIndexCounterclockwise = randint(0, int(len(journeysTrialsCounterclockwise)) - 1)
                    else:
                        randomIndexCounterclockwise = 0

                    journeyCounterclockwise = journeysTrialsCounterclockwise[randomIndexCounterclockwise]
                    journeyCounterclockwiseTemp = copy.copy(journeyCounterclockwise)
                    journeyCounterclockwiseTemp.updateJourneyTimes()  # This generate new waiting and travel times if the random modes were activated

                    del journeysTrialsCounterclockwise[randomIndexCounterclockwise]


                trial = ExperimentTrial(expType=self.expType, nTrials=self.nTrials, type = typeTrial
                        , learningMode=self.learningMode, participant=self.participant
                        , nTrial=len(self.trials)+1
                        , randomOrigin=randomOrigin
                        , randomDestination=randomDestination
                        , journeyClockwise=journeyClockwiseTemp
                        , journeyCounterclockwise=journeyCounterclockwiseTemp
                        , treatmentDirection=treatmentDirection
                        , treatmentDescriptiveOption=treatmentDescriptiveOption
                        , treatmentColor =  treatmentColor)

                trial.setDirection(trialDirection)
                trial.setColors(treatmentColor = treatmentColor)

                if trial.type == "descriptive":
                    self.setExpAlternatives(treatmentAlternative=treatmentDescriptiveOption)
                    self.descriptiveTrials.append(trial)

                else:
                    self.setExpColors(treatmentColor=treatmentColor)
                    self.trials.append(trial)

    def roundNumberProspect(self, number, digits):

        if number == "":
            return ""

        else:
            return round(number,digits)

    #Return a string of the prospect that will be printed in the txt file
    def getProspectToPrint(self, timeProspect):

        # The prospect have 2 components, the travel and waiting times prospect.
        travelProspect = timeProspect.travelProspect
        waitingProspect = timeProspect.waitingProspect
        journeyProspect = timeProspect.journeyProspect

        strWaitingProspect = ""
        strTravelProspect = ""
        strJourneyProspect = ""

        digits = 1 #Decimals

        # Journey Time Prospect

        if journeyProspect.p1 == 1:
            strJourneyProspect = "(" + str(self.roundNumberProspect(journeyProspect.journeyTime1,digits)) + "; " + str(self.roundNumberProspect(journeyProspect.p1,digits)) + "; " + ")"

        if journeyProspect.p2 == 1:
            strJourneyProspect = "(" + str(self.roundNumberProspect(journeyProspect.journeyTime1,digits)) + "; " + str(self.roundNumberProspect(journeyProspect.p1,digits)) + ";" + " " + ")"

        else:
            strJourneyProspect = "(" + str(self.roundNumberProspect(journeyProspect.journeyTime1,digits)) + "; " + str(self.roundNumberProspect(journeyProspect.p1,digits)) + ";" + str(
                journeyProspect.journeyTime2) + ")"

        #Travel Time Prospect

        if travelProspect.p1 == 1:
            strTravelProspect = "(" + str(self.roundNumberProspect(travelProspect.travelTime1,digits)) +"; " +  str(self.roundNumberProspect(travelProspect.p1,digits)) + "; " + ")"

        if travelProspect.p2 == 1:
            strTravelProspect = "(" + str(self.roundNumberProspect(travelProspect.travelTime1,digits)) + "; " + str(self.roundNumberProspect(travelProspect.p1,digits)) + ";" +" " + ")"

        else:
            strTravelProspect = "(" + str(self.roundNumberProspect(travelProspect.travelTime1,digits)) + "; " + str(self.roundNumberProspect(travelProspect.p1,digits)) + ";" + str(self.roundNumberProspect(travelProspect.travelTime2,digits)) + ")"

        #Waiting Time Prospect

        if waitingProspect.p1 == 1:
            strWaitingProspect = "(" + str(self.roundNumberProspect(waitingProspect.waitingTime1,digits)) +"; " +  str(self.roundNumberProspect(waitingProspect.p1,digits)) + "; " + ")"

        if waitingProspect.p2 == 1:
            strWaitingProspect = "(" + str(self.roundNumberProspect(waitingProspect.waitingTime1,digits)) + "; " + str(self.roundNumberProspect(waitingProspect.p1,digits)) + ";" +" " + ")"

        else:
            strWaitingProspect = "(" + str(self.roundNumberProspect(waitingProspect.waitingTime1,digits)) + "; " + str(self.roundNumberProspect(waitingProspect.p1,digits)) + ";" + str(self.roundNumberProspect(
                waitingProspect.waitingTime2,digits)) + ")"



        #This dictionary contains the labels for the waiting and travel time prospects
        dictStrProspects = {'waiting': strWaitingProspect, 'travel': strTravelProspect, 'journey':strJourneyProspect}

        return dictStrProspects


# Experiment 4: xDeterministicTravelTime must be greater or equal than xTravelTimeVariability
class Experiment4(ExperimentBlock):
    def __init__(self, expType, participant,nLearningTrials, nExtraLearningTrials, nConsequenceTrials, learningMode
                 , xDeterministicTravelTime, xVariabilityTravelTimeControl, xVariabilityTravelTimeTreatment
                 , csvExperiment, csvDescription,journeyLength,csvSimulatedLearningResponses,csvSimulatedChoiceResponses,csvDescriptiveChoiceResponses,id):

        super().__init__(participant = participant, expType = expType, nLearningTrials = nLearningTrials
                         ,csvExperiment = csvExperiment, csvDescription = csvDescription, id = id
                         , csvSimulatedLearningResponses = csvSimulatedLearningResponses, csvSimulatedChoiceResponses = csvSimulatedChoiceResponses,csvDescriptiveChoiceResponses = csvDescriptiveChoiceResponses
                         , learningMode = learningMode)

        self.journeyTime = journeyLength # The journey time is fixed in both scenarios
        # The amount of variability in the waiting time as a proportion of the mean journey time (Control and Treatment Routes)
        self.xVariabilityTravelTimeTreatment = xVariabilityTravelTimeTreatment
        self.xVariabilityTravelTimeControl = xVariabilityTravelTimeControl
        # The amount of waiting time as a proportion of the mean journey time in the alternative that will be deterministic
        self.xDeterministicTravelTime = xDeterministicTravelTime

    def setTimeAttributes(self, treatmentDirection):


        self.treatmentDirection = treatmentDirection #Variable waiting time is the treatment condition
        treatmentClockwise = None
        # These attributes will be used to build the treatment waiting time
        minTravelClockwise = None
        maxTravelClockwise = None
        minTravelCounterclockwise = None
        maxTravelCounterclockwise = None

        deterministicTravelTime = self.xDeterministicTravelTime * self.journeyTime

        # Waiting time is fixed for both routes
        waitingTime = self.journeyTime * (1 - self.xDeterministicTravelTime)


        if treatmentDirection == "counterclockwise":
            treatmentClockwise = False
            self.controlRoute = "clockwise"
            # Calculate lower and upper boundsfor waiting for the clockwise route
            minTravelClockwise = deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeControl
            maxTravelClockwise = deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeControl

            # Calculate lower and upper boundsfor waiting for the counterclockwise route
            minTravelCounterclockwise = deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeTreatment
            maxTravelCounterclockwise = deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeTreatment


        else: #Clockwise route is the treatment condition

            treatmentClockwise = True
            self.controlRoute = "counterclockwise"
            # Calculate lower and upper boundsfor waiting for the clockwise route
            minTravelClockwise = deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeTreatment
            maxTravelClockwise = deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeTreatment

            # Calculate lower and upper boundsfor waiting for the clockwise route
            minTravelCounterclockwise = deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeControl
            maxTravelCounterclockwise = deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeControl


        # Set waiting and travel times for both routes
        self.travelClockwise = Travel(minTravelTime=minTravelClockwise,maxTravelTime=maxTravelClockwise)
        self.waitingClockwise = Waiting(meanWaitingTime=waitingTime)

        self.travelCounterclockwise = Travel(minTravelTime=minTravelCounterclockwise,maxTravelTime=maxTravelCounterclockwise)
        self.waitingCounterclockwise = Waiting(meanWaitingTime=waitingTime)

        # Create Journey objects for each route.
        self.journeyClockwise = Journey(travel=self.travelClockwise,
                                               waiting=self.waitingClockwise,
                                               direction="clockwise", treatment = treatmentClockwise)

        # This generate deterministic waiting and travel times according to the mean values given before
        self.journeyCounterclockwise = Journey(travel=self.travelCounterclockwise,
                                               waiting=self.waitingCounterclockwise,
                                               direction="counterclockwise", treatment = not treatmentClockwise)

        # This generate deterministic waiting and travel times according to the mean values given before
        self.journeyClockwise.generateJourneyTimes(randomTravel=False, randomWait=False)
        self.journeyCounterclockwise.generateJourneyTimes(randomTravel=False, randomWait=False)

class Experiment5(ExperimentBlock):
    def __init__(self, expType, participant,nLearningTrials, nExtraLearningTrials, nConsequenceTrials, learningMode, journeyLength
                 , xDeterministicTravelTime, xVariabilityTravelTime, xDeterministicWaitingTime, xVariabilityWaitingTime,
                 csvExperiment, csvDescription,csvSimulatedLearningResponses,csvSimulatedChoiceResponses,id):

        super().__init__(participant=participant, expType=expType, nLearningTrials=nLearningTrials
                         , csvExperiment=csvExperiment, csvDescription = csvDescription,id = id
                         , csvSimulatedLearningResponses = csvSimulatedLearningResponses, csvSimulatedChoiceResponses = csvSimulatedChoiceResponses
                         , learningMode = learningMode)

        self.journeyTime = journeyLength  # The journey time is fixed in both scenarios

        self.xDeterministicTravelTime = xDeterministicTravelTime  # The amount of waiting time as a proportion of the mean journey time in the alternative that will be deterministic
        self.xVariabilityTravelTime = xVariabilityTravelTime  # The amount of variability in the waiting time as a proportion of the mean journey time

        self.xDeterministicWaitingTime = xDeterministicWaitingTime
        self.xVariabilityWaitingTime = xVariabilityWaitingTime

    def setTimeAttributes(self, treatmentDirection):
        self.treatmentDirection = treatmentDirection  # Variable travel time but fixed control time for clockwise (Treatment Condition).

        treatmentClockwise = None

        # These attributes will be used to build the waiting and travel time objects
        minTravelClockwise = None
        maxTravelClockwise = None
        minTravelCounterclockwise = None
        maxTravelCounterclockwise = None

        minWaitingClockwise = None
        maxWaitingClockwise = None
        minWaitingCounterclockwise = None
        maxWaitingCounterclockwise = None

        self.controlTravelTime = self.xDeterministicTravelTime * self.journeyTime
        self.controlWaitingTime = self.xDeterministicWaitingTime * self.journeyTime

        if treatmentDirection == "counterclockwise": #Variable travel time but fixed control time for counterclockwise

            treatmentClockwise = False
            self.controlRoute = "clockwise"
            # Calculate lower and upper bounds for waiting for the counterclockwise route
            minTravelCounterclockwise = self.controlTravelTime - self.journeyTime * self.xVariabilityTravelTime
            maxTravelCounterclockwise = self.controlTravelTime + self.journeyTime * self.xVariabilityTravelTime
            minWaitingCounterclockwise = self.controlWaitingTime
            maxWaitingCounterclockwise = self.controlWaitingTime

            # Calculate lower and upper bounds for waiting for the clockwise route
            minTravelClockwise = self.controlTravelTime
            maxTravelClockwise = self.controlTravelTime
            minWaitingClockwise = self.controlWaitingTime - self.journeyTime * self.xVariabilityWaitingTime
            maxWaitingClockwise = self.controlWaitingTime + self.journeyTime * self.xVariabilityWaitingTime

        else:  #Clockwise is Treatment Condition
            treatmentClockwise = True
            self.controlRoute = "counterclockwise"
            # Calculate lower and upper bounds for waiting for the clockwise route
            minTravelClockwise = self.controlTravelTime - self.journeyTime * self.xVariabilityTravelTime
            maxTravelClockwise = self.controlTravelTime + self.journeyTime * self.xVariabilityTravelTime
            minWaitingClockwise = self.controlWaitingTime
            maxWaitingClockwise = self.controlWaitingTime

            # Calculate lower and upper bounds for waiting for the clockwise route
            minTravelCounterclockwise = self.controlTravelTime
            maxTravelCounterclockwise = self.controlTravelTime
            minWaitingCounterclockwise =self.controlWaitingTime - self.journeyTime * self.xVariabilityWaitingTime
            maxWaitingCounterclockwise = self.controlWaitingTime + self.journeyTime * self.xVariabilityWaitingTime

        # Set waiting and travel times for both routes
        self.travelClockwise = Travel(minTravelTime=minTravelClockwise, maxTravelTime=maxTravelClockwise)

        self.waitingClockwise = Waiting(minWaitingTime=minWaitingClockwise,
                                                maxWaitingTime=maxWaitingClockwise)

        self.travelCounterclockwise = Travel(minTravelTime=minTravelCounterclockwise,
                                                     maxTravelTime=maxTravelCounterclockwise)

        self.waitingCounterclockwise = Waiting(minWaitingTime=minWaitingCounterclockwise,
                                                       maxWaitingTime=maxWaitingCounterclockwise)

        # Create Journey objects for each route.
        self.journeyClockwise = Journey(travel=self.travelClockwise,
                                               waiting=self.waitingClockwise,
                                               direction="clockwise", treatment = treatmentClockwise)

        # This generate deterministic waiting and travel times according to the mean values given before
        self.journeyCounterclockwise = Journey(travel=self.travelCounterclockwise,
                                               waiting=self.waitingCounterclockwise,
                                               direction="counterclockwise", treatment = not treatmentClockwise)

        # This generate deterministic waiting and travel times according to the mean values given before
        self.journeyClockwise.generateJourneyTimes(randomTravel=False, randomWait=False)
        self.journeyCounterclockwise.generateJourneyTimes(randomTravel=False, randomWait=False)

# **********************************************  Trial  ********************************************************** #

# A Trial object contains all the information that is printed in the output file (participantsExperiment.csv)
# In addition, we implemented the function deBriefMessage that show to the participant a a debrief message through the User Interface .

class ExperimentTrial:
    def __init__(self, expType, randomOrigin , randomDestination, participant, journeyClockwise, journeyCounterclockwise
                 , nTrial, nTrials, type, learningMode, treatmentDirection, treatmentColor,treatmentDescriptiveOption):

        self.expType = expType
        self.nTrial = nTrial #The number of trial
        self.nTrials = nTrials #The total number of trials in the experiment

        self.participant = participant
        self.journeyClockwise = journeyClockwise
        self.journeyCounterclockwise = journeyCounterclockwise

        self.descriptiveDay = None #E.g. 1,2,3,4 if there are four descriptive trials
        self.descriptiveTable = None #A or B
        self.simulatedDay = nTrial


        self.treatmentDirection = treatmentDirection
        self.controlDirection = None

        if self.treatmentDirection == "clockwise":
            self.controlDirection = "counterclockwise"

        else:
            self.controlDirection = "clockwise"

        self.treatmentDescriptiveOption = treatmentDescriptiveOption

        self.controlColor = None
        self.treatmentColor = None
        # self.setRouteColors(treatmentColor)


        self.typeRouteSelected = None
        self.colorRouteSelected = None

        self.type = type # Type of trial: learning, extra, consequence,

        if journeyClockwise is not None:
            self.waitingTimeClockwise = self.journeyClockwise.waitingTime
            self.travelTimeClockwise = self.journeyClockwise.travelTime
            self.journeyTimeClockwise = self.journeyClockwise.journeyTime

        if journeyCounterclockwise is not None:
            self.waitingTimeCounterclockwise = self.journeyCounterclockwise.waitingTime
            self.travelTimeCounterclockwise = self.journeyCounterclockwise.travelTime
            self.journeyTimeCounterclockwise = self.journeyCounterclockwise.journeyTime

        # The value of direction will be different than None if there is no free learning (guided learning)
        self.learningMode = learningMode
        self.direction = None
        self.randomOrigin = randomOrigin
        self.randomDestination = randomDestination

        self.waitingTime = None
        self.travelTime = None
        self.journeyTime = None


        # self.nMarblesCondition = nMarblesCondition  # Number of marbles after randomizing conditions (e.g. 2,10 or 100)
        # self.urnsPositions = urnsPositions  # Position of urns after randomizing positions (0 or 1). 0 if the random urn was on the right – urn B as was in the paper, and 1 if the random urn was on the left – urn A (0 or 1)
        # self.experimentId = experimentId  # Each trial is linked to a given experiment. This string allows to link a trial with its correponding experiment, but avoiding circular dependence between the classes (both class contains instances of each other)
        # self.urnA = urnA  # Urn A after randomization
        # self.urnB = urnB  # Urn B after randomization
        # self.urnSelected = urnSelected  # the selected urn, A or B
        #
        # self.marblePicked = marblePicked
        # self.prize = prize
        # self.colorPrize = colorPrize  # The participant win a prize depending on the color of the marble (e.g. blue or red)

    def setColors(self, treatmentColor):
        self.treatmentColor = treatmentColor

        if treatmentColor == "blue":
            self.controlColor = "red"
        else:
            self.controlColor = "blue"

        if self.treatmentDirection == self.direction:
            self.colorRouteSelected = treatmentColor
        else:
            self.colorRouteSelected = self.controlColor


    def setDirection(self, direction):
        # This value will be different than none if there is no free learning (guided learning)
        self.direction = direction

        if direction == self.treatmentDirection:
            self.typeRouteSelected = "treatment"

        else:
            self.typeRouteSelected = "control"


        if direction == "clockwise":
            self.waitingTime = self.waitingTimeClockwise
            self.travelTime = self.travelTimeClockwise
            self.journeyTime = self.journeyTimeClockwise

        else:
            self.waitingTime = self.waitingTimeCounterclockwise
            self.travelTime = self.travelTimeCounterclockwise
            self.journeyTime = self.journeyTimeCounterclockwise


    # The message will change whether the participant picked the marble that gives a prize
    def debriefMessage(self):
        if self.colorPrize == self.marblePicked:
            return "Congratulations, you won the price (" + str(
                self.prize) + " pounds) because you picked the " + self.colorPrize + " marble. "

        else:
            return "Unfortunately you did not won the price (" + str(
                self.prize) + " pounds) because you did not pick the " + self.colorPrize + " marble. "

    # The selected urn must be printed in the csv file using the following rule: 0 if the participant chose the random urn and 1 if he/she chose the 50:50 urn (0 or 1)
    def idUrnSelected(self):

        idUrnSelected = 1

        # if the participant selected the urn with random marbles, the following condition must be satisfied
        if (self.urnA.randomMarbles == True and self.urnSelected == "A") or (
                        self.urnB.randomMarbles == True and self.urnSelected == "B"):
            idUrnSelected = 0

        return idUrnSelected

# **********************************************  Participant Responses  ********************************************************** #

#This is what will be written in the csv files

class ExperimentResponse:
    def __init__(self, experiment, nLearningTrials,date,time, learningMode
                 , participant,treatmentDirection,controlRoute):

        #Experiment Type (1,2,3,4)
        self.experiment = experiment
        self.expType = experiment.expType
        self.relativeDp = experiment.id
        self.absoluteDp = experiment.dp
        self.expDps = experiment.maxId

        #Participant Information
        self.participantGender = participant.gender
        self.participantAge = participant.age
        self.participantEducationLevel = participant.educationLevel


        self.nLearningTrials = nLearningTrials
        self.date = date
        self.time = time
        self.learningMode=learningMode

        #Type of Bus Route (Control, Treatment)
        self.controlRoute = controlRoute # Counterclockwise or not counterclockwise
        self.treatmentDirection = treatmentDirection  # Counterclockwise or not counterclockwise

class SimulatedLearningResponse(ExperimentResponse):
    def __init__(self, experiment, nTrial, trial, nLearningTrials,date,time, learningMode
                 ,randomOrigin,randomDestination
                 , participant
                 , typeShown, directionShown, colorShown, treatmentDirection, controlRoute
                 , waitingTimeShown, travelTimeShown, journeyTimeShown
                 # , waitingTimeControl, travelTimeControl,journeyTimeControl
                 # , waitingTimeTreatment, travelTimeTreatment, journeyTimeTreatment

                 ):

        super().__init__(experiment = experiment, nLearningTrials = nLearningTrials, learningMode = learningMode
                         , date = date, time = time
                         , participant = participant
                         , treatmentDirection = treatmentDirection, controlRoute = controlRoute)


        self.directionShown = directionShown #Counterclockwise or not counterclockwise
        self.colorShown = colorShown
        self.typeShown = typeShown #Treatment or control

        self.waitingTimeShown = waitingTimeShown
        self.travelTimeShown = travelTimeShown
        self.journeyTimeShown = journeyTimeShown

        self.expOrder = experiment.simulationOrderId
        self.expAbsoluteOrder = experiment.simulationAbsoluteOrderId
        self.randomOrigin = randomOrigin
        self.randomDestination = randomDestination

        # # Information about Control Route (For experiment 3 and 4, this information changes in each learning trial)
        # self.waitingTimeControl = waitingTimeControl
        # self.travelTimeControl = travelTimeControl
        # self.journeyTimeControl = journeyTimeControl
        #
        # # Treatment Route
        # self.waitingTimeTreatment = waitingTimeTreatment
        # self.travelTimeTreatment = travelTimeTreatment
        # self.journeyTimeTreatment = journeyTimeTreatment

        self.nTrial = nTrial
        self.trial = trial


    # If colLabels is true it is because the file for writing does not have any registry
    def createLineExperimentResponsesCsv(self, experimentalCondition, colLabels = False):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        dictCsv = OrderedDict([('experimentalCondition', experimentalCondition), ('participantId', self.experiment.participant.id)
                                  ,('participantName', self.experiment.participant.name)
                                  , ('computerId', self.experiment.participant.computerId)
                                , ('experiment', self.expType),('dps',self.expDps), ('blockDP', self.relativeDp)
                                  , ('DP', self.absoluteDp), ('absOrder',self.expAbsoluteOrder),('relOrder',self.expOrder)
                                  , ('date',self.date),('time',self.time)
                   ,('nTrial', self.nTrial)
                   , ('typeTrial', self.trial.type)
                   # , ('nLearningTrials', self.nLearningTrials)
                   ,('learningMode',self.learningMode)
            # , ('age', self.participantAge), ('gender', self.participantGender)
            # , ('eduLevel', self.participantEducationLevel)  # the collected demographics
            , ('randomOrigin',self.randomOrigin)
            , ('randomDestination',self.randomDestination)
            , ('routeShown', self.typeShown)
            , ('controlRoute(c)', self.controlRoute)
            , ('treatmentRoute(t)', self.treatmentDirection)
            , ('directionShown', self.directionShown)
            , ('controlColor(c)', self.trial.controlColor)
            , ('treatmentColor(t)', self.trial.treatmentColor)
            , ('colorShown', self.colorShown)
            , ('waiting', round(self.waitingTimeShown,2))
            , ('travel', round(self.travelTimeShown,2))
            , ('journey', round(self.journeyTimeShown,2))

            # , ('waiting(c)', self.waitingTimeControl)
            # , ('travel(c)', self.travelTimeControl)
            # , ('journey(c)', self.journeyTimeControl)

            # , ('waiting(t)', self.waitingTimeTreatment)
            # , ('travel(t)', self.travelTimeTreatment)
            # , ('journey(t)', self.journeyTimeTreatment)

               # 'nMarbles':trial.nMarblesCondition, #the condition in which he/she participated, i.e. the number of balls in each urn (2, 10 or 100)
               # 'urnsPositions':trial.urnsPositions,   #the positions of the urns i.e. 0 if the random urn was on the right – urn B as was in the paper, and 1 if the random urn was on the left – urn A (0 or 1)
               # 'urnSelected':trial.idUrnSelected(), #the selected urn, i.e. 0 if the participant chose the random urn and 1 if he/she chose the 50:50 urn (0 or 1)
               # 'marble':trial.marblePicked #whether they got a red or a blue marble (red or blue)
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

class SimulatedChoiceResponse(ExperimentResponse):

    def __init__(self, experiment, type, nLearningTrials, date, time, learningMode
                 , participant, randomOrigin, randomDestination
                 , preferredRoute, treatmentDirection, controlRoute):

        super().__init__(experiment = experiment, nLearningTrials = nLearningTrials, learningMode = learningMode
                         , date = date, time = time
                         , participant = participant
                         , treatmentDirection = treatmentDirection, controlRoute = controlRoute)


        self.preferredRoute = preferredRoute
        self.randomOrigin = randomOrigin
        self.randomDestination = randomDestination
        self.expOrder = experiment.simulationOrderId
        self.expAbsoluteOrder = experiment.simulationAbsoluteOrderId
        self.type = type #decision or confirmation

    # If colLabels is true it is because the file for writing does not have any registry
    def createLineExperimentResponsesCsv(self, experimentalCondition, colLabels = False):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        dictCsv = OrderedDict([('experimentalCondition', experimentalCondition), ('participantId', self.experiment.participant.id)
                                  , ('participantName', self.experiment.participant.name)
                                  , ('computerId', self.experiment.participant.computerId)

                                  , ('experiment',self.expType),('type',self.type)
                                  ,('dps',self.expDps), ('blockDP', self.relativeDp)
                                  ,('DP', self.absoluteDp), ('absOrder',self.expAbsoluteOrder), ('relOrder',self.expOrder)
                    , ('date',self.date),('time',self.time)
                   , ('learningMode',self.learningMode)
                   ,('nLearningTrials', self.experiment.nLearningTrials)
                   ,('nExtraLearningTrials', self.experiment.nTotalExtraLearningTrials)
                   , ('nTotalLearningTrials', self.experiment.nTotalLearningTrials)
                   , ('nConsequenceTrials', self.experiment.nConsequenceTrials)
                   , ('nTotalTrials', self.experiment.nTrials)
                   # ,('age', self.participantAge),('gender', self.participantGender),('eduLevel', self.participantEducationLevel)  # the collected demographics
                   ,('randomOrigin', self.randomOrigin)
                   , ('randomDestination', self.randomDestination)
                   , ('preferredRoute', self.experiment.preferredType)
                   ,('controlRoute(c)',self.controlRoute)
                   ,('treatmentRoute(t)', self.treatmentDirection)
                   , ('preferredDirection', self.preferredRoute)
                   , ('controlColor(c)', self.experiment.controlColor)
                   , ('treatmentColor(t)', self.experiment.treatmentColor)
                   , ('preferredColor', self.experiment.preferredColor)
                   , ('certaintyLevel', str(self.experiment.certaintyLevel))
                   ])
        if not colLabels:
            valuesCsv = []
            for attribute in dictCsv.keys():
                valuesCsv.append(dictCsv[attribute])

            return valuesCsv

        else:
            return list(dictCsv.keys())

class DescriptiveLearningResponse(ExperimentResponse):
    def __init__(self, experiment, nTrial, trial, nLearningTrials,date,time, learningMode
                 # ,randomOrigin,randomDestination
                 , participant
                 , treatmentDirection, controlRoute
                 , waitingTimeShown, travelTimeShown, journeyTimeShown
                 # , waitingTimeControl, travelTimeControl,journeyTimeControl
                 # , waitingTimeTreatment, travelTimeTreatment, journeyTimeTreatment

                 ):

        super().__init__(experiment = experiment, nLearningTrials = nLearningTrials, learningMode = learningMode
                         , date = date, time = time
                         , participant = participant
                         , treatmentDirection = treatmentDirection, controlRoute = controlRoute)

        self.waitingTimeShown = waitingTimeShown
        self.travelTimeShown = travelTimeShown
        self.journeyTimeShown = journeyTimeShown

        # self.randomOrigin = randomOrigin
        # self.randomDestination = randomDestination

        # # Information about Control Route (For experiment 3 and 4, this information changes in each learning trial)
        # self.waitingTimeControl = waitingTimeControl
        # self.travelTimeControl = travelTimeControl
        # self.journeyTimeControl = journeyTimeControl
        #
        # # Treatment Route
        # self.waitingTimeTreatment = waitingTimeTreatment
        # self.travelTimeTreatment = travelTimeTreatment
        # self.journeyTimeTreatment = journeyTimeTreatment

        self.nTrial = nTrial
        self.trial = trial

        self.expOrder = experiment.descriptionOrderId
        self.expAbsoluteOrder = experiment.descriptionOrderId #This is not working well right now


    # If colLabels is true it is because the file for writing does not have any registry
    def createLineExperimentResponsesCsv(self, experimentalCondition, colLabels = False):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        dictCsv = OrderedDict([('experimentalCondition', experimentalCondition), ('participantId', self.experiment.participant.id)
                                  , ('participantName', self.experiment.participant.name)
                                  , ('computerId', self.experiment.participant.computerId)

            ,('experiment', self.expType),('dps',self.expDps),('dps',self.expDps), ('blockDP', self.relativeDp)
                                  , ('DP', self.absoluteDp), ('absOrder',self.expAbsoluteOrder),('relOrder',self.expOrder)
                                  , ('date',self.date),('time',self.time)
                   ,('simulatedDay', self.nTrial)
                   , ('descriptiveDay', self.trial.descriptiveDay)
                   , ('typeTrial', self.trial.type)
                   # , ('nLearningTrials', self.nLearningTrials)
                   ,('learningMode',self.learningMode)
                    ,('alternative',self.trial.descriptiveTable)
                    , ('route',self.trial.typeRouteSelected)
                    , ('direction', self.trial.direction)
            # , ('age', self.participantAge), ('gender', self.participantGender)
            # , ('eduLevel', self.participantEducationLevel)  # the collected demographics
            # , ('randomOrigin',self.randomOrigin)
            # , ('randomDestination',self.randomDestination)
            # , ('routeShown', self.typeShown)
            , ('controlRoute(c)', self.controlRoute)
            , ('treatmentRoute(t)', self.treatmentDirection)
            # , ('directionShown', self.directionShown)
            # , ('controlColor(c)', self.trial.controlColor)
            # , ('treatmentColor(t)', self.trial.treatmentColor)
            # , ('colorShown', self.colorShown)
            , ('waiting', round(self.waitingTimeShown,2))
            , ('travel', round(self.travelTimeShown,2))
            , ('journey', round(self.journeyTimeShown,2))

            # , ('waiting(c)', round(self.waitingTimeControl,2))
            # , ('travel(c)', round(self.travelTimeControl,2))
            # , ('journey(c)', round(self.journeyTimeControl,2))
            #
            # , ('waiting(t)', round(self.waitingTimeTreatment,2))
            # , ('travel(t)', round(self.travelTimeTreatment,2))
            # , ('journey(t)', round(self.journeyTimeTreatment,2))
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

class DescriptiveChoiceResponse(ExperimentResponse):

    def __init__(self, experiment, nLearningTrials, date, time, learningMode
                 , participant
                 , preferredRoute, treatmentDirection, controlRoute):

        super().__init__(experiment=experiment, nLearningTrials=nLearningTrials, learningMode=learningMode
                         , date=date, time=time
                         , participant = participant
                         , treatmentDirection=treatmentDirection, controlRoute=controlRoute)

        self.preferredRoute = preferredRoute
        self.expOrder = experiment.descriptionOrderId
        self.expAbsoluteOrder = experiment.descriptionOrderId  # This is not working well right now

    # If colLabels is true it is because the file for writing does not have any registry
    def createLineExperimentResponsesCsv(self, experimentalCondition, colLabels = False):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        dictCsv = OrderedDict([('experimentalCondition', experimentalCondition), ('participantId', self.experiment.participant.id)
                                  , ('participantName', self.experiment.participant.name)
                                  , ('computerId', self.experiment.participant.computerId)
            ,('experiment', self.expType),('dps',self.expDps),('dps',self.expDps), ('blockDP', self.relativeDp)
                                  , ('DP', self.absoluteDp), ('absOrder',self.expAbsoluteOrder),('relOrder',self.expOrder)
                                  , ('date',self.date),('time',self.time)
            , ('nDescriptiveTrials', self.experiment.nDescriptiveTrials), ('learningMode', self.learningMode)
            # , ('age', self.participantAge, 'gender', self.participantGender)
            # , ('eduLevel', self.participantEducationLevel)  # the collected demographics
            , ('preferredRoute', self.experiment.preferredDescriptiveType)
            , ('controlRoute(c)', self.controlRoute)
            , ('treatmentRoute(t)', self.treatmentDirection)
            , ('preferredDirection', self.experiment.preferredDescriptiveJourney)

            , ('controlAlternative(c)', self.experiment.controlAlternative)
            , ('treatmentAlternative(t)', self.experiment.treatmentAlternative)
            , ('preferredAlternative(t)', self.experiment.preferredDescriptiveAlternative)


                   ])

        if not colLabels:
            valuesCsv = []
            for attribute in dictCsv.keys():
                valuesCsv.append(dictCsv[attribute])

            return valuesCsv

        else:
            return list(dictCsv.keys())

# class ResponseExperiment1(ResponseExperiment):
#     def __init__(self, expType, participant):
#         super().__init__(participant = participant, expType=expType)
#
# class ResponseExperiment2(ResponseExperiment):
#     def __init__(self, expType, participant):
#         super().__init__(participant = participant, expType=expType)
#
# class ResponseExperiment3(ResponseExperiment):
#     def __init__(self, expType, participant):
#         super().__init__(participant = participant, expType=expType)
#
# class ResponseExperiment4(ResponseExperiment):
#     def __init__(self, expType, participant):
#         super().__init__(participant = participant, expType=expType)