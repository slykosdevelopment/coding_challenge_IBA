from fastapi import FastAPI

app = FastAPI()

def readCSV(filename):
    f=open(filename)
    content=f.read()
    return [line.split(",") for line in content.split('\n')][1:-1]

def getSignalsList():
    res=readCSV("signals.csv")
    return res

def getKeywordsList():
    res=readCSV("keywords.csv")
    return res

@app.get("/")
async def root():


    return {"debug" : getKeywordsList()}
    #return {"debug" : getSignalsList()}

    """
    signals_list=["testa","testb"]
    specific_signal="testc"
    
    return {
        "List of signals": signals_list,
        "Specific signal given its node id ":specific_signal
    }
    """
