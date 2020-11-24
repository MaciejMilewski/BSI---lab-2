from math import e

from utils.math_utility import e_power, is_time_correct, is_faliure_rate_correct

"""
A satellite has two redundant control systems, each has a failure rate = x failures/hour.
If one of the systems fails, the failure rate for the remaining system increases to y failures/hour.
What is the reliability of the redundant control systems at t hours?

system_with_2_units_fr = 0.000001
system_with_1_unit_fr = 0.00002
time = 175000

Solution = 0.78

Autor: Maciej Milewski
Źródło problemu: systemreliabilityproblem1.pdf/Performance check 41
"""

def reliability(first_fr, second_fr, time):
    return( e_power(first_fr, time) + (float(first_fr)/(float(first_fr) - float(second_fr))) * (e_power(second_fr, time) - e_power(first_fr, time)))

def is_function_input_in_domain(system_with_2_units_fr, system_with_1_unit_fr):
    if 2.0*float(system_with_2_units_fr) - float(system_with_1_unit_fr) == 0.0:
        return False
    else:
        return True


def input_validation_check(system_with_2_units_fr, system_with_1_unit_fr, time):
    if is_time_correct(time)                                                      and \
       is_faliure_rate_correct(system_with_2_units_fr)                            and \
       is_faliure_rate_correct(system_with_1_unit_fr)                             and \
       is_function_input_in_domain(system_with_2_units_fr, system_with_1_unit_fr):
        return True
    else:
        return False


def find_satelite_reliability():
    system_with_2_units_fr = input("Podaj wskaźnik awaryjności (Failure rate) dla systemów kontroli lotu: ")
    system_with_1_unit_fr = input("Podaj wskaźnik awaryjności (Failure rate) dla systemu po awarii jednego z systemów: ")
    time = input("Podaj czas pracy w godzinach: ")

    if input_validation_check(system_with_2_units_fr, system_with_1_unit_fr, time):
        fr_sum = 2.0*float(system_with_2_units_fr)
        satelite_reliability = reliability(fr_sum, system_with_1_unit_fr, time)
        return print("System reliability: ", round(satelite_reliability, 3))
    else:
        return print("Niepoprawne dane wejściowe.")    