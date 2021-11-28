# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: November 10 2021

import folium
import pandas as pd

csvName = input("Enter name of CSV file: ")
outName = input("Enter name of output file: ")

attractions = pd.read_csv(csvName)
# attractions = pd.read_csv("attractions.csv")

mapAttractions = folium.Map(location=[40.768731, -73.964915])

for index, row in attractions.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["NAME"]
    newMarker = folium.Marker([lat, lon], popup=name)
    newMarker.add_to(mapAttractions)

mapAttractions.save(outfile=outName)
