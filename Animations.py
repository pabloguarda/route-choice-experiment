import copy #To copy objects
import functools #To give parameters to function connected by timers

from myWidgets import * #Import py file with my own widgets
from Scripts.Location import * # class

# from Main import * #Mode class
#The width will be recalculated according to the dimensions of the real network


# ***************   Timers Functions *************************************** #

def personWalkingToBusStopTimer(stop,clockwise,person,myTimer,its,timerInterval,statusLbl, mainExperiment):

    # person.icon.setPicture(path="Pictures/walkingWork.png")

    if mainExperiment.languageCondition == "spanish":
        updateStatusSimulationExpPage(status="Caminando al paradero", statusLbl=statusLbl,
                                      mainExperiment=mainExperiment)

    if mainExperiment.languageCondition == "english":
        updateStatusSimulationExpPage(status="Walking to bus stop", statusLbl=statusLbl, mainExperiment=mainExperiment)

    myTimerCallBack = functools.partial(personMovingUI,person=person, destination=stop,clockwise=clockwise
                                        ,myTimer = myTimer, its = its, isWalking = True,statusLbl = statusLbl, mainExperiment = mainExperiment)
    myTimer.timeout.connect(myTimerCallBack)
    myTimer.start(timerInterval) #timerInterval in seconds

def personWalkingToBusStopInformationTimer(stop,clockwise,person,myTimer,its,timerInterval,targetedWaitingTime,statusLbl, mainExperiment):


    if mainExperiment.languageCondition == "spanish":
        updateStatusSimulationExpPage(status="Caminando al paradero", statusLbl=statusLbl,
                                      mainExperiment=mainExperiment)

    if mainExperiment.languageCondition == "english":
        updateStatusSimulationExpPage(status="Walking to bus stop", statusLbl=statusLbl, mainExperiment=mainExperiment)



    myTimerCallBack = functools.partial(personMovingBusStopInformationUI,person=person
                                        , stop=stop,clockwise=clockwise,myTimer = myTimer, its = its, isWalking = True
                                        ,remainingWaitingTime = targetedWaitingTime,statusLbl = statusLbl, mainExperiment = mainExperiment)
    myTimer.timeout.connect(myTimerCallBack)
    myTimer.start(timerInterval) #timerInterval in seconds

def personWalkingFromBusStopTimer(stop,clockwise,person,myTimer,its,timerInterval, mainExperiment):
    # person.icon.setPicture(path="Pictures/walkingWork.png")
    person.setWalkingDistanceFromStopToDestination(its.pathDistance(origin = person.position, destination = stop.position, clockwise = clockwise))
    myTimerCallBack = functools.partial(personMovingUI,person=person, destination=stop.position,clockwise=clockwise
                                        ,myTimer = myTimer, its = its, isWalking = True, mainExperiment = mainExperiment)
    myTimer.timeout.connect(myTimerCallBack)
    myTimer.start(timerInterval) #timerInterval in seconds

def personWalkingToWestLocationTimer(destination,clockwise,person,myTimer,its,timerInterval, mainExperiment):
    person.icon.setPicture(person.icons["eastToWest"].path)
    person.setWalkingDistanceFromOriginToDestination(its.pathDistance(origin = person.position, destination = destination, clockwise = clockwise))
    myTimerCallBack = functools.partial(personMovingUI,person=person, destination=destination,clockwise=clockwise,myTimer = myTimer, its = its, isWalking  = True, mainExperiment = mainExperiment)
    myTimer.timeout.connect(myTimerCallBack)
    myTimer.start(timerInterval) #timerInterval in seconds

def personWalkingToEastLocationTimer(destination,clockwise,person,myTimer,its,timerInterval, mainExperiment):

    person.icon.setPicture(person.icons["westToEast"].path)
    person.setWalkingDistanceFromOriginToDestination(
        its.pathDistance(origin=person.position, destination=destination, clockwise=clockwise))
    myTimerCallBack = functools.partial(personMovingUI,person=person, destination=destination,clockwise=clockwise, myTimer = myTimer, its = its, isWalking = True, mainExperiment = mainExperiment)
    myTimer.timeout.connect(myTimerCallBack)
    myTimer.start(timerInterval) #timerInterval in seconds

def personDrivingTimer(destination,clockwise,person,its,car,myTimer,timerInterval):
    person.icon.setPicture(car.icon.path)
    person.speed = car.speed
    myTimerCallBack = functools.partial(personMovingUI,person=person, destination=destination,clockwise=clockwise,myTimer = myTimer, its = its, isWalking = False)
    myTimer.timeout.connect(myTimerCallBack)
    myTimer.start(timerInterval) #timerInterval in seconds

def personBikingTimer(destination,clockwise,person,its,bike,myTimer,timerInterval):

    person.icon.setPicture(path="Pictures/bikingRight.png")
    person.icon.setPicture(bike.icon.path)
    person.speed = bike.speed
    myTimerCallBack = functools.partial(personMovingUI,person=person, destination=destination,clockwise=clockwise,myTimer = myTimer, its = its, isWalking = False)
    myTimer.timeout.connect(myTimerCallBack)
    myTimer.start(timerInterval) #timerInterval in seconds

def startBusTripTimer(trajectory,bus,its,myTimer, timerInterval, departureTime,person,personTimer
                      ,ui,nextJourneyClicked, statusLbl,lastUpdateLearningPhase, mainExperiment):
    # bus.icon.setPicture(bus.icon.path)
    # bus.icon.raise_()
    myTimerCallBack = functools.partial(completeBusTrip, trajectory=trajectory, bus=bus,
                                                 its=its, myTimer=myTimer, timerInterval = timerInterval
                                        ,person=person,personTimer = personTimer
                                        ,ui = ui
                                        ,nextJourneyClicked = nextJourneyClicked
                                        , statusLbl = statusLbl
                                        , lastUpdateLearningPhase = lastUpdateLearningPhase
                                        , mainExperiment = mainExperiment
                                        )
    myTimer.timeout.connect(myTimerCallBack)

    #Configure the timer for generate a random delay before the bus leave its departure terminal (setSingleshot)
    myTimer.setInterval(departureTime*1000)
    myTimer.setSingleShot(True)
    myTimer.start() # The bus will move after the delay (method completeBusRun()). This will allow to generate different waiting times at the bus stop

# ***************   Animations Functions *************************************** #

def busMovingUI(bus,destination,clockwise,timeInterval,its,busIcon):

    if bus.moving == False:
        busTrajectory = its.trajectory(origin=bus.position, destination=destination, clockwise=clockwise,timeInterval=timeInterval,speed=bus.speed)
        bus.move(trajectory=busTrajectory,clockwise = clockwise)

    bus.move(trajectory = bus.trajectory,clockwise = bus.clockwise) #if the bus is already moving there will be a trajectory and direction previously defined
    busVirtualPosition = its.getVirtualPosition(position = bus.position)
    busIcon.setGeometry(busVirtualPosition.x-busIcon.width()/2, busVirtualPosition.y-busIcon.height()/2, busIcon.width(), busIcon.height())

def personMovingUI(person,destination,clockwise,myTimer, its, isWalking,mainExperiment, statusLbl = None):

    trajectoryPerson = its.createTrajectory(origin=person.position, destination=destination,
                                                   clockwise=clockwise,
                                                   speed=person.speed)['trajectory']


    its.movePerson(person = person, trajectory = trajectoryPerson, isWalking = isWalking)

    #When the person stop walking, the timer needs to be stopped
    if person.moving == False: #Person has arrived to the first bus stop to take the bus
        if isinstance(destination,BusStop):
            destination.icon.setPicture("")
            destination.icon.setText("?")
            destination.icon.setFont(QFont(mainExperiment.fontLetter, mainExperiment.fontFactor * 24, QFont.Bold))
            destination.icon.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            person.icon.setVisible(False)
            # person.icon.setPicture(person.icons["waitingStop"].path)


            if statusLbl is not None:

                if mainExperiment.languageCondition == "spanish":
                    updateStatusSimulationExpPage(status="Esperando en paradero", statusLbl=statusLbl,
                                                  mainExperiment=mainExperiment)

                if mainExperiment.languageCondition == "english":
                    updateStatusSimulationExpPage(status="Waiting at bus stop", statusLbl=statusLbl,
                                                  mainExperiment=mainExperiment)

        myTimer.stop()

def personWaitingTimer(person, remainingWaitingTime, stop, statusLbl, mainExperiment):

    roundDigitsTime = 0

    if mainExperiment.variableWaitingTimer == True:
        unitLabel = "s"
        unitLabel = ""

    else:
        unitLabel =  " [s]"

    remainingWaitingTime = int(remainingWaitingTime)
    stop.icon.setPicture("")
    person.icon.setPicture(person.icons["waitingStop"].path)

    if mainExperiment.languageCondition == "spanish":
        updateStatusSimulationExpPage(
            status="Esperando en paradero (próximo bus en " + str(round(remainingWaitingTime, roundDigitsTime)) + " segundos)"
            , statusLbl=statusLbl, mainExperiment=mainExperiment)

    if mainExperiment.languageCondition == "english":
        updateStatusSimulationExpPage(
            status="Waiting at bus stop (next bus in " + str(round(remainingWaitingTime, roundDigitsTime)) + " seconds)"
            , statusLbl=statusLbl, mainExperiment=mainExperiment)

    person.icon.setVisible(False)

    stop.icon.setText(str(round(remainingWaitingTime,roundDigitsTime)) + unitLabel)
    stop.icon.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
    stop.icon.setFont(QFont(mainExperiment.fontLetter, mainExperiment.fontFactor*16, QFont.Bold))

def personMovingBusStopInformationUI(person, stop, clockwise, myTimer, remainingWaitingTime, its, isWalking,statusLbl, mainExperiment):

    if stop.getNextBusTime() is None:
        stop.setNextBusTime(nextBusTime= remainingWaitingTime)


    trajectoryPerson = its.createTrajectory(origin=person.position, destination=stop.position,
                                            clockwise=clockwise,
                                            speed=person.speed

                                            )['trajectory']

    its.movePerson(person=person, trajectory=trajectoryPerson, isWalking=isWalking)

    # This shows real time information when the person arrived to the bus stop.
    if person.moving == False:
        # a = stop.getNextBusTime()
        # b = remainingWaitingTime-1
        personWaitingTimer(person=person, remainingWaitingTime = stop.getNextBusTime() , stop=stop, statusLbl = statusLbl, mainExperiment = mainExperiment)

        # True if the counter for waiting time decrease second by second
        if mainExperiment.variableWaitingTimer == True:
            myTimer.stop()
            myTimer.setInterval(1000)
            myTimer.start(1000)
            stop.setNextBusTime(nextBusTime=stop.getNextBusTime()-1)


            if stop.getNextBusTime() <= 0:
                stop.setNextBusTime(nextBusTime=None)
                myTimer.stop()
                # stop.icon.setText(str(0))



        else:
            stop.setNextBusTime(nextBusTime=stop.getNextBusTime())
            myTimer.stop()

#Receive object type trajectory
def completeBusTrip(trajectory, bus, its,myTimer,person, timerInterval,personTimer,ui,nextJourneyClicked, lastUpdateLearningPhase,statusLbl, mainExperiment):
    nextJourneyButton = ui.nextJourneyButton
    trajectoryBus = copy.copy(trajectory)
    myTimer.setSingleShot(False) #The timer has been setted in one single shot to model the delay of a bus (a proxy for waiting time)
    myTimer.start(timerInterval) #Now, the timer allows to simualte the trajectory of the bus between the departure and arrival terminal
    firstBusStop = bus.route.busStops[1] #The first bus stop of the route, where the bus first will stop
    lastBusStop = bus.route.busStops[2] #The bus stop where the passenger will get off

    #If the bus has not arrived yet to the bus stop where the passenger is waiting (departing from terminal)
    if its.isNextPositionAhead(trajectory = trajectory,currentPosition = bus.position, nextPosition = firstBusStop.position) == True:
        if mainExperiment.languageCondition == "spanish":
            updateStatusSimulationExpPage(status="Bus llegando", statusLbl=statusLbl,mainExperiment = mainExperiment)

        if mainExperiment.languageCondition == "english":
            updateStatusSimulationExpPage(status="Bus arriving", statusLbl=statusLbl,mainExperiment = mainExperiment)

        bus.icon.setVisible(True)


        # firstBusStop.icon.setText("")
        # person.icon.setVisible(True)
        # person.icon.setPicture(person.icons["busArriving"].path)
        # # firstBusStop.icon.setPicture(firstBusStop.icon.originalPath)

        trajectoryToFirstBusStop = its.createTrajectory(origin = trajectory.origin,destination = firstBusStop.position,clockwise = trajectory.isClockwise(),speed = trajectory.speed)['trajectory']
        trajectoryBus = copy.copy(trajectoryToFirstBusStop)
        #Move the bus to the next position
        its.moveBus(trajectory = trajectoryBus, bus = bus)

    # If the bus has arrived to the bus stop where the passenger is waiting
    elif its.equalPositions(bus.position,firstBusStop.position) == True and firstBusStop.visited == False: #The bus arrive to the stop where the passenger is waiting

        person.icon.setVisible(True)
        bus.icon.setVisible(False)
        person.icon.setPicture(person.icons["busArriving"].path)

        if mainExperiment.languageCondition == "spanish":
            updateStatusSimulationExpPage(status="Subiendo al bus", statusLbl=statusLbl,mainExperiment = mainExperiment)

        if mainExperiment.languageCondition == "english":
            updateStatusSimulationExpPage(status="Boarding the bus", statusLbl=statusLbl,mainExperiment = mainExperiment)

        # trajectoryToFirstBusStop = its.createTrajectory(origin=trajectory.origin, destination=firstBusStop.position,
        #                                                 clockwise=trajectory.isClockwise(), speed=trajectory.speed)['trajectory']
        # trajectoryBus = copy.copy(trajectoryToFirstBusStop)

        firstBusStop.icon.setPicture("")


        person.icon.setVisible(True)
        person.icon.raise_()


        #This timer's operations allows to generate the dwell time at the bus stop
        myTimer.setSingleShot(True)
        myTimer.setInterval(firstBusStop.getDwellTime()*1000) #1 second of detention
        myTimer.start()
        firstBusStop.visited = True


        #Create a new icon picture using the bus image
        personBusIcon = PersonIcon(parent = bus.icon.parent,id = bus.icon.id, path = bus.icon.path
                   , realNetwork = bus.icon.realNetwork,virtualNetwork = bus.icon.virtualNetwork,
                   position = person.position,width = person.icon.width,height = person.icon.height)

        personWalkingIcon = PersonIcon(parent = person.icon.parent,id = person.icon.id, path = person.icon.path
                   , realNetwork = person.icon.realNetwork,virtualNetwork = person.icon.virtualNetwork,
                   position = person.position,width = person.icon.width,height = person.icon.height)

        person.addIcon(personBusIcon)
        person.addIcon(personWalkingIcon)
        # person.setPictureIcon(person.icons[personBusIcon.id].path)

        # # Move the bus to the next position
        # its.moveBus(trajectory=trajectoryBus, bus=bus)

    #If the bus has not arrived yet to the bus stop where the passenger is getting off
    elif its.isNextPositionAhead(trajectory = trajectory,currentPosition = bus.position, nextPosition = lastBusStop) == True:

        bus.icon.setVisible(True)
        person.icon.setPicture(person.icons["walking"].path)

        if mainExperiment.languageCondition == "spanish":
            updateStatusSimulationExpPage(status="Viajando al destino", statusLbl=statusLbl,mainExperiment = mainExperiment)

        if mainExperiment.languageCondition == "english":
            updateStatusSimulationExpPage(status="Travelling to destination", statusLbl=statusLbl,mainExperiment = mainExperiment)



        firstBusStop.icon.setPicture(firstBusStop.icon.originalPath)
        person.icon.setVisible(False)
        trajectoryToLastBusStop = its.createTrajectory(origin=trajectory.origin, destination=lastBusStop.position,
                                                        clockwise=trajectory.isClockwise(),
                                                        speed=trajectory.speed)['trajectory']

        trajectoryBus = copy.copy(trajectoryToLastBusStop)

        trajectoryPerson = copy.copy(trajectoryBus)
        its.movePerson(trajectory=trajectoryPerson, person=person, isWalking=False)

        # Move the bus to the next position
        its.moveBus(trajectory=trajectoryBus, bus=bus)

    # If the bus has arrived to the bus stop where the passenger is getting off
    elif its.equalPositions(bus.position,lastBusStop.position) == True  and lastBusStop.visited == False:

        if mainExperiment.languageCondition == "spanish":
            updateStatusSimulationExpPage(status="Bajando del bus", statusLbl=statusLbl,mainExperiment = mainExperiment)

        if mainExperiment.languageCondition == "english":
            updateStatusSimulationExpPage(status="Getting off the bus", statusLbl=statusLbl,mainExperiment = mainExperiment)

        person.icon.setVisible(True)
        bus.icon.setVisible(False)
        person.icon.setPicture(person.icons["alightingBus"].path)
        lastBusStop.icon.setPicture("")

        trajectoryToLastBusStop = its.createTrajectory(origin=trajectory.origin, destination=lastBusStop.position,
                                                        clockwise=trajectory.isClockwise(),
                                                        speed=trajectory.speed)['trajectory']

        trajectoryBus = copy.copy(trajectoryToLastBusStop)
        # myTimer.stop()
        myTimer.setInterval(lastBusStop.getDwellTime()*1000) #1 second of detention
        myTimer.setSingleShot(True)
        myTimer.start()
        lastBusStop.visited = True

        #Update the picture of the passenger because it got off from the bus.
        # person.setPictureIcon(person.icons[person.icon.id].path)


        # Move the bus to the next position
        its.moveBus(trajectory=trajectoryBus, bus=bus)

    # If the bus is departing the last bus stop and arriving to the arrival terminal
    else:
        person.icon.setPicture(person.icons["walking"].path)
        bus.icon.setVisible(False)

        if mainExperiment.languageCondition == "spanish":
            updateStatusSimulationExpPage(status="Caminando al destino", statusLbl=statusLbl,mainExperiment = mainExperiment)

        if mainExperiment.languageCondition == "english":
            updateStatusSimulationExpPage(status="Walking to destination", statusLbl=statusLbl,mainExperiment = mainExperiment)

        lastBusStop.icon.setPicture(lastBusStop.icon.originalPath)
        # Move the bus to the next position
        trajectoryBus = copy.copy(trajectory)
        its.moveBus(trajectory=trajectoryBus, bus=bus)

        #Move the person
        person.speed = person.walkingSpeed
        personMovingUI(person, destination = person.finalLocation.position, clockwise =  trajectoryBus.isClockwise(), myTimer = personTimer, its = its, isWalking = True, mainExperiment = mainExperiment)

    #When the bus arrive to the bus terminal
    if its.equalPositions(bus.position,bus.route.arrivalTerminal.position):
        bus.icon.setVisible(False)
        #When the person arrive to the final destination
        if its.equalPositions(person.position, person.finalLocation.position):
            myTimer.stop() #This stopped the timer for the bustrip. Then the thread will continue and will stop the timer of the person
            #Reset values of booleans variables
            firstBusStop.visited = False
            lastBusStop.visited = False
            person.icon.setVisible(False)

            if not mainExperiment.isLastTrial(mainExperiment.currentExperiment):
                nextJourneyButton.setVisible(False)
                nextJourneyClicked()

            else:
                nextJourneyButton.setVisible(True)
                lastUpdateLearningPhase(mainExperiment = mainExperiment, statusLbl = statusLbl)
                ui.simulationExpGrid.itemAtPosition(0, 0).widget().setText("")




    # completed = Fals
    # stop.icon.setPicture("Pictures/stop1.png")

def updateStatusSimulationExpPage(status, statusLbl, mainExperiment):
    # Update Status

    if mainExperiment.languageCondition == "spanish":
        statusLbl.setText("Estado: " + status)

    if mainExperiment.languageCondition == "english":
        statusLbl.setText("Status: " + status)





