import datetime

def parseSheets():
    dataLines=open("amritsarDutyList.txt").read().split("\n")
    return dataLines 

def createEvent(summary,dtstart,dtend,description=''):
    event=''
    return event

def createCalendar(events,calName):
    cal=''
    return cal

def convertToGMT(datetimestring):
    gmtTime=''
    return gmtTime

def isDayLightActive():
    return True
    #return False

def convertRowToNames(row):
    rowVals=row.split(" ")
    rowAr=[]
    for i in range(1,len(rowVals)-3,2):
        name=rowVals[i]+" "+rowVals[i+1]+" "+rowVals[i+2]
        rowAr.append(name)
    return rowAr
    

def getDateToRowMapping():
    dateToRow={}
    data=parseSheets()
    for i in range((len(data)/2)):
        dt=datetime.datetime.strptime((data[i].split(" "))[0],"%d-%m-%y")
                
    return dateAr
