import folium

# Lagos, Nigeria example
n = folium.Map(
    location=[6.5244, 3.3792],
    zoom_start=7,
    tiles="OpenStreetMap",
    attr="© OpenStreetMap contributors"
)

n.save("map.html")
