class PropertiesBase:

    def __init__(self, street, district, units, purchase_date, property_number, conversion_permit, seclusion_certificate, milieu_protection_area, akelius_sub, notes):
        self.name = street
        self.Stadtteil = district
        self.Wohneinheiten = units
        self.Kaufdatum = purchase_date
        self.Objektnummer = property_number
        self.Umwandlungserlaubnis = conversion_permit
        self.Abgeschlossenheitsbescheinigung = seclusion_certificate
        self.Milieuschutzgebiet = milieu_protection_area
        self.Akelius_Sub = akelius_sub
        self.Notizen = notes
