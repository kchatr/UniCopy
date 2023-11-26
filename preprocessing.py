import os
import json
import pandas as pd

df = pd.read_csv("patents.csv")

df_extracted = df[["publication_number", "abstract_localized.text", "claims_localized.text", "description_localized.text"]]
df_extracted.dropna(inplace=True)
df_extracted.reset_index(drop=True, inplace=True)

patent_dict = df_extracted.to_dict(orient='records')

patent_json = json.dumps(patent_dict)

with open('patents.json', 'w') as file:
    json.dump(patent_json, file)
