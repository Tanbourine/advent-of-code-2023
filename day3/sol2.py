from typing import (
    List,
    Dict,
    Set
)
import re

def import_txt(filename: str) -> List[str]:
    lines: List[str] = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip("\n"))
    return lines


class Schematic():
    def __init__(self, value: int, row: int, start_col: int, end_col: int):
        self.value = value
        self.row = row
        self.start_col = start_col
        self.end_col = end_col

    def __repr__(self):
        return f"Value: {self.value}, Row: {self.row}, Pos: {self.start_col}, {self.end_col}"


def parse_schematics(lines: str, regex: str, convert_to_int: bool = True) -> Dict[int, List[Schematic]]:
    schematics: Dict[int, List[Schematic]] = {}
    for row, line in enumerate(lines): 
        pattern = re.compile(regex)
        match = pattern.search(line)
        while match is not None:
            if convert_to_int:
                val = int(match.group(0))
            else:
                val = match.group(0)
            if not schematics.get(row):
                schematics[row] = []
            schematics[row].append((Schematic(val, row, match.start(), match.end())))
            match = pattern.search(line, pos=match.end())
    return schematics

def find_numbers_around_gears(symbols: List[Schematic], schematics: Dict[int, List[Schematic]]) -> int:
    total_gear_ratio = 0
    for symbol in symbols:
        print(symbol)
        # Find all schematics adjacent
        adjacent_schematics: Set[Schematic] = set()

        # Look Above
        above_schematics = schematics.get(symbol.row - 1)
        if above_schematics:
            for schematic in above_schematics:
                if (is_adjacent(schematic, symbol)):
                    print(f"Added above {schematic}")
                    adjacent_schematics.add(schematic)

        # Look Below
        below_schematics = schematics.get(symbol.row + 1)
        if below_schematics:
            for schematic in below_schematics:
                if (is_adjacent(schematic, symbol)):
                    print(f"Added below {schematic}")
                    adjacent_schematics.add(schematic)

        # Look in same row
        same_row_schematics = schematics.get(symbol.row)
        if same_row_schematics:
            for schematic in same_row_schematics:
                if (schematic.start_col == symbol.end_col) or (schematic.end_col == symbol.start_col):
                    print(f"Added left/right: {schematic}")
                    adjacent_schematics.add(schematic)

        if len(adjacent_schematics) == 2:
            gear_ratio = 1
            print(f"Adjacent Schematics: {adjacent_schematics}")
            for schematic in adjacent_schematics:
                gear_ratio *= schematic.value
            print(f"Gear Ratio: {gear_ratio}")
            total_gear_ratio += gear_ratio
    return total_gear_ratio


def is_adjacent(schematic: Schematic, symbol: Schematic) -> bool:
    return schematic.start_col - 1 <= symbol.start_col  and schematic.end_col + 1 >= symbol.end_col





def main():
    # lines = import_txt("example.txt")
    lines = import_txt("input.txt")
    schematics = parse_schematics(lines, "\d+")
    symbols = parse_schematics(lines, "[*]", convert_to_int=False)

    # print(schematics)
    # print(symbols)

    total_gear_ratio = 0
    for symbol in symbols.values():
        print(f"Symbol: {symbol}")
        total_gear_ratio += find_numbers_around_gears(symbol, schematics)
        print("==========")
        # break
    print(f"Total Gear Ratio: {total_gear_ratio}")








if __name__ == "__main__":
    main()