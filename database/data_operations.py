import pandas as pd

from database_connection import get_connection

CSV_FILE = "../dataset/sample_sales_data.csv"


def load_csv_to_db():

    conn = get_connection()

    df = pd.read_csv(CSV_FILE)

    df.to_sql(
        "sales_data",
        conn,
        if_exists="replace",
        index=False
    )

    conn.commit()

    conn.close()

    print("CSV Loaded Successfully")


def fetch_sales_data():

    conn = get_connection()

    query = "SELECT * FROM sales_data"

    df = pd.read_sql(query, conn)

    conn.close()

    return df


if __name__ == "__main__":
    load_csv_to_db()