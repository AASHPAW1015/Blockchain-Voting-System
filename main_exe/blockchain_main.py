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
    timestamp = int(time.time())  # Use integer for timestamp (Unix time)
    transactions_hash = hash_transaction(transaction)  # Hash the transactions for privacy
    block_hash = calculate_hash(index, timestamp, transactions_hash, previous_hash)
    
    block = {
        'index': index,
        'timestamp': timestamp,  # Save as integer
        'transactions_hash': transactions_hash,
        'previous_hash': previous_hash,
        'hash': block_hash
    }
    return block

# Function to create the genesis block
def create_genesis_block():
    return create_block(0, "Genesis Block", "0")

# Function to add a new block to the blockchain and save it to the database
def add_block(blockchain, transaction, connection, cursor):
    if blockchain is None:  # Double-check to ensure blockchain is initialized
        blockchain = (create_genesis_block(),)

    previous_block = blockchain[-1]  # Gets the last block in the blockchain
    index = previous_block['index'] + 1
    previous_hash = previous_block['hash']
    new_block = create_block(index, transaction, previous_hash)

    # Save the new block to the database
    cursor.execute("""
        INSERT INTO blockchain_metadata (block_index, timestamp, transaction_hash, previous_hash, block_hash)
        VALUES (%s, %s, %s, %s, %s)
    """, (new_block['index'], int(new_block['timestamp']), new_block['transactions_hash'], new_block['previous_hash'], new_block['hash']))

    connection.commit()

    # Return the updated blockchain tuple
    return blockchain + (new_block,)



def load_blockchain(cursor):
    try:
        cursor.execute("SELECT * FROM blockchain_metadata ORDER BY block_index")
        rows = cursor.fetchall()

        blockchain = []
        for row in rows:
            block = {
                'index': row[0],
                'timestamp': row[1],
                'transactions_hash': row[2],
                'previous_hash': row[3],
                'hash': row[4]
            }
            blockchain.append(block)

        if blockchain:
            return tuple(blockchain)  # Return the blockchain if it's not empty
        else:
            return None  # Return None if there are no blocks in the database
    except Exception as e:
        print("Error loading blockchain:", e)
        return None

def initialize_blockchain(cursor, connection):
    # Load blockchain, if empty, create the genesis block
    blockchain = load_blockchain(cursor)
    if blockchain is None:
        blockchain = (create_genesis_block(),)
        cursor.execute("""
            INSERT INTO blockchain_metadata (block_index, timestamp, transaction_hash, previous_hash, block_hash)
            VALUES (%s, %s, %s, %s, %s)
        """, (blockchain[0]['index'], int(blockchain[0]['timestamp']), blockchain[0]['transactions_hash'], blockchain[0]['previous_hash'], blockchain[0]['hash']))
        connection.commit()
    return blockchain





