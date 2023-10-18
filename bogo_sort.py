# -*- coding: utf-8 -*-
import random

#sorting algorithm that is really really bad. It randomizes the list until it gets the right order.

numbers = [1,5,4,8,3,6]

def is_sorted(values):
    #check if a list is sorted
    for index in range(len(values)-1):
        if values[index] > values[index+1] :
            return False
    return True

def bogo_sort(values):
    
    attemps = 0
    while not is_sorted(values):
        print(attemps)
        random.shuffle(values)
        attemps += 1
    return values

print(bogo_sort(numbers))
