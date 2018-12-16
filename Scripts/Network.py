from Scripts.Functions import * #Import py file with my own functions
# from ITS import * #Import py file with my own functions

class Network:

    #busStops: List of Bus Stops
    #busFleet: List of buses
    #length: length of the route
    #Routes have the shape of a square. The shape is given for a set of 4 objects type Position: northEastCorner,northWestCorner,southWestCorner,southEastCorner)
    #Points: It divides the total length of the routes in many segments depending on how many points are assigned.
    def __init__(self, busStops, buses, busRoutes, networkSpeed, width, height, start, end, nSegments, locations, busTerminals):

        #Elements of a route

        #Create a dictionary of bus stops
        self.busStops = {}
        for busStop in busStops:
            self.busStops[busStop.id] = busStop

        # Create a dictionary of buses
        self.buses = {}
        for bus in buses:
            self.buses[bus.id] = bus

        # Create a dictionary of bus terminals
        self.busTerminals = busTerminals

        #Shape of the route (objects type Position)
        self.start = start # The start of the route can be within any point defined by the square
        self.end = end # The end of the route can be within any point defined by the square

        self.width = width
        self.height = height
        self.southWestCorner = Position(0,0) #This is the point (0,0) for the map of the route and will be assumed as the southest corner. To transform then in the UI, we need to substract the y value of NW and calculate absolute value
        self.southEastCorner = Position(width,0)
        self.northWestCorner = Position(0,height)
        self.northEastCorner = Position(width,height)
        self.nSegments = nSegments

        self.busRoutes = busRoutes

        #Operational parameters
        self.networkSpeed = networkSpeed  # Each route operate at a given speed. All buses in the route operate at the same speed
        self.loadingTime = 0  # We assume that the passenger loading times at bus stops is 0.
        # self.length = ((self.origin.x-self.destination.x)**2-(self.origin.y-self.destination.y)**2)**(0.5)
        self.length = 2*(width+height) #Routes has a square or rectangular shapes.
        self.theorethicalFrequency = len(buses)*self.networkSpeed/self.length #Asumming constant speeds.
        self.theorethicalHeadway = 1/self.theorethicalFrequency #Asumming constant speeds.

        self.segmentLength = self.length/self.nSegments

        #List of locations
        self.locations = locations

    def length(self):
        return self.length

    def theorethicalFrequency(self):
        return self.theorethicalFrequency

    def theorethicalHeadway(self):
        return self.theorethicalHeadway
