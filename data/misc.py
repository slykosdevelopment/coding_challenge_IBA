"""
Difference between processed and not processed: processed have the index of keywords replaced by their names to make it easily readable
"""

def readCSV(filename):
    f=open(filename)
    content=f.read()
    f.close()
    return [line.split(",") for line in content.split('\n')][1:-1]

def getKeywordsAndSignals():
    return readCSV("keywords.csv"), readCSV("signals.csv")

def findKeyWord(keywords_list, keyword_id):
    return keywords_list[int(keyword_id)-1][1]

def getProcessedSignalsList():
    keywords_list, signal_list=getKeywordsAndSignals()

    processed_signals_list=[]

    for record in signal_list:
        new_record=processRecord(record, keywords_list)
        if new_record!=None:
            processed_signals_list.append(new_record)

    return processed_signals_list


def processRecord(record, keywords_list):

    if len(record)==6:
        new_record=[None for i in range (6)]

        for i in range (6):

            if i in [1,2,4]: #if data is int

                if record[i].isdigit():
                    new_record[i]=int(record[i])
                else:
                    new_record[i]=-1

            elif i in [0,3]: #if data is str
                new_record[i]=str(record[i])

            else: #if on the keywords list
                keywords_lst=[]
                
                for car in record[5].strip('[]').split(";"):
                    if len(car)>0:
                        keywords_lst.append(findKeyWord(keywords_list, car))

                new_record[5]=", ".join(keywords_lst)

        return new_record

    else:
        return None

