# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: 17 November 2021

import folium as fol
import pandas as pd

csvName = input("Please enter the name of the input file: ")
outName = input("Please enter the name of the output file: ")
borName = input("Please enter the name of the borough: ")

hotspots = pd.read_csv(csvName)
# hotspots = pd.read_csv("NYC_Wi-Fi_Hotspot_Locations.csv")

if borName.title() == "Brooklyn":
    nycMap = fol.Map(location=[40.650002, -73.949997])
elif borName.title() == "Queens":
    nycMap = fol.Map(location=[40.742054, -73.769417])
elif borName.title() == "New York":
    nycMap = fol.Map(location=[40.776676, -73.971321])
elif borName.title() == "Bronx":
    nycMap = fol.Map(location=[40.837048, -73.865433])
elif borName.title() == "Staten Island":
    nycMap = fol.Map(location=[40.579021, -74.151535])
else:
    nycMap = fol.Map(location=[40.75, -74.125])

borough = hotspots.groupby("City").get_group(borName)

for index, row in borough.iterrows():
    lat = row["Latitude"]
    long = row["Longitude"]
    name = row["Name"]
    newMarker = fol.Marker([lat, long], popup=name)
    newMarker.add_to(nycMap)

nycMap.save(outfile=outName)

# END
