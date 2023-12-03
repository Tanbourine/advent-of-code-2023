from typing import (
    List
)

WORD_TO_DIGIT = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

def import_txt(filename: str) -> List[str]:
    lines: List[str] = []
    with open(filename) as f:
        for line in f:
            lines.append(line.strip("\n"))
    return lines

def convert_to_int(line: str, reverse: bool = False) -> str:
    for word, digit in WORD_TO_DIGIT.items():
        if reverse:
            if word[::-1] in line:
                return str(digit)
            # line = line.replace(word[::-1], str(digit))
        else:
            # line = line.replace(word, str(digit))
            if word in line:
                return str(digit)
    return line


def get_digit(line: str, reverse: bool) -> int:
    if reverse:
        line = line[::-1]
    buffer = ""
    for character in line:
        buffer += character
        try:
            return int(character)
        except ValueError:
            potential_number = convert_to_int(buffer, reverse=reverse)
            try:
                return int(potential_number)
            except ValueError:
                continue

def convert_str_to_calibration(line: str) -> int:
    # line = convert_to_int(line)
    # first_digit = get_first_digit(line)
    # second_digit = get_second_digit(line)
    first_digit = get_digit(line, False)
    second_digit = get_digit(line, True)
    calibration = int(f"{first_digit}{second_digit}")
    return calibration

def main():
    filename = "input.txt"
    lines = import_txt(filename)
    calibration_sum = 0
    # print(convert_str_to_calibration("oneight")) # returns 11, should be 18
    # print(convert_str_to_calibration("4oneight")) # returns 41, should be 48
    # print(convert_str_to_calibration("88three1xoneighth")) # returns 81, should be 88
    for line in lines:
        calibration = convert_str_to_calibration(line)
        calibration_sum += calibration
        print(calibration)

    print(f"Calibration Sum: {calibration_sum}")


if __name__ == "__main__":
    main()