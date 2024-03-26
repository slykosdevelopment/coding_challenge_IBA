import sqlite3
from processRecordsFromCSV import *


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

    if len(signal)==6:

        this_request_data=[]

        for i in range (6):
            #TODO change this
            if (i==1 or i==2 or i==4):
                if (signal[i]!=''):
                    this_request_data.append(int(signal[i]))
                else:
                    this_request_data.append(1)
            elif (i==5):
                this_request_data.append(str(signal[i]))

            else:
                if (signal[i]!=''):
                    this_request_data.append(signal[i])
                else:
                    this_request_data.append("0")

        cur.execute("INSERT INTO signals (node_id, sampling_interval_ms, deadband_value, deadband_type, active, keywords) VALUES (?, ?, ?, ?, ?, ?)",tuple(this_request_data))
    
conn.commit()


# Display database
cur.execute("SELECT * FROM signals")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
