import pandas as pd
import glob

# List your 8 CSV files here
files = {
    "Lokoja": "Lokoja.csv",
    "Lagos": "Lagos.csv",
    "Makurdi": "Makurdi.csv",
    "Abuja": "Abuja.csv",
    "PortHarcourt": "PortHarcourt.csv",
    "Jos": "Jos.csv",
    "Kano": "Kano.csv",
    "Onitsha": "Onitsha.csv"
}

all_dfs = []

for city, filename in files.items():
    df = pd.read_csv(filename, skiprows=13)  # NASA files have 13 header rows
    df["location"] = city
    # Keep only useful columns
    df = df[["YEAR", "MO", "PRECTOTCORR", "location"]]
    all_dfs.append(df)

# Combine all cities
df_all = pd.concat(all_dfs, ignore_index=True)

# Save combined dataset
df_all.to_csv("Nigeria_Rainfall_2015_2024.csv", index=False)

print("✅ Combined project.csv")
print(df_all.head(12))  # preview first rows
