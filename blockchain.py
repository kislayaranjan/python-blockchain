import hashlib
import json
from time import time
from textwrap import dedent
from uuid import uuid4
from flask import Flask

class Blockchain( object ):
    """
    Skeleton of Blockchain model
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.difficulty = 4

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
        Creates a SHA-256 of a block
        :param block: <dict> block
        :return: <str> hash of block
        """
        # Sort by keys to avoid hashing inconsistencies
        block_string = json.dumps(block, sort_keys=True)
        # encode from utf-8 -> bytes
        block_string = block_string.encode()
        # hash the block byte string
        hash_digest = hashlib.sha256(block_string).hexdigest()
        return hash_digest
    
    @property
    def last_block(self):
        """
        Returns last block in the chain
        """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Proof of Work Algorithm:
        -   Find x such that hash(xx') has self.difficulty leading zeros
        -   x is new_proof and x' is last_proof
        :param last_proof: <int>
        :return: <int> proof
        """

        proof = 0

        while self.valid_proof(last_proof,proof) is False:
            proof += 1
        
        return proof
    
    @staticmethod
    def valid_proof(self,last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        prefix = "0" * self.difficulty
        return guess[:self.difficulty] == prefix

# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"
  
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)