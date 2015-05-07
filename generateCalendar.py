from commonFunctions import *

allEvents=[]

mappings = getDateTimeToNameMapping()

for mappingKey in mappings:
    start,end=mappingKey.split("_")
    summary=mappings[mappingKey]
    allEvents.append(createEvent(summary, start, end))

print createCalendar(allEvents, "Amritsar Duties")
