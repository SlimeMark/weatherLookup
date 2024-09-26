import json
import re
import plotbarb


def print_format_metar():
    with open('response.json') as f:
        data = json.load(f)
    for i in range(len(data['data'])):
        print("\n")
        print(f"Station: {data['data'][i]['station']['name']}")
        print(f"Time: {data['data'][i]['observed']}")
        print(f"Temperature: {data['data'][i]['temperature']['celsius']}°C")
        print(f"Dewpoint: {data['data'][i]['dewpoint']['celsius']}°C")
        try:
            print(f"Wind: {data['data'][i]['wind']['degrees']}° at "
                  f"{data['data'][i]['wind']['speed_kts']} knots")
            # Calls the plot_bard function
            wind_dir = data['data'][i]['wind']['degrees']
            wind_spd = data['data'][i]['wind']['speed_kts']
            plotbarb.plot_barb(wind_dir, wind_spd)
        except KeyError:
            print("Wind Calm")
        try:
            print("Clouds: ")
            print("+-----------------+")
            cloud = {}
            for j in range(len(data['data'][i]['clouds'])):
                cloud[data['data'][i]['clouds'][j]['text']] \
                    = [int(data['data'][i]['clouds'][j]['base_feet_agl'])]
            for key, value in sorted(cloud.items(),
                                     key=lambda x: x[1], reverse=True):
                print(f"{key} at {value[0]} feet AGL")
            print("+-----------------+")
            raw = data['data'][i]['raw_text']
            if re.search('CB', raw):
                print("Caution: CB reported")
            if re.search('TCU', raw):
                print("Caution: TCU reported")
            print(f"Ceiling: {data['data'][i]['ceiling']['feet']} feet")
        except KeyError:
            if not data['data'][i]['clouds']:
                print("+------CAVOK------+")
                print("+-----------------+")
            print("No ceiling reported")
        try:
            print("Conditions: ")
            print("+-----------------+")
            for k in range(len(data['data'][i]['conditions'])):
                print(f"{data['data'][i]['conditions'][k]['text']}")
            print("+-----------------+")
        except KeyError:
            print("No conditions reported")
        print(f"Visibility: {data['data'][i]['visibility']['meters']} meters")
        print(f"Altimeter: {data['data'][i]['barometer']['hpa']} hPa")
        print(f"Flight Category: {data['data'][i]['flight_category']}")
        print(f"Raw Report: {data['data'][i]['raw_text']}")
        print("\n")


def format_taf():
    pass
# TODO: TAF formatting, AIRMET/SIGMET formatting
