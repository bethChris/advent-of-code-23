def parseInput(file):
    schematic = []
    for line in file:
        row = ['.']
        line = line.strip()
        for i in range(len(line)):
            row += [line[i]]

        row += ['.']
        schematic.append(row)
    
    schematic.insert(0, ['.' for i in range(len(schematic[0]))])
    schematic.append(['.' for i in range(len(schematic[0]))])
       
    for line in schematic:
        i = 0
        while i < len(line):
            if line[i].isnumeric():
                j = i
                num = ''
                while line[j].isnumeric():
                    num += line[j]
                    j += 1

                for char in range(len(num)):
                    line[i+char] = num
                i += len(num) - 1
            i += 1

    return schematic


def get_adj_square(row, col, schematic):
    adjacent_square = [
        #top
        schematic[row-1][col-1],
        schematic[row-1][col],
        schematic[row-1][col+1],
        '.',
        #middle
        schematic[row][col-1],
        '.',
        schematic[row][col+1],
        '.',
        #bottom
        schematic[row+1][col-1],
        schematic[row+1][col],
        schematic[row+1][col+1]
    ]
    
    return adjacent_square


def check_adjacent(loc, schematic):
    row = loc[0]
    col = loc[1]
    
    adj_square = get_adj_square(row, col, schematic)
    found_symbol = False

    for item in adj_square:
        if not item.isnumeric() and item != '.':
            found_symbol = True

    if found_symbol:
        return True
    else:
        return False


def sum_part_nums(schematic):
    total_part_nums = 0
    for i in range(len(schematic)): #each row
        j = 0
        while j < len(schematic[0]): #each column value in row
            if schematic[i][j].isnumeric() and check_adjacent([i, j], schematic):       
                total_part_nums += int(schematic[i][j])
                while schematic[i][j].isnumeric():
                    j += 1
            else:
                j += 1

    return total_part_nums


def get_gear_ratio(row, col, schematic):
    if schematic[row][col] != '*':
        return 0

    adj_square = get_adj_square(row, col, schematic)
    numbers_in_square = []
    top_row = []
    i = 0

    while i < len(adj_square):
        if adj_square[i].isnumeric():
            numbers_in_square.append(int(adj_square[i]))
            while i < len(adj_square) and adj_square[i].isnumeric():
                i += 1
        else:
            i += 1
    
    if len(numbers_in_square) == 2:
        ratio = 1
        for item in numbers_in_square:
            ratio *= item
        
        print(ratio)
        return ratio

    return 0


def sum_gear_ratios(schematic):
    total_gear_ratios = 0

    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            total_gear_ratios += get_gear_ratio(i, j, schematic)
      
    return total_gear_ratios


def main():
    f = open("puzzle_input.txt", "r")
    schematic = parseInput(f)
    
    total_part_nums = sum_part_nums(schematic)
    print("Total of all Part Numbers: ", total_part_nums)

    total_gear_ratios = sum_gear_ratios(schematic)
    print("Total of all Gear Ratios: ", total_gear_ratios)


main()