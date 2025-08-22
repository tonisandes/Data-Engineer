from src import extract, transform, load

def main():
    print("🚀Starting ETL process...")
    extract.extract_users()
    transform.transform_users()
    load.load_users()
    print("🚀ETL process completed successfully.")

if __name__ == "__main__":
    main()