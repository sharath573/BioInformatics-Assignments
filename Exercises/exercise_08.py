"""
Exercise 8


1) Write a definition called 'compute' which takes in only **kwargs and meets the following specifications:
    - ensure that the key word 'input' is always be a list of integers before proceeding
    - if the key word 'action' is 'sum' then return the sum of all integers
    - if the key word 'action' is 'mean' then return  the mean of all integers
    - if the key word 'return_float' is 'True', then any return value should be a float

2) Implement an argument parser as a main function that meets the following requirements:
    - when run from terminal, your program should be able to accept any number of arguments
    - if -s is used, your program should print the sum of all arguments
        python3 exercise_08.py -s 1 5 20
        26
    - if -m is used, your program should multiply each value by the value of -m and print the result
        python3 exercise_08.py -m 5 1 5 20
        5
        25
        100
    - your program should also have descriptions and help attributes for each argument

"""
import sys
import argparse

def compute(**kwargs):
    if kwargs['action'] == 'sum':
     x = (sum(kwargs[('input')]))
    if kwargs['action'] == 'mean':
     x = ((sum(kwargs[('input')])/(len(kwargs[('input')]))))
    if kwargs.get('return_float') == True:
     float(x)
    return x
# print(compute(input=[1,2,3], action='sum',return_float=True ,kwarg2='abc'))
#print(compute(input=[1,2,3], action='mean',return_float=True ,kwarg2='abc'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-m', '--multiply', help='Numbers will be multiplied', type=int)
    parser.add_argument('-s', '--sum', help='numbers will be added', action='store_true')
    parser.add_argument('remainder', help=' Numbers to be Computed', nargs=argparse.REMAINDER)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(1)
    if args.sum:
        print(sum([int(x) for x in args.remainder]))
    if args.multiply:
        for number in [int(x) for x in args.remainder]:
            print (number* args.multiply)