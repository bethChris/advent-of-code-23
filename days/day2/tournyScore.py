#save info on points/plays in dictionary for readability

#open file

# total variable
# for each line in the file
    # split items first-opponent second-you
    # check who won
        # add to total necessary points
    # add to total the points you playedd


# if theres a tie, play score is same as opponent play score
# if you need to beat them, 
    # score is 2 if opponent was A, 3 if opponent was B, and 1 if opponent was C
#if you need to lose,
    # score is 3 if opponent was A, 1 if opponent was B and 2 if opponent was C



import sys


play = {
    'X' : 0,
    'Y' : 3,
    'Z' : 6 
}

win = {
    'A': 2,
    'B': 3,
    'C': 1
}

lose = {
    'A' : 3,
    'B' : 1,
    'C' : 2
}

tie = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}




data = sys.argv[1]
file = open(data)

score = 0

for line in file:
    if line.strip(): 
        opponent = line.split()[0]
        outcome = line.split()[1]

        if outcome == 'X':
            score += lose[opponent]
        elif outcome == 'Z':
            score += win[opponent]
        else:
            score += tie[opponent]
    
        score += play[outcome]


print(score)

file.close()

