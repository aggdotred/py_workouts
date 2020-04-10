
def mysum(*args):
    acc = 0
    for i in args:
        acc += i
    return acc


def get_numbers():
    return input("List the numbers to be added separated by a comma: ")


def parse_num_string(a_string_of_numbers):
    return a_string_of_numbers.split(',')


def convert_num_string(a_list_of_nums_as_strings):
    num_list = []
    for i in range(0, len(a_list_of_nums_as_strings)):
        try:
            num_list.append(int(a_list_of_nums_as_strings[i]))
        except:
            print("Please enter numbers separated by commas")
    return num_list


def add_numbers(a_list_of_numbers):
    acc = 0
    for i in range(0, len(a_list_of_numbers)):
        acc += a_list_of_numbers[i]
    return acc


num_string = get_numbers()
num_string_list = parse_num_string(num_string)
conv_num_list = convert_num_string(num_string_list)
print(add_numbers(conv_num_list))

# NOTE input would be better handled by passing args from the cli
# NOTE the original exercise intended to use the splat operator. //
# // but for passing input, parsing out a list makes more sense
