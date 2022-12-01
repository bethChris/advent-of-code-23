

#from sys.argv grab the filename of the data.txt
# for each line in the file
    # grab content of line
        #if content is nothing
            # if counter variable holds more than biggest variable
                # replace value of biggest with counter
            
            # set counter to 0 
        #else
            # add content of line to counter variable
            # move on


import sys

data = sys.argv[1]
file = open(sys.argv[1])

total = 0
first = 0
second = 0
third = 0


for line in file:
    if line == '\n':
        if total >= first:
            third = second
            second = first
            first = total    
        elif total >= second:
            third = second
            second = total
        elif total >= third:
            third = total

        total = 0
    else:
        calories = line.split('\n')[0]
        total += int(calories)

print(first)
print(second)
print(third)

print(first + second + third)
        
file.close()