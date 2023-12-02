import pprint
from typing import (
    List,
    Dict
)

BAG = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

class CubeSet():
    def __init__(self, red: int, green: int, blue: int):
        self.red = red
        self.green = green
        self.blue = blue

class Game():
    def __init__(self, id: int):
        self.id: int = id
        self.cube_sets: List[Dict[str, int]] = []

    def has_more_than_bag(self) -> bool:
        for cube_set in self.cube_sets:
            for color, num in cube_set.items():
                if num > BAG[color]:
                    print(f"Illegal Game {self.id}: Color: {color} Num: {num}, Bag: {BAG[color]}")
                    return True
        return False

    def __repr__(self):
        return f"Game {self.id}: {self.cube_sets}"


def import_txt(filename: str) -> List[str]:
    lines: List[str] = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip("\n"))
    return lines

def parse_games(lines: List[str]) -> List[Game]:
    games: List[Game] = []
    for line in lines:
        id = int(line.split(":")[0].split()[1])
        game = Game(id)
        cube_sets = line.split(":")[1].split(";")
        for cube_set in cube_sets:
            game.cube_sets.append(parse_set(cube_set))
        games.append(game)

    return games

def parse_set(cube_set: str) -> Dict[str, int]:
    draw = [x.strip() for x in cube_set.split(",")]
    cube_dict = {}
    for single_draw in draw:
        num, color = single_draw.split()
        cube_dict[color] = int(num)
    return cube_dict

def filter(games: List[Game]) -> List[Game]:
    filtered_games = []
    for game in games:
        if not game.has_more_than_bag():
            filtered_games.append(game)
    print(f"Leftover games {len(filtered_games)}")
    return filtered_games


def main():
    input = import_txt("input.txt")
    games: List[Game] = parse_games(input)
    filtered_games = filter(games)
    sum = 0
    for game in filtered_games:
        sum += game.id
    print(f"Total sum: {sum}")
    # pprint.pprint(filtered_games)


if __name__ == "__main__":
    main()