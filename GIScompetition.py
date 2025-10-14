import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Sample dataset (rainfall in mm, elevation in meters, flood yes=1 / no=0)
data = {
    "rainfall": [120, 300, 450, 80, 600, 200, 100, 400],
    "elevation": [50, 20, 15, 100, 10, 60, 90, 25],
    "flood": [1, 1, 1, 0, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

# Features (X) and Target (y)
X = df[["rainfall", "elevation"]]
y = df["flood"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Prediction

y_pred = model.predict(X_test)

print("Predictions:", y_pred)
print("\nClassification Report:\n", classification_report(y_test, y_pred))

import folium

# Example: plot locations with predicted risk
map_flood = folium.Map(location=[9.0820, 8.6753], zoom_start=6)  # Nigeria center

# Example predicted points (lat, lon, risk)
locations = [
    (9.0, 8.5, 1),  # Flood risk
    (7.5, 4.0, 0),  # No flood risk
]

for lat, lon, risk in locations:
    color = "red" if risk == 1 else "green"
    folium.CircleMarker(location=[lat, lon], radius=8, color=color,
                        popup="Flood Risk" if risk == 1 else "Safe").add_to(map_flood)

map_flood.save("flood_prediction_map.html")
print('a don ready to win')