# -*- coding: utf-8 -*-


def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list
    
    Divide : Find the midpoint of the list and divide into sublists
    
    Conquer : Recursively sort the sublists created in previous step
    
    Combine : Merge the sorted sublists created in previous step
    
    Takes O(n log n) time
    """
    
    if len(list) <= 1 :
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half) 
    right = merge_sort(right_half)
    

    
    return merge(left, right)

def split(list) :
    """
    Divide the unsorted list at midpoint into sublists

    Parameters
    ----------
    list

    Returns
    -------
    Two sublists - left and right
    
    Takes overall O( log n) time

    """
    
    mid = len(list) // 2
    left = list[:mid] #[:mid] veut dire depuis le premier indice, jusqu'à mid --> :mid
    
    #print("\nSplit - Left ", left)
    
    right = list[mid:] #[mid:] veut dire depuis mid jusqu'au dernier indice --> mid:
        
    #print("\nSplit - right ", right)
        
    return left, right

def merge(left, right):
    """
    Function merges two lists (arrays), sorting them in the process

    Parameters
    ----------
    2 lists


    Returns
    -------
    A new merged list
    
    Runs in overall O(n) time

    """
    
    l=[]
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        
        else :
            l.append(right[j])
            j += 1
            
    while i < len(left):
        l.append(left[i])
        i+= 1
        
    while j < len(right):
        l.append(right[j])
        j+= 1
        
    return l

def verify_sorted(list):
    
    n = len(list)
    
    if n == 0 or n == 1 :
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])

            
        
alist = [54 , 26 ,12 , 98 , 500 , 154 , 657 , 4 , 65 , 287 , 1 , 14 , 34 ,78 , 23]
    
l = merge_sort(alist)

print("\nFinal result", l)

print(verify_sorted(alist))

print(verify_sorted(l))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    