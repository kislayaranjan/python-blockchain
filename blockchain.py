import hashlib
import json
from time import time

class Blockchain( object ):
    """
    Skeleton of Blockchain model
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    
        #create genesis block
        self.new_block(previous_hash=1,proof=100) 

    def new_block(self, proof, previous_hash=None):
        """
        Creates a new block and adds it to the chain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous block
        :return: <dict> New block 
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.last_block),
        }

        # reset current list of transactions
        self.current_transactions = []

        # add block to chain
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Adds a new transaction to the list of transactions
        :param sender: <str> Address of sender
        :param recipient: <str> Address of recipient
        :param amount: <float> Amount
        :return: <int> Index of block to which transaction is to be added
        """
        new_trx = {
            'sender':sender,
            'recipient':recipient,
            'amount':amount
        }
        self.current_transactions.append(new_trx)
        return self.last_block['index'] + 1

        @staticmethod
    def hash(block):
        """
        Hashes a block
        """
        pass
    
    @property
    def last_block(self):
        """
        Returns last block in the chain
        """
        return self.chain[-1]