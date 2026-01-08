from Objects.Feature.FeatureBase import FeatureBase
from Objects.Feature.Properties import Properties

class Feature(FeatureBase):

    def __init__(self, street, units, property_number, purchase_date, akelius_sub, abr, seclusion_certificate, conversion_permit, sales_date, preemption, notes, milieu_protection_area, district=""):
        super().__init__()

        self.properties = Properties(street, district, units, purchase_date, property_number, conversion_permit, seclusion_certificate, milieu_protection_area, akelius_sub, notes)

    def populate(self, address):
        super().populate(address)
        
        if self.properties.Stadtteil == None:
            self.set_district(address.borough)

    def get_street(self):
        return self.properties.name

    def set_district(self, district):
        self.properties.Stadtteil = district

