from fastapi import FastAPI
import sqlite3

app = FastAPI()



def execureRequestOnDB(request):
    conn = sqlite3.connect('signals.db')

    cur = conn.cursor()

    cur.execute(request)
    rows = cur.fetchall()

    conn.close()

    return rows

@app.get("/")
async def root():
    return ["Welcome to the API. Use one of the two endpoints available to use the methods :","get_all_signals","get_by_id"]


@app.get("/get_all_signals")
async def root():
    return execureRequestOnDB("SELECT * FROM signals")

@app.get("/get_by_id/{item_id}")
async def root(item_id):
    #"ns=6;s=StarGateway:Shaco.Jinx.CU.AD_AspnW_zEyGUTZkYb"
    #return getGivenProcessedSignalList(item_id)
    return None

