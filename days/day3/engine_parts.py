def parseInput(file):
    schematic = []
    for line in file:
        #TODO: add '.' to the start and end of each row
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
        #middle
        schematic[row][col-1],
        schematic[row][col+1],
        #bottom
        schematic[row+1][col-1],
        schematic[row+1][col],
        schematic[row+1][col+1]
    ]

    

    return adjacent_square

def check_adjacent(loc, schematic):
    row = loc[0]
    col = loc[1]
    possible_part_num = int(schematic[row][col])
    
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


def main():
    f = open("day3/puzzle_input.txt", "r")
    schematic = parseInput(f)
    
    total_part_nums = sum_part_nums(schematic)
    print("Total of all Part Numbers: ", total_part_nums)

main()