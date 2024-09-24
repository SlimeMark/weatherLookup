import requests


with open('api-key.txt', 'r', encoding='utf-8') as file:
    api_key = file.readline().strip()


class GetMetarTaf:
    def __init__(self, type, station, latitude, longitude, radius, options):
        self.api_key = api_key
        self.type = type
        self.station = station
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.options = options
        self.url = f"https://api.checkwx.com/{type}"

    def get_info(self):
        # Check for any station, station+radius, coordinate, coordinate+radius
        if (self.station is None
                and self.longitude and self.latitude and self.radius):
            self.url += (f"/lat/{self.latitude}/lon/{self.longitude}"
                         f"/radius/{self.radius}")
        elif self.station is None and self.latitude and self.longitude:
            self.url += f"/lat/{self.latitude}/lon/{self.longitude}"
        elif self.station and self.radius:
            self.url += f"/{self.station}/radius/{self.radius}"
        else:
            self.url += f"/{self.station}"
        # Check for if decoding was required
        if self.options is not None:
            self.url += f"/{self.options}"

        return requests.get(self.url, headers={'X-API-Key': self.api_key})


class GetAirSig:
    def __init__(self, type, station, latitude, longitude, options):
        self.api_key = api_key
        self.type = type
        self.station = station
        self.latitude = latitude
        self.longitude = longitude
        self.options = options
        self.url = f"https://api.checkwx.com/{type}"

    def get_info(self):
        # Check for any station, coordinate
        if self.station is None and self.longitude and self.latitude:
            self.url += f"/lat/{self.latitude}/lon/{self.longitude}"
        else:
            self.url += f"/{self.station}"
        # Check for if decoding was required
        if self.options is not None:
            self.url += f"/{self.options}"

        return requests.get(self.url, headers={'X-API-Key': self.api_key})

