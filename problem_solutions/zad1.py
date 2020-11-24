from math import e

from utils.math_utility import e_power, is_time_correct, is_faliure_rate_correct

"""
There are two components that are identical in a parallel configuration where the
second unit is in standby and will be activated only upon failure of the primary unit. The
switching to the backup unit is considered certain. The failure rate for each component is 0.002
failures/hour. What is the reliability for 200 hours?

Autor: Michał Degowski
Źródło problemu: systemreliabilityproblem1.pdf/Problem 7
"""

def input_validation_check(failure_rate, time):
    if is_faliure_rate_correct(failure_rate) and \
       is_time_correct(time):
        return True
    else:
        return False

def find_reliability():
    failure_rate = input("Podaj wskaźnik awaryjności (Failure rate): ")
    time = input("Podaj czas pracy w godzinach: ")

    if input_validation_check(failure_rate, time):
        reliability = e_power(failure_rate, time) * (1 + (float(failure_rate) * int(time)))
        return print("Reliability: ", round(reliability, 3))
    else:
        return print("Niepoprawne dane wejściowe.")