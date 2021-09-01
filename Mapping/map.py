import folium
import pandas
import branca
def colour_fixing(elevation):
    if elevation<1000:
        return 'green'
    elif elevation>1000 and elevation<3000:
        return 'orange'
    else:
        return 'red'

data=pandas.read_csv("Volcanoes.txt")
htm = """<h4>Volcano information:</h4>
Height: %s m
"""
map = folium.Map(location=[48.7767982,-121.8109970], tiles="Stamen Terrain")
lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
iframe = branca.element.IFrame(html=htm, width=500, height=300)


"""fg=folium.FeatureGroup(name="My Map")"""
fgv=folium.FeatureGroup(name="Volcanoes")
for x,y,z in zip(lat,lon,elev):
    colour=colour_fixing(z)
    fgv.add_child(folium.Marker(location=[x, y], popup=folium.Popup(iframe),icon=folium.Icon(color=colour)))

fgp=folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <=x['properties']['POP2005']<20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map = map.save("map.html")

