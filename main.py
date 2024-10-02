import savejson
import formatJSON

# type = 'metar'

while True:
    
    type = input("Enter the type of data you want to retrieve "
                 "(metar, taf, airmet/sigmet): ")
    
    station = input("Enter the station code (e.g. ZSSS): ")
    # latitude = input("Enter the latitude (e.g. 31.2): ")
    # longitude = input("Enter the longitude (e.g. 121.3): ")
    # radius = input("Enter the radius (e.g. 100): ")
    # options = input("Enter any options (e.g. decoded): ")

    savejson.save_metar_taf(type, station, None, None, None, 'decoded')

    if type == 'metar':
        formatJSON.print_format_metar()
    elif type == 'taf':
        formatJSON.print_format_taf()

# TODO: TAF and AIRMET/SIGMET inquires
