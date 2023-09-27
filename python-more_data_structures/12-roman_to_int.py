#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }
        count = 0
        for letter in roman_string:
            if letter not in roman:
                return 0
        for i in range(len(roman_string)):
            if roman_string[i] in roman:
                if i + 1 < len(roman_string):
                    if roman_string[i] < roman_string[i + 1]:
                        count -= roman[roman_string[i]]
                    else:
                        count += roman[roman_string[i]]
                else:
                    count += roman[roman_string[i]]
        return count
    else:
        return 0
