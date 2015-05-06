import datetime
def createEvent(summary,dtstart,dtend,description=''):
    event=''
    event+="BEGIN:VEVENT\n"
    event+="DTSTART:"+dtstart+"\n"
    event+="DTEND"+dtend+"\n"
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
