import sys


def get_input():
    return (input("Enter a hexadecimal number: "))


def validate_input(raw_input):
    for i in range(0, len(raw_input)):
        try:
            int(raw_input[i])
        except:
            sys.exit("Enter numbers only")
    return raw_input


def convert_input_to_float(validated_input):
    decimal = 0
    for power, digit in enumerate(reversed(validated_input)):
        decimal += int(digit, 16) * (16**power)
    return decimal


raw_input = get_input()
validated_input = validate_input(raw_input)
converted_input = convert_input_to_float(validated_input)
print(converted_input)

# I should probably warp the function calls in a main function
