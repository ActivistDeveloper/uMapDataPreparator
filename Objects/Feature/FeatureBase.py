from Objects.Point import Point
import json

class FeatureBase:

    def __init__(self):
        self.type = "Feature"

    def set_geometry(self, geometry):
        self.geometry = geometry

    def populate(self, address):
        point = Point(address.longitude, address.latitude)
        self.set_geometry(point)

    def toJSON(self):
        return json.dumps(
            self,
            ensure_ascii=False,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)