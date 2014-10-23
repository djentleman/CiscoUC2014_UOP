import urllib2 as urllib
import time
import datetime

def getSchedule():
    url = "http://cisco.richardsolomou.com/api/v1/journeys/stations"
    jsonArr = strToJSON(requestUrl(url))
    schedule = []
    for elem in jsonArr:
        # we need arrival time, station id & journey id
        schedule.append((elem["ArrivalTime"], elem["Journey_ID"], elem["Station_ID"]))
    return schedule

def requestUrl(url):
    httpData = urllib.urlopen(url).read()
    return httpData

def strToJSON(string):
    return eval(string)

def strToTime(string):
    # (year, month, day, hr, min, sec)
    #2014-10-24 03:23:18
    return tuple(string.replace(":", "-").replace(" ", "-").split("-"))

def timeTupleToTime(tt):
    return (str(tt.tm_year), str(tt.tm_mon),
            str(tt.tm_mday), str(tt.tm_hour),
            str(tt.tm_min), str(tt.tm_sec))

def tupleToInt(tup):
    s = ""
    for elem in tup:
        if len(elem) > 1:
            s+=elem
        else:
            s+="0"+elem
    return int(s)
        
def compareDates(d1, d2):
    if (tupleToInt(d1) > tupleToInt(d2)):
        return True
    return False

def removePastEvents(schedule):
    newSchedule = []
    now = timeTupleToTime(datetime.datetime.now().timetuple())
    print now
    for event in schedule:
        print event[0]
        if compareDates(strToTime(event[0]), now):
            # event is in the future
            newSchedule.append(event)
    return newSchedule
        
    
 

def main():
    # this url needs to be contructed
    # a journey id and a station id need to be derived
    #url = "http://cisco.richardsolomou.com/api/v1/journeys/4/stations/3/carriageseatcount"
    #jsonArr = strToJSON(requestUrl(url))#


    # initalize schedule
    schedule = removePastEvents(getSchedule())

    # the next event is schedule[0]

    # remove all past events

    nextEventTime = strToTime(schedule[0][0])
    while 1:
        now = datetime.datetime.now().timetuple()
        print(timeTupleToTime(now))
        print(nextEventTime)
        if compareDates(timeTupleToTime(now), nextEventTime):
            print "get the data"
        else:
            print "not time yet"
        time.sleep(10)
        

    
    

if __name__ == "__main__":
    main()
