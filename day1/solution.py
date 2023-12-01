from typing import (
    List
)

def import_txt(filename: str) -> List[str]:
    lines: List[str] = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip("\n"))
    return lines

def get_first_digit(line: str) -> int:
    for character in line:
        try:
            first_digit = int(character)
            return first_digit
        except ValueError:
            continue

def get_second_digit(line: str) -> int:
    for character in line[::-1]:
        try:
            second_digit = int(character)
            return second_digit
        except ValueError:
            continue
        

def main():
    filename = "input.txt"
    lines = import_txt(filename)
    calibration_sum = 0
    for line in lines:
        print(line)
        first_digit = get_first_digit(line)
        second_digit = get_second_digit(line)
        calibration = int(f"{first_digit}{second_digit}")
        calibration_sum += calibration
        print(calibration, first_digit, second_digit)
        print("========")

    print(f"Calibration Sum: {calibration_sum}")


if __name__ == "__main__":
    main()