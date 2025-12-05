import pickle
import mysql.connector

def save_blockchain_to_db():
    # Load the blockchain from the .dat file
    try:
        file = open('blockchain.dat', 'rb')
        blockchain = pickle.load(file)
        file.close()
    except FileNotFoundError:
        print("No blockchain.dat file found.")
        return
    
    # Connect to the database
    connection = mysql.connector.connect(
        host="192.168.29.204",
        user="remote_voteruse",
        password="ashu@105",
        database="login_data"
    )
    cursor = connection.cursor()

    # Insert the blockchain into the database
    cursor.execute("DELETE FROM blockchain_metadata")  # Clear existing records

    for block in blockchain:
        cursor.execute("""
            INSERT INTO blockchain_metadata (block_index, timestamp, transaction_hash, previous_hash, block_hash)
            VALUES (%s, %s, %s, %s, %s)
        """, (block['index'], int(block['timestamp']), block['transactions_hash'], block['previous_hash'], block['hash']))

    connection.commit()
    print("Blockchain saved to database successfully.")
    connection.close()

save_blockchain_to_db()
