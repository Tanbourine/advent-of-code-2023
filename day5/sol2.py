from typing import (
    List,
    Dict,
    Set,
    Tuple
)
import re

def import_txt(filename: str) -> List[str]:
    lines: List[str] = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip("\n"))
    return lines

class Map():
    def __init__(self, dest: int, start: int, length: int):
        self.dest = dest
        self.start = start
        self.length = length

    def convert(self, input: int) -> int:
        if input >= self.start and input < (self.start + self.length):
            diff = input - self.start
            return self.dest + diff
        else:
            return None


    def __repr__(self):
        return f"Dest: {self.dest} | Start: {self.start} | Length: {self.length}"

def get_seeds(seeds: List[int]) -> List[Tuple[int, int]]:
    expanded_seeds = []
    for interval in range(0, len(seeds), 2):
        expanded_seeds.append((seeds[interval], seeds[interval+1]))
    return expanded_seeds


def main():
    # filename = "example.txt"
    filename = "input.txt"
    lines = import_txt(filename)
    # lines = [line.replace("\n", "") for line in lines]
    seeds: List[int] = []
    map_name = ""
    maps: Dict[str, List[Map]] = {}
    for idx, line in enumerate(lines):
        # skip empty lines
        if line == "":
            continue

        line = line.replace("\n\n", "")
        if idx == 0:
            temp_seeds = [int(num) for num in line.split(":")[1].strip().split(" ")]
            seeds = get_seeds(temp_seeds)
            # print(f"Seeds: {seeds}")
        else:
            match = re.match("\w+\-\w+\-\w+ \w+:", line)
            if match:
                # print(f"Map: {match}")
                map_name = match.group(0).split(" ")[0]
            else:
                numbers = [int(num) for num in line.split(" ")]
                # print(f"Numbers: {numbers}")
                current_map = maps.get(map_name)
                if not current_map:
                    # print(f"Created map: {map_name}")
                    maps[map_name] = []
                    current_map = maps[map_name]
                current_map.append(Map(numbers[0], numbers[1], numbers[2]))
                # print(f"Current Map: {map_name}: {current_map}")
    
    # print(maps)
    print(f"Seeds: {seeds}")
    all_locations = []
    for seed, seed_range in seeds:
        print(f"Starting: {seed}:{seed_range}")
        locations = []
        num = seed
        for i in range(seed_range):
            soil = map(num, maps["seed-to-soil"])
            fert = map(soil, maps["soil-to-fertilizer"])
            water = map(fert, maps["fertilizer-to-water"])
            light = map(water, maps["water-to-light"])
            temp = map(light, maps["light-to-temperature"])
            hum = map(temp, maps["temperature-to-humidity"])
            location = map(hum, maps["humidity-to-location"])
            # print(f"Soil: {soil} | Fert: {fert} | Water: {water} | Light: {light} | Temp: {temp} | Humidity: {hum} | Location: {location}")
            locations.append(location)
            num += 1
            if i % 1000000 == 0:
                print(f"Iteration: {i}")
        print(f"Completed: {seed}:{seed_range}")

        print(f"Min Location: {min(locations)}")
        all_locations.append(min(locations))
    print(f"Lowest location: {all_locations}")

def map(input: int, maps: List[Map]) -> int:
    for map in maps:
        converted = map.convert(input)
        if converted is not None:
            return converted
    return input








if __name__ == "__main__":
    main()