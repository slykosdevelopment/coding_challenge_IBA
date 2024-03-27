"""
Difference between processed and raw : processed have the index of keywords replaced by their names to make it easily readable

"""

def readCSV(filename):
    f=open(filename)
    content=f.read()
    f.close()
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

    if len(record)==6:
        data_types=[str, int,int, str, int, str]
        new_record=[]

        for i in range (6):

            if (data_types[i]==int):
                if record[i].isdigit():
                    new_record.append(int(record[i]))
                else:
                    new_record.append(-1)

            elif i==5:
                keywords_lst=[]
                
                for car in record[5].strip('[]').split(";"):
                    if len(car)>0:
                        keywords_lst.append(findKeyWord(keywords_list, car))

                new_record.append(", ".join(keywords_lst))

            else:
                new_record.append(str(record[i]))

        return new_record
    else:
        return None

def findKeyWord(keywords_list, keyword_id):
    return keywords_list[int(keyword_id)-1][1]


