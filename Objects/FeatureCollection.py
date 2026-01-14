import json

class FeatureCollection:

    def __init__(self, features):
        self.type = "FeatureCollection"
        self.features = features

    
    def toJSON(self):
        return json.dumps(
            self,
            ensure_ascii=False,
            default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)