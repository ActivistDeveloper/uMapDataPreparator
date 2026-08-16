import pandas as pandas
import math
from Objects.Feature.FeatureWithoutAkelius import FeatureWithoutAkelius 

class InputData:

    LAYER_WITHOUT_AKELIUS = "ohne Akelius"
    LAYER_AKELIUS_WITHOUT_SECLUSION_CERTIFICATE = "ex-Alius ohne Abgeschlossenheitsvereinbarung"
    LAYER_AKELIUS_WITH_SECLUSION_CERTIFICATE = "ex-Alius mit Abgeschlossenheitsvereinbarung"
    LAYER_SAVED = "gerettet"

    def __init__(self, file_path):
        self.file_path = file_path
        self.data_table = pandas.read_csv(self.file_path, header = 0)

    def get_features_without_akelius(self):
        filtered_data_table = self.data_table[self.data_table['Layer'] == self.LAYER_WITHOUT_AKELIUS]

        key_mapping = {'name' : 'street', 
                       'Bezirk' : 'locality',
                       'Stadtteil': 'district',
                       'Milieuschutzgebiet' : 'milieu_protection_area',
                       'Objektnummer' : 'property_number',
                       'Abgeschlossenheitsbescheinigung' : 'seclusion_certificate', 
                       'Abwendungsvereinbarung' : 'avoidance_agreement',
                       'Kaufdatum': 'purchase_date',
                       'Vorbesitzer_in' : 'former_owner',
                       'Umwandlungserlaubnis' : 'conversion_permit',
                       'Wohnungseinheiten': 'units',
                       'Gewerbeeinheiten' : 'commercial_units',
                       'Kaufdatum Akelius' : 'akelius_purchase_date',
                       'Unterfirma' : 'akelius_sub',
                       'Notizen' : 'notes'
                        }

        column_to_remove = "Layer"
        parameter_dict = self.convert_to_parameter_dictionary(filtered_data_table.to_dict(orient='index'), key_mapping, column_to_remove)

        return [FeatureWithoutAkelius(**kwargs) for kwargs in parameter_dict]
    
    def convert_to_parameter_dictionary(self, dict, key_mapping, column_to_remove):
        
        parameters = list()

        for index, dictionary in dict.items():
            parameter_dict = {}
            for item_key in dictionary:
                if item_key != column_to_remove:
                    new_key = key_mapping[item_key]
                    if new_key != None:
                        dict_value = self.remove_default_value(dictionary[item_key])
                        parameter_dict[new_key] = dict_value
                        print("newkey: " + new_key + " value " + str(dict_value))
            parameters.append(parameter_dict)

        return parameters
    
    def remove_default_value(self, value):
        cleaned_value = ""
        if type(value) == str:
            cleaned_value = value
        elif not math.isnan(value):
            cleaned_value = value
        return cleaned_value
