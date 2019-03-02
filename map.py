import folium
import requests as req

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