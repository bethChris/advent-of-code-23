def parseInput(file):
    scratchcards_data = {}
    for line in file:
        line = line.strip()
        card_id = line.replace("Card", "").split(":")[0]

        number_stats = line.replace("Card", "").split(":")[1].split("|")
        
        scratchcards_data[card_id] = {"winning_nums" : number_stats[0].split(), "my_nums": number_stats[1].split()}
    
    
    return scratchcards_data


def calculate_points(card):
    points = 0
    match_count = 0

    for num in card["my_nums"]:
        if num in card["winning_nums"]:
            if points == 0:
                points = 1
            else:
                points = points * 2 
    
    return points

def main():
    f = open("puzzle_input.txt")
    scratchcards_data = parseInput(f)
    sum_of_points = 0

    for card in scratchcards_data.values():
        sum_of_points += calculate_points(card)


    print("Sum of all Card Points: ", sum_of_points)


main()