from Objects.Geometry import Geometry

class Point(Geometry):

    def __init__(self, longitude, latitude):
        self.type = "Point"
        self.coordinates = [longitude, latitude]