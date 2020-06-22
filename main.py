import sys
import multiprocessing
import random

index = 0
max_random = 10
test_length = 10

class Data:
    def __init__(self):
        self.value = random.randint(0, max_random)


def data_set(size): # creates a list of Data objects
    result = []
    for i in range(size):
        result.append(Data())
    return result


testlist = data_set(test_length)


def main():
    print_values(testlist)
    one = multiprocessing.Process(target=print_values(process_list()))
    two = multiprocessing.Process(target=print_values(process_list()))
    one.start()
    two.start()
    one.join()
    two.join()


def process_list():  # returns the testlist with altered values
    global index, testlist
    result = []
    while index < len(testlist):
        testlist[index].value = dif(testlist[index].value)
        result.append(testlist[index])
        index += 1
    return result


def dif(val): # returns the difference between the data value and the maximum random number
    global max_random
    return abs(max_random - val)


def print_values(tl): # formats Data objects so Values are visible
    res = ""
    for d in tl:
        res += str(d.value) + ", "
    res = res[0:len(res) - 2]
    print(res)


if __name__ == '__main__':
    main()
