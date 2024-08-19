import re


def extract_hex_numbers(input_string: str) -> list:
    pattern = r'\b(0x[0-9A-F]+|(?<!0x)([0-9A-F]+))\b'
    matches = re.findall(pattern, input_string)
    hex_numbers = []
    for match in matches:
        if match[0].startswith('0x'):
            hex_numbers.append(match[0])
        elif match[1]:
            hex_numbers.append('0x' + match[1].upper())

    return hex_numbers


input_string = input()
result = extract_hex_numbers(input_string)
print(' '.join(result))