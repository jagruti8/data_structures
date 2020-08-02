# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 22:05:23 2020

@author: JAGRUTI
"""


# Defining the Node class for doubly linked list
class Node(object):
    
    def __init__(self, value=None, key=None):
        self.value = value
        self.key = key
        self.prev = None
        self.next = None

# Defining the Doubly_Linked_List class for maintaning the 
# order of Least Recently Used key in cache due to its O(1) time complexity for insertion as well as deletion
class Doubly_Linked_List(object):
    
    # initializing the node, with a head as well as tail pointer
    def __init__(self):
        self.head = None
        self.tail = None
    
    # function for printing the linked list
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += "{" + str(cur_head.key) + ":" + str(cur_head.value) + "}" + " -> "
            cur_head = cur_head.next
        if out_string == "":
            print("Empty Linked List")
        return out_string
        
    # for adding a node
    def add(self, node):
        newNode = node
        
        # if it is the first node in the linked list, set both the head and tail pointer to this node
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        # set the tail pointer to the newly created node
        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
      
    # for removing a node, 
    # if the node is at the end no need to remove it
    def remove(self, node):
        if node == self.tail:
            return None
        
        # return the node removed, to be added back at the tail
        remove_node = node
        
        # remove the first node and shift the head pointer to the next node
        if node == self.head:
            self.head = node.next
            self.head.prev = None
            node.prev = None
            node.next = None
            return remove_node
        
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None
    
        return remove_node
        
class LRU_Cache(object):

    def __init__(self, capacity = 10):
        # Initialize class variables
        self.capacity = capacity
        # dictionary of children where each key has a pointer to a doubly linked list node as value
        # this acts like a hash table for inserting as well as accessing a key in O(1) time complexity
        self.dict = {}  
        self.index = 0  # to keep count of no of keys added
        self.LinkedList = Doubly_Linked_List()

    def get(self, key):
        
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if self.capacity is 0 or self.capacity is None:
            print("Sorry our cache is empty due to no capacity")
            return
        
        if key is None:
            print("Error!Please insert a key")
            return
        
        if key not in self.dict:
            print("key: {} is not present".format(key))
            return -1
        # key of dictionary stores pointer to a node where again the key-value pairs are stored
        node = self.dict[key]
        value = node.value
        # recently accessed key is removed and added back at the tail so that least recently used key at the head
        # can be removed
        node_removed = self.LinkedList.remove(node)
        # if last key added is accessed, then no action is taken since it is already at the tail
        if node_removed is not None:
            self.LinkedList.add(node_removed)
        return value
        
    def set(self, key, value):

        if self.capacity is 0 or self.capacity is None:
            print("Sorry can't add, our cache capacity is 0")
            return
        
        if key is None:
            print("Error! Please insert a key:")
            return
        
        if value is None:
            print("Error! Please insert a value:")
            return
        
        # Set the new value of the key if it is present in the cache    
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            # recently modified key is removed and added back at the tail so that least recently used key at the head
            # can be removed
            node = self.LinkedList.remove(node)
            # if last key added is modified, then no action is taken since it is already at the tail
            if node is not None:
                self.LinkedList.add(node)
            return
        
        # If key is not present add the new key if capacity is not reached
        if self.index<self.capacity:
            # create a new node
            self.dict[key] = Node(value, key)
            # add it to linked list
            self.LinkedList.add(self.dict[key])
            # increase the no of keys in cache by 1 
            self.index += 1
            
        # If the cache is at capacity remove the oldest item ,i.e, the node that is at the head 
        # and then add the new key at the tail
        else:
            node = self.LinkedList.remove(self.LinkedList.head)
            old_key = node.key
            print("key: {} deleted as we inserted new key: {}".format(old_key, key))
            # remove the old key from the dictionary as well
            del self.dict[old_key]
            # create a new node
            self.dict[key] = Node(value, key)
            # add it to linked list
            self.LinkedList.add(self.dict[key])
            
## Example 1
our_cache = LRU_Cache(5)

print(our_cache.dict.keys())   # dict_keys([])
print(our_cache.LinkedList)    # Empty Linked List

our_cache.set(1, 1);
print(our_cache.dict.keys())  # dict_keys([1])
print(our_cache.LinkedList)   # {1:1} -> 

our_cache.set(2, 2);
print(our_cache.dict.keys())  # dict_keys([1, 2])
print(our_cache.LinkedList)   # {1:1} -> {2:2} -> 

our_cache.set(3, 3);
print(our_cache.dict.keys())  # dict_keys([1, 2, 3])
print(our_cache.LinkedList)   # {1:1} -> {2:2} -> {3:3} -> 

our_cache.set(4, 4);
print(our_cache.dict.keys())  # dict_keys([1, 2, 3, 4])
print(our_cache.LinkedList)   # {1:1} -> {2:2} -> {3:3} -> {4:4} -> 

print(our_cache.get(3))       # 3
print(our_cache.dict.keys())  # dict_keys([1, 2, 3, 4])
print(our_cache.LinkedList)   # {1:1} -> {2:2} -> {4:4} -> {3:3} -> 

print(our_cache.get(2))       # 2
print(our_cache.dict.keys())  # dict_keys([1, 2, 3, 4])
print(our_cache.LinkedList)   # {1:1} -> {4:4} -> {3:3} -> {2:2} -> 

print(our_cache.get(9))       # key: 9 is not present  |  -1
print(our_cache.dict.keys())  # dict_keys([1, 2, 3, 4]) 
print(our_cache.LinkedList)   # {1:1} -> {4:4} -> {3:3} -> {2:2} -> 

our_cache.set(5, 5)           
print(our_cache.dict.keys())  # dict_keys([1, 2, 3, 4, 5])
print(our_cache.LinkedList)   # {1:1} -> {4:4} -> {3:3} -> {2:2} -> {5:5} -> 

our_cache.set(6, 6)           # key: 1 deleted as we inserted new key: 6
print(our_cache.dict.keys())  # dict_keys([2, 3, 4, 5, 6])
print(our_cache.LinkedList)   # {4:4} -> {3:3} -> {2:2} -> {5:5} -> {6:6} -> 

our_cache.set(7, 7)           # key: 4 deleted as we inserted new key: 7
print(our_cache.dict.keys())  # dict_keys([2, 3, 5, 6, 7])
print(our_cache.LinkedList)   # {3:3} -> {2:2} -> {5:5} -> {6:6} -> {7:7} ->

print(our_cache.get(3))       # 3
print(our_cache.dict.keys())  # dict_keys([2, 3, 5, 6, 7])
print(our_cache.LinkedList)   # {2:2} -> {5:5} -> {6:6} -> {7:7} -> {3:3} -> 

## Example 2

our_cache = LRU_Cache()

print(our_cache.dict.keys())    # dict_keys([])
print(our_cache.LinkedList)     # Empty Linked List
our_cache.set(None, 1)          # Error! Please insert a key:
our_cache.set(None, None)       # Error! Please insert a key:
our_cache.set(1, None)          # Error! Please insert a value:
print(our_cache.dict.keys())    # dict_keys([])
print(our_cache.LinkedList)     # Empty Linked List

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)

print(our_cache.get(1))         # 1
our_cache.get(None)             # Error!Please insert a key
print(our_cache.dict.keys())    # dict_keys([1, 2, 3, 4, 5])
print(our_cache.LinkedList)     # {2:2} -> {3:3} -> {4:4} -> {5:5} -> {1:1} -> 

print(our_cache.get(5))         # 5
our_cache.set(5, 14)
our_cache.set(6, 6)
print(our_cache.dict.keys())    # dict_keys([1, 2, 3, 4, 5, 6])
print(our_cache.LinkedList)     # {2:2} -> {3:3} -> {4:4} -> {1:1} -> {5:14} -> {6:6} -> 

our_cache.set(7, 7)
our_cache.set(8, 8)
print(our_cache.get(5))         # 14

our_cache.set(9, 9)             
our_cache.set(10, 10)
our_cache.set(6, 15)
print(our_cache.dict.keys())    # dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(our_cache.LinkedList)     # {2:2} -> {3:3} -> {4:4} -> {1:1} -> {7:7} -> {8:8} -> {5:14} -> {9:9} -> {10:10} -> {6:15} -> 

our_cache.set(11, 11)           # key: 2 deleted as we inserted new key: 11
print(our_cache.dict.keys())    # dict_keys([1, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(our_cache.LinkedList)     # {3:3} -> {4:4} -> {1:1} -> {7:7} -> {8:8} -> {5:14} -> {9:9} -> {10:10} -> {6:15} -> {11:11} -> 

print(our_cache.get(2))         # key: 2 is not present | -1
print(our_cache.dict.keys())    # dict_keys([1, 3, 4, 5, 6, 7, 8, 9, 10, 11])
print(our_cache.LinkedList)     # {3:3} -> {4:4} -> {1:1} -> {7:7} -> {8:8} -> {5:14} -> {9:9} -> {10:10} -> {6:15} -> {11:11} -> 

## Example 3

our_cache = LRU_Cache(None)

print(our_cache.dict.keys())    # dict_keys([])
print(our_cache.LinkedList)     # Empty Linked List

our_cache.set(None, 1)          # Sorry can't add, our cache capacity is 0
our_cache.set(None, None)       # Sorry can't add, our cache capacity is 0
our_cache.set(1, None)          # Sorry can't add, our cache capacity is 0

our_cache.set(1, 1)             # Sorry can't add, our cache capacity is 0 
our_cache.set(2, 2)             # Sorry can't add, our cache capacity is 0

print(our_cache.get(1))         # Sorry our cache is empty due to no capacity | None
our_cache.get(None)             # Sorry our cache is empty due to no capacity

print(our_cache.dict.keys())    # dict_keys([])
print(our_cache.LinkedList)     # Empty Linked List

## Example 4

import random

our_cache = LRU_Cache(5)
list_keys = [i for i in range(1, 101)]
values = random.sample(range(1, 2000000), 100)
dictionary = dict(zip(list_keys, values))  # making key-value pairs to be added in the cache

iteration = 0

for i in range(len(list_keys)):
    key = list_keys[i]
    value = dictionary[key]
    our_cache.set(key, value)
    iteration = (iteration + 1) % our_cache.capacity   # to check in every 5 iterations
    
    if iteration == 0:
        # pick a random key out of the keys present in cache and access that key
        random_index = random.randint(0, our_cache.capacity-1)
        print(our_cache.dict.keys())
        key_random = list(our_cache.dict.keys())[random_index]
        print("random key picked:", key_random)
        print("Before accessing the key:", our_cache.LinkedList)
        our_cache.get(key_random)
        print("After accessing the key:", our_cache.LinkedList)
        
## Just showing a few iterations - this will show different results in different runs 
## due to the random number picked

"""
dict_keys([1, 2, 3, 4, 5])
random key picked: 3
Before accessing the key: {1:15088} -> {2:333086} -> {3:713218} -> {4:1277998} -> {5:1758789} -> 
After accessing the key: {1:15088} -> {2:333086} -> {4:1277998} -> {5:1758789} -> {3:713218} -> 
key: 1 deleted as we inserted new key: 6
key: 2 deleted as we inserted new key: 7
key: 4 deleted as we inserted new key: 8
key: 5 deleted as we inserted new key: 9
key: 3 deleted as we inserted new key: 10
dict_keys([6, 7, 8, 9, 10])
random key picked: 6
Before accessing the key: {6:357570} -> {7:774182} -> {8:636866} -> {9:1298803} -> {10:1813419} -> 
After accessing the key: {7:774182} -> {8:636866} -> {9:1298803} -> {10:1813419} -> {6:357570} -> 
key: 7 deleted as we inserted new key: 11
key: 8 deleted as we inserted new key: 12
key: 9 deleted as we inserted new key: 13
key: 10 deleted as we inserted new key: 14
key: 6 deleted as we inserted new key: 15
dict_keys([11, 12, 13, 14, 15])
random key picked: 12
Before accessing the key: {11:1602054} -> {12:1153976} -> {13:1726207} -> {14:1404640} -> {15:1103866} -> 
After accessing the key: {11:1602054} -> {13:1726207} -> {14:1404640} -> {15:1103866} -> {12:1153976} -> 
key: 11 deleted as we inserted new key: 16
key: 13 deleted as we inserted new key: 17
key: 14 deleted as we inserted new key: 18
key: 15 deleted as we inserted new key: 19
key: 12 deleted as we inserted new key: 20
dict_keys([16, 17, 18, 19, 20])
"""
        
