import sqlite3

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
#test value. TODO : eead csv and add for each
cur.execute("INSERT INTO signals (node_id, sampling_interval_ms, deadband_value, deadband_type, active, keywords) VALUES (?, ?, ?, ?, ?, ?)", ("ns=6;s=StarGateway:Shaco.Jinx.CU.AL_fOndt_KEPXQlFdRS", 500,88, "ABSOLUTE",1,"[3;4]"))
cur.execute("INSERT INTO signals (node_id, sampling_interval_ms, deadband_value, deadband_type, active, keywords) VALUES (?, ?, ?, ?, ?, ?)", ("ns=6;s=StarGateway:Shaco.Jinx.CU.AL_fOndt_KEPXQlFdrS", 500,89, "ABSOLUTE",0,"[1;3;4]"))

conn.commit()



# Display database
cur.execute("SELECT * FROM signals")
rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()
