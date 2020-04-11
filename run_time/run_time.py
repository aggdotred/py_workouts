import sys

run_times_list = []


def get_run_times():
    c = input("Enter 10km run time or 'q' to stop: ")
    if c != 'q' and c != 'Q':
        try:
            run_times_list.append(float(c))
            get_run_times()
        except:
            sys.exit("Please only enter numbers or 'q'.")

    return run_times_list


def return_average(number_list):
    acc = 0
    for i in range(0, len(number_list)):
        acc += number_list[i]
    return acc / (len(number_list) + 1)


times_list = get_run_times()
print(return_average(times_list))

# notes I like the separation of concerns over the proposed solution from the book
# but I wonder if the list is more expensive than keeping a sum and count.
