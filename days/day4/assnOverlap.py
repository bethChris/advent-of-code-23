# open file
# result counter var

# for each line in the file
    #take that line and split it by , then join by -
    #then split again by -
    #for each item in that list, turn to int
        #index 0-1 is elf1, 1-3 elf2
    #create sets of each elf
    #create a intersectioning set from both elves
    #if the intersection equals either of the elfs
        #increase fullOverlap
        #increase anyOverlap
    #else if they intersect at all
        #increase anyOverlap

#close file





import sys

data = sys.argv[1]

file = open(data)

fullOverlap = 0
anyOverlap = 0

for pair in file:
    #replaces , with - then takes out all -
    seperatedValues = '-'.join(pair.split(',')).split('-')

    intValues = [int(x) for x in seperatedValues]

    elf1 = {x for x in range(intValues[0], intValues[1]+1)}
    elf2 = {x for x in range(intValues[2], intValues[3]+1)}

    commonValues = set(elf1 & elf2)

    if commonValues == elf1 or commonValues == elf2:
        fullOverlap += 1
        anyOverlap += 1
    elif commonValues:
        anyOverlap +=1

print(fullOverlap)
print(anyOverlap)
