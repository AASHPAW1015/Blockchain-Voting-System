import blockchain_main
import pickle
import mysql.connector

# Function to save the current state of the votes (or other data) before closing the server
def save_data_image(cursor, filename="vote_snapshot.dat"):
    cursor.execute("SELECT * FROM data_main")
    current_votes = cursor.fetchall()

    file = open(filename, 'wb')
    pickle.dump(current_votes, file)
    file.close()

    print("Data image saved successfully.")

# Function to stop the server, including saving the current data state
def stop_server(cursor, connection):
    save_data_image(cursor)
    print("Stopping server...")
    connection.close()
    print("Server stopped and connection closed.")

# Function to validate the blockchain by comparing each block with the database records
def validate_blockchain(cursor):
    blockchain = blockchain_main.load_blockchain(cursor)
    if blockchain is None:
        print("No blockchain found. Initialization might be needed.")
        return
    
    for i in range(1, len(blockchain)):
        current_block = blockchain[i]

        # Recompute the hash and compare
        expected_hash = blockchain_main.calculate_hash(
            current_block['index'],
            current_block['timestamp'],
            current_block['transactions_hash'],
            current_block['previous_hash']
        )

        if current_block['hash'] != expected_hash:
            print(f"Block {i} is invalid.")

            # Retrieve the metadata from the database
            cursor.execute("SELECT * FROM blockchain_metadata WHERE block_index = %s", (current_block['index'],))
            metadata = cursor.fetchone()

            if metadata:
                db_transaction_hash = metadata[2]
                db_block_hash = metadata[4]

                if current_block['transactions_hash'] == db_transaction_hash and current_block['hash'] == db_block_hash:
                    print(f"Block {i} matches the database records.")
                else:
                    print(f"Block {i} does NOT match the database records.")
            else:
                print(f"No metadata found in the database for Block {i}.")

            choice = input("Do you want to delete this block? (yes/no): ")
            if choice.lower() == 'yes':
                return i  # Return the index of the invalid block
    
    print("Blockchain is valid.")
    return None

# Function to flag and fix an invalid block in the blockchain
def flag_and_fix_block(cursor):
    invalid_index = validate_blockchain(cursor)
    
    if invalid_index is not None:
        print(f"Block {invalid_index} is invalid.")
        choice = input("Do you want to delete this block? (yes/no): ")
        if choice.lower() == 'yes':
            blockchain = blockchain_main.load_blockchain()
            blockchain = blockchain[:invalid_index] + blockchain[invalid_index + 1:]
            for i in range(invalid_index, len(blockchain)):
                blockchain[i]['previous_hash'] = blockchain[i - 1]['hash']
                blockchain[i]['hash'] = blockchain_main.calculate_hash(
                    blockchain[i]['index'],
                    blockchain[i]['timestamp'],
                    blockchain[i]['transactions_hash'],
                    blockchain[i]['previous_hash']
                )
            blockchain_main.save_blockchain(blockchain)
            print("Invalid block removed and blockchain updated.")
            cursor.execute("DELETE FROM blockchain_metadata WHERE block_index = %s", (invalid_index,))
            connection.commit()
        else:
            print("No changes made to the blockchain.")
    else:
        print("No invalid blocks found.")

# Function to check for vote tampering by comparing the current votes with a saved snapshot
def check_vote_tampering(cursor):
    try:
        with open('vote_snapshot.dat', 'rb') as file:
            saved_votes = pickle.load(file)
    except FileNotFoundError:
        print("No saved snapshot found.")
        return

    cursor.execute("SELECT * FROM data_main")
    current_votes = cursor.fetchall()

    if saved_votes == current_votes:
        print("No tampering detected.")
    else:
        print("Vote tampering detected!")

    with open('vote_snapshot.dat', 'wb') as file:
        pickle.dump(current_votes, file)

    print("Vote snapshot updated.")

def show_votes(cursor):
    cursor.execute("SELECT * FROM login_data.candidates")
    candidate_data = cursor.fetchall()  # Fetch all rows as tuples
    index = 1
    for candidate in candidate_data:
        print(str(index) + ". " + candidate[0] + " (" + candidate[1] + ") - " + str(candidate[2]) + " votes")
        index += 1












