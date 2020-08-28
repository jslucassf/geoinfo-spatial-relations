import json
import pandas as pd

drawings = pd.read_csv("data/drawings.csv", sep=',', quotechar='"')

for ind, row in drawings.iterrows():
    geom = json.loads(row['geometry'])
    print(geom)
