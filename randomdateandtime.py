import datetime
import random
startdate=datetime.datetime(2025,1,1,0,0,0)
enddate=datetime.datetime(2025,12,31,23,59,59)
timedifference=enddate-startdate
randomsecond=random.randint(0,int(timedifference.total_seconds()))
randomdate=startdate+datetime.timedelta(seconds=randomsecond)
print("random date and time",randomdate)