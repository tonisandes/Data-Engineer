from sqlalchemy import create_engine
import pandas as pd

def load_users():
    df = pd.read_parquet("data/processed/users_processed.parquet")

    engine = create_engine('sqlite:///data/users.db')

    df.to_sql('users', engine, if_exists='replace', index=False)
    print("Data loaded into SQLite database at data/users.db")
    
