class Address:

    def __init__(self, address):
        self.longitude = float(address["lon"])
        self.latitude = float(address["lat"])
        additional_info = address["address"]
        self.suburb = ""
        self.city = ""
        if "city" in additional_info:
            self.city = additional_info["city"]
        elif "town" in additional_info:
            self.city = additional_info["town"]
        elif "village" in additional_info:
            self.city = additional_info["village"]
            
        self.postcode = additional_info["postcode"]
        self.country = additional_info["country"]
        
        self.suburb = ""
        if "suburb" in additional_info:
            self.suburb = additional_info["suburb"]
        
        borough = ""
        if "borough" in additional_info:
            borough = additional_info["borough"]
        elif "city_district" in additional_info:
            borough = additional_info["city_district"]
        self.borough = borough

    def __str__(self):
        string = "Longitude: " + str(self.longitude) + "\n" + \
        "Latitude: " + str(self.latitude) + "\n" + \
        "in " + self.postcode + " " + self.city + "(" + self.country + ")" + "\n" + \
        "Suburb: " + self.suburb + "\n" + \
        "Borough: " +  self.borough
        return string