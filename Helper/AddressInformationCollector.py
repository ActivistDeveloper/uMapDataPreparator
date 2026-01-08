import requests
from Objects.Address import Address

class AddressInformationCollector:

    def collect(self, street):
        """
        Query nominatim to get information (especially latitude and longitude) of the adress which is located at the given street.
        Returns (lat, lon). Raises ValueError if not found.
        """
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": street,
            "format": "json",
            "addressdetails": 1,
            "limit": 100
        }
        headers = {"User-Agent": "umap-prep-script/1.0"}   # <- required by Nominatim
        r = requests.get(url, params=params, headers=headers)
        r.raise_for_status()
        data = r.json()

        print(data)

        if not data:
            raise ValueError(f"Address not found: {street}")

        return self.process_address_information(data)
    
    def process_address_information(self, data):
        potential_addresses = list()
        for address in data:
            potential_addresses.append(Address(address))
        return potential_addresses
