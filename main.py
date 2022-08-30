#Create a blockchain class
#Write a function to create your first block
#Write a function(s) to create a blockchain
#Write a function to transact and get the previous block
#Write a function to hash the block
#write a function to send money

#import required libraries

import hashlib
import json
from time import time


#create the blockchain class
class Block_chain(object):
    def __init__(self):
        self.chain = []
        self.pendingTransactions = []

        self.newBlock(previousHash="Life is a mirror.",
                      the_proof=100)

    # Creating a new block listing key/value pairs of
    # block information in a JSON object.
    # Reset the list of pending transactions &
    # append the newest block to the chain.
    def newBlock(self, the_proof, previousHash=None):
        the_block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.pendingTransactions,
            'proof': the_proof,
            'previous_hash': previousHash or self.hash(self.chain[-1]),
        }
        self.pendingTransactions = []
        self.chain.append(the_block)

        return the_block

    # Searching the blockchain for the most recent block.
    @property
    def lastBlock(self):
        return self.chain[-1]

    # Adding a transaction with relevant info to the 'blockpool' - list of pending tx's.
    def newTransaction(self, the_sender, the_recipient, the_amount):
        the_transaction = {
            'sender': the_sender,
            'recipient': the_recipient,
            'amount': the_amount
        }
        self.pendingTransactions.append(the_transaction)
        return self.lastBlock['index'] + 1

    # receiving one block. Turning it into a string, turning that into
    # Unicode (for hashing). Hashing with SHA256 encryption,
    # then translating the Unicode into a hexidecimal string.
    def hash(self, the_block):
        stringObject = json.dumps(the_block, sort_keys=True)
        blockString = stringObject.encode()

        rawHash = hashlib.sha256(blockString)
        hexHash = rawHash.hexdigest()

        return hexHash


block_chain = Block_chain()
transaction1 = block_chain.newTransaction("Luke", "Peter", '10 BTC')
transaction2 = block_chain.newTransaction("John", "Paul", '2 BTC')
transaction3 = block_chain.newTransaction("Matthew", "James", '10 BTC')
block_chain.newBlock(10222)

transaction4 = block_chain.newTransaction("Ruth", "Lucy", '2 BTC')
transaction5 = block_chain.newTransaction("Tiffany", "Elizabeth", '1 BTC')
transaction6 = block_chain.newTransaction("Aquila", "Marcus", '1 BTC')
block_chain.newBlock(10976)

print("Genesis block: ", block_chain.chain)
