import pickle
import mysql.connector

# BLOCKCHAIN_VOTING_SYSTEM - Copyright (C) 2024 Ashutosh Pawar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

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
