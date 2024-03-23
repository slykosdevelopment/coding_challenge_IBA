from fastapi import FastAPI

app = FastAPI()

def readCSV(filename):
    f=open(filename)
    content=f.read()
    return [line.split(",") for line in content.split('\n')][1:-1]

def getRawSignalsList():
    return readCSV("signals.csv")

def getRawKeywordsList():
    return readCSV("keywords.csv")

def getProcessedSignalsList():
    keywords_list=getRawKeywordsList()
    signal_list=getRawSignalsList()

    for record in signal_list:
        this_record_keywords_id=record.pop()
        this_record_keywords=[]
        for car in this_record_keywords_id:
            if car.isdigit():
                this_record_keywords.append(findKeyWord(keywords_list, car))
        record.append(this_record_keywords)
    return signal_list

def findKeyWord(keywords_list, keyword_id):
    #return keywords_list[int(keyword_id)-1]
    return int(keyword_id)


@app.get("/")
async def root():

    return {"debug" : getProcessedSignalsList()}
    #return {"debug" : getRawKeywordsList()}
    #return {"debug" : getRawSignalsList()}

    """
    signals_list=["testa","testb"]
    specific_signal="testc"
    
    return {
        "List of signals": signals_list,
        "Specific signal given its node id ":specific_signal
    }
    """
