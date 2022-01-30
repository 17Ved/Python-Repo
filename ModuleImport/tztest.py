# 'pytz' module deals with time zone information by using pytz to create tz info object
# Pytz brings the Olson tz database into Python and thus supports almost all time zones.
# This module serves the date-time conversion functionalities and helps user serving international client’s base.
# It enables time-zone calculations in our Python applications and also allows us to create timezone aware datetime instances.

import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is  {}".format(datetime.datetime.utcnow()))


# for x in pytz.all_timezones:            # this will give you all possible country's strings that python accepts using pytz module
#     print(x)
#
# for x in sorted(pytz.country_names):            # this will give you all possible country's strings that python accepts using pytz module
#     print(x + ": " + pytz.country_names[x])
#
#
# for x in sorted(pytz.country_names):
#     print("{}: {}: {}:".format(x, pytz.country_names[x], pytz.country_timezones[x]))

# IMP NOTE --- The list of countries isn't actually good enough for getting the timezone and that's because many countries have got more than one timezone and so it is possible--
# to retrieve a list of all the time zones for a country code and display them after the country name...

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x]), end=": ")
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
        print("\t\t{}: {}".format(zone, local_time))
    else:
        print("\t\t No time zone defined")


# The safest way to deal with local time is to immediately convert them to UTC when you get them...









































































