def parseInput(file):
    game_stats = {}

    for line in file:
        game = line.replace(":", "").replace(",", "").replace(";", "").replace("Game", "").split()
        game_id = game[0]

        max_blue = max([int(game[i-1]) for i in range(len(game)) if game[i] == 'blue'] + [0])
        max_red = max([int(game[i-1]) for i in range(len(game)) if game[i] == 'red'] + [0])
        max_green = max([int(game[i-1]) for i in range(len(game)) if game[i] == 'green'] + [0])

        game_stats[game_id] = {
            "blue": max_blue,
            "red": max_red,
            "green": max_green
        }

    return game_stats


def is_valid_game(blue, red, green, game):
    if game["blue"] > blue:
        return False
    elif game["red"] > red:
        return False
    elif game["green"] > green:
        return False
    
    return True


def main():
    # from puzzle
    blue = 14 
    red = 12 
    green = 13 

    f = open("puzzle_input.txt", "r")
    game_stats = parseInput(f)

    possible_game_id_total = 0
    for game, stats in game_stats.items():
        if is_valid_game(blue, red, green, stats):
            possible_game_id_total += int(game)

    print("Possible Games ID Sum: ", possible_game_id_total)

main()