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
    processed_signals_list=[]

    for record in signal_list:
        new_record=processRecord(record, keywords_list)
        if new_record!=None:
            processed_signals_list.append(new_record)

    return processed_signals_list

def getGivenProcessedSignalList(node_id):
    keywords_list=getRawKeywordsList()
    signal_list=getRawSignalsList()


    for signal in signal_list:
        if (signal[0]==node_id):
            return processRecord(signal, keywords_list)
    return None

def processRecord(record, keywords_list):
    new_record=[]

    if len(record)==6:
        new_record=record[:5][::]
        this_record_keywords_id=record[-1]
        this_record_keywords=[]
        for car in this_record_keywords_id:
            if car.isdigit():
                this_record_keywords.append(findKeyWord(keywords_list, car))
        new_record.append(this_record_keywords)
    else:
        new_record=None
    return new_record

def findKeyWord(keywords_list, keyword_id):
    return keywords_list[int(keyword_id)-1][1]


@app.get("/")
async def root():

    #return {"1" : getProcessedSignalsList()}
    return {"2" : getGivenProcessedSignalList("ns=6;s=StarGateway:Shaco.Jinx.CU.AD_AspnW_zEyGUTZkYb")}

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
