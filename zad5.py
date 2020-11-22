from math import e

"""
A satellite has two redundant control systems, each has a failure rate = x failures/hour.
If one of the systems fails, the failure rate for the remaining system increases to y failures/hour.
What is the reliability of the redundant control systems at t hours?

Autor: Maciej Milewski
Źródło problemu: systemreliabilityproblem1.pdf/Performance check 41
"""

def problem():
    a_file = open("zad5.txt")
    lines = a_file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        print(line)
    print(" ")
    a_file.close()

def e_power(failure_rate, time):
    return (e ** (-(float(failure_rate) * int(time))))

def reliability(first_fr, second_fr, time):
    return( e_power(first_fr, time) + (float(first_fr)/(float(first_fr) - float(second_fr))) * (e_power(second_fr, time) - e_power(first_fr, time)))

def find_satelite_reliability():
    system_with_2_units_fr = input("Podaj wskaźnik awaryjności (Failure rate) dla systemów kontroli lotu: ")
    system_with_1_unit_fr = input("Podaj wskaźnik awaryjności (Failure rate) dla systemu po awarii jednego z systemów: ")
    time = input("Podaj czas pracy w godzinach: ")

    fr_sum = 2.0*float(system_with_2_units_fr)
    satelite_reliability = reliability(fr_sum, system_with_1_unit_fr, time)

    return print("System reliability: ", round(satelite_reliability, 3))