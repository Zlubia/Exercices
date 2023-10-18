# -*- coding: utf-8 -*-

numbers = [1,5,4,8,3,6, 25 , 68 , 2 , 12 , 18 , 33 , 15 , 7]

def selection_sort(values):
    #sorting, searching for the lowest value and extracting it to add it to a new list. Repeat until the whole list is sorted
    
    """O(n²) runtime"""
    
    sorted_list = []  
    
    for i in range (0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))

    return sorted_list


def index_of_min(values):
    min_index = 0
    for i in range (1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

print(selection_sort(numbers))