from typing import (
    List,
    Dict,
)
import re

def import_txt(filename: str) -> List[str]:
    lines: List[str] = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip("\n"))
    return lines

class Card():
    def __init__(self, id: int, winning: List[int], numbers: List[int]):
        self.id = id
        self.winning = winning
        self.numbers = numbers
        self.count = 1


    def __repr__(self):
        return f"Card {self.id} ({self.count}): {self.winning} | {self.numbers}"

def parse_numbers(number_list: str) -> List[int]:
    numbers = re.findall("\d+", number_list)
    return [int(num) for num in numbers]

def count_matches(winning: List[int], numbers: List[int]) -> int:
    matches = 0
    for number in numbers:
        if number in winning:
            matches += 1
    return matches


def main():
    # filename = "example.txt"
    filename = "input.txt"
    lines = import_txt(filename)

    deck: Dict[int, List[Card]] = {}
    for idx, line in enumerate(lines):
        all_numbers = line.split(":")[1]
        winning = parse_numbers(all_numbers.split("|")[0])
        numbers = parse_numbers(all_numbers.split("|")[1])
        deck[idx+1] = Card(idx+1, winning, numbers)

    for card in deck.values():
        for _ in range(card.count):
            matches = count_matches(card.winning, card.numbers)
            for i in range(matches):
                card_to_add = card.id + i + 1
                deck[card_to_add].count += 1
                # print(f"Adding 1 copy to card: {card_to_add}. Total Copies: {deck[card_to_add].count}")
        print(card, matches)

    total_scratchcards = 0
    for card in deck.values():
        total_scratchcards += card.count
    print(total_scratchcards)


if __name__ == "__main__":
    main()