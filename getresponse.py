import requests


with open('api-key.txt', 'r', encoding='utf-8') as file:
    api_key = file.readline().strip()

class GetMetarTaf:
    def __init__(self, station, latitude, longitude, radius, options):
        self.api_key = api_key
        self.station = station
        self.latitude = latitude
        self.longitude = longitude
        self.radius = radius
        self.options = options

    def add_params(self):
        params = {
            'radius': self.radius,
            'lat': self.latitude,
            'lon': self.longitude,
            'options': self.options,
        }
        params = {k: v for k, v in params.items() if v is not None}
        headers = {
            'X_API_Key': self.api_key
        }
        response = requests.get(self.url, params=params, headers=api_key)
        return response.json()


class GetMETAR(GetMetarTaf):
    def __init__(self, station, latitude, longitude, radius, options):
        super().__init__(station, latitude, longitude, radius, options)
        self.url = "https://api.checkwx.com/metar/{}".format(station)

    def get_response(self):
        return super().add_params()


class GetTAF(GetMetarTaf):
    def __init__(self, station, latitude, longitude, radius, options):
        super().__init__(station, latitude, longitude, radius, options)
        self.url = "https://api.checkwx.com/taf/{}".format(station)

    def get_response(self):
        return super().add_params()


class GetAIRMET:
    def __init__(self, station, latitude, longitude, options):
        self.api_key = api_key
        self.station = station
        self.latitude = latitude
        self.longitude = longitude
        self.options = options
        self.url = (
            "https://api.checkwx.com/airmet/{}".format(station) if options is not None
            else "https://api.checkwx.com/airmet/{}/decoded".format(station)
        )

    def get_response(self):
        response = requests.get(self.url, headers=api_key)
        return response.json()


class GetSIGMET(GetAIRMET):
    def __init__(self, station, latitude, longitude, options):
        super().__init__(station, latitude, longitude, options)
        self.url = (
            "https://api.checkwx.com/sigmet/{}".format(station) if options is not None
            else "https://api.checkwx.com/sigmet/{}/decoded".format(station)
        )

    def get_response(self):
        response = requests.get(self.url, headers=api_key)
        return response.json()


getMetar = GetMETAR('ZSSS', None, None, None, 'decoded')
print(getMetar.get_response())