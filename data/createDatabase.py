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

data_types=[str, int,int, str, int, str]

for signal in signals:

    if len(signal)==6:

        this_request_data=[]

        for i in range (6):
            if (data_types[i]==int):
                if signal[i].isdigit():
                    this_request_data.append(int(signal[i]))
                else:
                    this_request_data.append(-1)

            else:
                this_request_data.append(str(signal[i]))


        cur.execute("INSERT INTO signals (node_id, sampling_interval_ms, deadband_value, deadband_type, active, keywords) VALUES (?, ?, ?, ?, ?, ?)",tuple(this_request_data))
    
conn.commit()


# Display database
cur.execute("SELECT * FROM signals")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
