from math import e

"""
The primary unit has a failure rate of x failure/hour.
The unit in standby has a failure rate of y failures/hour.
If the reliability of the switch can be considered to be 1 (perfect).
What is the reliability for t hours?

Autor: Maciej Milewski
Źródło problemu: systemreliabilityproblem1.pdf/Problem 8
"""

def problem():
    a_file = open("zad4.txt")
    lines = a_file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        print(line)
    print(" ")
    a_file.close()

def e_power(failure_rate, time):
    return (e ** (-(float(failure_rate) * int(time))))

def reliability(primary_failure_rate, standby_failure_rate, time):
    return( e_power(primary_failure_rate, time) + (float(primary_failure_rate)/(float(standby_failure_rate) - float(primary_failure_rate))) * (e_power(primary_failure_rate, time) - e_power(standby_failure_rate, time)))

def find_system_reliability():
    primary_failure_rate = input("Podaj wskaźnik awaryjności (Failure rate) dla głównej jednostki: ")
    standby_failure_rate = input("Podaj wskaźnik awaryjności (Failure rate) dla rezerwowej jednostki: : ")
    time = input("Podaj czas pracy w godzinach: ")

    system_reliability = reliability(primary_failure_rate, standby_failure_rate, time)

    return print("System reliability: ", round(system_reliability, 3))