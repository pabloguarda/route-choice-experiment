class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# A structure with a point that represent the order, position (X) and time (T).
class XT:
    def __init__(self, order, time, position):
        self.order = order  # Starting from 0. Time increase as the order increase
        self.time = time
        self.position = position

class Trajectory:  # Time-space
    def __init__(self, origin, destination, direction, xts, speed):
        self.origin = origin  # The origin of the chain
        self.destination = destination  # The end of the chain
        self.direction = direction
        self.xts = xts  # list of XT positions-time states
        self.speed = speed
        self.nPositions = self.getNPositions()

    def getNPositions(self):
        maxOrder = 0
        for xt in self.xts:
            if xt.order>maxOrder:
                maxOrder = xt.order
        #Order start in 0
        return maxOrder+1

    def isClockwise(self):
        if self.direction.id == "clockwise":
            return True
        elif self.direction.id == "counterclockwise":
            return False
        else:
            return None

class Direction:
    def __init__(self, id):
        self.id = id

    def isClockwise(self):
        if self.id == "clockwise":
            return True
        elif self.id == "counterclockwise":
            return False
        else:
            return None
