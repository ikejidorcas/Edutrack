import folium
import geopandas as gpd
import random

q1 = "nigeria.jsonfile"
q2 = gpd.read_file(q1)

q3 = folium.Map( location=[9.0820, 8.6753], zoom_start=6)


def random_color(feature):
    return {
        'fillColor': f'#{random.randint(0, 0xFFFFFF):06x}',
        'color': 'blue',       
        'weight':2,
        'fillOpacity':0.7
    }

folium.GeoJson(
    q1,
    name="Nigeria States",
    style_function=random_color,
    tooltip=folium.GeoJsonTooltip(
        fields=["state", "capital"],  
        aliases=["State:", "Capital:"],
        localize=True
    )
).add_to(q3)

q3.save("nigeriamapcolored.html")
print("✅ Colored map saved as nigeria_map_colored.html")
