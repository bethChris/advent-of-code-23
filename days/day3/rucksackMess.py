# open file
# for each line in the file
    # half of the line goes into compartment1 (set)
    # the other half goes into compartment2 (set)
    # create an intersection of the two sets
    # add that intersection's value total into result


#open file
# for each line in the file
    # save every three lines
    # once you have three lines,
        # make each into a set
        # find the intersection of the 3 sets
        # for that intersection
            # add priority to total

import sys

data = sys.argv[1]

file = open(data)

total = 0
sacks = []


for rucksack in file:
    print(rucksack)
    print(set(rucksack))
    if len(sacks) == 3:
        commonItem = set(sacks[0] & sacks[1] & sacks[2])

        print(commonItem)    
        for item in commonItem:
            if item.isupper():
                total += ord(item) - 38
            else:
                total += ord(item) - 96

        sacks = []
    else:
        sacks.append(set(rucksack))


print(total)

file.close()




