from utils.math_utility import is_reliability_correct

"""
A home computer has two 3.5 inch disk drives, hard drive, cpu, keyboard and monitor.
What is the probability of the computer operating successfully
(with at least one disk drive)?

Autor: Maciej Milewski
Źródło problemu: systemreliabilityproblem1.pdf/Problem 4
"""

def input_validation_check(disk_drive_reliability, hard_drive_reliability, cpu_reliability, keyboard_reliability, monitor_reliability):
    if is_reliability_correct(disk_drive_reliability) and \
       is_reliability_correct(hard_drive_reliability) and \
       is_reliability_correct(cpu_reliability)        and \
       is_reliability_correct(keyboard_reliability)   and \
       is_reliability_correct(monitor_reliability):
        return True
    else:
        return False

def find_pc_reliability():
    disk_drive_reliability = input("Podaj niezawodność dla napędu dysku twardego: ")
    hard_drive_reliability = input("Podaj niezawodność dla dysku twardego: ")
    cpu_reliability = input("Podaj niezawodność dla procesora: ")
    keyboard_reliability = input("Podaj niezawodność dla klawiatury: ")
    monitor_reliability = input("Podaj niezawodność dla monitora: ")

    if input_validation_check(disk_drive_reliability, hard_drive_reliability, cpu_reliability, keyboard_reliability, monitor_reliability):
        disk_drives_combined_reliability = 1-(1-float(disk_drive_reliability))*(1-float(disk_drive_reliability))
        pc_reliability = float(disk_drives_combined_reliability)*float(hard_drive_reliability)*float(cpu_reliability)*float(keyboard_reliability)*float(monitor_reliability)
        return print("PC reliability: ", round(pc_reliability, 3))
    else:
        return print("Niepoprawne dane wejściowe.")