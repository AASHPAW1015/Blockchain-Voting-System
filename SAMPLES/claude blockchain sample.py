import hashlib
import time
import random

class Block:
    def __init__(self, index, votes, timestamp, previous_hash):
        self.index = index
        self.votes = votes
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.votes}{self.timestamp}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2
        self.pending_votes = []
        self.voters = set()

    def create_genesis_block(self):
        return Block(0, [], int(time.time()), "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_votes(self):
        if not self.pending_votes:
            return False

        block = Block(len(self.chain), self.pending_votes, int(time.time()), self.get_latest_block().hash)
        block.mine_block(self.difficulty)

        self.chain.append(block)
        self.pending_votes = []
        return True

    def cast_vote(self, voter, candidate):
        if voter in self.voters:
            print(f"{voter} has already voted!")
            return False
        self.pending_votes.append({
            "voter": voter,
            "candidate": candidate
        })
        self.voters.add(voter)
        return True

    def get_vote_count(self, candidate):
        votes = 0
        for block in self.chain:
            for vote in block.votes:
                if vote["candidate"] == candidate:
                    votes += 1
        return votes

def main():
    voting_system = Blockchain()
    candidates = ["Candidate A", "Candidate B", "Candidate C"]
    voters = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Henry", "Ivy", "Jack"]
    
    print("Starting the voting process...")
    print(f"Genesis block hash: {voting_system.get_latest_block().hash}")
    
    for voter in voters:
        candidate = random.choice(candidates)
        if voting_system.cast_vote(voter, candidate):
            print(f"{voter} voted for {candidate}")
        
        # Mine a block after every 3 votes
        if len(voting_system.pending_votes) >= 3:
            print("\nMining a new block...")
            voting_system.mine_pending_votes()
            print(f"Block mined! Hash: {voting_system.get_latest_block().hash}\n")
            print("Current vote counts:")
            for candidate in candidates:
                print(f"{candidate}: {voting_system.get_vote_count(candidate)}")
            print(f"Latest block hash: {voting_system.get_latest_block().hash}")
            print()

    # Mine any remaining votes
    if voting_system.pending_votes:
        print("\nMining final block...")
        voting_system.mine_pending_votes()
        print(f"Final block mined! Hash: {voting_system.get_latest_block().hash}\n")

    print("Final vote counts:")
    for candidate in candidates:
        print(f"{candidate}: {voting_system.get_vote_count(candidate)}")

    print(f"\nTotal blocks in the blockchain: {len(voting_system.chain)}")
    print("\nBlock hashes in the blockchain:")
    for block in voting_system.chain:
        print(f"Block {block.index}: {block.hash}")

if __name__ == "__main__":
    main()
