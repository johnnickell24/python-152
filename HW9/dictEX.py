def doubleScores(tmpDict):
    for key in tmpDict:
        tmpScore=tmpDict[key] * 2
        tmpDict[key]=tmpScore

myDict={1:100,2:80,3:95}
doubleScores(myDict)
print(myDict)
