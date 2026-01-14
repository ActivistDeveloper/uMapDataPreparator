import sys
from Helper.InputData import InputData
from Helper.FeaturePopulator import FeaturePopuplator
from Objects.FeatureCollection import FeatureCollection

def print_features(features):
    for feature in features:
        print(feature.toJSON())

def populate(unpopulated_features):
    for unpopulated_feature in unpopulated_features:
        print ("Possible options for: " + str(unpopulated_feature.feature.toJSON()))
        address_option_count = len(unpopulated_feature.possible_options)
        for i in range(address_option_count):
            print(str(i) + ": " + str(unpopulated_feature.possible_options[i]))
        selected_address = None
        while selected_address == None:
            input_string = input("Which address is matching?")
            matching_address_index = -1
            try:
                matching_address_index = int(input_string)
                if(matching_address_index >= 0 and matching_address_index < address_option_count):
                    selected_address = unpopulated_feature.possible_options[matching_address_index]
                    unpopulated_feature.feature.populate(selected_address)
            except:
                print("Please enter an integer!")
                

if __name__ == "__main__":
    input_file_path = "Neue-Heimstaden-Häuser-für-die-Karte.csv"

    if len(sys.argv) == 2:
        input_file_path = sys.argv[1]

    try:
        # Feature data from csv
        input_data_reader = InputData(input_file_path)
        features = input_data_reader.get_features_without_akelius()

        feature_populator = FeaturePopuplator(features)
        feature_populator.populate()

        print("Unpopulated features: ")

        unpopulatable_features = feature_populator.get_unpopulated_features()
        populate(unpopulatable_features)

        feature_collection = FeatureCollection(features)

        print("Feature Collection: ")
        print(feature_collection.toJSON())
    except FileNotFoundError:
        print("Could not load file from location: " + input_file_path)
    except:
        print("Ups, something went wrong!")

    
    