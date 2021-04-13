from math import sqrt, degrees, atan2


class Customer:

    x = 0
    y = 0
    demand = 0
    angleWithDepot = 0

    def __init__(self,name):
        self.name = name

    def setCor(self,x,y):
        self.x = x
        self.y = y

    def setDemand(self,d):
        self.demand = d

    def setAngleWithDepot(self, a):
        self.angleWithDepot = a

    def __str__(self):
        # return str(self.name) #+ " -> (" + str(self.pos.x) + ", " + \
                #str(self.pos.y) + ") -> " + str(self.demand)
        return "(" + str(self.pos.x) + ", " + \
                   str(self.pos.y) + " )"

    @classmethod
    # def calculateDepotAngle(self, x, y, depot_x, depot_y):
    #     angle = degrees(atan2(depot_x - x,  depot_y - y))
    #     bearing = (90 - angle) % 360
    #     return bearing
    def calculateDepotAngle(self, x, y, depot_x, depot_y):
        angle = degrees(atan2(x - depot_x, y - depot_y))
        bearing = (90 - angle) % 360
        return bearing
    # def calculateDepotAngle(self, x, y, depot_x, depot_y):
    #     angle = degrees(atan2(y - depot_y, x - depot_x))
    #     bearing = (90 - angle) % 360
    #     return bearing

    @classmethod
    def get_distance(self,cus1, cus2):
    # Euclideian
        dist = 0
        dist = sqrt(((cus1.x - cus2.x) ** 2) + ((cus1.y - cus2.y) ** 2))
        return dist

    @classmethod
    def get_saving(self,cus1, cus2, depot_x, depot_y):
    # Saving
        saving = 0
        saving = - sqrt(((cus1.x - cus2.x) ** 2) + ((cus1.y - cus2.y) ** 2)) + sqrt(((cus1.x - depot_x) ** 2) + ((cus1.y -
            depot_y) ** 2)) + sqrt(((cus1.x - depot_x) ** 2) + ((cus1.y - depot_y) ** 2))
        return saving



