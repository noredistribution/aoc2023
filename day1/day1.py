import re

def str_to_num(number: str) -> str:
    '''Converts a string to a number, if possible.'''
    if number == "one":
        return "1"
    elif number == "two":
        return "2"
    elif number == "three":
        return "3"
    elif number == "four":
        return "4"
    elif number == "five":
        return "5"
    elif number == "six":
        return "6"
    elif number == "seven":
        return "7"
    elif number == "eight":
        return "8"
    elif number == "nine":
        return "9"
    else:
        return number

def calibrate(data: list) -> int:
    '''Calibrates the data.'''
    calib_sum = 0
    for line in data:
        temp = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)

        calib_values = str_to_num(temp[0]) + str_to_num(temp[-1])
        #print(calib_values)
        calib_sum += int(calib_values)
    return calib_sum

with open("input.txt", "r") as f:
    data = f.readlines()

test_data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

print(f"Sum of example values: {calibrate(test_data.splitlines())}")
print(f"Sum of all calibration values: {calibrate(data)}")
