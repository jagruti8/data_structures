# data_structures
Short insightful projects on various data structures 

# requirements : python3

# LRU_Cache_Implementation:

The goal is to design a data structure known as a Least Recently Used (LRU) cache. 
An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit. 
We need to perform two operations, get() and put().
While doing the get() operation, if the entry is found in the cache, it is known as a cache hit.
If, however, the entry is not found, it is known as a cache miss. 
In case of a cache hit, the get() operation should return the appropriate value. 
In case of a cache miss, the get() should return -1. 
For the put(), operation, if the element is already there we need to change it's value. 
Otherwise, we have to check if the cache has not reached it's capacity, we can add the new element. 
However, if the cache is full, we need to remove the oldest item in the cache and then insert the new element. 
The lookup operation (i.e., get()) and put() is supposed to be fast for a cache memory meaning they should be done in O(1) time.

Analysis:
1. Two data structures,i.e, dictionary and doubly linked list are used for implementing LRU cache to have a time-complexity of O(1). 
2. Dictionary is used as a hash map, to store key-value pairs, where the value is a pointer pointing to a node in a doubly linked list.
   The node stores the key again(for a reason), value and the address of the next node as well as the previous node.
3. The linked list is such that, the head node is the oldest node which can be removed in O(1) time incase the cache gets full 
   and we need to insert a new key-value pair. 
4. A new node is always inserted at the tail (O(1) time complexity as we have a tail pointer as well). 
5. Incase we access a key or change it's value, the node corresponding to that key, is removed from the linked list
   (unless it is present at the tail) and added again at the tail, so that it is the most recently used key. 
   Again this operation is done in O(1) time, as we have the address of the present node to be removed as given 
   by the key in the dictionary and this node stores the address of both it's previous as well as next nodes. 
6. Incase, the cache is full, first we delete the key present at the head, then delete the same key from the dict as well
   (hence storing the key in the node). The we add the new node with the key-value pair at the tail. We add this key in the dictionary pointing to this node.
6. Hence, the time-complexity for set() and get() operations are O(1). 
7. We need an additional data structure doubly linked list besides the dictionary for maintaining LRU cache. 
   However the maximum it can grow is the size of the cache, which is constant, hence space complexity is also O(1).  

# File_Recursion:

Finding all files under a directory (and all directories beneath it) that end with ".c"

Analysis:
1. We can consider the above structure as a tree where root represents the main directory and it's children are the sub-directories. 
2. So if each node except the leaf node contains n children and the tree has a depth of h(starting from 1), 
   then for traversing the entire tree, the no of iterations is (((n^h)-1)/(n-1)), hence time complexity is O(n^h).
3. Space complexity is due to recursion which is the maximum depth of the tree ,i.e, h(starting from 1), 
   meaning the deeper the directory, the more is the space comlexity.

# Huffman_Coding:

Encoding and Decoding Algorithm for a huffman coding. 
First building a huffman tree, then encoding each character, encoding the string
For decoding, using the huffman tree to decode the encoded information

Analysis:
1. Length of string : n
2. No of ASCII characters : m (256 - constant)
3. Worst-Case : String contains all the characters

4. Encoding: 
   Time Complexity:
   a. Traverse the string to form character-value dictionary - O(n)
   b. Form MinHeap and Huffman Tree - m characters means m leaf nodes, hence m+m-1 total nodes in the Huffman Tree.
   c. Hence we have to insert and delete these many nodes from the minheap, however the maximum size of minheap is only at the beginning 
      ,i.e, m.
   d. Hence, it takes O(2(2m-1)log(m))[2 is multiplied for insertion and deletion] time to form minheap and huffman tree.
   e. To create code for all the characters, we have to traverse the entire Huffman Tree,i.e O(2m-1) time.
   f. Then to encode, we have to traverse the string again ,ie, O(n) and look-up for the code for the encountered character 
      is O(1)[Dictionary]

   Space Complexity:
   a. Dictionary - Character-Frequency - O(m)
   b. MinHeap - O(m)
   c. Huffman Tree - O(2m-1)
   d. Create coding then recursion, maximum depth can be m when it is a unbalanced tree[each node has two children 
      and it grows only in the left or right direction] - O(m) - Stack
   f. Dictionary - Character-Code - m characters with each having maximum code length m - O(m^2)

   If we take m as constant 256, then time complexity boils down to O(n) and space complexity to O(1)

5. Decoding:
   Time Complexity:
   Since the maximum code length is m, hence we have to traverse through mn characters maximum, to decode the string- 
   hence time complexity is O(n)
   [m is constant]

   Space Complexity:
   Huffman Tree - O(2m-1) - O(1)
   [m is constant]


# Active_Directory:

Function to find if a given user name exists in a directory

Analysis:
1. We can consider it like a tree, having n nodes in total hence the worst-case traversal time is O(n) 
   when the user-name is not there.
2. Space Complexity is due to recursion which is O(h), where h is the maximum depth of the tree[h starting from 1]

# Blockchain:

A Blockchain is a sequential chain of records, similar to a linked list.
Each block contains some information and how it is connected related to the other blocks in the chain.
Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. 
For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.
In this program, we implemented a simple block chain where each block meets has the above information and are connected in the form of
a linked list

Analysis:
Time Complexity:
1. For calculating the hash value for each data string of length m characters(maximum) - Time complexity is O(m) - Means creating one block.
2. Time Complexity for adding each block is O(1) since we have a tail pointer, hence for adding n blocks, O(n). 
3. Hence total time is O(mn) for creating and adding n blocks
4. For checking integrity, we have to traverse the block chain once hence - O(n)

Space Complexity:
5. SHA-256 is 256-bit - Constant. 
6. Each block stores m characters(maximum) long data, total n blocks - Hence O(mn) is the worst-case space complexity

# Union and Intersection:

Finding all and common elements between two linked lists

Analysis:
1. For union, first we have to traverse the first linked list having n elements. 
2. Then check each element if it is present in the set[O(1) Time Complexity] having elements which are already added.
3. If it is not present, then add it to the set as well as the linked list [O(1) Time Complexity], 
   since we are using a tail pointer for the linked list. 
3. Similar is the procedure for the 2nd linked list having m elements. 
4. Hence total time complexity is O(n+m) = O(n).
5. For intersection, too we have to traverse through both the lists, check in the set and then add accordingly
   - hence time complexity is O(n).
6. Space Complexity for both the operations is O(n+m) = O(n) that is required for storing the sets.
