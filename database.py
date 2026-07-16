import sqlite3

conn = sqlite3.connect("energy.db")

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

print("Database Created Successfully")