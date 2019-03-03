import folium
from folium.features import CustomIcon
import pandas as pd
import os
import numpy as np

data = pd.DataFrame({

# North and South...greater values are above center
'lat':[37.6527, 37.65177, 37.7337, 37.8175, 37.73090, 37.7315, 37.7519, 37.75194, 37.6466, 37.6787, 37.6789, 37.6539, 37.6527, 37.72048, 37.72045, 37.7314, 37.7315, 37.7329, 37.6524, 37.8159, 37.80285, 37.8029, 37.8487, 37.8399, 37.6440, 37.6418, 37.6429, 37.6443, 37.6458, 37.6438, 37.6426, 37.6412, 37.6465],

# East and West...greater absolute values are left of center
'lon':[-83.72515, -83.7098, -83.6388, -83.6639, -83.65582, -83.6565, -83.6615, -83.66370, -83.7229, -83.7356, -83.7358, -83.7176, -83.7177, -83.6628, -83.6627, -83.634, -83.6339, -83.6616, -83.7232, -83.58, -83.5741, -83.5744, -83.6635, -83.6460, -83.6785, -83.6840, -83.6820, -83.6795, -83.67999, -83.6795, -83.6855, -83.6805, -83.6802], 
'name_of_route':['Check Your Grip', 'Amarillo Sunset', 'Banshee', 'Mercy the Huff', 'The Return of Chris Snyder', 'Ro Shampo', 'Yellow Brick Road', 'No Place Like Home', "Don't Call It a Comeback", 'Crown of Thorns', 'Dog Bites & Fist Fights', '27 Years of Climbing', 'Starry Night', 'Bare Metal Teen', 'Steelworker', 'Jesus Wept', 'Triple Sec', 'Hippocrite', 'Dogleg', 'King Me', 'Prime Directive', 'Orange Juice', 'The Gift', 'Twinkie', 'Witness The Citrus', 'Brachial Plexus', 'Fatal Vision', 'Western Blot', 'Grim Reaper', 'Breakfast at Koops', 'Cloudy with a Chance of Seaman', 'Return of the Mohan', 'Dead on Arrival'],
'grade':['5.12a', '5.11b', '5.11c', '5.12b', '5.11d', '5.12a', '5.11b', '5.11b', '5.11d', '5.11c', '5.12d', '5.8', '5.12a', '5.12a', '5.12c', '5.12d', '5.12d', '5.12a', '5.12a', '5.11b', '5.11b', '5.12c', '5.12a', '5.12a', '5.11c', '5.11c', '5.11c', '5.11d', '5.12a', '5.11d', '5.11d', '5.11d', '5.11d']
})
data


# Create map object with longitude as the first argument and latitude as the second argument
m = folium.Map(location=[37.75, -83.6500], zoom_start=11)

img = folium.raster_layers.ImageOverlay(
    name='Mercator projection SW',
    image='mountain.png',
    bounds=[[-82, -180], [82, 180]],
    opacity=0.6,
    interactive=True,
    cross_origin=False,
    zindex=1,
)


# Global Tooltip
tooltip = 'Click For Route Info'


# Create markers
for i in range(0,len(data)):
    folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=folium.Popup(data.iloc[i]['name_of_route'] + '\n' + data.iloc[i]['grade'], max_width=150), icon=CustomIcon('mountain.png', icon_size=(30,30))).add_to(m)

# Circle Marker
folium.CircleMarker(
    location=[37.7195, -83.6615],
    radius=20,
    tooltip='Torrent Falls',
    color='#428bca',
    fill=True,
    fill_color='#428bca'
).add_to(m)

# folium.GeoJson(overlay, name='Land of Arches').add_to(m)
# Generate map
m.save('map.html')