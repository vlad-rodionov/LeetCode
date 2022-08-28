# 1st Solution

def check_record(s):

    absent = 0
    late = 0

    for char in s:

        if char == 'A':
            absent += 1

            if absent == 2:
                return False

        if char == 'L':
            late += 1
            if late > 2:
                return False
        else:
            late = 0

    return True


# 2nd Solution

def check_record_2(s):

    return s.count(A) <= 1 and s.count('LLL') == 0