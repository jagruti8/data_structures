# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 03:57:24 2020

@author: JAGRUTI
"""


import sys

# defining Node class for the tree
class Node(object):
    def __init__(self, value=None, char=None, binary_code=None):
        self.value = value  
        self.char = char 
        self.left = None
        self.right = None
        
# defining minHeap for priority queue implementation - O(log(n)) - insertion and deletion
class minHeap(object):
    def __init__(self):
        self.arr = []
        
    # for adding a node to priority queue
    def push(self, Node=None):
        
        self.arr.append(Node)
        
        # if it is not the first node
        if len(self.arr) > 1:
            
            child_index = len(self.arr)-1
            parent_index = (child_index-1) // 2
            
            # compare until the child is smaller than the parent or child becomes the root element means at the top
            while(parent_index>=0 and self.arr[child_index].value<self.arr[parent_index].value):
                
                # swap the values
                temp = self.arr[child_index]
                self.arr[child_index] = self.arr[parent_index]
                self.arr[parent_index] = temp
                
                # repeat the procedure at the parent node
                child_index = parent_index
                parent_index = (child_index-1) // 2
    
    # removing the top element from the minHeap
    def pop(self):
        
        if len(self.arr) == 0:
            return 
        
        node = self.arr[0] # the top element is the minimum
        self.arr[0] = self.arr[-1] # get the last element at the first
        self.arr.pop() # decrease the array size by '1' from the right side of the array
        
        # downheapify to set the top element at the correct position
        parent_index = 0
        while(parent_index<len(self.arr)):
            
            # find the minimum of the parent node and its two child nodes
            left_child_index = 2*parent_index + 1
            right_child_index = 2*parent_index + 2
            minimum = self.arr[parent_index]
            
            # if left child exists
            if left_child_index < len(self.arr):
                if self.arr[left_child_index].value<minimum.value:
                    minimum = self.arr[left_child_index]
                # if right child exists
                if right_child_index < len(self.arr):
                    if self.arr[right_child_index].value<minimum.value:
                        minimum = self.arr[right_child_index]
                    
            # if parent is the minimum, means it is at the correct position, hence come out of the loop
            if minimum == self.arr[parent_index]:
                break
                
            # if left child is minimum, swap parent and left child values and continue the process for the left child node
            elif minimum == self.arr[left_child_index]:
                self.arr[left_child_index] = self.arr[parent_index]
                self.arr[parent_index] = minimum
                parent_index = left_child_index
                
            # if right child is minimum, swap parent and right child values and continue the process for the right child node
            else:
                self.arr[right_child_index] = self.arr[parent_index]
                self.arr[parent_index] = minimum
                parent_index = right_child_index
        
        return node
        
def huffman_encoding(data):
    
    if len(data) is 0:
        print("Error! Enter some data:")
        return "", None
    
    # storing character and frequency as key, value pair
    dict_char = {}
    for char in data:
        if char not in dict_char:
            dict_char[char] = 1
        else:
            dict_char[char] += 1
    
    # creating the minHeap
    minHeap1 = minHeap()
    # adding elements to minHeap
    for char, frequency in dict_char.items():
        # each node contains the character and it's frequency
        newNode = Node(frequency, char)
        minHeap1.push(newNode)
    
    # building the huffman tree
    while(len(minHeap1.arr)>1):
        
        # remove the two minimum elements from the minHeap
        element1 = minHeap1.pop()
        element2 = minHeap1.pop()
        
        # add their values
        sum_elements = element1.value + element2.value
        
        # make a new node with the sum
        parent = Node(sum_elements)
        
        # make the smaller value node as left child and larger one as right child
        parent.left = element1
        parent.right = element2 
        
        # add the sum node to minHeap
        minHeap1.push(parent)
        
    # root of the huffman tree 
    root = minHeap1.pop()
    
    #pre_order_traversal(root)
    
    # create encoding for each character
    huff_char = create_code(root)
    
    # encode the string by using the encoding
    encoding = ""
    if huff_char:
        for char in data:
            encoding += huff_char[char]
            
    # this happens when the string contains only one character
    else:
        encoding = "0"
    
    return encoding, root

# create encoding for each character
def create_code(node, code=''):
    
    # code list
    list_of_codes = {}
    
    # if huffman tree has just one node ,i.e, the root
    if node.left == None and node.right == None:
        return list_of_codes
    
    # add a '0' for the left child
    code_left = code + '0'
    # if left child has a character, it is a leaf node, hence add the obtained code for that character 
    if node.left.char:
        list_of_codes[node.left.char] = code_left
    # else traverse the left child
    else:
        list_of_codes = create_code(node.left, code_left)
        
    # add a '1' for the right child
    code_right = code + '1'
    # if right child has a character, it is a leaf node, hence add the obtained code for that character
    if node.right.char:
        list_of_codes[node.right.char] = code_right
    # else traverse the right child
    else:
        list_of_codes.update(create_code(node.right, code_right))
    
    return list_of_codes
        
# for pre-order traversal of tree
def pre_order_traversal(node):
    if node is None:
        return
    print("Character: {}, Value:{}".format(node.char, node.value))
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

# for decoding the encoded string
def huffman_decoding(data, tree):
    
    # if the encoding has a single value, it means the string has just one character with frequency:tree.value"
    if len(data) == 1:
        word = "".join(tree.char for i in range(tree.value))
        return word
    
    # start from the huffman tree root
    node = tree
    index = 0
    decoded_data = ""
    
    while(index<len(data)):
        
        # if '0' is there traverse left
        if data[index] == '0':
            node = node.left
            
        # if '1' is there traverse right
        elif data[index] == '1':
            node = node.right
            
        # if node has a character, it means, leaf node is reached 
        # and hence add the character at the leaf of tree to the decoded data
        if node.char:
            decoded_data += node.char
            node = tree
        # increment the index
        index += 1
   
    return decoded_data
        
## Test Cases

if __name__ == "__main__":
    list_of_strings = ["AAAAAAABBBCCCCCCCDDEEEEEE", "The bird is the word", "a", "aa", "ab", "~!@#$%^&*()_+`1234567890-={}[]|\:;<>,.?/",
                      "Topic sentences are similar to mini thesis statements! Like a thesis statement, a topic sentence has a specific main point. Whereas the thesis is the main point of the essay, the topic sentence is the main point of the paragraph. Like the thesis statement, a topic sentence has a unifying function. But a thesis statement or topic sentence alone doesn’t guarantee unity. An essay is unified if all the paragraphs relate to the thesis, whereas a paragraph is unified if all the sentences relate to the topic sentence. Note: Not all paragraphs need topic sentences. In particular, opening and closing paragraphs, which serve different functions from body paragraphs, generally don’t have topic sentences?"
                      ,"bbbbbbbbbbbbbbb", ""]
    for index, string in enumerate(list_of_strings):
        print("Example: {}\n".format(index+1))
        print ("The size of the data is: {}\n".format(sys.getsizeof(string)))
        print ("The content of the data is: {}\n".format(string))

        encoded_data, tree = huffman_encoding(string)
        
        if tree:
        
            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            #print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the decoded data is: {}\n".format(decoded_data))
            
            if string == decoded_data:
                print("string: {} properly encoded and decoded".format(index + 1))
            else:
                print("string: {} not properly encoded and decoded".format(index + 1))
                
        print("\n--------------------------------------------------------------------------------\n")
        
## Outputs:

"""
Example: 1

The size of the data is: 74

The content of the data is: AAAAAAABBBCCCCCCCDDEEEEEE

The size of the encoded data is: 32

The size of the decoded data is: 74

The content of the decoded data is: AAAAAAABBBCCCCCCCDDEEEEEE

string: 1 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 2

The size of the data is: 69

The content of the data is: The bird is the word

The size of the encoded data is: 36

The size of the decoded data is: 69

The content of the decoded data is: The bird is the word

string: 2 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 3

The size of the data is: 50

The content of the data is: a

The size of the encoded data is: 24

The size of the decoded data is: 50

The content of the decoded data is: a

string: 3 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 4

The size of the data is: 51

The content of the data is: aa

The size of the encoded data is: 24

The size of the decoded data is: 51

The content of the decoded data is: aa

string: 4 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 5

The size of the data is: 51

The content of the data is: ab

The size of the encoded data is: 28

The size of the decoded data is: 51

The content of the decoded data is: ab

string: 5 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 6

The size of the data is: 89

The content of the data is: ~!@#$%^&*()_+`1234567890-={}[]|\:;<>,.?/

The size of the encoded data is: 56

The size of the decoded data is: 89

The content of the decoded data is: ~!@#$%^&*()_+`1234567890-={}[]|\:;<>,.?/

string: 6 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 7

The size of the data is: 1478

The content of the data is: Topic sentences are similar to mini thesis statements! Like a thesis statement, a topic sentence has a specific main point. Whereas the thesis is the main point of the essay, the topic sentence is the main point of the paragraph. Like the thesis statement, a topic sentence has a unifying function. But a thesis statement or topic sentence alone doesn’t guarantee unity. An essay is unified if all the paragraphs relate to the thesis, whereas a paragraph is unified if all the sentences relate to the topic sentence. Note: Not all paragraphs need topic sentences. In particular, opening and closing paragraphs, which serve different functions from body paragraphs, generally don’t have topic sentences?

The size of the encoded data is: 412

The size of the decoded data is: 1478

The content of the decoded data is: Topic sentences are similar to mini thesis statements! Like a thesis statement, a topic sentence has a specific main point. Whereas the thesis is the main point of the essay, the topic sentence is the main point of the paragraph. Like the thesis statement, a topic sentence has a unifying function. But a thesis statement or topic sentence alone doesn’t guarantee unity. An essay is unified if all the paragraphs relate to the thesis, whereas a paragraph is unified if all the sentences relate to the topic sentence. Note: Not all paragraphs need topic sentences. In particular, opening and closing paragraphs, which serve different functions from body paragraphs, generally don’t have topic sentences?

string: 7 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 8

The size of the data is: 64

The content of the data is: bbbbbbbbbbbbbbb

The size of the encoded data is: 24

The size of the decoded data is: 64

The content of the decoded data is: bbbbbbbbbbbbbbb

string: 8 properly encoded and decoded

--------------------------------------------------------------------------------

Example: 9

The size of the data is: 49

The content of the data is: 

Error! Enter some data:

--------------------------------------------------------------------------------

"""
   
    