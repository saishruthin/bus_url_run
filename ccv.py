import pandas as pd
dataset_url = "https://raw.githubusercontent.com/saishruthin/bus_fleet_details/main/Road%20Transport.csv"
df = pd.read_csv(dataset_url)
unique = pd.unique(df["Districts"])
print(len(unique))

