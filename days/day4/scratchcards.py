def parseInput(file):
    scratchcards_data = {}
    for line in file:
        line = line.strip()
        card_id = line.replace("Card", "").split(":")[0].strip()

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


def calculate_matches(card):
    match_count = 0

    for num in card["my_nums"]:
        if num in card["winning_nums"]:
            match_count += 1
    
    return match_count


def sum_total_cards(scratchcards_data):
    total_cards = 0
    multipliers = {k: 1 for k in scratchcards_data.keys()}
    for idx, card in scratchcards_data.items():
        current_card_id = int(idx)
        matches = calculate_matches(card)

        for i in range(matches):
            card_to_update = str(i+1+current_card_id)
            multipliers[card_to_update] += multipliers[idx] #add 1 for every copy of this card that is produced


    return sum(multipliers.values())


def main():
    f = open("puzzle_input.txt")
    scratchcards_data = parseInput(f)
    sum_of_points = 0

    for card in scratchcards_data.values():
        sum_of_points += calculate_points(card)

    total_cards = sum_total_cards(scratchcards_data)

    print("Sum of all Card Points: ", sum_of_points)
    print("Sum of total Cards Won: ", total_cards)


main()