import sqlite3
import pandas as pd

DATABASE = "energy.db"

def save_prediction(hour, temperature, humidity,
                    occupancy, appliance_usage,
                    energy, bill, carbon):

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

    df = pd.read_sql(
        "SELECT * FROM predictions",
        conn
    )

    conn.close()

    return df