import re
from pprint import pprint as pp

criteria = {"red": 12, "green": 13, "blue":14}

test_data ="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def parse_data(data: str) -> list:
    '''Parses the data.'''
    games = []
    for line in data.splitlines():
        game_line = line.split(": ")
        #id = game_line[0].split(" ")[1]
        games.append((game_line[1]))
    return games

def parse_games(games: list) -> list:
    '''Parses the games.'''
    parsed_games = []
    for game in games:
        parsed_games.append(game.split("; "))
    return parsed_games

def parse_rounds(games: list) -> list:
    '''Parses the rounds.'''
    game_db = {}
    game_db_possible = []
    game_db_impossible = []
    for ctr, game in enumerate(games):
        red = []
        green = []
        blue = []
        for round in game:
            split_round = round.split(", ")

            for sp_round in split_round:
                temp = sp_round.split(" ")
                if temp[1] == "red":
                    red.append(int(temp[0]))
                elif temp[1] == "green":
                    green.append(int(temp[0]))
                elif temp[1] == "blue":
                    blue.append(int(temp[0]))
                if criteria[temp[1]] < int(temp[0]):
                    game_db.update({ctr+1:{"game_id": ctr+1, "possible": False}})
                    game_db_impossible.append(ctr+1)
                    #break
                else:
                    game_db_possible.append(ctr+1)
                    game_db.update({ctr+1:{"game_id": ctr+1, "possible": True}})
                game_db[ctr+1]["red"] = red
                game_db[ctr+1]["green"] = green
                game_db[ctr+1]["blue"] = blue
        game_db[ctr+1]["max"] = {"red": max(red), "green": max(green), "blue": max(blue)}
        game_db[ctr+1]["power"] = max(red) * max(green) * max(blue)
    sum_max = 0
    for game in game_db:
        sum_max += game_db[game]["power"]

    return game_db, set(game_db_possible) - set(game_db_impossible), sum_max

def parse_round(round: str) -> list:
    '''Parses a single round.'''
    return round.split(", ")

with open("input.txt", "r") as f:
    data = f.read()

parsed_data = parse_data(test_data)
games = parse_games(parsed_data)
game_db, possible_games, sum_max = parse_rounds(games)
pp(game_db)
print(f"Sum of possible game IDs: {sum(possible_games)}")
print(f"Sum of the power of the sets for test_data: {sum_max}")

parsed_data = parse_data(data)
games = parse_games(parsed_data)
game_db, possible_games, sum_max = parse_rounds(games)
#print(game_db)
print(f"Sum of possible game IDs: {sum(possible_games)}")
print(f"Sum of the power of the sets for the day input: {sum_max}")
