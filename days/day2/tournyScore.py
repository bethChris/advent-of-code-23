#save info on points/plays in dictionary for readability

#open file

# total variable
# for each line in the file
    # split items first-opponent second-you
    # check who won
        # add to total necessary points
    # add to total the points you playedd



import sys


points = {
    'X' : 1,
    'Y' : 2,
    'Z' : 3 
}

beats = {
    'X' : 'C',
    'Y' : 'A',
    'Z' : 'B',

    'A' : 'Z',
    'B' : 'X',
    'C' : 'Y'
}


data = sys.argv[1]
file = open(data)

score = 0

for line in file:
    if line.strip(): 
        opponent = line.split()[0]
        me = line.split()[1]

        if beats[me] is opponent:
            score += 6
        elif (beats[opponent] is me):
            score += 0
        else:
            score += 3

        score += points[me]


print(score)

file.close()

