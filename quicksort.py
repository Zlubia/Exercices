# -*- coding: utf-8 -*-

numbers = [1,5,4,8,3,6, 25 , 68 , 2 , 12 , 18 , 33 , 15 , 7]

def quicksort(values):
    #Sorting using recursion, each time seperating the list into 2 lists based on a pivot element.
    #On prend la première valeur de la liste, on crée 2 liste, une avec tous les éléments plus petit que cette valeur,
    #et une avec tous les éléments plus grands que cette valeur
    #ensuite on assemble les 2 listes.
    #on répète ça sur chaque sous-liste (comme le merge sort) et on termines avec la liste ordonnées.
    
    """in the best case it has O(n log n) but in worst case is O(n²) runtime. En général on est plus proche du best case,
    surtout si on prend un index random pour le pivot plutôt que le premier élément de la liste."""
    
    if len(values) <= 1 :
        return values
    
    less_than_pivot = []
    greater_than_pivot = [] 
    pivot = values[0]
    
    for value in values[1:] :
        if value <= pivot :
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
            
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
    
    
    
    
sorted_numbers = quicksort(numbers)
print(sorted_numbers)


    
