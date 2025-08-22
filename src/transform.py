import pandas as pd
import json

def transform_users():
    with open("data/raw/users_raw.json", "r") as f:
        data = json.load(f)
    
    users = []

    for user in data:
        transformed= {
            "id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "phone": user["phone"],
            "website": user["website"],
            "address_city": user["address"]["city"],
            "address_street": user["address"]["street"],
            "company_name": user["company"]["name"]
        }
        users.append(transformed)
    df = pd.DataFrame(users)
    assert not df.empty, "Transformed DataFrame is empty"
    assert "email" in df.columns, "Email column is missing in the DataFrame"

    df.to_parquet("data/processed/users_processed.parquet", index=False)
    print("Data transformed and saved to data/processed/users_processed.parquet")
    return df

