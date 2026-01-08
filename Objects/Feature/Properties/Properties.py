from Objects.Feature.Properties.PropertiesBase import PropertiesBase

class Properties(PropertiesBase):

    def __init__(self, street, district, units, property_number, purchase_date, akelius_sub, abr, seclusion_certificate, conversion_permit, sales_date, preemption, notes, milieu_protection_area):
        super().__init__(street, district, units, purchase_date, property_number, conversion_permit, seclusion_certificate, milieu_protection_area, akelius_sub, notes)
        self.ABR = abr
        self.Verkaufsdatum = sales_date
        self.Vorkauf = preemption