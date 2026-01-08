from Objects.Feature.FeatureBase import FeatureBase
from Objects.Feature.Properties.WithoutAkeliusProperties import WithoutAkeliusProperties

class FeatureWithoutAkelius(FeatureBase):

    def __init__(self, street, units, commercial_units, avoidance_agreement, purchase_date, akelius_purchase_date, former_owner, property_number, conversion_permit, seclusion_certificate, milieu_protection_area, akelius_sub, notes, postcode="", locality="", district=""):
        super().__init__()

        self.properties = WithoutAkeliusProperties(street, postcode, locality, district, units, commercial_units, avoidance_agreement, purchase_date, akelius_purchase_date, former_owner, property_number, conversion_permit, seclusion_certificate, milieu_protection_area, akelius_sub, notes)

    def get_street(self):
        return self.properties.name
    
    def populate(self, address):
        super().populate(address)

        if self.IsNoneOrEmpty(self.properties.Stadtteil):
            self.set_district(address.suburb)
    
        if self.IsNoneOrEmpty(self.properties.Bezirk):
            self.set_loyalty(address.borough)

    def set_district(self, district):
        self.properties.Stadtteil = district

    def set_loyalty(self, loyalty):
        self.properties.Bezirk = loyalty

    def IsNoneOrEmpty(self, value):
        return value == None or not value
    