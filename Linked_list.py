# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 09:31:11 2023

@author: Pierrick
"""

class Node :
    """
    An object for storing a single node of a linked list
    Models 2 attributes - data and the link to the next node in the list
    """
    
    data = None
    next_node = None
    
    def __init__(self, data):
        self.data = data
        
    def __repr__(self):
        """Ceci imprimera Node data : les données du nodes, lorsqu'on veut imprimer l'objet. Sinon python imprimerait un 
        identifiant chiffré qu'on ne comprendrait pas'
        """
        return "<Node data: %s>" % self.data

#testing node object:
    
N1 = Node(10)

print("Print N1 : ", N1)

N2 = Node(20)
N1.next_node = N2

print("Print N1.next_node : ",N1.next_node)


#creating linked list of nodes:
        
class LinkedList:
    """
    Singly linked list
    """
    
    
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        """
        Même principe que pour la class Node, on imprime un truc lisible
        Return a string representation of the list
        Takes O(n) time (linear runtime)
        """
        
        nodes = []
        current = self.head
        
        while current : 
            if current is self.head :
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None :
                nodes.append("[Tail: %s]" % current.data)
            else :
                nodes.append("[%s]" % current.data)
        
            current = current.next_node
            
        return '-> '.join(nodes)
        
        
    def is_empty(self):
        #return True when the list is empty
        return self.head == None
    
    def size(self):
        """ On devra parcourir toute la linked list pour savoir combien d'éléments il y a dedans.
        
        Returns the number of nodes in the list
        Takes O(n) times (linear runtime)
        """
        current = self.head
        count = 0
        
        while current :
            #while current, veut dire la même chose que while current != None, donc que current == à quelque chose.
            count += 1
            current = current.next_node
            
        return count
    
    def add(self, data):
        """
        Adds new Node containing data at head of the list
        Takes O(1) (Constant time)
        """ 
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        
    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Return the node or 'None' if not found
        
        Takes O(n) time (linear time)
        """
        current = self.head
        
        while current : 
            if current.data == key :
                return current
            else:
                current = current.next_node
                
        return None
    
    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position
        Insertion takes constant time O(1) but finding the node at the
        insertion point takes O(n) time (linear time)
        
        Therefore takes O(n) time (linear time)
        """
        
        if index == 0:
            self.add(data)
            
        if index > 0 :
            new = Node(data)
            
            position = index
            current = self.head
            
            while position > 1 :
                current = current.next_node
                position -= 1
                
            prev_node = current
            next_node = current.next_node
            
            prev_node.next_node = new
            new.next_node = next_node
            
    def remove(self, key) :
        """
        Removes Node containing data that matches the key
        Retuns the node or None if key doesn't exist
        
        Takes O(n) time
        """
        
        current = self.head
        previous = None
        found = False
        
        while current and not found:
            
            if current.data == key and current == self.head :
                found = True
                self.head = current.next_node
                
            elif current.data == key :
                found = True
                previous.next_node = current.next_node
                
            else :
                previous = current
                current = current.next_node
                
        return current
        
        
    def remove_at_index (self, index) :
        """
        EXERCICE
        Removes Node containing data that matches the index
        Retuns the node or None if index doesn't exist
        
        Takes O(n) time
        """    
        
        current = self.head
        
        
        if index == 0 :
            self.head = current.next_node
            
        elif index > 0 :
            #new = Node()
            
            position = index
            
            while position > 1 :
                previous = current
                current = current.next_node
                position -= 1    
                
            previous = current.next_node
        
        
        return current
    
    def node_at_index(self, index) :
        if index == 0 :
            return self.head
        else :
            current = self.head
            position = 0
            
            while position < index :
                current = current.next_node
                position += 1
            
            return current
                       

            
#test linked list :
    
l = LinkedList()
l.add(1)

print("\nsize of l : ", l.size())
    
l.add(2)
l.add(3)

print("\nsize of l after adding 2 other nodes : ", l.size())

print("\nWe'll print l now :\n")
print(l)

print("\nWe'll add 2 more nodes (45 and 15) and search for 45")

l.add(45)
l.add(15)

n = l.search(45)

print("\nWe'll print the node we searched now :\n")
print(n)

















