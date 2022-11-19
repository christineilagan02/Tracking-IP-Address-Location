import geocoder
import folium

g = geocoder.ip("me")
Address = g.latlng

my_map1 = folium.Map(location=Address,
                     zoom_start=12)

folium.CircleMarker(location=Address, 
                    radius=50, popup="location").add_to(my_map1)

folium.Marker(Address, popup="location").add_to(my_map1)

my_map1.save("my_map.html")