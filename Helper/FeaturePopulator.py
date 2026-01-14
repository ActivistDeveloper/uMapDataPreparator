import time
from Helper.AddressInformationCollector import AddressInformationCollector
from Helper.MultipleOptionFeature import MultipleOptionFeature

class FeaturePopuplator:

    def __init__(self, features):
        self.features = features

    def populate(self):
        self.unpopulatable_feature = list()

        address_collector = AddressInformationCollector()

        for feature in self.features:
            try:
                potential_adresses = address_collector.collect(feature.get_street())
                if len(potential_adresses) == 1:
                    feature.populate(potential_adresses[0])
                else:
                    multiple_option_feature = MultipleOptionFeature(feature, potential_adresses)
                    self.unpopulatable_feature.append(multiple_option_feature)

            except ValueError as e:
                print(e)
                no_option_feature = MultipleOptionFeature(feature, list())
                self.unpopulatable_feature.append(no_option_feature)
                continue

            # Respect Nominatim's rate limit
            time.sleep(1)

    def get_unpopulated_features(self):
        return self.unpopulatable_feature