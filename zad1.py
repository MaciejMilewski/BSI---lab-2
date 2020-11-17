from math import e

"""
There are two components that are identical in a parallel configuration where the
second unit is in standby and will be activated only upon failure of the primary unit. The
switching to the backup unit is considered certain. The failure rate for each component is 0.002
failures/hour. What is the reliability for 200 hours?
"""


def find_reliability():
    failure_rate = input("Podaj wskaźnik awaryjności: ")
    time = input("Podaj czas: ")
    reliability = (e ** (-(float(failure_rate) * int(time)))) * (1 + (float(failure_rate) * int(time)))
    return print("Reliability: ", round(reliability, 3))
