# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 05:25:45 2020

@author: JAGRUTI
"""

# defining a Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

# defining linked list class
class LinkedList:
    
    # initializing the linked list class, has both head and tail pointer
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # for printing the linked list
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    # adding a linked list - O(1) time complexity
    def append(self, value):

        # if it is the 1st node, set head and tail to this new node
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size += 1
            return

        # add new node to the tail and shift tail to the new node
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1
        
    # return size of the linked list
    def size(self):
        return self.size

# finding union of two linked lists
def union(llist_1, llist_2):
    # Your Solution Here
    
    # set to store value already added to the linked list, so as to avoi duplication and have a fast look-up[O(1)]
    set_union = set()
    # creating new linked list
    Linked_List_Union = LinkedList()
    
    # traversing the 1st linked list
    node = llist_1.head
    while(node):
        # if value not present in the set, add it to the linked list as well as the set
        if node.value not in set_union:
            Linked_List_Union.append(node)
            set_union.add(node.value)
        node = node.next
        
    # traversing the 1st linked list
    node = llist_2.head
    while(node):
        # if value not present in the set, add it to the linked list as well as the set
        if node.value not in set_union:
            Linked_List_Union.append(node)
            set_union.add(node.value)
        node = node.next
    
    # check if there were no elements
    if Linked_List_Union.head is None:
        print("Sorry empty linked list")
    return Linked_List_Union
                
# find intersection of two linked lists
def intersection(llist_1, llist_2):
    # Your Solution Here
    
    # maintain two sets for the two linked lists
    set_1 = set()
    set_2 = set()
    
    # first traverse the 2nd linked list
    node = llist_2.head
    while(node):
        # if value not present in set_2, add it to the linked list as well as the set
        if node.value not in set_2:
            set_2.add(node.value)
        node = node.next
        
    # create new linked list for storing the common elements
    Linked_List_Intersection = LinkedList()
    
    # traverse the 1st linked list
    node = llist_1.head
    while(node):
        # if value is present in set_2 and not in set_1, add it to the linked list as well as to set_1
        if node.value in set_2 and node.value not in set_1:
            Linked_List_Intersection.append(node)
            set_1.add(node.value)
        node = node.next
        
    # if there are no elements or no common elements in both the linked lists
    if Linked_List_Intersection.head is None:
        print("Sorry empty linked list")
    return Linked_List_Intersection
    
# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))         # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
print (intersection(linked_list_1,linked_list_2))  # 4 -> 6 -> 21 -> 

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))         # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
print (intersection(linked_list_3,linked_list_4))  # Sorry empty linked list

# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))          # Sorry empty linked list
print (intersection(linked_list_3,linked_list_4))   # Sorry empty linked list


# Test case 4

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [8, 7, 6, 5, 20, 19, 18, 19, 19, 20, 6, 5]
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))          # 8 -> 7 -> 6 -> 5 -> 20 -> 19 -> 18 -> 
print (intersection(linked_list_3,linked_list_4))   # Sorry empty linked list

# Test case 5

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = [-8, -7, -6, -5, -20, -19, -18, -19, -19, -20, -6, -5]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))         # -8 -> -7 -> -6 -> -5 -> -20 -> -19 -> -18 -> 
print (intersection(linked_list_3,linked_list_4))  # Sorry empty linked list

# Test case 6

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [i for i in range(0,100,2)] + [i for i in range(0,100,3)]
element_2 = [i for i in range(0,100,5)] + [i for i in range(0,100,10)]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 0 -> 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> 16 -> 18 -> 20 -> 22 -> 24 -> 26 -> 28 -> 30 -> 32 -> 34 -> 
# 36 -> 38 -> 40 -> 42 -> 44 -> 46 -> 48 -> 50 -> 52 -> 54 -> 56 -> 58 -> 60 -> 62 -> 64 -> 66 -> 68 -> 
# 70 -> 72 -> 74 -> 76 -> 78 -> 80 -> 82 -> 84 -> 86 -> 88 -> 90 -> 92 -> 94 -> 96 -> 98 -> 3 -> 9 -> 15 
# -> 21 -> 27 -> 33 -> 39 -> 45 -> 51 -> 57 -> 63 -> 69 -> 75 -> 81 -> 87 -> 93 -> 99 -> 5 -> 25 -> 35  
# -> 55 -> 65 -> 85 -> 95 -> 
print (intersection(linked_list_3,linked_list_4))
# 0 -> 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> 70 -> 80 -> 90 -> 15 -> 45 -> 75 -> 

# Test case 7

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [i for i in range(0,100,2)] + [i for i in range(0,100,3)]
element_2 = [i for i in range(0,100,5)] + [i for i in range(0,100,7)]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# 0 -> 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> 14 -> 16 -> 18 -> 20 -> 22 -> 24 -> 26 -> 28 -> 30 -> 32 -> 
# 34 -> 36 -> 38 -> 40 -> 42 -> 44 -> 46 -> 48 -> 50 -> 52 -> 54 -> 56 -> 58 -> 60 -> 62 -> 64 ->  
# 66 -> 68 -> 70 -> 72 -> 74 -> 76 -> 78 -> 80 -> 82 -> 84 -> 86 -> 88 -> 90 -> 92 -> 94 -> 96 -> 
# 98 -> 3 -> 9 -> 15 -> 21 -> 27 -> 33 -> 39 -> 45 -> 51 -> 57 -> 63 -> 69 -> 75 -> 81 -> 87 -> 93 
# -> 99 -> 5 -> 25 -> 35 -> 55 -> 65 -> 85 -> 95 -> 7 -> 49 -> 77 -> 91 -> 
print (intersection(linked_list_3,linked_list_4))
# 0 -> 10 -> 14 -> 20 -> 28 -> 30 -> 40 -> 42 -> 50 -> 56 -> 60 -> 70 -> 80 -> 84 -> 90 -> 
# 98 -> 15 -> 21 -> 45 -> 63 -> 75 -> 