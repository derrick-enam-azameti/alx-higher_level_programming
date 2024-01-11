#!/usr/bin/python3
def to_subtract(list_num):
    return max(list_num) - sum(num for num in list_num if num < max(list_num))


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    num = 0
    last_rom = 0
    list_num = [0]

    for ch in roman_string:
        if ch in rom_n:
            if rom_n[ch] <= last_rom:
                num += to_subtract(list_num)
                list_num = [rom_n[ch]]
            else:
                list_num.append(rom_n[ch])

            last_rom = rom_n[ch]

    num += to_subtract(list_num)

    return num
