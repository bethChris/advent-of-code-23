def calibration_value(line):
    two_digit = 0
    numbers = [num for num in line if num.isnumeric()]
    if len(numbers) > 0:
        two_digit = "".join([numbers[0], numbers[-1:][0]])
     
    return int(two_digit)

def modified_calibration_value(line):
    number_map = {
        "zero":0,
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9    
    }

    two_digit = 0
    print(line.strip(), end=" : ")
    for number in number_map.keys():
        line = line.replace(number, f'{number}{number_map[number]}{number}')

    print(line.strip(), end=" : ")
    numbers = [num for num in line if num.isnumeric()]
    

    if len(numbers) > 0:
        two_digit = "".join([numbers[0], numbers[-1:][0]])
    
    print(two_digit)
    return int(two_digit)

    
def main():
    f = open("puzzle_input.txt", "r")
    total_cal_val = 0
    total_cal_val_mod = 0

    for line in f:
        total_cal_val += calibration_value(line)
        total_cal_val_mod += modified_calibration_value(line)
    
    print("Total Calibration Value: ", total_cal_val)
    print("Total Calibration Value Modified: ", total_cal_val_mod)


main()