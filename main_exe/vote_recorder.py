import mysql.connector
import blockchain_main
from mysql.connector import Error



def fetch_candidate_names(cursor):
    query = "SELECT name_cand, house_party FROM candidates"
    cursor.execute(query)
    results = cursor.fetchall()
    
    if results:
        candidates = []
        for row in results:
            candidates.append({'name': row[0], 'party': row[1]})
        return candidates
    else:
        print("No candidates found.")
        return []

def can_vote(cursor, user_id):
    # Check if the user has votes left
    query = "SELECT VoteCn FROM data_main WHERE user_accountno = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    
    if result is None:
        print("Error: User not found.")
        return False
    
    vote_count = result[0]
    if vote_count is None or vote_count == 0:
        print("You have no votes left.")
        return False
    
    return True

def vote(cursor, connection, user_id, blockchain):  # Pass blockchain as a parameter
    if not can_vote(cursor, user_id):
        return  # Exit if the user cannot vote
    
    candidates = fetch_candidate_names(cursor)
    
    if not candidates:
        print("No candidates available to vote for.")
        return

    print("Please select the candidate number to vote for:")
    for index in range(len(candidates)):
        print(str(index + 1) + ". " + candidates[index]['name'] + " (" + candidates[index]['party'] + ")")

    choice = int(input("Enter your choice: "))

    if choice < 1 or choice > len(candidates):
        print("Invalid choice. Please try again.")
        return

    selected_candidate = candidates[choice - 1]['name']
    
    # Create a string representation of the transaction using concatenation
    transaction = "User " + str(user_id) + " voted for " + selected_candidate

    # Add block to the blockchain
    blockchain = blockchain_main.add_block(blockchain, transaction, connection, cursor)

    # Deduct a vote after voting
    cursor.execute("UPDATE data_main SET VoteCn = VoteCn - 1 WHERE user_accountno = %s", (user_id,))
    cursor.execute("UPDATE candidates SET votes = votes + 1 WHERE name_cand = %s", (selected_candidate,))
    connection.commit()

    print("\nBlockchain Updated:")
    print(blockchain[-1])




