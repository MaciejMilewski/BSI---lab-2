from math import e

from utils.math_utility import e_power, is_time_correct, is_faliure_rate_correct, is_reliability_correct

"""
What is this system's reliability at 700 hours?
Component failure data is :
Failure rate of A = 0.0007 failures/hr
Reliability of B = 0.92
MTTF of C = 1400 hours
Reliability of D = 0.85

    --------- A ---------
    |                   |
    |                   |
    |                   |
    --------- B ---------
    |                   |
----|                   |----
    |                   |
    --------- C ---------
    |                   |
    |                   |
    |                   |
    --------- D ---------
    
Autor: Michał Degowski
Źródło problemu: systemreliabilityproblem1.pdf/Performance check 38
"""

def input_validation_check(time, failure_rate_A, reliability_B, mttf_C, reliability_D):
    if is_time_correct(time)                    and \
       is_faliure_rate_correct(failure_rate_A)  and \
       is_reliability_correct(reliability_B)    and \
       is_time_correct(mttf_C)                  and \
       is_reliability_correct(reliability_D):
        return True
    else:
        return False    

def find_system_reliability():
    time = input("Podaj czas pracy w godzinach: ")
    failure_rate_A = input("Podaj wskaźnik awaryjności (Failure rate): ")
    reliability_B = input("Podaj niezawodność (Reliability): ")
    mttf_C = input("Podaj średni czas do wystąpienia awarii (MTTF): ")
    reliability_D = input("Podaj niezawodność (Reliability): ")

    if input_validation_check(time, failure_rate_A, reliability_B, mttf_C, reliability_D):
        reliability_A = (e ** (-(float(failure_rate_A) * int(time))))
        reliability_C = (e ** (-(int(time) / int(mttf_C))))
        reliability_S = (1 - (1 - float(reliability_A)) * (1 - float(reliability_B)) * (1 - float(reliability_C)) * (1 - float(reliability_D)))
        return print("System reliability: ", round(reliability_S, 3))
    else:
        return print("Niepoprawne dane wejściowe.")    
