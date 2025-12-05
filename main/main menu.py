import vote_recorder
import main_libs_voters
import main_libs_mods
import blockchain_main
import moderator_tools
import mysql.connector
import pickle

def display_license(): 
    print(""" 
BLOCKCHAIN_VOTING_SYSTEM - Copyright (C) 2024 Ashutosh Pawar. This program comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions. [GNU General Public License Version 3, 29 June 2007] For full details, visit: https://www.gnu.org/licenses/gpl-3.0.en.html 
""") 
display_license()

def voter_menu(cursor, connection, blockchain):
    while True:
        print("\nVoter Menu:")
        print("1. Log In")
        print("2. Sign Up")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = main_libs_voters.login_main(cursor)
            if user_id:
                while True:
                    print("\nLogged In as Voter:")
                    print("1. Vote")
                    print("2. Back")

                    logged_in_choice = input("Enter your choice: ")

                    if logged_in_choice == '1':
                        vote_recorder.vote(cursor, connection, user_id, blockchain)
                    elif logged_in_choice == '2':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '2':
            main_libs_voters.signup_main(cursor, connection)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def moderator_menu(cursor, connection, blockchain):
    while True:
        print("\nModerator Menu:")
        print("1. Log In")
        print("2. Back")
        print("WARNING!: If you close the server you can't run other operations, you need to reopen the program..")

        choice = input("Enter your choice: ")

        if choice == '1':
            mod_id = main_libs_mods.login_main_mods(cursor)
            if mod_id:
                while True:
                    print("\nLogged In as Moderator:")
                    print("1. Validate Blockchain")
                    print("2. Flag and Fix Invalid Block")
                    print("3. Check Vote Tampering")
                    print("4. Stop Server")
                    print("5. Show Votes")
                    print("6. Back")

                    mod_choice = input("Enter your choice: ")

                    if mod_choice == '1':
                        moderator_tools.validate_blockchain(cursor)
                    elif mod_choice == '2':
                        moderator_tools.flag_and_fix_block(cursor)
                    elif mod_choice == '3':
                        moderator_tools.check_vote_tampering(cursor)
                    elif mod_choice == '4':
                        moderator_tools.stop_server(cursor, connection)
                    elif mod_choice == '5':
                        moderator_tools.show_votes(cursor)
                    elif mod_choice == '6':
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

# Establishing connection to the database
connection = mysql.connector.connect(
    host="192.168.29.204",
    user="remote_voteruse",
    password="ashu@105",
    database="login_data"
)
cursor = connection.cursor()

# Load blockchain using cursor
blockchain = blockchain_main.initialize_blockchain(cursor, connection)



# Main Menu Loop
while True:
    print("\nMain Menu:")
    print("1. Voter")
    print("2. Moderator")
    print("3. Show Blockchain")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        voter_menu(cursor, connection, blockchain)
    elif choice == '2':
        moderator_menu(cursor, connection, blockchain)
    elif choice == '3':
        cursor.execute("SELECT * FROM blockchain_metadata ORDER BY block_index")
        print("The Blockchain is:")
        blockchain_rows = cursor.fetchall()
        for row in blockchain_rows:
            print(row)
    elif choice == '4':
        print("Exiting...")
        connection.close()
        break
    else:
        print("Invalid choice. Please try again.")

