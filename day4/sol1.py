from ast import parse
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

def parse_numbers(number_list: str) -> List[int]:
    numbers = re.findall("\d+", number_list)
    return [int(num) for num in numbers]

def count_points(winning: List[int], numbers: List[int]) -> int:
    matches = 0
    for number in numbers:
        if number in winning:
            matches += 1
    if matches == 0:
        return 0
    return 2**(matches-1)


def main():
    # filename = "example.txt"
    filename = "input.txt"
    lines = import_txt(filename)

    total_points = 0
    for line in lines:
        all_numbers = line.split(":")[1]
        winning = parse_numbers(all_numbers.split("|")[0])
        numbers = parse_numbers(all_numbers.split("|")[1])
        points = count_points(winning, numbers)
        total_points += points

        
        print(points, winning, numbers)
    print(f"Total Points: {total_points}")



if __name__ == "__main__":
    main()