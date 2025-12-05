
import hashlib
import json
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({"index": self.index,
                                   "timestamp": str(self.timestamp),
                                   "data": self.data,
                                   "previous_hash": self.previous_hash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

# Simulate voting transactions
voter1_vote = {"voter_id": "123", "candidate": "A"}
voter2_vote = {"voter_id": "456", "candidate": "B"}
voter3_vote = {"voter_id": "789", "candidate": "C"}

# Create blockchain and add voting transactions
blockchain = Blockchain()
blockchain.add_block(Block(1, datetime.datetime.now(), voter1_vote, blockchain.get_latest_block().hash))
blockchain.add_block(Block(2, datetime.datetime.now(), voter2_vote, blockchain.get_latest_block().hash))
blockchain.add_block(Block(3, datetime.datetime.now(), voter3_vote, blockchain.get_latest_block().hash))

# Print blockchain ledger
print("Blockchain Ledger:")
for block in blockchain.chain:
    print("Index:", block.index)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Previous Hash:", block.previous_hash)
    print("Hash:", block.hash)
    print()
