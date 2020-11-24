from math import e

def e_power(failure_rate, time):
    return (e ** (-(float(failure_rate) * int(time))))

def is_time_correct(time):
    if is_digit(time):
        if int(time) > 0:
            return True
        else:
            return False
    else:
        return False

def is_reliability_correct(reliability):
    if is_float(reliability):
        if float(reliability) > 0.0 and float(reliability) <= 1.0:
            return True
        else:
            return False
    else:
        return False
    return True

def is_faliure_rate_correct(faliure_rate):
    if is_float(faliure_rate):
        if float(faliure_rate) > 0:
            return True
        else:
            return False
    else:
        return False 

def is_float(check_input):
    if '.' in check_input:
        split_number = check_input.split('.')
        if len(split_number) == 2 and split_number[0].isdigit() and split_number[1].isdigit():
                return True
    return False

def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False