import os
import json
import pandas as pd

def get_sources():
    df = pd.read_csv("patents.csv")

    df_extracted = df[["publication_number", "abstract_localized.text", "claims_localized.text", "description_localized.text"]]
    df_extracted.dropna(inplace=True)
    df_extracted.reset_index(drop=True, inplace=True)

    patent_list = df_extracted.to_dict(orient='records')

    return patent_list
