import hashlib
import secrets
import time

class Block:
    def __init__(self, previous_hash):
        self.transactions = []
        self.previous_hash = previous_hash
        self.timestamp = time.time()
        self.nonce = 0
        self.hash = self.compute_hash()

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def compute_hash(self):
        # Compute hash of block header
        block_header = str(self.previous_hash) + str(self.timestamp) + str(self.transactions) + str(self.nonce)
        return hashlib.sha256(block_header.encode()).hexdigest()

    def mine(self, difficulty):
        # Find nonce that satisfies the proof-of-work algorithm
        while self.hash[:difficulty] != '0' * difficulty:
            self.nonce += 1
            self.hash = self.compute_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Create the genesis block (first block in the chain)
        return Block(previous_hash='0')

    def add_block(self, block):
        # Add a new block to the blockchain
        block.previous_hash = self.chain[-1].hash
        block.mine(2)  # Adjust difficulty as needed
        self.chain.append(block)

    def is_valid(self):
        # Validate the entire blockchain
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if current block's hash is valid
            if current_block.hash != current_block.compute_hash():
                return False

            # Check if current block's previous hash matches previous block's hash
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

# Create a blockchain
blockchain = Blockchain()

# Create some sample transactions
transactions = [
    {"sender": "Alice", "recipient": "Bob", "amount": 1},
    {"sender": "Bob", "recipient": "Charlie", "amount": 2},
    {"sender": "Charlie", "recipient": "Alice", "amount": 3},
]

# Add transactions to blocks
for transaction_data in transactions:
    transaction = str(transaction_data)
    block = Block(previous_hash=blockchain.chain[-1].hash)
    block.add_transaction(transaction)
    blockchain.add_block(block)

# Print blockchain
for block in blockchain.chain:
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print("Transactions:", block.transactions)
    print("---------------------------")
