import getresponse
import json


options = 'decoded'  # Force response decoded, as raw text was contained.


def save_metar_taf(type, station, latitude, longitude, radius, options):
    response = getresponse.GetMetarTaf(type, station, latitude, longitude,
                                       radius, options).get_info().json()
    with open('response.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(response))


def save_air_sig(type, station, latitude, longitude, options):
    response = getresponse.GetAirSig(type, station, latitude,
                                     longitude, options).get_info().json()
    with open('response.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(response))
