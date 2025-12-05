import hashlib
import time

# Function to calculate the hash of a block
def calculate_hash(index, timestamp, transactions_hash, previous_hash):
    block_string = str(index) + str(timestamp) + str(transactions_hash) + str(previous_hash)
    return hashlib.sha256(block_string.encode()).hexdigest()  # Creates a SHA-256 hash

# Function to hash transaction data
def hash_transaction(transaction):
    return hashlib.sha256(transaction.encode()).hexdigest()  # To keep the privacy of a voter

# Function to create a new block
def create_block(index, transaction, previous_hash):
    timestamp = time.time()
    transactions_hash = hash_transaction(transaction)  # Hashes the transactions for privacy
    block_hash = calculate_hash(index, timestamp, transactions_hash, previous_hash)
    
    block = {'index': index,'timestamp': timestamp,'transactions_hash': transactions_hash,'previous_hash': previous_hash,'hash': block_hash}
    return block

# Function to create the genesis block
def create_genesis_block():
    return create_block(0, "Genesis Block", "0")

# Function to add a new block to the blockchain
def add_block(blockchain, transaction):
    previous_block = blockchain[-1]  # Gets the last block in the blockchain
    index = previous_block['index'] + 1
    previous_hash = previous_block['hash']
    new_block = create_block(index, transaction, previous_hash)
    return blockchain + (new_block,)  # Adds it in the form of a tuple


