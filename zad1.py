from math import e

"""
There are two components that are identical in a parallel configuration where the
second unit is in standby and will be activated only upon failure of the primary unit. The
switching to the backup unit is considered certain. The failure rate for each component is 0.002
failures/hour. What is the reliability for 200 hours?

Autor: Michał Degowski
Źródło problemu: systemreliabilityproblem1.pdf/Problem 7
"""


def problem():
    a_file = open("zad1.txt")
    lines = a_file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        print(line)
    print(" ")
    a_file.close()


def find_reliability():
    failure_rate = input("Podaj wskaźnik awaryjności (Failure rate): ")
    time = input("Podaj czas pracy w godzinach: ")

    reliability = (e ** (-(float(failure_rate) * int(time)))) * (1 + (float(failure_rate) * int(time)))
    return print("Reliability: ", round(reliability, 3))
