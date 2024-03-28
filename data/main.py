from fastapi import Request,FastAPI
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
    return ["Welcome to the API. Use one of the two available GET operations: get_all_signals and get_by_id. Or, use the POST method on create_new"]


@app.get("/get_all_signals")
async def root():
    return executeRequestOnDB("SELECT * FROM signals")

@app.get("/get_by_id/{item_id}")
async def root(item_id):
    return executeRequestOnDB('SELECT * FROM signals WHERE node_id="'+item_id+'"')

@app.post("/create_new")
async def root(request: Request): #create new signal, will first retrieve caracteristics of the signal then insert into db
    req_json=await request.json()

    args=(req_json['node_id'], req_json['sampling_interval_ms'], req_json['deadband_value'], req_json['deadband_type'], req_json['active'], req_json['keywords'])
    
    return executeRequestOnDB("INSERT INTO signals (node_id, sampling_interval_ms, deadband_value, deadband_type, active, keywords) VALUES (?, ?, ?, ?, ?, ?)", args)

