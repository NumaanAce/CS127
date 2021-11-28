# Name: Numaan Qureshi
# Email: numaan.qureshi58@myhunter.cuny.edu
# Date: November 10 2021

import folium

mapChelseaPiers = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.7420577, -74.0101494], popup = "Little Island").add_to(mapChelseaPiers)

mapChelseaPiers.save(outfile='nycMap.html')
