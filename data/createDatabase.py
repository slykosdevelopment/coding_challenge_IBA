import sqlite3
from misc import *


conn = sqlite3.connect('signals.db')

cur = conn.cursor()

# Create datatable
cur.execute('''CREATE TABLE IF NOT EXISTS signals (
                node_id TEXT PRIMARY KEY,
                sampling_interval_ms INT,
                deadband_value INT,
                deadband_type TEXT,
                active INT,
                keywords TEXT)''')


# fill data table
signals=getProcessedSignalsList()


for signal in signals:
    print(signal)
    if len(signal)==6:
        cur.execute("INSERT INTO signals (node_id, sampling_interval_ms, deadband_value, deadband_type, active, keywords) VALUES (?, ?, ?, ?, ?, ?)",tuple(signal))
    
conn.commit()


# Display database
cur.execute("SELECT * FROM signals")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
