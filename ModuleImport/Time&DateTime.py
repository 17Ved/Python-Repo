
# Time & Datetime Module in python--
# 2 main sources of problems with dates and times, they're -- localization & daylight saving
# The datetime module supplies classes for manipulating dates and times.
# While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.
# Date and time objects may be categorized as “aware” or “naive” depending on whether they include or not timezone information.
# Python provides 3 modules to help us deal with dates and times that's ----> 1.time, 2.datetime and 3.calendar modules.
# Documentation states that GM Time and local time convert the number of seconds into s struct_time & that's actually named tuple...
# "Aware" object - With sufficient knowledge of applicable algorithmic and political time adjustments, such as time zone and daylight saving time information, an aware object can locate itself relative to other aware objects.
# An aware object represents a specific moment in time that is not open to interpretation.
# "Naive" object - A naive object does not contain enough information to unambiguously locate itself relative to other date/time objects.
# Whether a naive object represents Coordinated Universal Time (UTC), local time, or time in some other timezone is purely up to the program, just like it is up to the program whether a particular number represents metres, miles, or mass.
# Naive objects are easy to understand and to work with, at the cost of ignoring some aspects of reality.


import time
# print(time.gmtime(0))
#
# print(time.localtime())         # GMT time always works in UTC so, to get the local time we can use the local time function
#
# print(time.time())

# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Day:", time_here[2], time_here.tm_mday)


from time import process_time as my_timer
import random

input("Press enter start")
wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at" + time.strftime("%X", time.localtime(start_time)))
print("Ended at" + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {} seconds".format(end_time - start_time))


# If you want to measure actual elapse time then use the perf_counter.
# & if you want to know how much time the CPU is spent on a particular task, then used process_time.
# To deal with real times rather than just measuring durations use time() function

















































































