import datetime
from datetime import timedelta

def parseSheets():
    dataLines=open("amritsarDutyList.csv").read().split("\n")
    return dataLines 

def getGMTDiff():
    return 5*60+30

def convertRowToNames(row):
    rowVals=row.split(",")
    rowAr=[]
    for i in range(1,len(rowVals)):
        rowAr.append(rowVals[i])
    return rowAr

def getDateTimeObjects():
    startDate="20150501"    #yyyymmdd
    endDate="20150515"      #yyyymmdd
    timeVals=[["2:15","3:15"],["3:15","6:15"],["6:20","8:00"],["8:00","9:00"],["9:00","10:00"],["10:00","11:00"],["11:00","12:00"],["12:00","13:10"],["13:10","14:20"],["14:20","15:20"],["15:20","16:20"],["16:20","17:45"],["17:45","19:15"],["19:30","21:00"],["21:00","22:30"]]
        
    dateTimeVals=[]
        
    curDate=datetime.datetime.strptime(startDate,"%Y%m%d")
    while curDate<=datetime.datetime.strptime(endDate,"%Y%m%d"):
        for timeVal in timeVals:
            dateTimeObj_start=datetime.datetime.strptime(curDate.strftime("%Y%m%d")+timeVal[0],"%Y%m%d%H:%M" )
            dateTimeObj_end=datetime.datetime.strptime(curDate.strftime("%Y%m%d")+timeVal[1],"%Y%m%d%H:%M" )
            dateTimeVals.append([dateTimeObj_start,dateTimeObj_end])
        curDate+=timedelta(days=1)
        
    return dateTimeVals

def getNameStrings():    
    data=parseSheets()
    names=[]
    for i in range(len(data)):
        row=data[i]
        for name in row.split(","):
            names.append(name)
    return names

def getDateTimeToNameMapping():
    names=getNameStrings()
    timeData=getDateTimeObjects()
    dateToName={}
    for i in range(len(timeData)):
        dateToName[(timeData[i][0]-timedelta(minutes=getGMTDiff())).strftime("%Y%m%dT%H%M00Z")+"_"+(timeData[i][1]-timedelta(minutes=getGMTDiff())).strftime("%Y%m%dT%H%M00Z")]=names[i]
    return dateToName

def createEvent(summary,dtstart,dtend,description=''):
    event=''
    event+="BEGIN:VEVENT\n"
    event+="DTSTART:"+dtstart+"\n"
    event+="DTEND:"+dtend+"\n"
    event+="DTSTAMP:20150505T145509Z"+"\n"
    event+="UID:"+"\n"
    event+="CREATED:20140505T141602Z"+"\n"
    event+="DESCRIPTION:"+description+"\n"
    event+="LAST-MODIFIED:20140505T141602Z"+"\n"
    event+="LOCATION:"+"\n"
    event+="SEQUENCE:0"+"\n"
    event+="STATUS:CONFIRMED"+"\n"
    event+="SUMMARY:"+summary+"\n"
    event+="TRANSP:OPAQUE"+"\n"
    event+="END:VEVENT"+"\n"
    return event
    
def createCalendar(events,calName):
    cal=''
    cal+="BEGIN:VCALENDAR"+"\n"
    cal+="PRODID:-//Google Inc//Google Calendar 70.9054//EN"+"\n"
    cal+="VERSION:2.0"+"\n"
    cal+="CALSCALE:GREGORIAN"+"\n"
    cal+="METHOD:PUBLISH"+"\n"
    cal+="X-WR-CALNAME:"+calName+"\n"
    cal+="X-WR-TIMEZONE:Asia/Calcutta"+"\n"
    cal+="X-WR-CALDESC:"+"\n"
    for event in events:
        cal+=event+"\n"
    cal+="END:VCALENDAR"+"\n"
    return cal
