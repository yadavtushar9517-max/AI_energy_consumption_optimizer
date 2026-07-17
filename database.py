import sqlite3

DATABASE = "energy.db"

def create_database():
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