from math import e

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
Źródło problemu: systemreliabilityproblem1.pdf/Problem 38
"""


def problem():
    a_file = open("zad2.txt")
    lines = a_file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        print(line)
    print(" ")
    a_file.close()

def find_system_reliability():
    time = input("Podaj czas: ")
    failure_rate_A = input("Podaj wskaźnik awaryjności (Failure rate): ")
    reliability_B = input("Podaj niezawodność (Reliability): ")
    MTTF_C = input("Podaj średni czas do wystąpienia awarii (MTTF): ")
    reliability_D = input("Podaj niezawodność (Reliability): ")
    reliability_A = (e ** (-(float(failure_rate_A) * int(time))))
    reliability_C = (e ** (-(int(time) / int(MTTF_C))))
    reliability_S = (1 - (1 - float(reliability_A)) * (1 - float(reliability_B)) * (1 - float(reliability_C))
                     * (1 - float(reliability_D)))
    return print("System reliability: ", round(reliability_S, 3))
