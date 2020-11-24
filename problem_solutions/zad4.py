from math import e
from utils.math_utility import e_power, is_time_correct, is_faliure_rate_correct

"""
The primary unit has a failure rate of x failure/hour.
The unit in standby has a failure rate of y failures/hour.
If the reliability of the switch can be considered to be 1 (perfect).
What is the reliability for t hours?

Autor: Maciej Milewski
Źródło problemu: systemreliabilityproblem1.pdf/Problem 8
"""

def reliability(primary_failure_rate, standby_failure_rate, time):
    return( e_power(primary_failure_rate, time) + (float(primary_failure_rate)/(float(standby_failure_rate) - float(primary_failure_rate))) * (e_power(primary_failure_rate, time) - e_power(standby_failure_rate, time)))

def is_function_input_in_domain(primary_failure_rate, standby_failure_rate):
    if float(standby_failure_rate) - float(primary_failure_rate) == 0.0:
        return False
    else:
        return True

def input_validation_check(primary_failure_rate, standby_failure_rate, time):
    if is_function_input_in_domain(primary_failure_rate, standby_failure_rate) and \
       is_time_correct(time)                                                   and \
       is_faliure_rate_correct(primary_failure_rate)                           and \
       is_faliure_rate_correct(standby_failure_rate):
        return True
    else:
        return False

def find_system_reliability():
    primary_failure_rate = input("Podaj wskaźnik awaryjności (Failure rate) dla głównej jednostki: ")
    standby_failure_rate = input("Podaj wskaźnik awaryjności (Failure rate) dla rezerwowej jednostki: : ")
    time = input("Podaj czas pracy w godzinach: ")

    if input_validation_check(primary_failure_rate, standby_failure_rate, time):
        system_reliability = reliability(primary_failure_rate, standby_failure_rate, time)
        return print("System reliability: ", round(system_reliability, 3))
    else:
        return print("Niepoprawne dane wejściowe.")