"""
A home computer has two 3.5 inch disk drives.
What is the probability of the computer operating successfully
(with at least one disk drive).

Autor: Maciej Milewski
Źródło problemu: systemreliabilityproblem1.pdf/Problem 4
"""

def problem():
    a_file = open("zad3.txt")
    lines = a_file.readlines()
    for line in lines:
        line = line.rstrip("\n")
        print(line)
    print(" ")
    a_file.close()

def find_pc_reliability():
    disk_drive_reliability = input("Podaj niezawodność dla napędu dysku twardego: ")
    hard_drive_reliability = input("Podaj niezawodność dla dysku twardego: ")
    cpu_reliability = input("Podaj niezawodność dla procesora: ")
    keyboard_reliability = input("Podaj niezawodność dla klawiatury: ")
    monitor_reliability = input("Podaj niezawodność dla monitora: ")

    disk_drives_combined_reliability = 1-(1-float(disk_drive_reliability))*(1-float(disk_drive_reliability))
    pc_reliability = float(disk_drives_combined_reliability)*float(hard_drive_reliability)*float(cpu_reliability)*float(keyboard_reliability)*float(monitor_reliability)
    return print("PC reliability: ", round(pc_reliability, 3))