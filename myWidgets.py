from Scripts.Functions import * #Import py file with my own functions


# ***************   Classes *************************************** #

class Icon(QLabel):
    def __init__(self, id, path,parent):
        self.id = id
        self.path = path
        self.parent = parent

        super().__init__(parent=self.parent)

    def setBackgroundColor(self,color):
        setBackgroundColorQLabel(self, color)

class ClickableOptionIcon(Icon):

    clicked = pyqtSignal()

    def __init__(self, parent, type, id, path,myGrid):
        self.type = type
        self.id = id #home, work, stop1, stop2, stop3, stop4,counterClockwise, clockwise, car, taxi, bus1, bus2, bike, walk, tube,
        #Setting the picture of the label
        self.path = path #path of the picture shown in the icon
        self.myGrid = myGrid

        super().__init__(parent = parent, id = id, path = path)

        self.resetBackgroundColor() #The initial status of the buttons is in white
        self.setPicture(path = path)

    def setType(self,type):
        self.type = type # origin, destination, direction, mode.

    def setPicture(self,path):
        #complete
        self.setPixmap(QtGui.QPixmap(path))
        self.setScaledContents(True)
        self.setFrameShape(QFrame.Box)

    def mouseReleaseEvent(self, mouseEvent):
        self.clicked.emit()
        # self.setBackgroundColor(color = "lightgray")
        self.setBackgroundColor(color="yellow")

    def manualClick(self):
        # self.setBackgroundColor(color="lightgray")
        self.setBackgroundColor(color = "yellow")

    def setBackgroundColor(self,color):
        setBackgroundColorQLabel(self, color)

    #Reset the background color to the initial color (nothing)
    def resetBackgroundColor(self):
        self.setBackgroundColor(color = "white")


class PersonIcon(Icon):
    def __init__(self, parent, id, path,realNetwork,virtualNetwork,position,width,height):
        self.icons = [] # List with the path of the icon and the id
        # self.icons.append(Icon(id,path))

        super().__init__(parent = parent, id = id, path = path)

        self.realNetwork = realNetwork
        self.virtualNetwork = virtualNetwork

        self.width = width
        self.height = height
        self.position = position

        self.setPicture(path=path)
        self.setPosition(position=position, realNetwork=realNetwork, virtualNetwork=virtualNetwork, width=width,
                         height=height)

    def setPicture(self,path):
        #complete
        self.path = path
        self.setPixmap(QtGui.QPixmap(path))
        self.setScaledContents(True)
        self.raise_() #Bring Icon to the front. 'Lower()' does the oppposite

    def addIcon(self,id, path):
        self.icons.append(Icon(id = id, path = path))

    def setIcon(self, id):
        a=0

    def setPosition(self,position,realNetwork,virtualNetwork,width,height):
        #This method convert the positions from the real network to the virtual network (the one that the person see in the experiment)
        virtualPosition = reMapping(position=position, realNetwork=realNetwork,virtualNetwork=virtualNetwork)
        self.setGeometry(virtualPosition.x - width / 2,
                         virtualPosition.y - width / 2, width, height)


class VehicleIcon(Icon):
    def __init__(self, parent, id, path,realNetwork,virtualNetwork,position,width,height,originalPosition=None):
        self.icons = [] # List with the path of the icon and the id
        self.position = position
        self.originalPosition = originalPosition

        super().__init__(id=id, path=path, parent=parent)

        # self.width = width
        # self.height = height
        self.realNetwork = realNetwork
        self.virtualNetwork = virtualNetwork
        self.setPicture(path=path)
        self.setPosition(position=position, realNetwork=realNetwork, virtualNetwork=virtualNetwork, width=width,
                         height=height)


    def setPicture(self, path):
        self.setPixmap(QtGui.QPixmap(path))
        self.setScaledContents(True)
        self.path = path
        self.raise_()

    def setPosition(self,position,realNetwork,virtualNetwork,width,height):
        #This method convert the positions from the real network to the virtual network (the one that the person see in the experiment)
        virtualPosition = reMapping(position=position, realNetwork=realNetwork,virtualNetwork=virtualNetwork)
        self.setGeometry(virtualPosition.x - width / 2,
                         virtualPosition.y - width / 2, width, height)

    def addIcon(self,id, path):
        self.icons.append(Icon(id = id, path = path))

class NetworkLocationIcon(Icon):
    def __init__(self, id, path, parent,realNetwork,virtualNetwork,position,width,height, originalPath = None):
        super().__init__(id = id, path = path,parent = parent)
        self.originalPath = originalPath
        self.setPicture(path = path)
        self.setPosition(position = position,realNetwork = realNetwork,virtualNetwork = virtualNetwork,width = width,height=height)

    def setIcon(self, icon):
        self.setPicture(icon.path)

    def setPicture(self, path):
        # complete
        self.setPixmap(QtGui.QPixmap(path))
        self.setScaledContents(True)
        self.setFrameShape(QFrame.Box)
        self.path = path
        # self.raise_()
        setBackgroundColorQLabel(self, "white")



    def setPosition(self,position,realNetwork,virtualNetwork,width,height):
        #This method convert the positions from the real network to the virtual network (the one that the person see in the experiment)
        virtualPosition = reMapping(position=position, realNetwork=realNetwork,virtualNetwork=virtualNetwork)

        self.setGeometry(virtualPosition.x - width / 2,
                         virtualPosition.y - width / 2, width, height)


class VirtualNetwork(QLabel):
    def __init__(self, id, parent, panel, realNetwork, percentageMaxWidth, percentageMaxHeight):
        self.id = id
        self.panel = panel #Qlabel panel where the map will be shown
        self.realNetwork = realNetwork
        self.percentageMaxWidth = percentageMaxWidth # maxDim: It is the maximum size of a dimension
        self.percentageMaxHeight = percentageMaxHeight

        super().__init__(parent = parent)

        self.setMapPicture()
        self.setMapGeometry(panel,realNetwork,maxHeight = panel.height()*self.percentageMaxHeight, maxWidth = panel.width()*self.percentageMaxWidth)
        self.centerMap(panel)


    def setMapPicture(self, path=None):
        self.setFrameShape(QFrame.Box)

    def setMapGeometry(self,panel,realNetwork,maxHeight, maxWidth):

        scaleFactor = max(maxHeight/realNetwork.height,maxWidth/realNetwork.width)
        scaledWidth = scaleFactor*realNetwork.width
        scaledHeight = scaleFactor*realNetwork.height

        if scaledWidth > maxWidth:
            scaleFactor = maxWidth/scaledWidth
            scaledWidth = scaleFactor * scaledWidth
            scaledHeight = scaleFactor * scaledHeight


        if scaledHeight > maxHeight:
            scaleFactor = maxHeight/scaledHeight
            scaledWidth = scaleFactor * scaledWidth
            scaledHeight = scaleFactor * scaledHeight

        self.setGeometry(panel.x(), panel.y(), scaledWidth,
                         scaledHeight)

    #This method center the map in the panel
    def centerMap(self,panel):
        self.setGeometry(self.x() + (panel.width()-self.width())/2, self.y() + (panel.height()-self.height())/2, self.width(), self.height())


class mySliderBar(QWidget):

    def __init__(self, sliderTitle, levels, allLevels, sliderGrid, discreteRange, language
                 , fontLetter,fontSize, fontFactor, defaultValue = None, parent=None):
        super(mySliderBar, self).__init__(parent)

        self.language = language
        self.fontLetter = fontLetter
        self.fontFactor = fontFactor
        self.fontSize = fontSize

        self.sliderTitle = sliderTitle

        self.columnWidth = 173 #173
        self.columnHeight = 100
        self.layout = QGridLayout()

        #Eliminate spacing of grid
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.layout.setMargin(0)

        #Create Slider

        self.sl = QSlider(Qt.Horizontal)

        #Levels
        self.levels = levels
        self.allLevels = allLevels

        self.sliderGrid = ""
        self.certaintyLevel = None
        self.currentCertaintyLevel = None

        self.createCertaintyLevelLbl(sliderGrid = sliderGrid)

        self.discreteRange = discreteRange

        if self.discreteRange is True:

            self.min = 1
            self.max = len(allLevels.keys())
            self.half = int((self.min + self.max) / 2)
            self.sl.setRange(self.min, self.max)
            self.valueTicks()

            if defaultValue is None:
                self.setSliderValue(self.max)  # Set the value in "I am sure about my decision"
            else:
                self.setSliderValue(defaultValue)

        else:

            self.defaultValue =defaultValue

            self.min = 0
            self.max = 100
            self.half = int((self.min + self.max)/2)
            self.sl.setRange(self.min, self.max)
            self.valueTicks()

            # Initial Value
            if defaultValue is None:
                self.setSliderValue(self.max)  # Set the value in "I am sure about my decision"
            else:
                self.setSliderValue(defaultValue)


        # self.layout.addWidget(self.certaintyLevel,1,1,1,5)



        #Ticks marks
        self.sl.setTickPosition(QSlider.TicksBelow)
        self.sl.setTickInterval(1)


        # self.sl.setMinimum(int(min))
        # self.sl.setMaximum(int(max))
        # self.sl.setValue(3)


        self.sl.setSingleStep(1)


        #This is the row where the slider is located

        leftBlankLabel = QLabel()
        leftBlankLabel.setFixedWidth(self.columnWidth/2-10)
        # leftBlankLabel.setText("L")
        # leftBlankLabel.setFrameShape(QFrame.Box)

        self.layout.addWidget(leftBlankLabel, 1, 0, 1, 1)

        #Here is the slider
        self.layout.addWidget(self.sl,1,1,1,5)
        # self.layout.width.itemAtPosition(1, 1).setFixedHeight(30)
        self.layout.itemAtPosition(1,1).setAlignment(QtCore.Qt.AlignBottom)

        rightBlankLabel = QLabel()
        # rightBlankLabel.setText("R")
        # rightBlankLabel.setFrameShape(QFrame.Box)
        rightBlankLabel.setFixedWidth(self.columnWidth/2-10)
        self.layout.addWidget(rightBlankLabel, 1,6,1,1)

        #Blank spaces below so the slider is centered
        blankLabel = QLabel()
        self.layout.addWidget(blankLabel, 0, 0, 1, 7)

        self.sl.valueChanged.connect(self.valuechange)
        self.setLayout(self.layout)
        # self.setWindowTitle("SpinBox demo")
        # Example: https://stackoverflow.com/questions/27661877/qt-slider-widget-with-tick-text-labels
        # addWidget(QWidget * widget, int fromRow, int fromColumn, int rowSpan, int columnSpan, Qt::Alignment alignment = 0)
        # https://stackoverflow.com/questions/33194678/qt-gridlayout-spanning-multiple-columns

    def setStyleSheet1(self):
        self.stylesheet = """
           QSlider::groove:horizontal {
    border: 1px solid #999999;
    height: 16px; /* the groove expands to the size of the slider by default. by giving it a height, it has a fixed size */
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 white, stop:1 white);
    margin: 2px 0;
}

QSlider::handle:horizontal {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #b4b4b4, stop:1 #8f8f8f);
    border: 1px solid #5c5c5c;
    width: 18px;
    margin: -2px 0; /* handle is placed by default on the contents rect of the groove. Expand outside the groove */
    border-radius: 3px;
}
           """

        self.setStyleSheet(self.stylesheet)

    def createCertaintyLevelLbl(self, sliderGrid):

        self.sliderGrid = sliderGrid
        self.sliderGrid.addWidget(QLabel(""), 0, 0)
        self.certaintyLevel = self.sliderGrid.itemAtPosition(0, 0).widget()

        self.certaintyLevel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.certaintyLevel.setFont(QFont(self.fontLetter, self.fontFactor * self.fontSize, QFont.Bold))

    def valuechange(self):
        # size = self.sl.value()
        # self.l1.setFont(QFont("Arial", size))

        #This allows to have a slider bar with discrete values:
        self.setSliderValue(value = self.sl.value())

        # certaintyLevel

    def setDefaultValue(self,defaultValue = None):
        if defaultValue is None:
            self.setSliderValue(self.defaultValue)

        else:
            self.setSliderValue(defaultValue)

    def currentValue(self):
        return self.currentCertaintyLevel

    def getAlternatives(self, all):
        if all is True:
            return self.allLevels

        else:
            return self.levels

    def setSliderTitle(self,sliderTitle):
        self.sliderTitle = sliderTitle

    def setSliderValue(self, value):

        # value = ""
        if self.discreteRange is True:

            value = int(value)
            self.sl.setValue(value)
        else:
            self.sl.setValue(value)
            # value = value

        integerValue = self.sl.value()

        #Show the label in bold
        if integerValue in self.tickLabels.keys():
            label = self.tickLabels[integerValue]
            label.setFont(QFont(self.fontLetter, self.fontFactor * self.fontSize, QFont.Bold))

        #Hide the bold letters for the remaining labels
        for otherValues in self.tickLabels.keys():
            if otherValues != value:
                label = self.tickLabels[int(otherValues)]
                self.tickLabels[int(otherValues)].setFont(QFont(self.fontLetter, self.fontFactor * self.fontSize))

        #Show value of the certainty level (discrete or continues range)

        self.certaintyLevel.setText(self.sliderTitle+ ": " + str(value) + "%")

        self.currentCertaintyLevel = value
        # self.certaintyLevel.setText(str(value))

    def valueTicks(self):
        # self.tickLabelsLayout = QGridLayout()
        # self.layout.addWidget(self.tickLabelsLayout,2,0)

        # label1 = QLabel("Completely Not Sure")
        label1 = QLabel(self.allLevels[1])
        label2 = QLabel(self.allLevels[2])
        label3 = QLabel(self.allLevels[3])

        self.tickLabels = {self.min:label1,self.half:label2,self.max:label3}

        # label5 = QLabel("Completely Sure")
        # layout = grid

        for label in [label1,label2,label3]:
            # label.setFrameShape(QFrame.Box)
            label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
            label.setFont(QFont(self.fontLetter, self.fontFactor * self.fontSize))
            label.setWordWrap(True)
            label.setFixedWidth(self.columnWidth)
            label.setFixedHeight(self.columnHeight)

            # if label == label1 or label == label5:
            #     label.setFixedWidth(self.columnWidth)

            # else:
            #     label.setFixedWidth(self.columnWidth/2)

        self.layout.addWidget(label1,2,0,1,2)
        self.layout.addWidget(label2,2,2,1,3)
        self.layout.addWidget(label3,2,5,1,2)


        # self.layout.addWidget(label4,1,4,1,1)
        # self.layout.addWidget(label5,1,5,1,2)

        # layout.addWidget(label4, 1, 3)¡
        # setLayout(layout);

