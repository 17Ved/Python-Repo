
# "Aware" object - With sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information, an aware object can locate itself relative to other aware objects.
# An aware object represents a specific moment in time that is not open to interpretation.
# "Naive" object - A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects.
# Whether a naive object represents Coordinated Universal Time (UTC), local time, or time in some other timezone is purely up to the program, just like it is up to the program whether a particular number represents metres, miles, or mass.
# Naive objects are easy to understand and to work with, at the cost of ignoring some aspects of reality.

import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

aware_local_time = pytz.utc.localize(local_time).astimezone()
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time{}, time zone{}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC time{}, time zone{}".format(aware_utc_time, aware_utc_time.tzinfo))


gap_time = datetime.datetime(2021, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())


s = 1445733000
t = s + (60 * 60)


gb = pytz.timezone('GB')
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))





















































































