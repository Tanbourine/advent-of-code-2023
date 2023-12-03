from tabnanny import check
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

def check_above_below(symbol_row_num: int, filtered_schematics: Set[Schematic], schematic_list: List[Schematic], symbols: Dict[int, List[Schematic]], is_above: bool):
    symbol_row = symbols.get(symbol_row_num)
    if symbol_row:
        for schematic in schematic_list:
            for symbol in symbol_row:
                # print(f"Symbol: {symbol}")
                if (schematic.start_col - 1 <= symbol.start_col  and schematic.end_col + 1 >= symbol.end_col):
                    if is_above:
                        print(f"Added above: {schematic}")
                    else:
                        print(f"Added below: {schematic}")

                    filtered_schematics.add(schematic)

def filter_schematics(schematics: Dict[int, List[Schematic]], symbols: Dict[int, List[Schematic]], max_rows: int) -> List[Schematic]:
    filtered_schematics: Set[Schematic] = set()
    for row, schematic_list in schematics.items():
        print(row)
        # Check above
        if row - 1 > 0:
            check_above_below(row-1, filtered_schematics, schematic_list, symbols, True)
        
        # Check below
        if row + 1 < max_rows:
            check_above_below(row+1, filtered_schematics, schematic_list, symbols, False)

        # Check left
        symbol_row = symbols.get(row)
        if symbol_row:
            for schematic in schematic_list:
                for symbol in symbol_row:
                    if (schematic.start_col == symbol.end_col) or (schematic.end_col == symbol.start_col):
                        print(f"Added left/right: {schematic}")
                        filtered_schematics.add(schematic)
    return filtered_schematics



def main():
    # lines = import_txt("example.txt")
    lines = import_txt("input.txt")
    schematics = parse_schematics(lines, "\d+")
    symbols = parse_schematics(lines, "[^.\d]+", convert_to_int=False)
    filtered_schematics = filter_schematics(schematics, symbols, len(lines))
    # print(schematics)
    # print(symbols)
    # print(filtered_schematics)

    total = 0
    for schematic in filtered_schematics:
        total += schematic.value
    print(f"Total: {total}")







if __name__ == "__main__":
    main()