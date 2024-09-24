import json


with open('response.json') as f:
    data = json.load(f)


def print_format_metar():
    for i in range(len(data['data'])):
        print(f"Station: {data['data'][i]['station']['name']}")
        print(f"Time: {data['data'][i]['observed']}")
        print(f"Temperature: {data['data'][i]['temperature']['celsius']}°C")
        print(f"Dewpoint: {data['data'][i]['dewpoint']['celsius']}°C")
        print(f"Wind: {data['data'][i]['wind']['degrees']}° at "
              f"{data['data'][i]['wind']['speed_kts']} knots")
        print("Clouds: ")
        print("+-----------------+")
        cloud = {}
        try:
            for j in range(len(data['data'][i]['clouds'])):
                cloud[data['data'][i]['clouds'][j]['text']] \
                    = [int(data['data'][i]['clouds'][j]['base_feet_agl'])]
            for key, value in sorted(cloud.items(),
                                     key=lambda x: x[1], reverse=True):
                print(f"{key} at {value[0]} feet AGL")
        except KeyError:
            pass
        print("+-----------------+")
        print(f"Ceiling: {data['data'][i]['ceiling']['feet']} feet")
        print(f"Visibility: {data['data'][i]['visibility']['meters']} meters")
        print(f"Altimeter: {data['data'][i]['barometer']['hpa']} hPa")
        print(f"Flight Category: {data['data'][i]['flight_category']}")
        print(f"Raw Report: {data['data'][i]['raw_text']}")
        print("\n")


def format_taf():
    pass
# TODO: TAF formatting, AIRMET/SIGMET formatting
