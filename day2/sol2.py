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

    def get_fewest_cubes(self) -> Dict[str, int]:
        fewest: Dict[str, int] = {}
        for cube_set in self.cube_sets:
            for color, num in cube_set.items():
                if not fewest.get(color):
                    fewest[color] = num
                else:
                    if num > fewest[color]:
                        fewest[color] = num
        return fewest

    def get_power(self) -> int:
        fewest_cubes = self.get_fewest_cubes()
        power = 1
        for num in fewest_cubes.values():
            power *= num
        print(f"Game {self.id}: Power: {power} : {fewest_cubes}")
        return power

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



def main():
    input = import_txt("input.txt")
    games: List[Game] = parse_games(input)
    power = 0
    for game in games:
        power += game.get_power()
    print(f"Total sum: {power}")
    # pprint.pprint(filtered_games)


if __name__ == "__main__":
    main()