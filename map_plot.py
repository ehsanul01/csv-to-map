import folium
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="csv-mapper")
map = folium.Map(location=[42.8864, -78.8784], zoom_start=6)




with open("addresses.txt") as f:
    for line in f:
        try:
            location = geolocator.geocode(line.strip())
            if location:
                folium.CircleMarker(
                    location=[location.latitude, location.longitude],
                    radius=5,
                    color='red',
                    fill=True,
                    fill_opacity=0.7,
                    popup=line.strip()
                ).add_to(map)
            time.sleep(1)  # avoid rate limits
        except:
            pass

map.save("map.html")
print("Map saved as map.html")
