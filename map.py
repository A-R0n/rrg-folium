import folium
import pandas as pd

data = pd.DataFrame({

# North and South...greater values are above center
'lat':[37.6527, 37.65177, 37.7337, 37.8145, 37.73090, 37.7315, 37.7519, 37.75194, 37.6466, 37.6787, 37.6789, 37.6539, 37.6527, 37.72048, 37.72045, 37.7314, 37.7315],

# East and West...greater absolute values are left of center
'lon':[-83.72515, -83.7098, -83.6388, -83.6639, -83.65582, -83.6565, -83.6615, -83.66370, -83.7229, -83.7356, -83.7358, -83.7176, -83.7177, -83.6628, -83.6627, -83.634, -83.6339], 
'name_of_route':['Check Your Grip', 'Amarillo Sunset', 'Banshee', 'Mercy the Huff', 'The Return of Chris Snyder', 'Ro Shampo', 'Yellow Brick Road', 'No Place Like Home', "Don't Call It a Comeback", 'Crown of Thorns', 'Dog Bites & Fist Fights', '27 Years of Climbing', 'Starry Night', 'Bare Metal Teen', 'Steelworker', 'Jesus Wept', 'Triple Sec'],
'grade':['5.12a', '5.11b', '5.11c', '5.12b', '5.11d', '5.12a', '5.11b', '5.11b', '5.11d', '5.11c', '5.12d', '5.8', '5.12a', '5.12a', '5.12c', '5.12d', '5.12d']
})
data


# Create map object with longitude as the first argument and latitude as the second argument
m = folium.Map(location=[37.75, -83.7000], zoom_start=11)

# Global Tooltip
tooltip = 'Click For Route Info'
# Create markers

# It goes (y axis N<-->S, x axis E<-->W)

for i in range(0,len(data)):
    folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], popup=folium.Popup(data.iloc[i]['name_of_route'] + '\n' + data.iloc[i]['grade'], max_width=150), tooltip=tooltip, icon=folium.Icon(icon='picture', icon_color='white', color='black')).add_to(m)

# Generate map
m.save('map.html')