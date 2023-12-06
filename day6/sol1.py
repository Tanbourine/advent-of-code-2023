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

def race_boat(time: int, distance: int) -> List[int]:
    winning_holds = []
    for hold in range(time):
        travel_time = time - hold
        if (hold * travel_time > distance):
            print(f"Winning hold: {hold}")
            winning_holds.append(hold)

        # print(hold, hold * travel_time, distance)
    return winning_holds
        

def main():
    filename = "example.txt"
    filename = "input.txt"
    lines = import_txt(filename)
    times = [int(num) for num in lines[0].split(":")[1].split()]
    distances = [int(num) for num in lines[1].split(":")[1].split()]

    races = {}
    for i in range(len(times)):
        races[i] = (times[i], distances[i])

    ways_to_win = []
    for race in races.values():
        winning_holds = race_boat(race[0], race[1])
        ways_to_win.append(len(winning_holds))

    total = 1
    for way in ways_to_win:
        total *= way
    print(total)




    

if __name__ == "__main__":
    main()