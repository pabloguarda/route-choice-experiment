def createPreferredJourneyInstructions(self, experiment, txtFileName):
    # Readtxt file with the generic instruction
    fileInstruction = open("Descriptions/" + txtFileName, 'r')
    infoFileInstruction = fileInstruction.readlines()
    fileInstruction.close()

    dictNewLabels = {'_origin_': experiment.currentTrial.randomOrigin,
                     '_destination_': experiment.currentTrial.randomDestination}

    instructions = ""

    for paragraph in infoFileInstruction:
        for label in dictNewLabels.keys():
            paragraph = paragraph.replace(str(label), str(dictNewLabels[label]))
        instructions += paragraph + "\n"

    return instructions

def runExperimentTrial1(self):
    currentTrialExp1 = self.trialsExp1[self.nExperimentTrial]

    self.launchExperiment()

    self.nTrialExp1 += 1

    return currentTrialExp1


def runExperimentTrial2(self):
    currentTrialExp2 = self.trialsExp2[self.nTrialExp2]

    self.launchExperiment()

    self.nTrialExp2 += 1

    return currentTrialExp2


def runExperimentTrial3(self):
    currentTrialExp3 = self.trialsExp3[self.nTrialExp3]

    self.launchExperiment()

    self.nTrialExp3 += 1

    return currentTrialExp3


def buttonNextSimulationExpPage():
    # Go to the last page of the stacked Widget (Debrief Page)
    ui.stackedWidget.setCurrentIndex(ui.stackedWidget.currentIndex() + 1)  # Go to next page

ui.buttonNextSimulationExpPage.clicked.connect(buttonNextSimulationExpPage)

# ***************   Indicators for the journey *************************************** #

def createJourneyIndicators():

    #Time
    ui.waitingTimeTitle.setText("Waiting Time")
    ui.waitingTimeLbl.setText("")
    ui.travelTimeTitle.setText("Travel Time")
    ui.travelTimeLbl.setText("")
    ui.walkingTimeTitle.setText("Walking Time")
    ui.walkingTimeLbl.setText("")
    ui.journeyTimeTitle.setText("Journey Time")
    ui.journeyTimeLbl.setText("")
    ui.dwellTimeTitle.setText("Dwell Time")
    ui.dwellTimeLbl.setText("")

    #Distance
    ui.walkingDistanceTitle.setText("Walking Distance")
    ui.walkingDistanceLbl.setText("")
    ui.travelDistanceTitle.setText("Travel Distance")
    ui.travelDistanceLbl.setText("")
    ui.journeyDistanceTitle.setText("Journey Distance")
    ui.journeyDistanceLbl.setText("")


createJourneyIndicators()

#It updates the panel with all the indicators for that trip
def updateJourneyIndicators():

    decimals = 1

    #Indicators (Time and Distance)

    ui.waitingTimeLbl.setText(str(round(window.currentTrip.waitingTime,decimals)))
    ui.walkingTimeLbl.setText(str(round(window.currentTrip.walkingTime,decimals)))
    ui.travelTimeLbl.setText(str(round(window.currentTrip.travelTime,decimals)))
    ui.dwellTimeLbl.setText(str(round(window.currentTrip.dwellTime,decimals)))
    ui.journeyTimeLbl.setText(str(round(window.currentTrip.journeyTime, decimals)))

    ui.walkingDistanceLbl.setText(str(round(window.currentTrip.walkingDistance,decimals)))
    ui.travelDistanceLbl.setText(str(round(window.currentTrip.travelDistance,decimals)))
    ui.journeyDistanceLbl.setText(str(round(window.currentTrip.journeyDistance, decimals)))


# ***************   Miscellaneous *************************************** #

# middlePoint = ui.visualRoute.width()/2-ui.busIcon.width()/2

# ui.busIcon.setGeometry(ui.visualRoute.x()+middlePoint, ui.visualRoute.y(), window.iconWidth, window.iconHeight)




# ui.passengerIcon.setPixmap(QtGui.QPixmap("Pictures/passenger.png"))

#
# # Hide picture of the marble that was not picked and keep the picture of the picked marble (e.g. if the user picked the blue marble, the picture of the red marble is hidden)
# if window.marblePicked == "blue":
#     ui.lblRedMarble.hide()
#     ui.lblBlueMarble.setGeometry(ui.lblPickedMarble.x(), ui.lblPickedMarble.y(), marbleWidth, marbleHeight)
#
# else:
#     ui.lblBlueMarble.hide()
#     ui.lblRedMarble.setGeometry(ui.lblPickedMarble.x(), ui.lblPickedMarble.y(), marbleWidth, marbleHeight)
#
# # Display a message showing whether the participant wins a prize for picking the marble.
# ui.lblDebrief2.setText(window.currentTrial.debriefMessage())
# ui.lblDebrief2.setWordWrap(True)
# ui.lblDebrief2.setGeometry(ui.lblDebrief2.x(), ui.lblDebrief2.y(), 400, 100)



# for i in range(ui.originGrid.count()):
#     if isinstance(ui.originGrid.itemAt(i).widget(),ClickableIconOption):
#         ui.originGrid.itemAt(i).widget().clicked.connect(tripGeneration)
#
# for i in range(ui.destinationGrid.count()):
#     if isinstance(ui.destinationGrid.itemAt(i).widget(), ClickableIconOption):
#         ui.destinationGrid.itemAt(i).widget().clicked.connect(tripGeneration)
#
# for i in range(ui.directionGrid.count()):
#     if isinstance(ui.directionGrid.itemAt(i).widget(), ClickableIconOption):
#         ui.directionGrid.itemAt(i).widget().clicked.connect(tripGeneration)
#
# for i in range(ui.modeGrid.count()):
#     if isinstance(ui.modeGrid.itemAt(i).widget(), ClickableIconOption):
#         ui.modeGrid.itemAt(i).widget().clicked.connect(tripGeneration)

window.originSelected = None
window.destinationSelected = None
window.clockwiseSelected = None
window.transportModeSelected = None

window.originClicked = None
window.destinationClicked = None
window.clockwiseClicked = None
window.transportModeClicked = None
window.startJourney = None


def tripGeneration():

    journeyClickableLabelClicked = ui.journeyClickableGrid.sender()

    originClicked = ui.originGrid.sender() #Identify which of the origins "Clickedlabel" emitted the signal
    destinationClicked = ui.destinationGrid.sender()  # Identify which of the destinations "Clickedlabel" emitted the signal
    directionClicked = ui.directionGrid.sender()  # Identify which of the direction "Clickedlabel" emitted the signal
    modeClicked = ui.modeGrid.sender()  # Identify which of the mode "Clickedlabel" emitted the signal

    # if window.originClicked in [ui.originGrid.widgets]:
    #     window.originClicked = originClicked
    #     oneClickedLabel(clickedLabel=window.originClicked, grid=ui.originGrid)
    #
    # if window.destinationSelected != None:
    #     window.destinationClicked = destinationClicked
    #     oneClickedLabel(clickedLabel=window.destinationClicked, grid=ui.destinationGrid)
    #
    # if window.clockwiseSelected != None:
    #     window.directionClicked = directionClicked
    #     oneClickedLabel(clickedLabel=window.directionClicked, grid=ui.directionGrid)
    #
    # if window.transportModeSelected != None:
    #     oneClickedLabel(clickedLabel=modeClicked, grid=ui.modeGrid)

    if originClicked == ui.originHomeSelectedIcon:
        window.originSelected = window.currentPassenger.homePosition
        #Set the background color of the others clickedLabels in blank

    if originClicked == ui.originWorkSelectedIcon:
        window.originSelected = window.currentPassenger.workPosition
        #Set the background color of the others clickedLabels in blank

    if destinationClicked == ui.destinationWorkSelectedIcon:
        window.destinationSelected = window.currentPassenger.workPosition

    if destinationClicked == ui.destinationHomeSelectedIcon:
        window.destinationSelected = window.currentPassenger.homePosition

    if directionClicked == ui.directionClockwiseSelectedIcon:
        window.clockwiseSelected = True #

    if directionClicked == ui.directionCounterClockwiseSelectedIcon:
        window.clockwiseSelected = False #

    if modeClicked == ui.bus1ModeSelectedIcon:
        window.transportModeSelected = "Bus1"

    if modeClicked == ui.drivingModeSelectedIcon:
        window.transportModeSelected = "Driving"


    if modeClicked == ui.walkingModeSelectedIcon:
        window.transportModeSelected = "Walking"

    if window.originSelected != None and window.destinationSelected != None and window.clockwiseSelected !=None and window.transportModeSelected != None and window.startJourney != None:

        window.currentPassenger.position = window.originSelected

        if window.transportModeSelected == "Walking":
            #Generate a trajectory with the class ITS
            # window.currentNetwork.buses["bus1"].speed

            if window.destinationSelected == window.currentPassenger.workPosition:
                ui.passengerIcon.setPixmap(QtGui.QPixmap("Pictures/walkingWork.png"))
                ui.passengerIcon.setScaledContents(True)
                # ui.passengerIcon.setFrameShape(QFrame.Box)

                # trajectory = window.its.trajectory(origin = window.originSelected,destination = window.destinationSelected,network = window.currentNetwork,clockwise = window.clockwiseSelected,timeInterval=1,speed = window.currentPassenger.walkingSpeed)
                #
                #  passengerWalkingStop(stop = window.currentNetwork.busStops["stop1"], clockwise = window.clockwiseSelected,passenger = window.currentPassenger,network=window.currentNetwork)
                passengerWalkingWork(destination=window.destinationSelected, clockwise=window.clockwiseSelected,
                                     passenger=window.currentPassenger, network=window.currentNetwork)

            if window.destinationSelected == window.currentPassenger.homePosition:
                passengerWalkingHome(destination=window.destinationSelected, clockwise=window.clockwiseSelected,
                                     passenger=window.currentPassenger, network=window.currentNetwork)


        if window.transportModeSelected == "Driving":
            ui.passengerIcon.setPixmap(QtGui.QPixmap("Pictures/car.png"))
            ui.passengerIcon.setScaledContents(True)
            passengerDrivingWork(destination=window.currentPassenger.workPosition, clockwise=window.clockwiseSelected,
                                 passenger=window.currentPassenger, network=window.currentNetwork, car = window.car)


    # TripStage(origin = originClicked, destination = destinationClicked, mode = modeClicked, trajectory,departureTime, arrivalTime)


    def trajectory(self,origin,destination,network,clockwise,speed,timeInterval=1):

        positions = []
        #If the origin or the destination are higher than either the width or height of the network, it will make them equal
        if origin.x>network.width:
            origin.x = network.width

        if origin.y>network.height:
            origin.y = network.height

        #Points: Number of points to divide the shape of the network

        sideOrigin = self.sideDetection(origin,network)
        accDistance = 0
        accTime = 0
        accOrder = 0
        distance = self.distance(origin=origin,destination=destination,network=network,clockwise=clockwise)
        xts = [] #List with states of position-time
        segmentLength = timeInterval*speed

        while accDistance < distance:
            xt = XT(order = accOrder,position = Position(origin.x, origin.y),time = accTime)
            xts.append(xt)

            positions.append({'position':Position(origin.x, origin.y),'accDistance':accDistance})

            if clockwise == True:
                if sideOrigin in ["southWestCorner","west"]: #Bus needs to go North
                    origin.y += segmentLength
                    difference = network.height-origin.y  #If the position is higher than the limit of the vertical position of the network, the dif will be lower than 0
                    if difference < 0:
                        origin.x = abs(difference)
                        origin.y = network.height

                elif sideOrigin in ["northWestCorner", "north"]: #Bus needs to go East
                    origin.x += segmentLength
                    difference = network.width-origin.x
                    if difference < 0:
                        origin.y = origin.y-abs(difference)
                        origin.x = network.width

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
                    difference = network.width - origin.x
                    if difference < 0:
                        origin.y = origin.y + abs(difference)
                        origin.x = network.width

                elif sideOrigin in ["southEastCorner", "east"]: #Bus needs to go West
                    origin.y += segmentLength
                    difference = network.height - origin.y
                    if difference < 0:
                        origin.x = origin.x - abs(difference)
                        origin.y = network.height

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

            sideOrigin = self.sideDetection(origin, network)
            accDistance += segmentLength
            accOrder += 1
            accTime += timeInterval

        positions.append({'position': destination, 'accDistance': distance})

        return {'positions':positions, 'xts':xts}
        # network.northEastCorner


    # #Home Position
    # homeVirtualPosition = reMapping(position=window.person.homeLocation, realNetwork=window.network,
    #                                virtualNetwork=ui.virtualNetwork)
    #
    # # ui.homeIcon.setGeometry(homeVirtualPosition.x - window.iconWidth / 2, homeVirtualPosition.y - window.iconWidth / 2,
    # #                         window.iconWidth, window.iconHeight)
    #
    # ui.homeIcon.setGeometry(homeVirtualPosition.x - window.iconWidth / 2, homeVirtualPosition.y - window.iconWidth / 2,
    #                         window.iconWidth, window.iconHeight)


    #Bus Stops Position (4 bus stops)
    # stop1VirtualPosition = reMapping(position=window.network.busStops["stop1"].position, realNetwork=window.network,
    #                                 virtualNetwork=ui.virtualNetwork)
    #
    # ui.stop1Icon.setGeometry(stop1VirtualPosition.x - window.iconWidth / 2, stop1VirtualPosition.y - window.iconWidth / 2,
    #                          window.iconWidth, window.iconHeight)

    # stopWork2VirtualPosition = reMapping(position=window.network.busStops["stop2"].position,realNetwork=window.network,
    #                                 virtualNetwork=ui.virtualNetwork)
    #
    # ui.stop2Icon.setGeometry(stopWork2VirtualPosition.x - window.iconWidth / 2, stopWork2VirtualPosition.y - window.iconWidth / 2,
    #                          window.iconWidth, window.iconHeight)
    #
    # stop3VirtualPosition = reMapping(position=window.network.busStops["stop3"].position, realNetwork=window.network,
    #                                 virtualNetwork=ui.virtualNetwork)
    #
    # ui.stop3Icon.setGeometry(stop3VirtualPosition.x - window.iconWidth / 2, stop3VirtualPosition.y - window.iconWidth / 2,
    #                          window.iconWidth, window.iconHeight)
    #
    # stop4VirtualPosition = reMapping(position=window.network.busStops["stop4"].position,realNetwork=window.network,
    #                                 virtualNetwork=ui.virtualNetwork)
    #
    # ui.stop4Icon.setGeometry(stop4VirtualPosition.x - window.iconWidth / 2, stop4VirtualPosition.y - window.iconWidth / 2,
    #                          window.iconWidth, window.iconHeight)

    # #Terminals Positions
    # terminal1VirtualPosition = reMapping(position=window.network.busStops["stop1"].position, realNetwork=window.network,
    #                                 virtualNetwork=ui.virtualNetwork)
    #
    # ui.terminal1Icon.setGeometry(ui.terminal1IconVirtualPosition.x - window.iconWidth / 2, stop1VirtualPosition.y - window.iconWidth / 2,
    #                          window.iconWidth, window.iconHeight)



    # #Work Position
    # workVirtualPosition = reMapping(position = window.person.workLocation,realNetwork = window.network, virtualNetwork= ui.virtualNetwork)
    # ui.workIcon.setGeometry(workVirtualPosition.x-window.iconWidth/2, workVirtualPosition.y-window.iconWidth/2, window.iconWidth, window.iconHeight)
    # # ui.workIcon.setGeometry(workVirtualPosition.x, workVirtualPosition.y,
    # #                         window.iconWidth, window.iconHeight)
    #


# ui.passengerIcon.setGeometry(passengerVirtualPosition.x - 2*window.iconWidth / 2, passengerVirtualPosition.y - 2*window.iconWidth / 2,
    #                              window.iconWidth, window.iconHeight)

    # ui.homeIcon = NetworkLocationIcon(parent=ui.pageExpSimulation, path="Pictures/home.png", id = window.home.id)
    # ui.workIcon = NetworkLocationIcon(parent=ui.pageExpSimulation, path="Pictures/work.png", id = window.work.id)


window.iconWidth = 50
window.iconHeight = 50

# ui.gridIndicators.setEnabled(False)

# for icon in [ui.stop1Icon,ui.stop2Icon,ui.stop3Icon,ui.stop4Icon,ui.homeIcon,ui.workIcon,ui.terminal1Icon,ui.terminal2Icon,ui.terminal3Icon,ui.terminal4Icon]:
#     icon.setScaledContents(True)
#     icon.setFrameShape(QFrame.Box)
#     icon.setGeometry(icon.x(), icon.y(), window.iconWidth, window.iconHeight)
#     setBackgroundColorQLabel(icon,"white")


# #This loop set the same color for every page of the stacked widget
# for page in ui.stackedWidget.children():
#     if isinstance(page,QWidget):
#         backgroundStackedWidget(page, "white") #Set Background colour of all the stack pages

# mapResizing(virtualNetwork = ui.virtualNetwork,realNetwork = window.realNetwork , maxDim = window.maxDimVirtualNetwork)


def increaseWaitingTime():
    window.waitimeTime += 1

def decreaseWaitingTime():
    window.waitimeTime += 1

def increaseTravelTime():
    window.travelTime += 1

def decreaseTravelTime():
    window.travelTime += 1

# ***************   Timers *************************************** #

#Time bus and passenger moving

# ui.stop2Icon.clicked.connect(nextButtonExpSimulation)

#Timer for bus stop
myTimerBusStop = QTimer()
busStopTimerInterval = 0.2  #In seconds
busStopTimerCallBack = functools.partial(busStopTimer, busStop = window.realNetwork .busStops["stop2"],timeInterval = busStopTimerInterval,realNetwork = window.realNetwork,its = window.its,nextBusLbl = ui.nextBusLbl)
myTimerBusStop.timeout.connect(busStopTimerCallBack)
myTimerBusStop.start(busStopTimerInterval*1000)

myTimerBusPositions = QTimer()

# busPositionsTimerInterval = window.busRoute1.headway/10 #In seconds
# busPositionsTimerInterval = 1 #In seconds
# myTimerBusPositions.timeout.connect(busPositions)
# myTimerBusPositions.start(busPositionsTimerInterval*1000)

#Timer for bus movement
myTimerBus = QTimer()
busTimerInterval = 0.2 #In seconds
# window.realNetwork .buses["bus1"].position = window.realNetwork .busStops["2"].position

# #This allow to add arguments in the function linked with the timer
# timerBusCallBack = functools.partial(busMovingTimer,bus=window.realNetwork .buses["bus1"], destination=window.realNetwork .busStops["2"].position,realNetwork=window.realNetwork ,clockwise=False,timeInterval=busTimerInterval)
# myTimerBus.timeout.connect(timerBusCallBack)
# myTimerBus.start(busTimerInterval*1000)

# #We need to make a copy of the icon, otherwise the icon of all buses will be referenced to the same object.
# copyBusRouteIcon = VehicleIcon(parent=ui.expSimulationPanel, path="Pictures/bus1.png", id=window.busRoute1Counterclockwise,
#                            realNetwork=window.realNetwork, virtualNetwork=ui.virtualNetwork,
#                            position=window.busRoute1Clockwise.departureTerminal, width=window.vehicleIconWidth * 0.3,
#                            height=window.vehicleIconHeight * 0.3)

# newBusRunTimer = QTimer()
#
# newBusRunTimer.setInterval()
# def busRunsGeneration(busRoute):
#     newBusRunTimerCallBack = functools.partial(busGeneration, busRoute = busRoute)
#     newBusRunTimer.timeout.connect(newBusRunTimerCallBack)
#     newBusRunTimer.setInterval()
#     newBusRunTimer.singleShot(1)
#     # newBusRunTimer.start(1 * 1000)#Timer for passenger walking to the Stop
#     # newBusRunTimer.stop()
#     # busGeneration(busRoute=busRoute)


# # Timer for bus stop
    # window.myTimerBusStop = QTimer()
    # busStopTimerInterval = 0.2  # In seconds
    # busStopTimerCallBack = functools.partial(busStopTimer, busStop=window.realNetwork.busStops["stop2"],
    #                                          timeInterval=busStopTimerInterval, its=window.its,
    #                                          nextBusLbl=ui.timeNextBusLbl)
    # window.myTimerBusStop.timeout.connect(busStopTimerCallBack)
    # myTimerBusStop.start(busStopTimerInterval*1000)

    myTimerBusPositions = QTimer()

    # busPositionsTimerInterval = window.busRoute1.headway/10 #In seconds
    # busPositionsTimerInterval = 1 #In seconds
    # myTimerBusPositions.timeout.connect(busPositions)
    # myTimerBusPositions.start(busPositionsTimerInterval*1000)

    # Timer for bus movement
    myTimerBus = QTimer()
    busTimerInterval = 0.2  # In seconds
    # window.realNetwork .buses["bus1"].position = window.realNetwork .busStops["2"].position

    # #This allow to add arguments in the function linked with the timer
    # timerBusCallBack = functools.partial(busMovingTimer,bus=window.realNetwork .buses["bus1"], destination=window.realNetwork .busStops["2"].position,realNetwork=window.realNetwork ,clockwise=False,timeInterval=busTimerInterval)
    # myTimerBus.timeout.connect(timerBusCallBack)
    # myTimerBus.start(busTimerInterval*1000)


    # ui.metroModeSelectedIcon = ClickableOptionIcon(parent = ui.simulationExpPanel, type = "mode", id = "metro", path= "Pictures/TfLStation.png",myGrid = ui.modeGrid)
    # ui.wheelchairModeSelectedIcon = ClickableOptionIcon(parent = ui.simulationExpPanel, type = "mode", id = "wheelchair", path= "Pictures/wheelchair.png",myGrid = ui.modeGrid)
    # ui.bus1ModeSelectedIcon = ClickableOptionIcon(parent = ui.simulationExpPanel, type = "mode", id = "bus1", path= "Pictures/bus1.png",myGrid = ui.modeGrid)
    # ui.bus2ModeSelectedIcon = ClickableOptionIcon(parent = ui.simulationExpPanel, type = "mode", id = "bus2", path= "Pictures/bus2.png",myGrid = ui.modeGrid)
    # ui.carSharingModeSelectedIcon = ClickableOptionIcon(parent = ui.simulationExpPanel, type = "mode", id = "taxi", path= "Pictures/taxi.png",myGrid = ui.modeGrid)

# Calculate , departureTime, arrivalTime
# self.departureTime = departureTime
# self.arrivalTime = arrivalTime


# def walk(self,trajectory):
#     self.walkingDistance +=
#     self.move(trajectory)
#
# self.walking = True
# self.destination = destination
# self.position = self.trajectory[self.positionTrajectory]['position']
#
# if self.positionTrajectory == len(self.trajectory)-1:
#     self.stop()
#
# self.walkingTime += timeInterval
# self.positionTrajectory += 1


def tripDuration(self, trajectory):
    a = 0
    #
    # for xt in trajectory.xts:
    #     xt.order == trajectory.xts
    #
    #     xt.position
    #
    # max()


# Generate instances of speed using a probability distribution
def speedGeneration(self):
    a = 0


# Randomly allocate buses in the network based on the number of vehicles and their speed. We assume all buses has the same speed.
# According to the headway desired it generate a list of buses

def busRouteGeneration(self, headway, speed):
    # Generate a list of buses
    a = 0


# This method find the number of buses and what speed they should have to achieve the desire headway (seconds) and travel time (seconds)
def busScheduling(self, travelTime, headway, departureStop, arrivalStop, direction, busRoute):
    distanceBusStops = self.shortestPathDistance(origin=departureStop.position, destination=arrivalStop.position,
                                                 realNetwork=self.realNetwork)

    # Speed needed to have the required travel time. We assumed the speed is constant in each segment of the bus route.
    routeSpeed = distanceBusStops / travelTime

    # def busOptimizatoin(self):

    # #Cycle time is the amount of time needed by a bus to make a run between the terminals
    # distanceBetweenBusTerminals = self.shortestPathDistance(departureStop.position, arrivalStop.position,realNetwork = realNetwork)
    # timeBetweenBusTerminals = distanceBetweenBusTerminals/routeSpeed #The amount of time a bus need to travel between two terminals


    #     # The number of buses departing from the terminal per unit of time to provide the required headway (time interval between buses)
    #     nBuses = timeBetweenBusTerminals / headway
    #
    #     # The number of bus dispatches per unit of time is calculated based on the headway
    #     headway
    #
    #     # The number of buses needs to be an integer number so we need to round up the number
    #     nBuses = roundUp(nBuses)

    # After doing this approximation, the buses will increase and thus, the headway will decrease. To keep the same headway, a solution is holding buses in bus terminals.
    # By holding buses in terminals, we increase the cycle time per bus and thus, we can reduce the headway at the desired level




    # The frequency of buses per unit of time


# def nextBus(self,busStop,realNetwork):
#     #It will return the the bus that is closest the the bus stop
#     arrivalTimes = self.arrivalTimes(busStop,realNetwork)
#     for bus i in arrivalTimes.keys():
#
#         self.arrivalTimes
#
#
#     return self.travelTime(self,origin,destination,realNetwork,!clockwise,speed)

# Object of class point()
def euclideanDistance(self, position1, position2):
    return ((position1.x - position2.x) ** 2, (position1.y - position2.y) ** 2) ** (0.5)


def travelTimeEstimation(self, origin, destination):
    distance = self.euclideanDistance(origin, destination)
    speed = self.realNetwork.networkSpeed
    travelTime = distance / speed
    return travelTime

#In class animations

def busStopTimer(busStop,timeInterval,its,nextBusLbl):
    arrivalTimes = its.arrivalTimes(busStop = busStop)
    nextBusLbl.setText(str(int(round(arrivalTimes["bus1"],0)))) #The distance now is calculated with bus 1 but will be generalized
    # its.createTrajectory(origin = busStop.position, destination = bus.position,realNetwork = realNetwork,clockwise = not bus.clockwise,t)


# def personTravellingTimer(timeInterval,person,bus,timer,destination,travelTimeLbl,its, icon):
#     if person.travelling == True:personWalkingHomeTimer(destination,clockwise,person,myTimer,its,timerInterval)
#         person.travel(timeInterval = timeInterval,travelSpeed = bus.speed,destinatio= destination) #in seconds.
#         travelTimeLbl.setText(str(int(round(person.travelTime,1))))
#         moveBus(bus = bus, destination = destination, clockwise = bus.clockwise, timeInterval = timeInterval)
#         personMovingUI(person = person,destination = destination, clockwise = bus.clockwise,timeInterval = timeInterval, icon = icon)
#     else:
#         timer.stop()

# # If in addition the person has arrived to his final destination
# if its.equalPositions(person.position, person.finalLocation.position):
#     a = 0




#Creation of timers to show travel and waiting times

def busMovingTimer(bus,destination,its,clockwise,timeInterval,myTimerBus,person):
    realNetwork = its.realNetwork
    moveBus(bus,destination,realNetwork,clockwise,timeInterval)
    if bus.moving == False:
        myTimerBus.stop()
        person.waiting = False

        # myTimerPersonTravelling  = QTimer()
        # window.person.travel(0,bus.speed,destination = window.person.homeLocation)
        # PersonTravelTimerInterval= 1 #In seconds
        # timerPersonWaitingCallBack = functools.partial(personTravellingTimer,person = window.person,timeInterval =  PersonTravelTimerInterval,timer = myTimerPersonTravelling,bus=bus,destination = window.person.homeLocation)
        # myTimerPersonTravelling.timeout.connect(timerPersonWaitingCallBack)
        # myTimerPersonTravelling.start(PersonTravelTimerInterval * 1000)

def updateWalkingIndicators(walkingTimeLbl,walkingDistanceLbl,person):
    walkingTimeLbl.setText(str(int(round(person.walkingTime,0))))
    walkingDistanceLbl.setText(str(round(person.walkingTime*person.walkingSpeed,1)))

#The floowing is was in method to move the person

# if its.equalPositions(person.position,destination): #If the person arrives to destination, he will not be walking
#     myTimer.stop()
# #     a= 0
#
#     #If person is going home, he will be waiting only in the bus stop nearby his work
#     if person.destination in [realNetwork.busStops["stop1"].position,realNetwork.busStops["stop2"].position]:
#
#         myTimerPersonWaiting = QTimer()
#
#         person.waitBusStop(0) #Person start waiting
#         PersonWaitingTimerInterval = 1 #In seconds
#         timerPersonWaitingCallBack = functools.partial(personWaitingTimer,person = person,timeInterval = PersonWaitingTimerInterval,timer = myTimerPersonWaiting)
#         myTimerPersonWaiting.timeout.connect(timerPersonWaitingCallBack)
#         myTimerPersonWaiting.start(PersonWaitingTimerInterval * 1000)
#     # ui.waitingTimeLbl.setText("Waiting")
#     # personWaitingTimer(timeInterval = PersonWaitingTimerInterval*1000)


#Class ITS: Functions for moving the bus has these lines

# if self.equalPositions(bus.position, trajectory.destination) == True:
#     bus.

# if self.equalPositions(bus.position,bus.route.arrivalTerminal.position):
#     trajectory = self.createTrajectory(origin=bus.position, destination=bus.route.departureTerminal.position,
#                                        clockwise= not trajectory.direction.isClockwise(),
#                                        speed=trajectory.speed)['trajectory']
#     bus.move(trajectory=trajectory)  # if the bus is already moving there will be a trajectory and direction previously defined
#     self.updateVehicleMapPosition(vehicle=bus, icon=bus.icon)
# else:
#     trajectory = self.createTrajectory(origin=bus.position, destination=bus.route.arrivalTerminal.position,
#                           clockwise=trajectory.direction.isClockwise(),
#                           speed=trajectory.speed)['trajectory']
#     bus.move(trajectory=trajectory)  # if the bus is already moving there will be a trajectory and direction previously defined
#     self.updateVehicleMapPosition(vehicle=bus, icon=bus.icon)


routesToHome = []  # List of routes that leaves you close to home
for route in window.realNetwork.busRoutes:
    if route.arrivalTerminal == window.busTerminal4 or route.arrivalTerminal == window.busTerminal1:
        routesToHome.append(route)

if window.directionTripStage.id == "clockwise":
    for route in routesToHome:
        if route.direction.isClockwise():
            busRunGeneration(busRoute=route, myTimer=window.completeBusRunTimer, randomDelay=0)

if window.destinationTripStage == window.person.workLocation:
    routesToWork = []  # List of routes that leaves you close to work

    for route in window.realNetwork.busRoutes:
        if route.arrivalTerminal == window.busTerminal2 or route.arrivalTerminal == window.busTerminal3:
            busRunGeneration(busRoute=route, myTimer=window.completeBusRunTimer, randomDelay=0)
            routesToWork.append(route)



            # trajectory = window.its.createTrajectory(origin = window.originSelected,destination = window.destinationSelected,clockwise = window.clockwiseSelected,timeInterval=1,speed = window.person.walkingSpeed)
            #
            #  personWalkingStop(stop = window.realNetwork .busStops["stop1"], clockwise = window.clockwiseSelected,person = window.person,realNetwork=window.realNetwork )

            # tripStage = TripStage(window.person, origin = window.originTripStage, destination = window.destinationTripStage,mode = window.modeTripStage,trajectory = currentTrajectory)
            # window.person.position = window.person.homeLocation)
currentTrajectory = window.its.createTrajectory(origin = window.originTripStage.position,destination = window.destinationTripStage.position, clockwise = window.directionTripStage.isClockwise(), speed = window.modeTripStage.speed)

# bus.position = Position(busPosition.x,busPosition.y)
    # busVirtualPoint = reMapping(position = bus.position, virtualNetwork=its.virtualNetwork, realNetwork=its.realNetwork)

    #Assign a number to each bus and add each bus run in a list or registry
    # ui.bus11Icon = VehicleIcon(parent=ui.expSimulationPanel, path= "Pictures/bus1.png", id = "bus",
    #                                        realNetwork=window.realNetwork , virtualNetwork=ui.virtualNetwork,
    #                                        position=window.busTerminal1.position, width=window.terminalIconWidth,
    #                                        height=window.terminalIconHeight)

    # bus.icon.setGeometry(busVirtualPoint.x-bus.icon.width()/2, busVirtualPoint.y-bus.icon.height()/2, bus.icon.width(), bus.icon.height())
    # ui.travelDistanceLbl.setText(str(round(busAccDistance,2)))


    # if its.equalPositions(bus.position,trajectoryBusStop.destination)
    #     a=0
        # myTimer.stop()

# def busPositions():
#
#     # myTimerBusMoving = QTimer()
#     # busMovingTimerInterval = 0.5
#     # myTimerBusPositions.timeout.connect(busPositions)
#
#     ui.bus11Icon = PersonIcon(parent=ui.expSimulationPanel, path="Pictures/person.png", id="bus11")
#     bus11VirtualPosition = reMapping(position=window.bus11.position,realNetwork = window.realNetwork , virtualNetwork= ui.virtualNetwork)
#     ui.bus11Icon.setGeometry(200, 200, window.iconWidth, window.iconHeight)
#     # ui.bus11Icon.setGeometry(bus11VirtualPosition.x- window.iconWidth / 2, bus11VirtualPosition.y - window.iconWidth / 2, window.iconWidth, window.iconHeight)
#     # ui.bus11Icon.setScaledContents(True)
#
#     startBusRun(bus = window.bus11,
#             destination = window.busRoute1.arrivalTerminal,realNetwork = window.realNetwork,clockwise = window.busRoute1.direction.isClockwise(),timeInterval = 1)
#     # personTimerInterval = 0.2  #In seconds
#     person.walkingSpeed = car.speed
#     busPositionsTimerCallBack = functools.partial(personWalkingUI,person=person, destination=destination,realNetwork=realNetwork,clockwise=clockwise,timeInterval=personTimerInterval)
#     myTimerPersonWalking.timeout.connect(personTimerCallBack)
#     myTimerPersonWalking.start(personTimerInterval*1000)




# walkingStop1TimerCallBack = functools.partial(personWalkingStop,stop = window.realNetwork .busStops["stop1"],clockwise = True)
# ui.stop1Icon.clicked.connect(walkingStop1TimerCallBack)
#
# walkingStop2TimerCallBack = functools.partial(personWalkingStop,stop = window.realNetwork .busStops["stop2"],clockwise = False)
# ui.stop2Icon.clicked.connect(walkingStop2TimerCallBack)
#
# walkingStop3TimerCallBack = functools.partial(personWalkingStop,stop = window.realNetwork .busStops["stop3"],clockwise = True)
# ui.stop3Icon.clicked.connect(walkingStop3TimerCallBack)
#
# walkingStop4TimerCallBack = functools.partial(personWalkingStop,stop = window.realNetwork .busStops["stop4"],clockwise = False)
# ui.stop4Icon.clicked.connect(walkingStop4TimerCallBack)

def personMovingUI(person,destination,clockwise,timeInterval,its,icon):
    realNetwork = its.realNetwork

    if person.walking == False:
        personTrajectory = its.createTrajectory(origin=person.position, destination=destination, clockwise=clockwise,speed=person.walkingSpeed)['positions']
        person.trajectory = personTrajectory

    # personPositions = trajectory[window.countPersonMovements]['position']
    # walkingAccDistance = trajectory[window.countPersonMovements]['accDistance']

    person.walk(timeInterval,destination = destination)

    its.updatePersonMapPosition(person = person, icon = icon)

    # def updateWalkingIndicators(walkingTimeLbl, walkingDistanceLbl, person):

    # bus.position = Position(busPosition.x,busPosition.y)
    # personVirtualTrajectory = reMapping(position=person.position, virtualNetwork=ui.virtualNetwork,
    #                                       realNetwork=window.realNetwork )

    # ui.personIcon.setGeometry(personVirtualTrajectory.x-window.iconWidth/2, personVirtualTrajectory.y-window.iconHeight/2, window.iconWidth, window.iconHeight)
    # ui.walkingDistanceLbl.setText(str(round(walkingAccDistance,2)))

# # Bus Stops (1,2,3,4)
# ui.originStop1SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "origin", id = "stop1", path="Pictures/stop1.png",myGrid = ui.originGrid)
# ui.originStop2SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "origin", id = "stop2", path="Pictures/stop2.png",myGrid = ui.originGrid)
# ui.originStop3SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "origin", id = "stop3", path="Pictures/stop3.png",myGrid = ui.originGrid)
# ui.originStop4SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "origin", id = "stop4", path="Pictures/stop4.png",myGrid = ui.originGrid)

# # Bus Stops (1,2,3,4)
# ui.destinationStop1SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "destination", id = "stop1", path="Pictures/stop1.png",myGrid = ui.destinationGrid)
# ui.destinationStop2SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "destination", id = "stop2", path="Pictures/stop2.png",myGrid = ui.destinationGrid)
# ui.destinationStop3SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "destination", id = "stop3", path="Pictures/stop3.png",myGrid = ui.destinationGrid)
# ui.destinationStop4SelectedIcon = ClickableOptionIcon(parent = ui.expSimulationPanel, type = "destination", id = "stop4", path="Pictures/stop4.png",myGrid = ui.destinationGrid)



# def hideNextJourneyButton(boolean):
#     if boolean == True:
#         # setBackgroundColorQLabel(ui.nextJourneyPanel, "White")
#         # ui.nextJourneyPanel.raise_()
#         ui.nextJourneyButton.hide()
#
#     else:
#         # ui.nextJourneyPanel.lower()
#         ui.nextJourneyPanel.hide()
#         # ui.nextJourneyButton.raise_()
#         ui.nextJourneyButton.show()
#
# def hideNextExperiment(boolean):
#     if boolean == True:
#         setBackgroundColorQLabel(ui.nextExperimentPanel, "White")
#         ui.nextExperimentPanel.raise_()
#
#     else:
#         ui.nextExperimentPanel.lower()


# Speeds
ui.walkingSpeedTitle.setText("Walking Speed")
ui.walkingSpeedLbl.setText("")
ui.travelSpeedTitle.setText("Travel Speed")
ui.travelSpeedLbl.setText("")

# #Time Next Bus
# ui.timeNextBusTitle.setText("Next Bus")
# ui.timeNextBusLbl.setText("")

ui.walkingSpeedLbl.setText(str(round(window.currentTrip.walkingSpeed, decimals)))
ui.travelSpeedLbl.setText(str(round(window.currentTrip.travelSpeed, decimals)))

# #If the mode is bus or walking
# if window.tripMode.id in [window.walkingMode.id,window.busMode.id]:
#     ui.walkingSpeedLbl.setText(str(window.person.walkingSpeed))
#     if window.tripMode.id == window.busMode.id:
#         window.its.stop
#
#
# elif window.tripMode.id == window.busMode.id:
#     ui.walkingSpeedLbl.setText(str(window.person.walkingSpeed))


#
# ui.initializeButton.clicked.connect(reset)

# def buttonNextConsentClicked():
#     if ui.cBoxConsent.checkState()==2: #If the consent check box is checked
#         ui.stackedWidget.setCurrentIndex(ui.stackedWidget.currentIndex() + 1) #Go to next page







def nextExpSimulationButton():
    ui.stackedWidget.setCurrentIndex(ui.stackedWidget.currentIndex() + 1)  # Go to next page

ui.nextExpSimulationButton.clicked.connect(nextExpSimulationButton)

def backButtonExpChoice():
    ui.stackedWidget.setCurrentIndex(ui.stackedWidget.currentIndex() - 1)  # Go to previous page

ui.ExpChoiceBackButton.clicked.connect(backButtonExpChoice)

# ui.initializeButton.clicked.connect(virtualInitialization)





# § connect its “timeout” signal to the function you want to repeat

# moveBus(trajectory=window.busTrajectory)

# its.createTrajectory(origin=Position(0,0),destination=window.person.workLocation,realNetwork=window.realNetwork ,clockwise=False)





# myTimer.setInterval(2000) # change the interval
# § start the timer, indicating the interval in milliseconds myTimer.start(2000) # execute funToRepeat every 2 seconds
# § Some useful methods of QTimer:
# § myTimer.setInterval(xxx) # change the interval
# § myTimer.setSingleShot(True) #will fire once after the interval § myTimer.stop() # stop it (e.g. after a countdown)

#
# brush = QtGui.QBrush(QtCore.Qt.SolidPattern)
#
# qp = QtGui.QPainter()
# qp.begin(ui)
# ui.drawText(event, qp)
# qp.end()

# ui.pageExpMode.setBrush(brush)
# ui.pageExpMode.drawRect(10, 15, 90, 60)

# ***************   Main Class Experiment Assignment 2 *************************************** #

# window.prize = 30 #Prize if the participant get the marble with the color defined in "window.colorPrize"
# window.randomColor = "blue" #To define the proportion of blue balls in the ambiguous urn, the number of "blue" balls is first defined randomly, and then the number of red balls is calculated as the difference with the total number of balls in the urn
# window.colorPrize = "blue"

# Name of the output files containing the information on the trials and experiments conducted by the experimenter
window.csvExperiment = "Experiment"+str(window.experimentId)+".csv"
window.csvParticipants = "Participants"+window.csvExperiment  # Filename for the output csv file

window.txtInstructions = "instructionsExperiment.txt" #Instructions of the experiment (page 3: Experiment)


# ***************   (Page 3) Experiment Assignment 2 *************************************** #

#Instructions of the experiment: Page 34, Pulford and Colman (2008)

# Create urns A and B without balls initially (See the class Urn in Urn.py for more details)
window.urnA = Urn("A")
window.urnB = Urn("B")

#Create an instance of the experiment (See the class Experiment in Experiment.py for more details)
window.currentExperiment = Experiment(nMarblesConditions=window.conditions,prize=window.prize,colorPrize=window.colorPrize
                                      ,randomColor=window.randomColor,experimentId=window.experimentId,urnA=window.urnA,urnB = window.urnB,csvExperiment=window.csvExperiment)

#This method of the class Experiment, Create a txt file with the number of marbles per condition and the name of the txt file where the participants trials will be written
window.currentExperiment.launchExperiment()

# Random selection of a certain condition in the experiment trial (Number of marbles per urn)
window.currentExperiment.randConditions()

#This variable holds the number of marbles in the current condition (randomly selected).
window.condition = window.currentExperiment.nMarbles

# Generate randomly the positions of the urns in the current experiment trial (i.e. which is the random urn)
window.currentExperiment.randPositions()

# Add the marbles to each urn based on the randomly selected condition (e.g. 4, 10 or 100)
window.currentExperiment.addMarbles()

#Instructions of the experiment for a given condition
window.instructions = window.currentExperiment.createInstruction(txtInstructions=window.txtInstructions)

#Create a Scroll Area Widget where a QLabel with the instruction of the experiment are displayed (ui.lblInstructions)
ui.scrollInstructionPage = QScrollArea(ui.pageExp)

#QLabel containing the instruction of the experiment
ui.lblInstructions = QLabel()

#Format of the Qlabel widget that displays the experiment's instructions to the user
ui.lblInstructions.setText(window.instructions)
ui.lblInstructions.setWordWrap(True)
ui.lblInstructions.setAlignment(QtCore.Qt.AlignTop)
ui.lblInstructions.setAlignment(QtCore.Qt.AlignLeft)

#Add label in the scroll area
ui.scrollInstructionPage.setWidget(ui.lblInstructions)
ui.scrollInstructionPage.setWidgetResizable(True) #The advantage of the scroll area has the advantage of being resizable.
ui.scrollInstructionPage.setFixedSize(ui.stackedWidget.width()*0.5,ui.stackedWidget.height()*0.5) #Set the size of the Scroll Area Widget to the hall of the size of the window

#Label created to describe the options that will be displayed to the user in the combobox widget.
ui.lblUrnSelection = QLabel(ui.pageExp)
ui.lblUrnSelection.setText("I prefer to draw a marble from Urn A/Urn B")
heightUrnSelection = 30
ui.lblUrnSelection.setGeometry(ui.scrollInstructionPage.x(),ui.scrollInstructionPage.y()+ui.scrollInstructionPage.height(),250,heightUrnSelection) #The widget is located just below the Scroll Area Widget.

#Combobox widget created to make easier to the user choose one of the urns
ui.cBoxUrnSelection = QComboBox(ui.pageExp)
ui.cBoxUrnSelection.addItems(["","Urn A","Urn B"]) #Options shown to the user in the combobox
ui.cBoxUrnSelection.setGeometry(ui.lblUrnSelection.x()+ui.lblUrnSelection.width(),ui.lblUrnSelection.y(),80,heightUrnSelection) #Format and position of the combobox (in the right next to the Qlabel "lblUrnSelection")

# An error is raised if the participant does choose an option in the combobox (Urn A or Urn B).
ui.lblErrorUrnSection = QLabel(ui.pageExp)

# Function "buttonNextExpClicked()"
# The error message shown in the Qlabel lblErrorUrnSection" is updated using this function
# This function executes the function createTrial(), which will register the information of the participant and the picked marble in a given trial.
def buttonNextExpClicked():

    urnASelected = ui.cBoxUrnSelection.currentText() == "Urn A"
    urnBSelected = ui.cBoxUrnSelection.currentText() == "Urn B"

    # Check if the participant choose an option and hold that value in a trial object in the Experiment class.
    if urnASelected or urnBSelected:
        if urnASelected:
            window.urnSelected = "A"
        if urnBSelected:
            window.urnSelected = "B"

        #Go to the next page
        window.currentExperiment.pickMarble(window.urnSelected) #This method pick a marble of the urn selected by the participant (A or B)
        window.marblePicked = window.currentExperiment.marblePicked #Return the label 'Blue' or 'Red' according the proportions of blue and red marbles in the selected urn
        # ui.lblMarblePicked.setText(window.marblePicked)  # window.urnChosen is the label of the urn selected

        #This function updates the contents of the Debrief page (see the description below)
        debriefPage()

        #Go to the last page of the stacked Widget (Debrief Page)
        ui.stackedWidget.setCurrentIndex(ui.stackedWidget.currentIndex() + 1)  # Go to next page

    else:
        #Here I should show an error message asking to the paricipant to select an option (created a method to use here and for the demographics).
        window.urnChosen = None  # The participant has not selected an option yet. I add this conditional just for readibility

        setRedLettersQLabel(Qlabel=ui.lblErrorUrnSection)
        ui.lblErrorUrnSection.setText("Please choose an Urn")
        ui.lblErrorUrnSection.setGeometry(ui.lblUrnSelection.x(),ui.lblUrnSelection.y() + ui.lblUrnSelection.height(), 200,20)  # Format of the cbox

    def debriefPage():
        # This create a new trial of the experiment
        window.currentTrial = Trial(nMarblesCondition=window.currentExperiment.nMarbles,
                                    urnA=window.currentExperiment.urnA
                                    , urnB=window.currentExperiment.urnB,
                                    urnsPositions=window.currentExperiment.urnsPositions,
                                    participant=window.currentParticipant, urnSelected=window.urnSelected,
                                    marblePicked=window.marblePicked,
                                    prize=window.prize,
                                    colorPrize=window.colorPrize,
                                    experimentId=window.experimentId
                                    )
        # Add that trial in the experiment list of trials (this will allow to keep a registry)
        window.currentExperiment.addTrial(window.currentTrial)

        # Write a line in the txt file with the Demographics information of the participant and the picked marble (based on what was asked in description of assignment 2)
        window.currentExperiment.writeTrialExperimentCsv(window.currentTrial,
                                                         window.csvParticipants)  # Method to write a new line in the csv file with the participant information
        # Note: In the resulting csv, each line should correspond to one participant and the various fields will be separated by commas.

        # Display the debrief message
        window.marblePicked = window.currentTrial.marblePicked

        ui.lblDebrief1.setText("You picked the " + window.marblePicked + " marble: ")
        ui.lblDebrief1.setGeometry(ui.lblDebrief1.x(), ui.lblDebrief1.y(), 200, 20)

        ui.lblPickedMarble.setText(
            "")  # This label is used only to get the position where the picture of the marble selected is shown

        # Add pictures of the blue and red marble in the last page of the StackWidget
        ui.lblRedMarble.setPixmap(QtGui.QPixmap("redMarble.png"))
        ui.lblBlueMarble.setPixmap(QtGui.QPixmap("blueMarble.png"))
        marbleWidth = 100
        marbleHeight = 100

        # Hide picture of the marble that was not picked and keep the picture of the picked marble (e.g. if the user picked the blue marble, the picture of the red marble is hidden)
        if window.marblePicked == "blue":
            ui.lblRedMarble.hide()
            ui.lblBlueMarble.setGeometry(ui.lblPickedMarble.x(), ui.lblPickedMarble.y(), marbleWidth, marbleHeight)

        else:
            ui.lblBlueMarble.hide()
            ui.lblRedMarble.setGeometry(ui.lblPickedMarble.x(), ui.lblPickedMarble.y(), marbleWidth, marbleHeight)

        # Display a message showing whether the participant wins a prize for picking the marble.
        ui.lblDebrief2.setText(window.currentTrial.debriefMessage())
        ui.lblDebrief2.setWordWrap(True)
        ui.lblDebrief2.setGeometry(ui.lblDebrief2.x(), ui.lblDebrief2.y(), 400, 100)

# ***************   Class Experiment *************************************** #

class Experiment:

    def __init__(self, nMarblesConditions,urnA,urnB,prize,colorPrize,randomColor,experimentId,csvExperiment):

        self.nMarblesConditions = nMarblesConditions #conditions is a list that contains the number of marbles used in each condition
        self.nConditions = len(nMarblesConditions) #Number of conditions in the experiment
        self.participant = None
        self.urnA = urnA # Urn A
        self.urnB = urnB # Urn B
        self.nMarbles = None # Number of marbles for a given condition
        self.urnsPositions = None #0 or 1
        self.trials = []
        self.marblePicked = None #Blue or Red
        self.experimentId = experimentId
        self.attributesCsv = ['name', 'age', 'gender','eduLevel', 'nMarbles', 'urnsPositions', 'urnSelected', "marble"] #You should not modify this attribute later.
        self.prize = prize
        self.colorPrize = colorPrize #The participant win a prize depending on the color of the marble (e.g. blue or red)
        self.randomColor = randomColor
        self.csvExperiment = csvExperiment

    def launchExperiment(self):
        # See whether the file with registries of participant was already created
        if self.existingExperiment(self.csvExperiment): #if the file of the experiment has not been created yet (i.e. the first trial of the experiment)
            # Create a file with the main information about the experiment (id, number of participants, conditions.
            fileExperiment = open(self.csvExperiment, 'w')
            # Write the first two lines of the file, with the name of the file with the trials of that experiment and the experiment id
            fileExperiment.write(printCsvLine(["Experiment Id", str(self.experimentId)]))
            fileExperiment.write(printCsvLine(["Filename participants", "participants" + self.csvExperiment]))
            # The next line will contain the distirbution of marbles in the random urn, since for trials of the same experiment, this distribution keeps the same.
            # This will update it later in the method randomMarbles
            fileExperiment.close()

            # Create file for participants as well (File with a list of trials for a given experiment)
            fileParticipants = open("participants"+self.csvExperiment, 'w')
            #Write the columns of this file
            fileParticipants.write(printCsvLine(self.attributesCsv))
            fileParticipants.close()

            # Add some rows to the Experiment txt file with the number of red and blue marbles in each condition under the random allocation.
            fileExperiment = open(self.csvExperiment, 'a')

            # The first line has the label of the columns (red and blue marbles)
            fileExperiment.write(printCsvLine(["\n "]))  # Blank line
            fileExperiment.write(
                printCsvLine(["Marbles", "Red (Random)", "Blue (Random)", "Red (5050)", "Blue (5050)"]))

            for nMarbles in self.nMarblesConditions:  # nMarbles holds the number of marles for a given condition
                nBlue = 0
                nRed = 0

                if self.randomColor == "blue":
                    nBlue = randint(0, nMarbles)
                    nRed = int(nMarbles - nBlue)

                if self.randomColor == "red":
                    nRed = randint(0, nMarbles)
                    nBlue = int(nMarbles - nRed)

                fileExperiment.write(printCsvLine(
                    [str(nMarbles), str(nRed), str(nBlue), str(int(nMarbles / 2)), str(int(nMarbles / 2))]))

            fileExperiment.close()

        else:  # If the file exists
            self.readExistingExperiment(self.csvExperiment)

    # Return a bool whether the experiment was already created (i.e. True if this is the first trial)
    def existingExperiment(self, csvExperiment):
        return csvExperiment not in listdir()

    #This method review the existing trials of participants. I assumed that the file with the experiment trials in the same
    #folder from where this file is being executed.
    def readExistingExperiment(self,csvExperiment):

        files = listdir()

        # Reading file contents
        fileExperiment = open(csvExperiment, 'r')  # Read the csv file for Experiment
        infoFileExperiment = fileExperiment.readlines()  # infoFile is a list of strings that has all the string lines inside the participant's file
        fileExperiment.close()  # Close the file for this participant as the information is already stored in the variable 'infoFile'

        #The first line of this file has the name of the file with the summary of the participant trials for that experiment
        csvParticipants = infoFileExperiment[1].split(",")[1].replace("\n","").replace(" ","")
        fileParticipants = open(csvParticipants, 'r')  # Read the csv file for Experiment
        infoFileParticipants = fileParticipants.readlines()  # infoFile is a list of strings that has all the string lines inside the participant's file
        fileParticipants.close()  # Close the file for this participant as the information is already stored in the variable 'infoFile'

        #First row of the file (Name of the columns)
        colNames = infoFileParticipants[0].split(",")
        colValues = infoFileParticipants[1:]
        for lineParticipantsInfo in colValues:
            lineTrial = lineParticipantsInfo.split(",")
            participant = Participant(name = lineTrial[0], age=lineTrial[1],  gender=lineTrial[2],educationLevel=lineTrial[3])
            urnA = Urn(label="A")
            urnB = Urn(label="A")
            trial = Trial(nMarblesCondition=lineTrial[4],urnA=urnA,urnB=urnB,urnsPositions=lineTrial[5],participant=participant
                          ,urnSelected=lineTrial[6],marblePicked=lineTrial[7],prize=self.prize, colorPrize=self.colorPrize,experimentId=self.experimentId)
            self.addTrial(trial)

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

    def randConditions(self):

        #First check if there are enough participants in any of the conditions
        dictConditions = {}
        dictConditionsCompleted = {}

        #Create a dictionary where the keys are the number of marbles per condition (e.g. 2,4 and100) and the values of the dictionary are initilized in 0.
        for condition in self.nMarblesConditions:
            dictConditions[str(condition)] = 0

        conditions = list(dictConditions.keys()) #E.g [2,4,100]
        nConditions = len(conditions)
        nTrials = len(self.trials)
        completeCondition = int(nTrials % nConditions)
        iteration = int(nTrials/nConditions)+1

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

    def randPositions(self):
        """the positions of the urns i.e. 0 if the random urn was on the right – urn B as was in the
    #paper, and 1 if the random urn was on the left – urn A (0 or 1)"""
        urnsPositions = randint(0, 1)

        if urnsPositions == 0:
            self.urnA.randomMarbles = True
            self.urnB.randomMarbles = False
            self.urnsPositions = 1  # 1 if the random urn was on the left – urn A
        else:
            self.urnA.randomMarbles = False
            self.urnB.randomMarbles = True
            self.urnsPositions = 0 # 0 if the random urn was on the right – urn B as was in the paper

    #Receive a lable (A or B and return the object for that urn)
    def urnObj(self,urnLabel):

        urn = None

        if urnLabel == "A":
            urn = self.urnA
        if urnLabel == "B":
            urn = self.urnB

        return urn

    # This method assigns the number of red and blue marbles depending on the condition (number of marbles) and
    # whether the urn was randomly selected to have 50:50 or ambigous distrbutin of marbles)

    def addMarbles(self):

        #Read the information of the experiment csv file on the number of red and blue marbles in this condition

        fileExperiment = open(self.csvExperiment, 'r')
        infoFile = fileExperiment.readlines()
        fileExperiment.close()

        infoConditions = infoFile[4:]
        dictMarbles = {}

        # Now, we create a rich dictionary with the number of marbles in each condition reading the existing csv file of the experiment
        for line in infoConditions:
            lineArray= line.replace("\n","").split(",")
            nMarbles = str(lineArray[0])
            dictMarbles[nMarbles] = {'redRandom':lineArray[1],'blueRandom':lineArray[2],'red50':lineArray[3],'blue50':lineArray[4]}

        # Fill urns A and B with red and blue marbles (using random or 50:50 pattern)
        for urn in [self.urnA, self.urnB]:
            if urn.randomMarbles:
                urn.nBlue = int(dictMarbles[str(self.nMarbles)]['blueRandom'])
            else:
                urn.nBlue = int(dictMarbles[str(self.nMarbles)]['blue50'])
            urn.nRed = int(self.nMarbles - urn.nBlue)

    # When a participant choose an urn, this method is called.
    # This is the marble picked by the participant but it is only the label
    def pickMarble(self,labelUrnSelected):
        urn = self.urnObj(labelUrnSelected)
        # Let's assume a case where there are R red Marbles and B blue marbles in an urn ('urn').
        # Then, R+B (equal to 'N') is the total number of marbles in the urn,
        #If each marble has the same probability to be picked, for a given trial (i.e. pick a ball of the urn)
        # the probability of picking a red or blue marble is given just by the proportion of blue or red marbles in the urn.
        # We can use a uniform distribution to map the probability density distribution (PDF) of this process.

        randN = randint(1,urn.nMarbles)

        if randN <= urn.nBlue:
            self.marblePicked = "blue"
        else:
            self.marblePicked = "red"

        #Finally, the probability of picking a Red (or Blue) Marble (or not) for one trial (picking one ball) will exhibit a binomial distribution

    # Of course, your experiment must also record each participant’s results. Therefore, before the experiment window is closed,
    # you must write to a csv file (common for all participants) the following:

    # - the collected demographics
    # - the condition in which he/she participated, i.e. the number of balls in each urn (2, 10 or 100)
    # - the positions of the urns i.e. 0 if the random urn was on the right – urn B as was in the paper, and 1 if the random
    #   urn was on the left – urn A (0 or 1)
    # - the selected urn, i.e. 0 if the participant chose the random urn and 1 if he/she chose the 50:50 urn (0 or 1)
    # - whether they got a red or a blue marble (red or blue)

    def lineTrialCsv(self, trial):
        """This method return a dictionary with keys equal to the variable names and values equal to the values will be printed in the csv"""

        # dictCsv = {'name':trial.participant.name,'age':trial.participant.age}

        dictCsv = {'name':trial.participant.name,'age': trial.participant.age, 'gender':trial.participant.gender, 'eduLevel':trial.participant.educationLevel, #the collected demographics
                               'nMarbles':trial.nMarblesCondition, #the condition in which he/she participated, i.e. the number of balls in each urn (2, 10 or 100)
                               'urnsPositions':trial.urnsPositions,   #the positions of the urns i.e. 0 if the random urn was on the right – urn B as was in the paper, and 1 if the random urn was on the left – urn A (0 or 1)
                            'urnSelected':trial.idUrnSelected(), #the selected urn, i.e. 0 if the participant chose the random urn and 1 if he/she chose the 50:50 urn (0 or 1)
                            'marble':trial.marblePicked #whether they got a red or a blue marble (red or blue)
                   }
        return dictCsv

    def numberSequence(self,nMarbles):

        numberSequence = ""
        #This is the number sequence if the number of marbles is greater than 4
        if nMarbles >4 :
            numberSequence = "0, 1, 2, ..., "+str(nMarbles)
        elif nMarbles == 3:
            numberSequence = "0, 1, 2, "+str(nMarbles)
        elif nMarbles == 2:
            numberSequence = "0, 1, " + str(nMarbles)

        return numberSequence

    def createInstruction(self,txtInstructions):
        paperBasedInstruction = "write down your decision below. You will draw a marble from your chosen urn straight afterwards." #Participants where instructed to write this, after they picked the marble
        computerBasedInstruction = "in the following page, click one of the two alternatives and press 'Next.'" #This is the new instruction

        # Readtxt file with the generic instruction
        fileInstruction = open(txtInstructions,'r')
        infoFileInstruction = fileInstruction.readlines()
        fileInstruction.close()

        dictNewLabels = {'_prize_': self.prize #Equal to 30 pounds in the paper-based experiment
                         ,'_colorPrize_':self.colorPrize #Blue in the paper-based experiment and with lowercase
                         ,'_labelUrnA_':self.urnA.label
                         ,'_labelUrnB_': self.urnB.label
                         ,'_randomColor_':self.randomColor #Color of the marble selected to do the random allocation of balls (blue in the paper experiment)
                         ,'_nRedNonRandomUrn_':self.nonRandomUrn().nRed
                         ,'_nRedRandomUrn_':self.randomUrn().nRed
                         ,'_nBlueNonRandomUrn_':self.nonRandomUrn().nBlue
                         ,'_nBlueRandomUrn_':self.randomUrn().nBlue
                         ,'_nMarbles_': self.nMarbles
                         ,'_numberSequence_':self.numberSequence(self.nMarbles)
                         ,'_labelRandomUrn_':self.randomUrn().label
                         ,'_labelNonRandomUrn_':self.nonRandomUrn().label
                         ,'_marblePickedInstruction_': computerBasedInstruction
                    }

        instructions = ""

        for paragraph in infoFileInstruction:
            for label in dictNewLabels.keys():
                paragraph = paragraph.replace(str(label),str(dictNewLabels[label]))
            instructions += paragraph+"\n"

        return instructions

    #Return the object of the random urn
    def randomUrn(self):
        if self.urnA.randomMarbles:
            return self.urnA
        else:
            return self.urnB

    def nonRandomUrn(self):
        if self.urnA.randomMarbles:
            return self.urnB
        else:
            return self.urnA

    #Write information of the current trial (or participant) in the corresponding csv file of an experiment
    def writeTrialExperimentCsv(self,trial,csvParticipants):

        dictTrial = self.lineTrialCsv(trial)

        valuesCsv = []
        for attribute in self.attributesCsv:
            valuesCsv.append(dictTrial[attribute])

        fileParticipants = open(csvParticipants, 'a')

        fileParticipants.write(printCsvLine(valuesCsv))
        fileParticipants.close()

    def addTrial(self,trial):
        self.trials.append(trial) #This add the trial to the existing list of trials

# ***************   Class Trial *************************************** #

#A Trial object contains all the information that is printed in the output file (participantsExperiment.csv)
#In addition, we implemented the function deBriefMessage that show to the participant a a debrief message through the User Interface .

class Trial:

    def __init__(self, nMarblesCondition,urnA, urnB,urnsPositions,participant,urnSelected,marblePicked,prize,colorPrize,experimentId):
        self.nMarblesCondition = nMarblesCondition #Number of marbles after randomizing conditions (e.g. 2,10 or 100)
        self.urnsPositions = urnsPositions #Position of urns after randomizing positions (0 or 1). 0 if the random urn was on the right – urn B as was in the paper, and 1 if the random urn was on the left – urn A (0 or 1)
        self.experimentId = experimentId #Each trial is linked to a given experiment. This string allows to link a trial with its correponding experiment, but avoiding circular dependence between the classes (both class contains instances of each other)
        self.urnA = urnA # Urn A after randomization
        self.urnB = urnB # Urn B after randomization
        self.urnSelected = urnSelected #the selected urn, A or B
        self.participant = participant
        self.marblePicked = marblePicked
        self.prize = prize
        self.colorPrize = colorPrize  # The participant win a prize depending on the color of the marble (e.g. blue or red)

    #The message will change whether the participant picked the marble that gives a prize
    def debriefMessage(self):
        if self.colorPrize == self.marblePicked:
            return "Congratulations, you won the price (" + str(self.prize) +" pounds) because you picked the " + self.colorPrize + " marble. "

        else:
            return "Unfortunately you did not won the price (" + str(self.prize) +" pounds) because you did not pick the " + self.colorPrize + " marble. "

    # The selected urn must be printed in the csv file using the following rule: 0 if the participant chose the random urn and 1 if he/she chose the 50:50 urn (0 or 1)
    def idUrnSelected(self):

        idUrnSelected = 1

        #if the participant selected the urn with random marbles, the following condition must be satisfied
        if (self.urnA.randomMarbles == True and self.urnSelected == "A") or (self.urnB.randomMarbles == True and self.urnSelected == "B"):
            idUrnSelected = 0

        return idUrnSelected


        # Of course, your experiment must also record each participant’s results. Therefore, before the experiment window is closed,
        # you must write to a csv file (common for all participants) the following:

        # - the collected demographics
        # - the condition in which he/she participated, i.e. the number of balls in each urn (2, 10 or 100)
        # - the positions of the urns i.e. 0 if the random urn was on the right – urn B as was in the paper, and 1 if the random
        #   urn was on the left – urn A (0 or 1)
        # - the selected urn, i.e. 0 if the participant chose the random urn and 1 if he/she chose the 50:50 urn (0 or 1)
        # - whether they got a red or a blue marble (red or blue)


def numberSequence(self, nMarbles):
    numberSequence = ""
    # This is the number sequence if the number of marbles is greater than 4
    if nMarbles > 4:
        numberSequence = "0, 1, 2, ..., " + str(nMarbles)
    elif nMarbles == 3:
        numberSequence = "0, 1, 2, " + str(nMarbles)
    elif nMarbles == 2:
        numberSequence = "0, 1, " + str(nMarbles)

    return numberSequence


window.block2 = Experiment2(participant=participant, experimentType=2, id=1, nTrials=window.nTrials,
                            learningMode=window.learningMode
                            , xDeterministicWaitingTime=1 / 3, xVariabilityWaitingTimeControl=1 / 5,
                            xVariabilityWaitingTimeTreatment=1 / 4
                            , csvExperiment="Experiment2Conditions.csv", csvDescription="ExperimentDescription.txt"
                            , csvLearningResponses="Experiment2LearningResponses.csv",
                            csvChoiceResponses="Experiment2ChoiceResponses.csv"
                            , journeyLength=window.journeyLengthConditions[0])

window.experiment.setup(window.block2)

# Experiment 2: xDeterministicWaitingTime must be greater or equal than xWaitingTimeVariability
class Experiment2(Experiment):
    def __init__(self, experimentType, participant
                 , nTrials, learningMode,journeyLength,id
                 , xDeterministicWaitingTime, xVariabilityWaitingTimeControl, xVariabilityWaitingTimeTreatment
                 , csvExperiment, csvDescription, csvLearningResponses, csvChoiceResponses):

        super().__init__(participant = participant, experimentType = experimentType, nTrials = nTrials
                         ,csvExperiment = csvExperiment, csvLearningResponses = csvLearningResponses,id = id
                         , csvDescription = csvDescription, csvChoiceResponses = csvChoiceResponses,learningMode = learningMode)

        self.journeyTime = journeyLength  # The journey time is fixed in both scenarios
        # The amount of variability in the waiting time as a proportion of the mean journey time (Control and TreatmentRoute)
        self.xVariabilityWaitingTimeControl = xVariabilityWaitingTimeControl
        self.xVariabilityWaitingTimeTreatment = xVariabilityWaitingTimeTreatment
        # The amount of waiting time as a proportion of the mean journey time in the alternative that will be deterministic
        self.xDeterministicWaitingTime = xDeterministicWaitingTime

    def setTimeAttributes(self, treatmentRoute):

        self.treatmentRoute = treatmentRoute #Variable waiting time is the treatment condition

        treatmentClockwise = None

        #These attributes will be used to build the treatment waiting time
        minWaitingClockwise = None
        maxWaitingClockwise = None
        minWaitingCounterclockwise = None
        maxWaitingCounterclockwise = None

        # Travel time is fixed for both routes
        travelTime = round(self.journeyTime * (1 - self.xDeterministicWaitingTime), 2)

        self.deterministicWaitingTime = round(self.xDeterministicWaitingTime * self.journeyTime, 2)
        # self.travelTimeControl = travelTime # Travel time is fixed for both routes
        # self.journeyTimeControl = self.waitingTimeControl + self.travelTimeControl

        if treatmentRoute == "counterclockwise":

            treatmentClockwise = False
            self.controlRoute = "clockwise"

            # Calculate lower and upper bounds for waiting for the clockwise route
            minWaitingClockwise = round(self.deterministicWaitingTime-self.journeyTime*self.xVariabilityWaitingTimeControl, 2)
            maxWaitingClockwise = round(self.deterministicWaitingTime+self.journeyTime*self.xVariabilityWaitingTimeControl, 2)

            # Calculate lower and upper bounds for waiting for the counterclockwise route
            minWaitingCounterclockwise = round(self.deterministicWaitingTime-self.journeyTime*self.xVariabilityWaitingTimeTreatment, 2)
            maxWaitingCounterclockwise = round(self.deterministicWaitingTime+self.journeyTime*self.xVariabilityWaitingTimeTreatment, 2)


        else: #Clockwise route is the treatment condition

            treatmentClockwise = True
            self.controlRoute = "counterclockwise"
            # Calculate lower and upper bounds for waiting for the clockwise route
            minWaitingClockwise = round(self.deterministicWaitingTime-self.journeyTime*self.xVariabilityWaitingTimeTreatment, 2)
            maxWaitingClockwise = round(self.deterministicWaitingTime+self.journeyTime*self.xVariabilityWaitingTimeTreatment, 2)

            # Calculate lower and upper bounds for waiting for the clockwise route
            minWaitingCounterclockwise = round(self.deterministicWaitingTime-self.journeyTime*self.xVariabilityWaitingTimeControl, 2)
            maxWaitingCounterclockwise = round(self.deterministicWaitingTime+self.journeyTime*self.xVariabilityWaitingTimeControl, 2)

        #
        # self.waitingTimeTreatment = round(self.xWaitingTimeTreatment * self.journeyTime, 2)
        # self.travelTimeTreatment = travelTime # Travel time is fixed for both routes
        # self.journeyTimeTreatment = self.waitingTimeTreatment + self.travelTimeTreatment
        #



        # Set waiting and travel times for both routes
        self.waitingClockwise = Waiting(minWaitingTime=minWaitingClockwise,maxWaitingTime=maxWaitingClockwise)
        self.travelClockwise = Travel(meanTravelTime=travelTime)

        self.waitingCounterclockwise = Waiting(minWaitingTime=minWaitingCounterclockwise, maxWaitingTime=maxWaitingCounterclockwise)
        self.travelCounterclockwise = Travel(meanTravelTime=travelTime)

        # Create Journey objects for each route.
        self.journeyClockwise = Journey(travel=self.travelClockwise,
                                               waiting=self.waitingClockwise,
                                               direction="clockwise", treatment = treatmentClockwise)

        # This generate deterministic waiting and travel times according to the mean values given before
        self.journeyCounterclockwise = Journey(travel=self.travelCounterclockwise,
                                               waiting=self.waitingCounterclockwise,
                                               direction="counterclockwise", treatment = not treatmentClockwise)

        #This generate deterministic waiting and travel times according to the mean values given before
        self.journeyClockwise.generateJourneyTimes(randomTravel=False,randomWait=False)
        self.journeyCounterclockwise.generateJourneyTimes(randomTravel=False, randomWait=False)

    window.experiment3 = Experiment3(participant=participant, experimentType=3, id=1, nTrials=window.nTrials,
                                     learningMode=window.learningMode
                                     , xDeterministicTravelTime=2 / 3, xVariabilityTravelTimeControl=1 / 5,
                                     xVariabilityTravelTimeTreatment=1 / 4
                                     , csvExperiment="Experiment3Conditions.csv",
                                     csvDescription="ExperimentDescription.txt"
                                     , csvLearningResponses="Experiment3LearningResponses.csv",
                                     csvChoiceResponses="Experiment3ChoiceResponses.csv"
                                     , journeyLength=window.journeyLengthConditions[0])

    window.experiment.setup(window.experiment3)

    # Experiment 4
    window.experiment4 = Experiment4(participant=participant, experimentType=4, id=1, nTrials=window.nTrials,
                                     learningMode=window.learningMode
                                     , xDeterministicWaitingTime=1 / 3, xVariabilityWaitingTime=1 / 4
                                     , xDeterministicTravelTime=2 / 3, xVariabilityTravelTime=1 / 4
                                     , csvExperiment="Experiment4Conditions.csv",
                                     csvDescription="ExperimentDescription.txt"
                                     , csvLearningResponses="Experiment4LearningResponses.csv",
                                     csvChoiceResponses="Experiment4ChoiceResponses.csv"
                                     , journeyLength=window.journeyLengthConditions[0])

    window.experiment.setup(window.experiment4)


# Experiment 3: xDeterministicTravelTime must be greater or equal than xTravelTimeVariability
class Experiment3(Experiment):
    def __init__(self, experimentType, participant, nTrials, learningMode
                 , xDeterministicTravelTime, xVariabilityTravelTimeControl, xVariabilityTravelTimeTreatment
                 , csvExperiment, csvDescription,journeyLength,csvLearningResponses,csvChoiceResponses,id):

        super().__init__(participant = participant, experimentType = experimentType, nTrials = nTrials
                         ,csvExperiment = csvExperiment, csvDescription = csvDescription, id = id
                         , csvLearningResponses = csvLearningResponses, csvChoiceResponses = csvChoiceResponses, learningMode = learningMode)

        self.journeyTime = journeyLength # The journey time is fixed in both scenarios
        # The amount of variability in the waiting time as a proportion of the mean journey time (Control and Treatment Routes)
        self.xVariabilityTravelTimeTreatment = xVariabilityTravelTimeTreatment
        self.xVariabilityTravelTimeControl = xVariabilityTravelTimeControl
        # The amount of waiting time as a proportion of the mean journey time in the alternative that will be deterministic
        self.xDeterministicTravelTime = xDeterministicTravelTime

    def setTimeAttributes(self, treatmentRoute):


        self.treatmentRoute = treatmentRoute #Variable waiting time is the treatment condition
        treatmentClockwise = None
        # These attributes will be used to build the treatment waiting time
        minTravelClockwise = None
        maxTravelClockwise = None
        minTravelCounterclockwise = None
        maxTravelCounterclockwise = None

        deterministicTravelTime = round(self.xDeterministicTravelTime * self.journeyTime, 2)

        # Waiting time is fixed for both routes
        waitingTime = round(self.journeyTime * (1 - self.xDeterministicTravelTime), 2)


        if treatmentRoute == "counterclockwise":
            treatmentClockwise = False
            self.controlRoute = "clockwise"
            # Calculate lower and upper boundsfor waiting for the clockwise route
            minTravelClockwise = round(deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeControl, 2)
            maxTravelClockwise = round(deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeControl, 2)

            # Calculate lower and upper boundsfor waiting for the counterclockwise route
            minTravelCounterclockwise = round(deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeTreatment, 2)
            maxTravelCounterclockwise = round(deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeTreatment, 2)


        else: #Clockwise route is the treatment condition

            treatmentClockwise = True
            self.controlRoute = "counterclockwise"
            # Calculate lower and upper boundsfor waiting for the clockwise route
            minTravelClockwise = round(deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeTreatment, 2)
            maxTravelClockwise = round(deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeTreatment, 2)

            # Calculate lower and upper boundsfor waiting for the clockwise route
            minTravelCounterclockwise = round(deterministicTravelTime-self.journeyTime*self.xVariabilityTravelTimeControl, 2)
            maxTravelCounterclockwise = round(deterministicTravelTime+self.journeyTime*self.xVariabilityTravelTimeControl, 2)


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

class Experiment4(Experiment):
    def __init__(self, experimentType, participant, nTrials, learningMode, journeyLength
                 , xDeterministicTravelTime, xVariabilityTravelTime, xDeterministicWaitingTime, xVariabilityWaitingTime,
                 csvExperiment, csvDescription,csvLearningResponses,csvChoiceResponses,id):

        super().__init__(participant=participant, experimentType=experimentType, nTrials=nTrials
                         , csvExperiment=csvExperiment, csvDescription = csvDescription,id = id
                         , csvLearningResponses = csvLearningResponses, csvChoiceResponses = csvChoiceResponses
                         , learningMode = learningMode)

        self.journeyTime = journeyLength  # The journey time is fixed in both scenarios

        self.xDeterministicTravelTime = xDeterministicTravelTime  # The amount of waiting time as a proportion of the mean journey time in the alternative that will be deterministic
        self.xVariabilityTravelTime = xVariabilityTravelTime  # The amount of variability in the waiting time as a proportion of the mean journey time

        self.xDeterministicWaitingTime = xDeterministicWaitingTime
        self.xVariabilityWaitingTime = xVariabilityWaitingTime

    def setTimeAttributes(self, treatmentRoute):
        self.treatmentRoute = treatmentRoute  # Variable travel time but fixed control time for clockwise (Treatment Condition).

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

        self.controlTravelTime = round(self.xDeterministicTravelTime * self.journeyTime, 2)
        self.controlWaitingTime = round(self.xDeterministicWaitingTime * self.journeyTime, 2)

        if treatmentRoute == "counterclockwise": #Variable travel time but fixed control time for counterclockwise

            treatmentClockwise = False
            self.controlRoute = "clockwise"
            # Calculate lower and upper bounds for waiting for the counterclockwise route
            minTravelCounterclockwise = round(self.controlTravelTime - self.journeyTime * self.xVariabilityTravelTime, 2)
            maxTravelCounterclockwise = round(self.controlTravelTime + self.journeyTime * self.xVariabilityTravelTime, 2)
            minWaitingCounterclockwise = round(self.controlWaitingTime, 2)
            maxWaitingCounterclockwise = round(self.controlWaitingTime, 2)

            # Calculate lower and upper bounds for waiting for the clockwise route
            minTravelClockwise = round(self.controlTravelTime, 2)
            maxTravelClockwise = round(self.controlTravelTime, 2)
            minWaitingClockwise = round(self.controlWaitingTime - self.journeyTime * self.xVariabilityWaitingTime, 2)
            maxWaitingClockwise = round(self.controlWaitingTime + self.journeyTime * self.xVariabilityWaitingTime, 2)

        else:  #Clockwise is Treatment Condition
            treatmentClockwise = True
            self.controlRoute = "counterclockwise"
            # Calculate lower and upper bounds for waiting for the clockwise route
            minTravelClockwise = round(self.controlTravelTime - self.journeyTime * self.xVariabilityTravelTime, 2)
            maxTravelClockwise = round(self.controlTravelTime + self.journeyTime * self.xVariabilityTravelTime, 2)
            minWaitingClockwise = round(self.controlWaitingTime, 2)
            maxWaitingClockwise = round(self.controlWaitingTime, 2)

            # Calculate lower and upper bounds for waiting for the clockwise route
            minTravelCounterclockwise = round(self.controlTravelTime, 2)
            maxTravelCounterclockwise = round(self.controlTravelTime, 2)
            minWaitingCounterclockwise = round(self.controlWaitingTime - self.journeyTime * self.xVariabilityWaitingTime, 2)
            maxWaitingCounterclockwise = round(self.controlWaitingTime + self.journeyTime * self.xVariabilityWaitingTime, 2)

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



# ***************   (Page 5) Experiment: Travel/Waiting time choices *************************************** #

def nextButtonChoiceExpPage():
    ui.stackedWidget.setCurrentIndex(ui.stackedWidget.currentIndex() + 1)  # Go to next page

ui.buttonNextChoiceExpPage.clicked.connect(nextButtonChoiceExpPage)

#Visualization parameters
lengthTimesLbl = 500  # This will be the length of the maximum journey time
heightTimesLbl = 20

def initializeChoices():
    for label in [ui.detWaitingTimeALbl,ui.randWaitingTimeALbl,ui.detTravelTimeALbl,ui.randTravelTimeALbl,ui.detWaitingTimeBLbl,ui.randWaitingTimeBLbl,ui.detTravelTimeBLbl,ui.randTravelTimeBLbl,]:
        label.setFrameShape(QFrame.Box)
        label.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignVCenter)
        label.setGeometry(label.x(), label.y(), 0, heightTimesLbl)
        label.setFixedHeight(heightTimesLbl)

    for label in [ui.detWaitingTimeA,ui.detWaitingTimeB, ui.diffDetWaitingTime, ui.detTravelTimeA, ui.detTravelTimeB, ui.diffDetTravelTime, ui.detJourneyTimeA, ui.detJourneyTimeB, ui.diffDetJourneyTime,
                  ui.randWaitingTimeA,ui.randWaitingTimeB, ui.diffRandWaitingTime, ui.randTravelTimeA,ui.randTravelTimeB, ui.diffRandTravelTime, ui.randJourneyTimeA, ui.randJourneyTimeB, ui.diffRandJourneyTime,
                  ui.waitingTimeA, ui.waitingTimeB,ui.diffWaitingTime,ui.travelTimeA,ui.travelTimeB, ui.diffTravelTime, ui.journeyTimeA,ui.journeyTimeB,ui.diffJourneyTime]:
        label.setText("")

initializeChoices()

def generateChoices():

    initializeChoices()
    #Create a journey time
    waitingTimeA = Waiting(minWaitingTime = 0, maxWaitingTime = 20, meanWaitingTime = (0+20)/2, sdWaitingTime = 2)
    travelTimeA = Travel(minTravelTime = 30, maxTravelTime = 40, meanTravelTime=(30+40)/2,sdTravelTime = 2)
    journeyTimeA = Journey(travelTimeA, waitingTimeA)
    journeyTimeA.generateJourneyTimes(randomWait=True, randomTravel=True)

    waitingTimeB = Waiting(minWaitingTime=0, maxWaitingTime=10, meanWaitingTime=(0 + 10) / 2, sdWaitingTime=2)
    travelTimeB = Travel(minTravelTime = 20, maxTravelTime = 30, meanTravelTime = (20+30)/2, sdTravelTime = 2)
    journeyTimeB = Journey(travelTimeB, waitingTimeB)
    journeyTimeB.generateJourneyTimes(randomWait=True, randomTravel=True)

    #Visualization

    scaleFactor = 0
    if journeyTimeA.journeyTime == max(journeyTimeA.journeyTime,journeyTimeB.journeyTime):
        scaleFactor = lengthTimesLbl/journeyTimeA.journeyTime

    else:
        scaleFactor = lengthTimesLbl / journeyTimeB.journeyTime

    # Visualization Option A

    #Waiting Time (WT)
    detWaitingTimeALblWidth = journeyTimeA.detWaitingTime * scaleFactor
    ui.detWaitingTimeA.setText(str(journeyTimeA.detWaitingTime))
    ui.detWaitingTimeALbl.setText("Det WT")
    ui.detWaitingTimeALbl.setGeometry(ui.choiceALbl.x() + ui.choiceALbl.width(), ui.choiceALbl.y(),
                                       detWaitingTimeALblWidth, heightTimesLbl)

    randWaitingTimeALblWidth = journeyTimeA.randWaitingTime * scaleFactor
    ui.randWaitingTimeA.setText(str(journeyTimeA.randWaitingTime))
    ui.randWaitingTimeALbl.setText("Rand WT")
    setBackgroundColorQLabel(ui.randWaitingTimeALbl, colorString="red")
    ui.randWaitingTimeALbl.setGeometry(ui.detWaitingTimeALbl.x() + ui.detWaitingTimeALbl.width(), ui.choiceALbl.y(),
                                         randWaitingTimeALblWidth,
                                      heightTimesLbl)

    ui.waitingTimeA.setText(str(waitingTimeA.waitingTime))

    # Travel Time (TT)
    detTravelTimeALblWidth = journeyTimeA.detTravelTime * scaleFactor
    ui.detTravelTimeA.setText(str(journeyTimeA.detTravelTime))
    ui.detTravelTimeALbl.setText("Det TT")
    ui.detTravelTimeALbl.setGeometry(ui.randWaitingTimeALbl.x() + ui.randWaitingTimeALbl.width(), ui.randWaitingTimeALbl.y(),
                                     detTravelTimeALblWidth, heightTimesLbl)

    randTravelTimeLblWidth = journeyTimeA.randTravelTime * scaleFactor
    ui.randTravelTimeA.setText(str(journeyTimeA.randTravelTime))
    ui.randTravelTimeALbl.setText("Rand TT")
    setBackgroundColorQLabel(ui.randTravelTimeALbl, colorString="red")
    ui.randTravelTimeALbl.setGeometry(ui.detTravelTimeALbl.x() + ui.detTravelTimeALbl.width(), ui.detTravelTimeALbl.y(),
                                        randTravelTimeLblWidth, heightTimesLbl)

    ui.travelTimeA.setText(str(travelTimeA.travelTime))

    # Journey Time (JT)
    ui.detJourneyTimeA.setText(str(journeyTimeA.detJourneyTime))
    ui.randJourneyTimeA.setText(str(journeyTimeA.randJourneyTime))
    ui.journeyTimeA.setText(str(journeyTimeA.journeyTime))

    #Visualization Option B

    #Waiting Time (WT)
    detWaitingTimeBLblWidth = journeyTimeB.detWaitingTime * scaleFactor
    ui.detWaitingTimeB.setText(str(journeyTimeB.detWaitingTime))
    ui.detWaitingTimeBLbl.setText("Det WT")
    ui.detWaitingTimeBLbl.setGeometry(ui.choiceBLbl.x() + ui.choiceBLbl.width(), ui.choiceBLbl.y(),
                                       detWaitingTimeBLblWidth, heightTimesLbl)

    randWaitingTimeBLblWidth = journeyTimeB.randWaitingTime * scaleFactor
    ui.randWaitingTimeB.setText(str(journeyTimeB.randWaitingTime))
    ui.randWaitingTimeBLbl.setText("Rand WT")
    setBackgroundColorQLabel(ui.randWaitingTimeBLbl, colorString="red")
    ui.randWaitingTimeBLbl.setGeometry(ui.detWaitingTimeBLbl.x() + ui.detWaitingTimeBLbl.width(), ui.choiceBLbl.y(),
                                      randWaitingTimeBLblWidth,
                                      heightTimesLbl)

    ui.waitingTimeB.setText(str(waitingTimeB.waitingTime))

    #Travel Time (TT)
    detTravelTimeBLblWidth = journeyTimeB.detTravelTime * scaleFactor
    ui.detTravelTimeB.setText(str(journeyTimeB.detTravelTime))
    ui.detTravelTimeBLbl.setText("Det TT")
    ui.detTravelTimeBLbl.setGeometry(ui.randWaitingTimeBLbl.x() + ui.randWaitingTimeBLbl.width(),
                                      ui.randWaitingTimeBLbl.y(),
                                      detTravelTimeBLblWidth, heightTimesLbl)

    randTravelTimeBLblWidth = journeyTimeB.randTravelTime * scaleFactor
    ui.randTravelTimeB.setText(str(journeyTimeB.randTravelTime))
    ui.randTravelTimeBLbl.setText("Random TT")
    setBackgroundColorQLabel(ui.randTravelTimeBLbl, colorString="red")
    ui.randTravelTimeBLbl.setGeometry(ui.detTravelTimeBLbl.x() + ui.detTravelTimeBLbl.width(),
                                     ui.detTravelTimeBLbl.y(),
                                     randTravelTimeBLblWidth, heightTimesLbl)

    ui.travelTimeB.setText(str(travelTimeB.travelTime))

    # Journey Time (JT)
    ui.detJourneyTimeB.setText(str(journeyTimeB.detJourneyTime))
    ui.randJourneyTimeB.setText(str(journeyTimeB.randJourneyTime))
    ui.journeyTimeB.setText(str(journeyTimeB.journeyTime))

    # Comparison of alternatives
    ui.diffDetWaitingTime.setText(str(journeyTimeA.detWaitingTime-journeyTimeB.detWaitingTime))
    ui.diffDetTravelTime.setText(str(journeyTimeA.detTravelTime - journeyTimeB.detTravelTime))
    ui.diffDetJourneyTime.setText(str(journeyTimeA.detJourneyTime - journeyTimeB.detJourneyTime))

    ui.diffRandWaitingTime.setText(str(journeyTimeA.randWaitingTime - journeyTimeB.randWaitingTime))
    ui.diffRandTravelTime.setText(str(journeyTimeA.randTravelTime - journeyTimeB.randTravelTime))
    ui.diffRandJourneyTime.setText(str(journeyTimeA.randJourneyTime - journeyTimeB.randJourneyTime))

    ui.diffWaitingTime.setText(str(journeyTimeA.waitingTime - journeyTimeB.waitingTime))
    ui.diffTravelTime.setText(str(journeyTimeA.travelTime - journeyTimeB.travelTime))
    ui.diffJourneyTime.setText(str(journeyTimeA.journeyTime - journeyTimeB.journeyTime))

generateChoices()

ui.generateChoiceButton.clicked.connect(generateChoices)

# def personWaitingTimer(timeInterval,person,timer,waitingTimeLbl):
#
#     if person.waiting == True:
#         person.waitBusStop(timeInterval = timeInterval) #in seconds.
#         waitingTimeLbl.setText(str(int(round(person.waitingTime,0))))
#     else:
#         timer.stop()


def randPositions(self):
    """the positions of the urns i.e. 0 if the random urn was on the right – urn B as was in the
#paper, and 1 if the random urn was on the left – urn A (0 or 1)"""
    urnsPositions = randint(0, 1)

    if urnsPositions == 0:
        self.urnA.randomMarbles = True
        self.urnB.randomMarbles = False
        self.urnsPositions = 1  # 1 if the random urn was on the left – urn A
    else:
        self.urnA.randomMarbles = False
        self.urnB.randomMarbles = True
        self.urnsPositions = 0  # 0 if the random urn was on the right – urn B as was in the paper


# Receive a lable (A or B and return the object for that urn)
def urnObj(self, urnLabel):
    urn = None

    if urnLabel == "A":
        urn = self.urnA
    if urnLabel == "B":
        urn = self.urnB

    return urn


# This method assigns the number of red and blue marbles depending on the condition (number of marbles) and
# whether the urn was randomly selected to have 50:50 or ambigous distrbutin of marbles)

def addMarbles(self):
    # Read the information of the experiment csv file on the number of red and blue marbles in this condition

    fileExperiment = open(self.pathExperiment, 'r')
    infoFile = fileExperiment.readlines()
    fileExperiment.close()

    infoConditions = infoFile[4:]
    dictMarbles = {}

    # Now, we create a rich dictionary with the number of marbles in each condition reading the existing csv file of the experiment
    for line in infoConditions:
        lineArray = line.replace("\n", "").split(",")
        nMarbles = str(lineArray[0])
        dictMarbles[nMarbles] = {'redRandom': lineArray[1], 'blueRandom': lineArray[2], 'red50': lineArray[3],
                                 'blue50': lineArray[4]}

    # Fill urns A and B with red and blue marbles (using random or 50:50 pattern)
    for urn in [self.urnA, self.urnB]:
        if urn.randomMarbles:
            urn.nBlue = int(dictMarbles[str(self.nMarbles)]['blueRandom'])
        else:
            urn.nBlue = int(dictMarbles[str(self.nMarbles)]['blue50'])
        urn.nRed = int(self.nMarbles - urn.nBlue)


# When a participant choose an urn, this method is called.
# This is the marble picked by the participant but it is only the label
def pickMarble(self, labelUrnSelected):
    urn = self.urnObj(labelUrnSelected)
    # Let's assume a case where there are R red Marbles and B blue marbles in an urn ('urn').
    # Then, R+B (equal to 'N') is the total number of marbles in the urn,
    # If each marble has the same probability to be picked, for a given trial (i.e. pick a ball of the urn)
    # the probability of picking a red or blue marble is given just by the proportion of blue or red marbles in the urn.
    # We can use a uniform distribution to map the probability density distribution (PDF) of this process.

    randN = randint(1, urn.nMarbles)

    if randN <= urn.nBlue:
        self.marblePicked = "blue"
    else:
        self.marblePicked = "red"

        # Finally, the probability of picking a Red (or Blue) Marble (or not) for one trial (picking one ball) will exhibit a binomial distribution


# Return the object of the random urn
def randomUrn(self):
    if self.urnA.randomMarbles:
        return self.urnA
    else:
        return self.urnB


def nonRandomUrn(self):
    if self.urnA.randomMarbles:
        return self.urnB
    else:
        return self.urnA

#     if page == 3:
#
#         resetPicturesGrid(grid=ui.experimentPicturesGrid)
#
#         ui.buttonBackSimulationExperimentGeneralDescription.setVisible(True)
#
#         folderInstructions = "GeneralInstructions"
#
#         if window.mainExperiment.languageCondition == "spanish":
#             setTitlePage(grid=ui.simulationExpGeneralDescriptionTitleGrid,
#                          text="Instrucciones Generales - Página " + str(int(page))
#                          , fontFactor=window.fontFactor, fontLetter=window.fontLetter)
#
#             setupExpGeneralDescriptionText(txtInstructions="GeneralInstructionsPage3SPA.html"
#                                             , grid=ui.experimentDescriptionGrid
#                                             , folder = folderInstructions)
#
#         if window.mainExperiment.languageCondition == "english":
#             setTitlePage(grid=ui.simulationExpGeneralDescriptionTitleGrid,
#                          text="General Instructions - Page " + str(int(page))
#                          , fontFactor=window.fontFactor, fontLetter=window.fontLetter)
#
#             setupExpGeneralDescriptionText(txtInstructions="GeneralInstructionsPage3ENG.html"
#                                            , grid=ui.experimentDescriptionGrid
#                                            , folder=folderInstructions)
#
#         folder = "Pictures/generalDescription3/"
#
#         pathPicture1 = "origin.png"
#         pathPicture2 = "destination.png"
#         pathPicture3 = "routesPanel.png"
#         pathPicture4 = "directionClockwiseOriginWestBlueNorth.png"
#         pathPicture5 = "directionClockwiseOriginWestRedNorth"
#         pathPicture6 = "directionCounterclockwiseOriginEastBlueNorth.png"
#         pathPicture7 = "directionCounterclockwiseOriginEastRedNorth.png"
#
#
#         pathPictures = [pathPicture1, pathPicture2, pathPicture3, pathPicture4, pathPicture5, pathPicture6, pathPicture7]
#         counterPicture = 1
#         for pathPicture in pathPictures:
#             setupExpGeneralDescriptionPictures(pathPicture=folder + pathPicture, number=counterPicture,
#                                                grid=ui.experimentPicturesGrid)
#             counterPicture += 1
#
# # window.mainExperiment.nBlockDecisionProblem = 0




def createFormLayoutTravelBehaviourPage(page):
    #FORM LAYOUT WITH QUESTIONS

    #Create the form layout with the questions at the end of the experiment.
    if page == 1:

        window.nTravelBehaviourQuestionsPage1 = 1
        #QUESTION 1

        ui.descriptionQ1ATravelBehaviourPage = QLabel("")

        ui.radioButtonsQ1A = QButtonGroup() #Group of radio buttonsfor question 1 (Q1)
        ui.radioButtonYesExperimentIdentification = QRadioButton()        #Radio button Option 'Yes'
        ui.radioButtonNoExperimentIdentification = QRadioButton()        # Radio button Option 'No'


        #We temporally set the answer yes as a default
        ui.radioButtonYesExperimentIdentification.setChecked(True)

        for radioButton in [ui.radioButtonYesExperimentIdentification,ui.radioButtonNoExperimentIdentification]:
            radioButton.setFocusPolicy(QtCore.Qt.NoFocus)
            radioButton.setFont(QFont(window.fontLetter, window.fontFactor*16))
            ui.radioButtonsQ1A.addButton(radioButton)

        # Information Text Labels
        folderTravelBehaviourQuestionsPage1 = "TravelBehaviourQuestions/Page1"

        #Description and text in options questions Page 1
        if window.mainExperiment.languageCondition == "english":
            ui.buttonNextTravelBehaviourPage.setText("Next Page")

            #Q1
            ui.radioButtonYesExperimentIdentification.setText("Yes")
            ui.radioButtonNoExperimentIdentification.setText("No")

            descriptionQ1ATravelBehaviourPage = updateInstruction(
                experiment=window.mainExperiment.currentExperiment
                , txtInstructions="q1AENG.html"
                , folder=folderTravelBehaviourQuestionsPage1)

        if window.mainExperiment.languageCondition == "spanish":
            ui.buttonNextTravelBehaviourPage.setText("Siguiente Página")

            ui.radioButtonYesExperimentIdentification.setText("Si")
            ui.radioButtonNoExperimentIdentification.setText("No")

            descriptionQ1ATravelBehaviourPage = updateInstruction(
                experiment=window.mainExperiment.currentExperiment
                , txtInstructions="q1ASPA.html"
                , folder=folderTravelBehaviourQuestionsPage1)

        ui.descriptionQ1ATravelBehaviourPage.setFont(QFont(window.fontLetter, window.fontFactor * 16))
        ui.descriptionQ1ATravelBehaviourPage.setText(descriptionQ1ATravelBehaviourPage)
        ui.descriptionQ1ATravelBehaviourPage.setWordWrap(True)



        ui.travelBehaviourFormLayoutPage1.addRow(ui.descriptionQ1ATravelBehaviourPage)
        ui.travelBehaviourFormLayoutPage1.addRow(ui.radioButtonYesExperimentIdentification)
        ui.travelBehaviourFormLayoutPage1.addRow(ui.radioButtonNoExperimentIdentification)


def readWriteTravelBehaviourQuestionsFields(page):

    fieldsCompleted = None

    #Here a list with all the variables, except for the radio buttons

    if page == 1:

        # PAGE 1
        ui.experimentIdentificationTravelBehaviourPage = None

        #Question 1(Q1)

        ui.experimentIdentification = None

        if ui.radioButtonNoExperimentIdentification.isChecked():
            ui.experimentIdentificationTravelBehaviourPage = "no"

        elif ui.radioButtonYesExperimentIdentification.isChecked():
            ui.experimentIdentificationTravelBehaviourPage = "yes"

        else: #There is no an option checked
            pass #Show error message


        if ui.experimentIdentificationTravelBehaviourPage == "yes" or ui.experimentIdentificationTravelBehaviourPage == "no":
            fieldsCompleted = True

        else:
            fieldsCompleted = False


def createFormLayoutExperimentDebriefPage(page):

    #I might randomize the order in which the pages are shown.

    if page == 1: #General description about this section
        # Page 1 Experiment Debrief Section

        fontIncreaseFactor = 1

        if window.mainExperiment.languageCondition == "english":

            setTitlePage(grid=ui.experimentDebriefTitleGrid, text="Questions about the experiments"  # Replace Title
                         , capitalLetters=True, centered=False, fontFactor=window.fontFactor,
                         fontLetter=window.fontLetter)

            window.experimentDescription = updateInstruction(
                txtInstructions="experimentDebriefDescriptionENG.html"
                , experiment=window.mainExperiment.currentExperiment
                , folder="ExperimentDebriefQuestions/Page1")

        if window.mainExperiment.languageCondition == "spanish":
            setTitlePage(grid=ui.experimentDebriefTitleGrid, text="Preguntas sobre los experimentos "
                         , capitalLetters=True, centered=False, fontFactor=window.fontFactor,
                         fontLetter=window.fontLetter)

            window.experimentDescription = updateInstruction(
                txtInstructions="experimentDebriefDescriptionSPA.html"
                , experiment=window.mainExperiment.currentExperiment
                , folder="ExperimentDebriefQuestions/Page1")

        # Create a Scroll Area Widget to add on it the QLabel that contains the text displayed in the description page.
        ui.scrollExperimentDescription = QScrollArea()
        # ui.scrollExperimentDescription.setFrameShape(QFrame.Box)
        ui.scrollExperimentDescription.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        ui.scrollExperimentDescription.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        ui.scrollExperimentDescription.setEnabled(False)
        ui.scrollExperimentDescription.setFrameShape(QFrame.NoFrame)
        ui.lblExperimentDescription = QLabel()
        ui.lblExperimentDescription.setFont(QFont(window.fontLetter, window.fontFactor * fontIncreaseFactor * 18))
        ui.lblExperimentDescription.setStyleSheet("QLabel { background-color : white; color : black; }")

        # Format of the Qlabel widget that displays the text of experiment's description page to the user
        ui.lblExperimentDescription.setText(window.experimentDescription)
        ui.lblExperimentDescription.setWordWrap(True)
        ui.lblExperimentDescription.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)

        # We add a Qlabel in the scroll area
        ui.scrollExperimentDescription.setWidget(ui.lblExperimentDescription)

        ui.scrollExperimentDescription.setWidgetResizable(
            True)  # The advantage of the scroll area has the advantage of being resizable but if the text exceed the maximum height or width set in the following line, it displays a scrollbar
        # ui.scrollExperimentDescription.setFixedSize(ui.stackedWidget.width()*0.8,ui.stackedWidget.height()*0.8) #Set the size of the Scroll Area Widget to the hall of the size of the window

        ui.experimentDebriefDescriptionGridPage1.addWidget(ui.scrollExperimentDescription, 0, 0)

    elif page == 2: #Questions about the experienced experiment

        sliderTitle = ""
        window.sliderLevels = None

        if window.mainExperiment.languageCondition == "spanish":
            # sliderLevels = {1: "No estoy segura (1)", 2: "No lo sé",3: "Estoy segura (2)"}
            window.sliderLevels = {1: "Poca \n(Nivel de Importancia: 0%)",
                                   2: "Mucha \n(Nivel de Importancia: 100%)"}
            window.allSliderLevels = {1: "Poca \n(0%)", 2: "",
                                      3: "Mucha \n(100%)"}  # This is what is shown in the slider

            sliderTitle = "Nivel de importancia"

        if window.mainExperiment.languageCondition == "english":
            # sliderLevels = {1: "I am not sure (1)",2: "I do not know (2)", 3: "I am sure (3)"}
            window.sliderLevels = {1: "Low \n(Importance Level: 0%)",
                                   2: "High \n(Importance Level: 100%)"}
            window.allSliderLevels = {1: "Low\n(0%)", 2: "",
                                      3: "High\n(100%)"}  # This is what is shown in the slider

            sliderTitle = "Importance Level"

        # window.lastSliderLevel = window.sliderLevels[len(window.sliderLevels.keys())]
        # window.firstSliderLevel = window.sliderLevels[1]

        # Create slider for each of the four items evaluated by participants

        # i) Waiting Time
        ui.sliderWaitingTimeExperiencedStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                        allLevels=window.allSliderLevels
                                                                        , levels=window.sliderLevels
                                                                        ,
                                                                        language=window.mainExperiment.languageCondition
                                                                        , discreteRange=False
                                                                        , sliderGrid=ui.experiencedStrategyWaitingTimeSliderGrid
                                                                        , fontLetter=window.fontLetter
                                                                        , fontSize = 14, fontFactor=window.fontFactor)

        ui.experiencedStrategyWaitingTimeSliderGrid.addWidget(ui.sliderWaitingTimeExperiencedStrategyExperimentDebriefPage, 0, 0)

        ui.experiencedStrategyWaitingTimeSliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.experiencedStrategyWaitingTimeSliderLbl = ui.experiencedStrategyWaitingTimeSliderLblGrid.itemAtPosition(0, 0).widget()
        ui.experiencedStrategyWaitingTimeSliderLbl.setText("Waiting Times")

        # ii) Waiting Time Reliability
        ui.sliderWaitingTimeReliabilityExperiencedStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                                   allLevels=window.allSliderLevels,
                                                                                   levels=window.sliderLevels,
                                                                                   language=window.mainExperiment.languageCondition
                                                                                   , discreteRange=False,
                                                                                   sliderGrid=ui.experiencedStrategyWaitingTimeReliabilitySliderGrid,
                                                                                   fontLetter=window.fontLetter
                                                                                   ,fontSize = 14, fontFactor=window.fontFactor)

        ui.experiencedStrategyWaitingTimeReliabilitySliderGrid.addWidget(ui.sliderWaitingTimeReliabilityExperiencedStrategyExperimentDebriefPage, 0,0)

        ui.experiencedStrategyWaitingTimeReliabilitySliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.experiencedStrategyWaitingTimeReliabilitySliderLbl = ui.experiencedStrategyWaitingTimeReliabilitySliderLblGrid.itemAtPosition(0, 0).widget()
        ui.experiencedStrategyWaitingTimeReliabilitySliderLbl.setText("Reliability of Waiting Times")

        # iii) In-Vehicle Time
        ui.sliderInVehicleTimeExperiencedStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                          allLevels=window.allSliderLevels,
                                                                          levels=window.sliderLevels,
                                                                          language=window.mainExperiment.languageCondition
                                                                          , discreteRange=False,
                                                                          sliderGrid=ui.experiencedStrategyInVehicleTimeSliderGrid,
                                                                          fontLetter=window.fontLetter
                                                                          ,fontSize = 14, fontFactor=window.fontFactor)

        ui.experiencedStrategyInVehicleTimeSliderGrid.addWidget(ui.sliderInVehicleTimeExperiencedStrategyExperimentDebriefPage, 0, 0)

        ui.experiencedStrategyInVehicleTimeSliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.experiencedStrategyInVehicleTimeSliderLbl = ui.experiencedStrategyInVehicleTimeSliderLblGrid.itemAtPosition(0, 0).widget()
        ui.experiencedStrategyInVehicleTimeSliderLbl.setText("In-Vehicle Times")

        # iv) In-Vehicle Time Reliability
        ui.sliderInVehicleTimeReliabilityExperiencedStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                                     allLevels=window.allSliderLevels,
                                                                                     levels=window.sliderLevels,
                                                                                     language=window.mainExperiment.languageCondition
                                                                                     , discreteRange=False,
                                                                                     sliderGrid=ui.experiencedStrategyInVehicleTimeReliabilitySliderGrid,
                                                                                     fontLetter=window.fontLetter
                                                                                     ,fontSize = 14, fontFactor=window.fontFactor)

        ui.experiencedStrategyInVehicleTimeReliabilitySliderGrid.addWidget(ui.sliderInVehicleTimeReliabilityExperiencedStrategyExperimentDebriefPage,
                                                        0, 0)

        ui.experiencedStrategyInVehicleTimeReliabilitySliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.experiencedStrategyInVehicleTimeReliabilitySliderLbl = ui.experiencedStrategyInVehicleTimeReliabilitySliderLblGrid.itemAtPosition(0, 0).widget()
        ui.experiencedStrategyInVehicleTimeReliabilitySliderLbl.setText("Reliability of In-Vehicle Times")

        # v) Overall Journey Time

        ui.sliderJourneyTimeExperiencedStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                    allLevels=window.allSliderLevels,
                                                                    levels=window.sliderLevels,
                                                                    language=window.mainExperiment.languageCondition
                                                                    , discreteRange=False,
                                                                    sliderGrid=ui.experiencedStrategyJourneyTimeSliderGrid,
                                                                    fontLetter=window.fontLetter
                                                                    ,fontSize = 14, fontFactor=window.fontFactor)

        ui.experiencedStrategyJourneyTimeSliderGrid.addWidget(ui.sliderJourneyTimeExperiencedStrategyExperimentDebriefPage, 0, 0)

        ui.experiencedStrategyJourneyTimeSliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.experiencedStrategyJourneyTimeSliderLbl = ui.experiencedStrategyJourneyTimeSliderLblGrid.itemAtPosition(0, 0).widget()
        ui.experiencedStrategyJourneyTimeSliderLbl.setText("Overall Journey Time")

        for sliderBarTripEvaluation in [ui.sliderWaitingTimeExperiencedStrategyExperimentDebriefPage
                                        ,ui.sliderWaitingTimeReliabilityExperiencedStrategyExperimentDebriefPage
            , ui.sliderInVehicleTimeExperiencedStrategyExperimentDebriefPage
                                        ,ui.sliderInVehicleTimeReliabilityExperiencedStrategyExperimentDebriefPage
            , ui.sliderJourneyTimeExperiencedStrategyExperimentDebriefPage]:
            # Format of slider bars
            sliderBarTripEvaluation.setStyleSheet1()

            # Set initial slider value
            sliderBarTripEvaluation.setSliderValue(sliderBarTripEvaluation.max)

    elif page == 3:  #Questions about descriptive experiment

        if window.mainExperiment.languageCondition == "english":
            setTitlePage(grid=ui.experimentDebriefTitleGrid, text="Questions on Decision-From-Description"  # Replace Title
                         , capitalLetters=True, centered=False, fontFactor=window.fontFactor,
                         fontLetter=window.fontLetter)

        if window.mainExperiment.languageCondition == "spanish":
            setTitlePage(grid=ui.experimentDebriefTitleGrid, text="Preguntas sobre Decisiones desde la Descripción "
                         , capitalLetters=True, centered=False, fontFactor=window.fontFactor,
                         fontLetter=window.fontLetter)

        sliderTitle = ""
        window.sliderLevels = None

        if window.mainExperiment.languageCondition == "spanish":
            # sliderLevels = {1: "No estoy segura (1)", 2: "No lo sé",3: "Estoy segura (2)"}
            window.sliderLevels = {1: "Poca \n(Nivel de Importancia: 0%)",
                                   2: "Mucha \n(Nivel de Importancia: 100%)"}
            window.allSliderLevels = {1: "Poca \n(0%)", 2: "",
                                      3: "Mucha \n(100%)"}  # This is what is shown in the slider

            sliderTitle = "Nivel de importancia"

        if window.mainExperiment.languageCondition == "english":
            # sliderLevels = {1: "I am not sure (1)",2: "I do not know (2)", 3: "I am sure (3)"}
            window.sliderLevels = {1: "Low \n(Importance Level: 0%)",
                                   2: "High \n(Importance Level: 100%)"}
            window.allSliderLevels = {1: "Low\n(0%)", 2: "",
                                      3: "High\n(100%)"}  # This is what is shown in the slider

            sliderTitle = "Importance Level"

        # window.lastSliderLevel = window.sliderLevels[len(window.sliderLevels.keys())]
        # window.firstSliderLevel = window.sliderLevels[1]

        # Create slider for each of the four items evaluated by participants

        # i) Waiting Time
        ui.sliderWaitingTimeDescriptiveStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                                   allLevels=window.allSliderLevels
                                                                                   , levels=window.sliderLevels
                                                                                   , language=window.mainExperiment.languageCondition
                                                                                   , discreteRange=False
                                                                                   ,sliderGrid=ui.descriptiveStrategyWaitingTimeSliderGrid
                                                                                   , fontLetter=window.fontLetter
                                                                                   , fontSize = 14
                                                                                   , fontFactor=window.fontFactor)

        ui.descriptiveStrategyWaitingTimeSliderGrid.addWidget(
            ui.sliderWaitingTimeDescriptiveStrategyExperimentDebriefPage, 0, 0)

        ui.descriptiveStrategyWaitingTimeSliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.descriptiveStrategyWaitingTimeSliderLbl = ui.descriptiveStrategyWaitingTimeSliderLblGrid.itemAtPosition(0,
                                                                                                                   0).widget()
        ui.descriptiveStrategyWaitingTimeSliderLbl.setText("Waiting Times")

        # ii) Waiting Time Reliability
        ui.sliderWaitingTimeReliabilityDescriptiveStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                                              allLevels=window.allSliderLevels,
                                                                                              levels=window.sliderLevels,
                                                                                              language=window.mainExperiment.languageCondition
                                                                                              , discreteRange=False,
                                                                                              sliderGrid=ui.descriptiveStrategyWaitingTimeReliabilitySliderGrid,
                                                                                              fontLetter=window.fontLetter
                                                                                              ,fontSize = 14
                                                                                              ,fontFactor=window.fontFactor)

        ui.descriptiveStrategyWaitingTimeReliabilitySliderGrid.addWidget(
            ui.sliderWaitingTimeReliabilityDescriptiveStrategyExperimentDebriefPage, 0, 0)

        ui.descriptiveStrategyWaitingTimeReliabilitySliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.descriptiveStrategyWaitingTimeReliabilitySliderLbl = ui.descriptiveStrategyWaitingTimeReliabilitySliderLblGrid.itemAtPosition(
            0, 0).widget()
        ui.descriptiveStrategyWaitingTimeReliabilitySliderLbl.setText("Reliability of Waiting Times")

        # iii) In-Vehicle Time
        ui.sliderInVehicleTimeDescriptiveStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                                     allLevels=window.allSliderLevels,
                                                                                     levels=window.sliderLevels,
                                                                                     language=window.mainExperiment.languageCondition
                                                                                     , discreteRange=False,
                                                                                     sliderGrid=ui.descriptiveStrategyInVehicleTimeSliderGrid,
                                                                                     fontLetter=window.fontLetter
                                                                                     ,fontSize = 14
                                                                                     ,fontFactor=window.fontFactor)

        ui.descriptiveStrategyInVehicleTimeSliderGrid.addWidget(
            ui.sliderInVehicleTimeDescriptiveStrategyExperimentDebriefPage, 0, 0)

        ui.descriptiveStrategyInVehicleTimeSliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.descriptiveStrategyInVehicleTimeSliderLbl = ui.descriptiveStrategyInVehicleTimeSliderLblGrid.itemAtPosition(
            0, 0).widget()
        ui.descriptiveStrategyInVehicleTimeSliderLbl.setText("In-Vehicle Times")

        # iv) In-Vehicle Time Reliability
        ui.sliderInVehicleTimeReliabilityDescriptiveStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                                                allLevels=window.allSliderLevels,
                                                                                                levels=window.sliderLevels,
                                                                                                language=window.mainExperiment.languageCondition
                                                                                                , discreteRange=False,
                                                                                                sliderGrid=ui.descriptiveStrategyInVehicleTimeReliabilitySliderGrid,
                                                                                                fontLetter=window.fontLetter
                                                                                                ,fontSize = 14, fontFactor=window.fontFactor)

        ui.descriptiveStrategyInVehicleTimeReliabilitySliderGrid.addWidget(
            ui.sliderInVehicleTimeReliabilityDescriptiveStrategyExperimentDebriefPage,
            0, 0)

        ui.descriptiveStrategyInVehicleTimeReliabilitySliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.descriptiveStrategyInVehicleTimeReliabilitySliderLbl = ui.descriptiveStrategyInVehicleTimeReliabilitySliderLblGrid.itemAtPosition(
            0, 0).widget()
        ui.descriptiveStrategyInVehicleTimeReliabilitySliderLbl.setText("Reliability of In-Vehicle Times")

        # v) Overall Journey Time

        ui.sliderJourneyTimeDescriptiveStrategyExperimentDebriefPage = mySliderBar(sliderTitle=sliderTitle,
                                                                                   allLevels=window.allSliderLevels,
                                                                                   levels=window.sliderLevels,
                                                                                   language=window.mainExperiment.languageCondition
                                                                                   , discreteRange=False,
                                                                                   sliderGrid=ui.descriptiveStrategyJourneyTimeSliderGrid,
                                                                                   fontLetter=window.fontLetter
                                                                                   ,fontSize = 14, fontFactor=window.fontFactor)

        ui.descriptiveStrategyJourneyTimeSliderGrid.addWidget(
            ui.sliderJourneyTimeDescriptiveStrategyExperimentDebriefPage, 0, 0)

        ui.descriptiveStrategyJourneyTimeSliderLblGrid.addWidget(QLabel(), 0, 0)
        ui.descriptiveStrategyJourneyTimeSliderLbl = ui.descriptiveStrategyJourneyTimeSliderLblGrid.itemAtPosition(0,
                                                                                                                   0).widget()
        ui.descriptiveStrategyJourneyTimeSliderLbl.setText("Overall Journey Time")

        for sliderBarTripEvaluation in [ui.sliderWaitingTimeDescriptiveStrategyExperimentDebriefPage
            , ui.sliderWaitingTimeReliabilityDescriptiveStrategyExperimentDebriefPage
            , ui.sliderInVehicleTimeDescriptiveStrategyExperimentDebriefPage
            , ui.sliderInVehicleTimeReliabilityDescriptiveStrategyExperimentDebriefPage
            , ui.sliderJourneyTimeDescriptiveStrategyExperimentDebriefPage]:
            # Format of slider bars
            sliderBarTripEvaluation.setStyleSheet1()

            # Set initial slider value
            sliderBarTripEvaluation.setSliderValue(sliderBarTripEvaluation.max)


def readWriteExperimentDebriefPageQuestionsFields(page):

    elif page == 2:  # Strategies in the experienced experiment

    ui.waitingTimeImportanceExperiencedStrategyExperimentDebriefPage = ui.sliderWaitingTimeExperiencedStrategyExperimentDebriefPage.currentValue()
    ui.waitingTimeReliabilityImportanceExperiencedStrategyExperimentDebriefPage = ui.sliderWaitingTimeReliabilityExperiencedStrategyExperimentDebriefPage.currentValue()
    ui.inVehicleTimeImportanceExperiencedStrategyExperimentDebriefPage = ui.sliderInVehicleTimeExperiencedStrategyExperimentDebriefPage.currentValue()
    ui.inVehicleTimeReliabilityImportanceExperiencedStrategyExperimentDebriefPage = ui.sliderInVehicleTimeReliabilityExperiencedStrategyExperimentDebriefPage.currentValue()
    ui.journeyTimeImportanceExperiencedStrategyExperimentDebriefPage = ui.sliderJourneyTimeExperiencedStrategyExperimentDebriefPage.currentValue()

    fieldsCompleted = True

    elif page == 3:  # Strategies in the descriptive experiment

    ui.waitingTimeImportanceDescriptiveStrategyExperimentDebriefPage = ui.sliderWaitingTimeDescriptiveStrategyExperimentDebriefPage.currentValue()
    ui.waitingTimeReliabilityImportanceDescriptiveStrategyExperimentDebriefPage = ui.sliderWaitingTimeReliabilityDescriptiveStrategyExperimentDebriefPage.currentValue()
    ui.inVehicleTimeImportanceDescriptiveStrategyExperimentDebriefPage = ui.sliderInVehicleTimeDescriptiveStrategyExperimentDebriefPage.currentValue()
    ui.inVehicleTimeReliabilityImportanceDescriptiveStrategyExperimentDebriefPage = ui.sliderInVehicleTimeReliabilityDescriptiveStrategyExperimentDebriefPage.currentValue()
    ui.journeyTimeImportanceDescriptiveStrategyExperimentDebriefPage = ui.sliderJourneyTimeDescriptiveStrategyExperimentDebriefPage.currentValue()

    fieldsCompleted = True


def isComboBoxOtherOriginPlaceSelected():
    if ui.comboBoxOriginPlace.currentText() == "Other":
        ui.lineEditOtherOrigin.setVisible(True)
        ui.lineEditOtherOriginLbl.setVisible(True)

    elif ui.comboBoxOriginPlace.currentText() != "Other":
        ui.lineEditOtherOrigin.setVisible(False)
        ui.lineEditOtherOriginLbl.setVisible(False)

def isComboBoxOtherDestinationPlaceSelected():
    if ui.comboBoxDestinationPlace.currentText() == "Other":
        ui.lineEditOtherDestination.setVisible(True)
        ui.lineEditOtherDestinationLbl.setVisible(True)

    elif ui.comboBoxDestinationPlace.currentText() != "Other":
        ui.lineEditOtherDestination.setVisible(False)
        ui.lineEditOtherDestinationLbl.setVisible(False)

def isRadioButtonOtherOriginChecked():
    if ui.radioButtonOtherOrigin.isChecked() is True:
        ui.lineEditOtherOrigin.setVisible(True)
        ui.lineEditOtherOriginLbl.setVisible(True)

    elif ui.radioButtonOtherOrigin.isChecked() is False:
        ui.lineEditOtherOrigin.setVisible(False)
        ui.lineEditOtherOriginLbl.setVisible(False)

def isRadioButtonOtherDestinationChecked():
    if ui.radioButtonOtherDestination.isChecked() is True:
        ui.lineEditOtherDestination.setVisible(True)
        ui.lineEditOtherDestinationLbl.setVisible(True)

    elif ui.radioButtonOtherDestination.isChecked() is False:
        ui.lineEditOtherDestination.setVisible(False)
        ui.lineEditOtherDestinationLbl.setVisible(False)


# # if window.mainExperiment.languageCondition == "english": ui.errorLbl.setText("Please correctly complete the fields marked in red") # Error Message
#         #
#         # if window.mainExperiment.languageCondition == "spanish": ui.errorLbl.setText("Por favor completa correctamente los campos marcados en rojo") # Error Message
#
#         # Check if the fields are correctly completed.
#         attributesLblErrorList = []  # This list contains all the attributes in the page that are not rrectly completed
#
#         if ui.busRouteTravelBehaviourPage == "":
#             attributesLblErrorList.append(ui.busRouteTravelBehaviourPageLbl)
#
#         if ui.departureTimeTravelBehaviourPage == "00:00":
#             attributesLblErrorList.append(ui.departureTimeTravelBehaviourPageLbl)
#
#         if ui.tripsPerWeekMostFreqBusRouteTravelBehaviourPage == 0:
#             attributesLblErrorList.append(ui.tripsPerWeekMostFreqBusRouteTravelBehaviourPageLbl)
#
#         if ui.originPlaceTravelBehaviourPage == " ":
#             if ui.otherOriginPlaceTravelBehaviourPage == " ":
#                 attributesLblErrorList.append(ui.comboBoxOriginPlaceLbl)
#                 attributesLblErrorList.append(ui.lineEditOtherOriginPlaceLbl)
#
#             if ui.otherOriginPlaceTravelBehaviourPage != " ":
#                 attributesLblErrorList.append(ui.comboBoxOriginPlaceLbl)
#
#         if ui.originBoroughTravelBehaviourPage == " ":
#             if ui.otherOriginBoroughTravelBehaviourPage == " ":
#                 attributesLblErrorList.append(ui.comboBoxOriginBoroughLbl)
#                 attributesLblErrorList.append(ui.lineEditOtherOriginBoroughLbl)
#
#             if ui.otherOriginBoroughTravelBehaviourPage != " ":
#                 attributesLblErrorList.append(ui.comboBoxOriginBoroughLbl)
#
#         if ui.destinationPlaceTravelBehaviourPage == " ":
#             if ui.otherDestinationPlaceTravelBehaviourPage == " ":
#                 attributesLblErrorList.append(ui.comboBoxDestinationPlaceLbl)
#                 attributesLblErrorList.append(ui.lineEditOtherDestinationPlaceLbl)
#
#             if ui.otherDestinationPlaceTravelBehaviourPage != " ":
#                 attributesLblErrorList.append(ui.comboBoxDestinationPlaceLbl)
#
#         if ui.destinationBoroughTravelBehaviourPage == " ":
#             if ui.otherDestinationBoroughTravelBehaviourPage == " ":
#                 attributesLblErrorList.append(ui.comboBoxDestinationBoroughLbl)
#                 attributesLblErrorList.append(ui.lineEditOtherDestinationBoroughLbl)
#
#             if ui.otherDestinationBoroughTravelBehaviourPage != " ":
#                 attributesLblErrorList.append(ui.comboBoxDestinationBoroughLbl)