import sqlite3
import pandas as pd

DATABASE = "energy.db"


def create_table():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        hour INTEGER,
        temperature REAL,
        humidity REAL,
        occupancy INTEGER,
        appliance_usage REAL,
        predicted_energy REAL,
        bill REAL,
        carbon REAL
    )
    """)

    conn.commit()
    conn.close()


def save_prediction(hour, temperature, humidity,
                    occupancy, appliance_usage,
                    energy, bill, carbon):

    create_table()

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions(
        hour,
        temperature,
        humidity,
        occupancy,
        appliance_usage,
        predicted_energy,
        bill,
        carbon
    )
    VALUES(?,?,?,?,?,?,?,?)
    """, (
        hour,
        temperature,
        humidity,
        occupancy,
        appliance_usage,
        energy,
        bill,
        carbon
    ))

    conn.commit()
    conn.close()


def get_predictions():

    conn = sqlite3.connect(DATABASE)

    try:
        df = pd.read_sql(
            "SELECT * FROM predictions",
            conn
        )
    except Exception:
        df = pd.DataFrame()

    conn.close()

    return df