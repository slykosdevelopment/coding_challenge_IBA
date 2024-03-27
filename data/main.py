from fastapi import FastAPI
import sqlite3

app = FastAPI()

def executeRequestOnDB(request,values=None):
    conn = sqlite3.connect('signals.db')

    cur = conn.cursor()

    if values:
        cur.execute(request,values)

        conn.commit()

    else:
        cur.execute(request)

    rows = cur.fetchall()

    conn.close()

    return rows

@app.get("/")
async def root():
    return ["Welcome to the API. Use one of the two endpoints available to use the methods :","get_all_signals","get_by_id"]


@app.get("/get_all_signals")
async def root():
    return executeRequestOnDB("SELECT * FROM signals")

@app.get("/get_by_id/{item_id}")
async def root(item_id):
    return executeRequestOnDB('SELECT * FROM signals WHERE node_id="'+item_id+'"')

@app.post("/create_new")
async def root():
    return executeRequestOnDB("INSERT INTO signals (node_id, sampling_interval_ms, deadband_value, deadband_type, active, keywords) VALUES (?, ?, ?, ?, ?, ?)", ('test',2,3,'4',5,'6'))