# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 04:56:16 2020

@author: JAGRUTI
"""

import hashlib

# defining the Block class
class Block:
    
    # initiliazing the Block object 
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
        
    # calculate hash value for the data
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
# defining the Blockchain class
class Blockchain:
    
    # initializing it with two pointers head and tail, tail is maintained for O(1) addition of a new block
    def __init__(self):
        self.blockhead = None
        self.blocktail = None
        
    # add a new block
    def add_block(self, timestamp, data):
        
        if timestamp == None or timestamp == "":
            print("Please enter timestamp")
            return
        if data == None or data == "":
            print("Please enter data")
            return
        
        # if it is the first block, set the head and tail to the new block
        if self.blockhead is None:
            newBlock = Block(timestamp, data, 0)
            self.blockhead = newBlock
            self.blocktail = self.blockhead
            
        # add the new block to the tail and set tail to the new block
        else:
            newBlock = Block(timestamp, data, self.blocktail.hash)
            self.blocktail.next = newBlock
            self.blocktail = self.blocktail.next
         
    # for printing the blockchain
    def __str__(self):
       
        current_block = self.blockhead
        s = ""
        i = 0
        while(current_block):
            s += "Block:" + str(i) +"\n" + "Timestamp:" + str(current_block.timestamp) + "\n" + "Data:" + str(current_block.data) + "\n" + "SHA256 Hash:" + str(current_block.hash) + "\n" + "Previous Hash:" + str(current_block.previous_hash)
            s += "\n----------------------------------------------------------------------------------------\n"
            current_block = current_block.next
            i += 1
            if i>9:
                break
        if s == "":
            s = "Sorry no blocks"
            
        return s
    
    # for checking if the blocks are properly linked meaning matching hash value of one node 
    # with the previous hash value of the next node
    def check(self):
        # setting the integrity to True 
        integrity = True
        current_block = self.blockhead
        
        # if blockchain exists
        if current_block:
            
            while(current_block.next):
                
                # incase it doesn't match, set integrity to False and break from the loop
                if current_block.next.previous_hash != current_block.hash:
                    integrity = False
                    break
                    
                current_block = current_block.next
            return integrity
        # if blockchain doesn't exist
        else:
            return None

## Test Cases

## Example 1
            
blockchain = Blockchain()
blockchain.add_block("17:00 25-12-2020", "Hello!")
blockchain.add_block("17:01 25-12-2020", "How are you?")
blockchain.add_block("17:02 25-12-2020", "I am fine.")
if blockchain.check():
    print("Blockchain successfully done")
else:
    print("Blockchain not properly implemented")
print(blockchain)

"""
Blockchain successfully done
Block:0
Timestamp:17:00 25-12-2020
Data:Hello!
SHA256 Hash:334d016f755cd6dc58c53a86e183882f8ec14f52fb05345887c8a5edd42c87b7
Previous Hash:0
----------------------------------------------------------------------------------------
Block:1
Timestamp:17:01 25-12-2020
Data:How are you?
SHA256 Hash:df287dfc1406ed2b692e1c2c783bb5cec97eac53151ee1d9810397aa0afa0d89
Previous Hash:334d016f755cd6dc58c53a86e183882f8ec14f52fb05345887c8a5edd42c87b7
----------------------------------------------------------------------------------------
Block:2
Timestamp:17:02 25-12-2020
Data:I am fine.
SHA256 Hash:790516f5ec4778f045cfaf7531205321bc98d7ada497a9a5503994ffc748a74f
Previous Hash:df287dfc1406ed2b692e1c2c783bb5cec97eac53151ee1d9810397aa0afa0d89
----------------------------------------------------------------------------------------
"""

## Example 2

blockchain = Blockchain()
blockchain.add_block("", "")
blockchain.add_block("", "How are you?")
blockchain.add_block("17:02 25-12-2020", "")
if blockchain.check():
    print("Blockchain successfully done")
else:
    print("Blockchain not properly implemented")
print(blockchain)
"""
Please enter timestamp
Please enter timestamp
Please enter data
Blockchain not properly implemented
Sorry no blocks
"""

## Example 3

dates = ["25-12-2020"]
hours = [h for h in range(0,2)]
minutes = [i for i in range(0,60)]
datetime = []
for date in dates:
    for hour in hours:
        for minute in minutes:
            if hour>=0 and hour<=9:
                hour_string = "0" + str(hour)
            else:
                hour_string = str(hour)
            if minute>=0 and minute<=9:
                minute_string = "0" + str(minute)
            else:
                minute_string = str(minute)
            time = hour_string + ":" + minute_string + " " + date
            datetime.append(time)

data = "Often, the body paragraph demonstrates and develops your topic sentence through an ordered, logical progression of ideas. There are a number of useful techniques for expanding on topic sentences and developing your ideas in a paragraph. Illustration in a paragraph supports a general statement by means of examples, details, or relevant quotations (with your comments)."
length = min(len(datetime), len(data))
blockchain = Blockchain()
for i in range(length):
    blockchain.add_block(datetime[i], data[i])
if blockchain.check():
    print("Blockchain successfully done")
else:
    print("Blockchain not properly implemented")
print(blockchain)


## Results shown only for the first 10 blocks

"""
Blockchain successfully done
Block:0
Timestamp:00:00 25-12-2020
Data:O
SHA256 Hash:c4694f2e93d5c4e7d51f9c5deb75e6cc8be5e1114178c6a45b6fc2c566a0aa8c
Previous Hash:0
----------------------------------------------------------------------------------------
Block:1
Timestamp:00:01 25-12-2020
Data:f
SHA256 Hash:252f10c83610ebca1a059c0bae8255eba2f95be4d1d7bcfa89d7248a82d9f111
Previous Hash:c4694f2e93d5c4e7d51f9c5deb75e6cc8be5e1114178c6a45b6fc2c566a0aa8c
----------------------------------------------------------------------------------------
Block:2
Timestamp:00:02 25-12-2020
Data:t
SHA256 Hash:e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8
Previous Hash:252f10c83610ebca1a059c0bae8255eba2f95be4d1d7bcfa89d7248a82d9f111
----------------------------------------------------------------------------------------
Block:3
Timestamp:00:03 25-12-2020
Data:e
SHA256 Hash:3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea
Previous Hash:e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8
----------------------------------------------------------------------------------------
Block:4
Timestamp:00:04 25-12-2020
Data:n
SHA256 Hash:1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9
Previous Hash:3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea
----------------------------------------------------------------------------------------
Block:5
Timestamp:00:05 25-12-2020
Data:,
SHA256 Hash:d03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7
Previous Hash:1b16b1df538ba12dc3f97edbb85caa7050d46c148134290feba80f8236c83db9
----------------------------------------------------------------------------------------
Block:6
Timestamp:00:06 25-12-2020
Data: 
SHA256 Hash:36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068
Previous Hash:d03502c43d74a30b936740a9517dc4ea2b2ad7168caa0a774cefe793ce0b33e7
----------------------------------------------------------------------------------------
Block:7
Timestamp:00:07 25-12-2020
Data:t
SHA256 Hash:e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8
Previous Hash:36a9e7f1c95b82ffb99743e0c5c4ce95d83c9a430aac59f84ef3cbfab6145068
----------------------------------------------------------------------------------------
Block:8
Timestamp:00:08 25-12-2020
Data:h
SHA256 Hash:aaa9402664f1a41f40ebbc52c9993eb66aeb366602958fdfaa283b71e64db123
Previous Hash:e3b98a4da31a127d4bde6e43033f66ba274cab0eb7eb1c70ec41402bf6273dd8
----------------------------------------------------------------------------------------
Block:9
Timestamp:00:09 25-12-2020
Data:e
SHA256 Hash:3f79bb7b435b05321651daefd374cdc681dc06faa65e374e38337b88ca046dea
Previous Hash:aaa9402664f1a41f40ebbc52c9993eb66aeb366602958fdfaa283b71e64db123
----------------------------------------------------------------------------------------

"""
