from fastapi import FastAPI

app = FastAPI()

def readFile(filename):
    f=open(filename)
    content=f.read()
    return [line for line in content.split('\n')]

def getSignalsList():
    res=readFile("signals.csv")
    return res

def getKeywordsList():
    res=readFile("keywords.csv")
    return res

@app.get("/")
async def root():


    return {"debug" : getKeywordsList()}

    """
    signals_list=["testa","testb"]
    specific_signal="testc"
    
    return {
        "List of signals": signals_list,
        "Specific signal given its node id ":specific_signal
    }
    """
