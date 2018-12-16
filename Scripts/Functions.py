# ***************  Generic Functions *************************************** #

import sys
from os import listdir # This library has some functions to read the list of files names in a folder
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from ExperimentInterface import * #UI of the experiment
from datetime import datetime #This library contain functions that return the current time and date in the computer. It will be used for the function fileNameId
from Scripts.TimeSpace import *

#Group radio buttons so if the user select one of them the other is not selected
def setRadioButtons(radioButton1,radioButton2):
    if radioButton1.isChecked():
        radioButton2.setChecked(False)

    if radioButton2.isChecked():
        radioButton1.setChecked(False)

def setPairCheckBoxButtons1(QCheckBox1,QCheckBox2):

    if QCheckBox1.isChecked():
        QCheckBox2.setCheckState(0)

    if QCheckBox2.isChecked():
        QCheckBox1.setCheckState(0)


def windowMaximized(window,fullScreen, showMainWindowTitle):
    """Create a new window just to calculate the height and width when it is maximized.
    # In this way, the program will work well, regardless the screen resolution
    Percentage of the window that will be margin (default 0)
    """
    screen = QtGui.QDesktopWidget().screenGeometry()
    window.setGeometry(0, 0, screen.width(), screen.height())

    windowMaximized = QMainWindow()
    # windowMaximized.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
    windowMaximized.showMaximized()
    heightWindowMaximized = windowMaximized.height()
    widthWindowMaximized = windowMaximized.width()
    windowMaximized.close()

    if fullScreen is True:
        # window.showFullScreen()
        window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        percentageScreen = 1

    else:
        percentageScreen = 0.9

    if showMainWindowTitle is False:
        window.setWindowTitle(" ")
        # window.setWindowFlags(QtCore.Qt.CustomizeWindowHint)  # Hide the name of the window

    # Set the dimensions of the window based on a percentage of the total width and height of the screen
    windowWidth = widthWindowMaximized*percentageScreen
    windowHeight = heightWindowMaximized*percentageScreen

    #Set the size of the window to a maximized window (Optional)
    window.setGeometry(0, 0, windowWidth, windowHeight)



def removeUpperButtonsWindow(window):
    """Remove Maximize, Minimize and close buttons"""
    window.setWindowFlags(window.windowFlags() | QtCore.Qt.CustomizeWindowHint)
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
    window.setWindowFlags(window.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
    #Source: http://stackoverflow.com/questions/18600081/how-to-disable-the-window-maximize-icon-using-pyqt4

def backgroundStackedWidget(stackedWidget, color):
    """Set the color of the window (e.g. color = red). uclLogo is a boolean"""
    stackedWidget.setAutoFillBackground(True)
    stackedWidgetColours = stackedWidget.palette() #get the palette
    stackedWidgetColours.setColor(QPalette.Window, QColor(color))
    stackedWidget.setPalette(stackedWidgetColours)

def nextButtonFormat(buttonNext, language, fontFactor, fontLetter, small = False):
    """Add next button to the lower corner of every window"""
    pageStackedWidget = buttonNext.parentWidget()  # page of the stacked widget where the button was located

    if small == True:
        buttonNextWidth = 120
        buttonNextHeight = 40

        buttonNext.setGeometry(pageStackedWidget.width() - buttonNextWidth * 1.1
                               , pageStackedWidget.height() - buttonNextHeight,
                               buttonNextWidth, buttonNextHeight)

    else:
        buttonNextWidth = 300
        buttonNextHeight = 80

        buttonNext.setGeometry(pageStackedWidget.width() - buttonNextWidth * 1.15
                               , pageStackedWidget.height() - buttonNextHeight* 1.1,
                               buttonNextWidth, buttonNextHeight)

    if language == "english":
        buttonNext.setText("Next")

    if language == "spanish":
        buttonNext.setText("Siguiente")

    buttonNext.setFont(QFont(fontLetter, fontFactor*20))
    buttonNext.setFocusPolicy(QtCore.Qt.NoFocus)
    buttonNext.raise_()


# Transform numbers in word (spanish or english)

def getNumberToWord(number, language, cardinal,capitalLetter = True):

    if cardinal is True:

        if language == "spanish":
            if number == 1: word = "Primer"
            elif number == 2: word = "Segundo"
            elif number == 3: word = "Tercer"
            elif number == 4: word = "Cuarto"
            elif number == 5: word = "Quinto"
            elif number == 6: word = "Sexto"
            elif number == 7: word = "Séptimo"
            elif number == 8: word = "Octavo"
            elif number == 9: word = "Noveno"
            elif number == 10: word = "Décimo"
            elif number == 11: word = "Oncéavo"
            elif number == 12: word = "Docéavo"
            else: word = ""

        if language == "english":
            if number == 1: word = "First"
            elif number == 2: word = "Second"
            elif number == 3: word = "Third"
            elif number == 4: word = "Fourth"
            elif number == 5: word = "Fifth"
            elif number == 6: word = "Sixth"
            elif number == 7: word = "Seventh"
            elif number == 8: word = "Eighth"
            elif number == 9: word = "Ninth"
            elif number == 10: word = "Tenth"
            elif number == 11: word = "Eleventh"
            elif number == 12: word = "Twelveth"


            else: word = ""

    if cardinal is False:

        if language == "spanish":

            if number == 1: word = "Uno"
            elif number == 2: word = "Dos"
            elif number == 3: word = "Tres"
            elif number == 4: word = "Cuatro"
            elif number == 5: word = "Cinco"
            elif number == 6: word = "Seis"
            elif number == 7: word = "Siete"
            elif number == 8: word = "Ocho"
            elif number == 9: word = "Nueve"
            elif number == 10: word = "Diez"
            elif number == 11: word = "Once"
            elif number == 12: word = "Doce"
            else: word = ""

        if language == "english":

            if number == 1: word = "One"
            elif number == 2: word = "Two"
            elif number == 3: word = "Three"
            elif number == 4: word = "Four"
            elif number == 5: word = "Five"
            elif number == 6: word = "Six"
            elif number == 7: word = "Seven"
            elif number == 8: word = "Eight"
            elif number == 9: word = "Nine"
            elif number == 10: word = "Ten"
            elif number == 11: word = "Eleven"
            elif number == 12: word = "Twelve"
            else: word = ""

    if capitalLetter is False:

        if word is not "":
            return word.lower()

        else:
            return ""

    else:
        return word



# def wordNumberSpanish(number):
#     if

# ***************  Functions for writing csv files *************************************** #

def attributeLabel(attribute): #Sometimes attributes have blank spaces or \n. We will remove them to avoid errors later.
    newAttributeLabel = attribute.replace(" ", "")  # Remove empty space from the attribute name.
    newAttributeLabel = newAttributeLabel.replace("\n", "")  # Remove empty lines from the attribute name.
    return newAttributeLabel

def printCsvLine(attributesList): #Function Receive a list of attributes (strings or numbers) and return a line following the required formt for csv files
    csvLine = ""

    if len(attributesList) == 1:
        csvLine = attributesList[0] + "\n"

    elif len(attributesList) == 2:
        csvLine = attributesList[0] + ", " + attributesList[1]+ "\n"

    elif len(attributesList)>2:
        for i in range(0,len(attributesList)):
            attribute = str(attributesList[i])
            # attribute = attribute.replace(" ","") #Remove empty space from the attribute name.
            attribute = attribute.replace("\n","") #Remove empty lines from the attribute name.

            if i < len(attributesList)-1: #If the attribute is not the last one to be added in the line
                csvLine += attribute + ","
            else:
                csvLine += attribute + "\n" #If it is the last attribute in the line, \n has to be added to follow the format of a csv file.

    return(csvLine)

#fileNameId is a simple function that adds between the filename (first argument) an the file extension(second argument) an id with the date and time following the format was used for the participants' entries filenames.
def fileNameId(fileName,extension):
    dateTimeNow = datetime.now().strftime(
        '%d%m%Y%H%M%S')  # Current date and time. It follows the same format than what was used in the participants file names.
    return(fileName + dateTimeNow +"."+ extension)  # Name of the summary file including the current date and time.

def roundUp(number):
    if number-int(number)>0:
        return int(number)+1

    else:
        return number


# ***************  Interface Functions *************************************** #

# This function receive a (x,y) pair from the GIS position and transform it to the positions used in the UI.

#map: It is the picture of the route followed by the bus. All positions are relative to the North West Corner and Y increase toward the South
def reMapping(position, realNetwork, virtualNetwork):
    # The width of the route icon is ...
    scaleWidthFactor = virtualNetwork.width() / realNetwork.width
    scaleHeightFactor = virtualNetwork.height() / realNetwork.height

    virtualPosition = Position(x = virtualNetwork.x() + scaleWidthFactor * position.x, y = virtualNetwork.y() +virtualNetwork.height()-scaleHeightFactor * position.y)

    return virtualPosition


#Grid with options of origin, destinations and modes.

def addRowIconsGrid(grid,nRow,nameRow,icons, nIcons,width,height, horizontal = True):

    nCol = 0

    for icon in icons:
        icon.setGeometry(icon.x(), icon.y(), width, height)
        grid.addWidget(icon,nRow,nCol)
        nCol += 1

    #icons: Number of icons per row in the grid layouts. If there are less icons, this method will add blank Qlabels, which are not clickable nor visibles.
    # In this way, the space will be qually distributed among the four grids (Origin,destination,direction, mode)

    if horizontal == True:
        if len(icons) < nIcons:

            for i in range(nCol,nIcons):
                grid.addWidget(QLabel(), nRow, nCol)
                blankQLabel = grid.itemAtPosition(nRow, nCol).widget()
                blankQLabel.setPixmap(QtGui.QPixmap("Pictures/blankSquare.png"))
                blankQLabel.setScaledContents(True)
                blankQLabel.setGeometry(blankQLabel.x(), blankQLabel.y(),width, height)
                nCol += 1

    else:

        if len(icons) < nIcons:
            for i in range(nCol, nIcons):
                grid.addWidget(QLabel(), nCol, nRow)
                blankQLabel = grid.itemAtPosition(nCol,nRow ).widget()
                blankQLabel.setPixmap(QtGui.QPixmap("Pictures/blankSquare.png"))
                blankQLabel.setScaledContents(True)
                blankQLabel.setGeometry(blankQLabel.x(), blankQLabel.y(), width, height)
                nCol += 1

#Set the background color of the others clickedLabels in blank
def oneClickedLabel(clickableLabel):
    myGrid = clickableLabel.myGrid
    for i in range(myGrid.count()):
        setBackgroundColorQLabel(myGrid.itemAt(i).widget(),"white")
    setBackgroundColorQLabel(clickableLabel,"yellow")

# ***************   General Functions for widgets *************************************** #

#subWidget is centered in the main widget
def centerWidget(mainWidget, subWidget):
    subWidget.setGeometry((mainWidget.width() - subWidget.width()) / 2, (mainWidget.height() - subWidget.height()) / 2,
                          subWidget.width(), subWidget.height())

#Only the method move() works to change position of stacked widgets
def centerStackedWidget(mainWindow, stackedWidget):
    # ui.stackedWidget.children():
    stackedWidget.move((mainWindow.width() - stackedWidget.width()) / 2,(mainWindow.height() - stackedWidget.height()) / 2)
    for page in stackedWidget.children():
        if isinstance(page, QWidget):
            page.setGeometry(0, 0, stackedWidget.width(), stackedWidget.height())

def isClockwise(direction):
    if direction == "clockwise":
        return True
    elif direction == "counterclockwise":
        return False
    else:
        return None

# ***************   General Functions for widgets *************************************** #

def clearQFormLayout(layout):
    for i in reversed(range(layout.count())):
        layout.itemAt(i).widget().setParent(None)

def setNoRedLettersColourQLabel(QLabel):
    QLabel.setStyleSheet("color: black")

# Receive a QLabel (label) and change its color
def setRedLettersQLabel(QLabel):
    myPalette = QPalette()
    myPalette.setColor(QtGui.QPalette.Foreground, QtCore.Qt.red)
    QLabel.setPalette(myPalette)

def setLettersColorQLabel(QLabel, colorString):
    myPalette = QPalette()
    myPalette.setColor(QtGui.QPalette.WindowText, QColor(colorString))
    QLabel.setPalette(myPalette)

def UCLTheme(QLabel):
    QLabel.setStyleSheet("color: white ; border: 1px solid  black; background: black ;")
    # setLettersColorQLabel(QLabel=QLabel, colorString="white")
    # setBackgroundColorQLabel(QLabel = QLabel, colorString = "black")
    QLabel.setFrameShape(QFrame.Box)
    # QLabel.setAlignment(QtCore.Qt.bottom)

def setBackgroundColorQLabel(QLabel, colorString):
    QLabel.setAutoFillBackground(True)
    myPalette = QLabel.palette()
    myPalette.setColor(QPalette.Window, QColor(colorString))
    QLabel.setPalette(myPalette)

# Error background(Red)
def setErrorBackgroundColorQLabel(QLabel):
    setBackgroundColorQLabel(QLabel, colorString="red")

#Change colors of the letters
def setRedErrorLettersColorQLabel(QLabel):
    QLabel.setStyleSheet("color: red")

def setErrorBackgroundColorQWidget(qWidget):
    qWidget.setStyleSheet("background-color: #f6989d")

# Clear any coloured background
def setNoBackgroundColorQLabel(QLabel):
    setBackgroundColorQLabel(QLabel, colorString="white")




# ***************   Read and print Consent Form *************************************** #


def getTicksConsentForm(language):

    if language == "spanish":

      tick1 = "leido la hoja de información"
      tick2 = "tenido la oportunidad de hacer preguntas y discutir el estudio"
      tick3 = "recibido respuestas satisfactorias a todas mis preguntas o he sido aconsejada/o por una persona " \
              "para contactar por respuestas para preguntas pertinentes acerca de la investigación y mis derechos como " \
              "participante y a quién contactar en el caso de una lesión asociada a la investigación."

      tick4 = "entendido que yo tengo el derecho para abandonar en cualquier etapa simplemente cerrando el programa de computador"
      tick5 = "entendido que yo consiento procesar mi información personal sólo para el propósito de este estudio " \
              "y que tal información será tratada como estrictamente confidencial y manejada de acuerdo con las disposiciones " \
              "de la Ley de Protección de Datos de 1998."
      tick6 = "entendido que, al hacer click en 'Continuar', yo consiento participar en este estudio"


    if language == "english":

        tick1 = "read the information sheet"
        tick2 = "had the opportunity to ask questions and discuss the study"
        tick3 = "received satisfactory answers to all my questions or have been advised of an individual " \
                "to contact for answers to pertinent questions about the research and my rights as a participant and " \
                "whom to contact in the event of a research-related injury."

        tick4 = "understood that I have the right to withdraw at any stage simply by closing the computer program"
        tick5 = "understood that I consent to the processing of my personal information for the purposes of this study " \
                "only and that any such information will be treated as strictly confidential and handled in accordance " \
                "with the provisions of the Data Protection Act 1998."
        tick6 = "understood that, by clicking ‘Continue’, I consent to participate in this study"

    ticks = []

  # ticks.append(tick1,tick2)


    for tick in [tick1,tick2,tick3,tick4,tick5,tick6]:
        ticks.append(tick)

    return ticks
















