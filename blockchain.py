class Blockchain( object ):
    """
    Skeleton of Blockchain model
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []
    def new_block(self):
        """
        Creates a new block and adds it to the chain
        """
        pass
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
        pass