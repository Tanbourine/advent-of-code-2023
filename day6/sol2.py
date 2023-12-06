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
            print(f"Winning hold: {hold} | Inputs: {hold * travel_time} | {travel_time} | {distance}")
            winning_holds.append(hold)
        
        # if len(winning_holds) > 3:
        #     break

        # print(hold, hold * travel_time, distance)
    return winning_holds
        

def main():
    filename = "example.txt"
    # filename = "input.txt"
    lines = import_txt(filename)
    # times = [int(num) for num in lines[0].split(":")[1]]
    time = int(lines[0].split(":")[1].replace(" ", ""))
    distance = int(lines[1].split(":")[1].replace(" ", ""))
    print(time, distance)
    starting = 0
    end = 0
    for hold in range(time, 0, -1):
        travel_time = time - hold
        if (hold * travel_time > distance) and starting == 0:
            print(hold)
            starting = hold
        elif starting != 0 and hold * travel_time < distance:
            end = hold + 1
            break
    print(starting, end)
    print(f"Hold: {starting - end}")

    




    ways_to_win = []
    # winning_holds = race_boat(time, distance)
    # ways_to_win.append(len(winning_holds))

    # total = 1
    # for way in ways_to_win:
    #     total *= way
    # print(total)




    

if __name__ == "__main__":
    main()