from Objects.Feature.Properties.PropertiesBase import PropertiesBase

class WithoutAkeliusProperties(PropertiesBase):

    def __init__(self, street, postcode, locality, district, units, commercial_units, avoidance_agreement, purchase_date, akelius_purchase_date, former_owner, property_number, conversion_permit, seclusion_certificate, milieu_protection_area, akelius_sub, notes):
        super().__init__(street, district, units, purchase_date, property_number, conversion_permit, seclusion_certificate, milieu_protection_area, akelius_sub, notes)
        self.Abwendungsvereinbarung =  avoidance_agreement
        self.Bezirk = locality
        self.Vorbesitzer_in = former_owner
        self.Gewerbeeinheiten = commercial_units
        self.PLZ = postcode
        self.KaufdatumAkelius = akelius_purchase_date