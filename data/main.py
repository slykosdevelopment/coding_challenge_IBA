from fastapi import FastAPI

app = FastAPI()




@app.get("/")
async def root():

    return ["Welcome to the API. Use one of the two endpoints available to use the methods :","get_all_signals","get_by_id"]


@app.get("/get_all_signals")
async def root():

    #return getProcessedSignalsList()
    return None

@app.get("/get_by_id/{item_id}")
async def root(item_id):
    #return {"2" : getGivenProcessedSignalList("ns=6;s=StarGateway:Shaco.Jinx.CU.AD_AspnW_zEyGUTZkYb")}
    #return getGivenProcessedSignalList(item_id)
    return None

