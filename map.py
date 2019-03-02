import folium
import requests as req

url = 'https://www.mountainproject.com/data/get-routes?routeIds=106286621&key=200368472-ed680d2e3b4f3efd04ececb8fd95705a'
resp = req.get(url)
status_code = resp.status_code
print(status_code)


# Create map object
m = folium.Map(location=[37.8139, -83.6279], zoom_start=12)

# Global Tooltip
tooltip = 'Click For Route Info'
# Create markers
folium.Marker([37.6524, -83.7246],
    popup='<strong>Breakfast Burrito</strong>',
    tooltip=tooltip).add_to(m)

# Generate map
m.save('map.html')