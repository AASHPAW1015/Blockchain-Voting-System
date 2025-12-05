# 🗳️ Blockchain-Based Voting System

> **A tamper-proof, transparent, and decentralized voting architecture built from scratch.**

---

## 📖 About The Project

This project is a full-stack implementation of a secure electronic voting system. Unlike traditional voting apps that simply update a counter in a database (which can be easily hacked), this system implements a custom **Blockchain** to record every vote.

Each vote is cryptographically hashed and linked to the previous vote, making it **mathematically impossible** to alter past records without breaking the entire chain. It also features a dual-verification system that compares the live database against a local encrypted snapshot to detect any unauthorized database manipulation instantly.

*This was built as a capstone exploration into cryptography, data structures, and database management.*

---

## ⚙️ How It Works (The Architecture)

The system is modularized into three core layers:

### 1. The Interface Layer (Client)
*   **Current State**: CLI-based menu system (separated into `voter_menu` and `moderator_menu`).
*   **Next Gen**: A fully prototyped Qt GUI (see Future Scope) is ready for integration.
*   **Function**: Handles Voter/Moderator authentication securely.

### 2. The Logic Layer (Blockchain Core)
*   **SHA-256 Hashing**: Every vote is converted into a unique 64-character hash.
*   **Chaining**: `Block[n].previous_hash` must match `Block[n-1].hash`.
*   **Immutability**: If someone changes a vote in the database, the hash calculation will fail validation, alerting the moderator immediately via `moderator_tools.py`.

### 3. The Storage Layer (Persistence)
*   **MySQL Database**: Stores the "blocks" and user data permanently.
*   **Local Snapshots (.dat files)**: Uses Python's `pickle` serialization to keep a hidden, local backup of the vote state. The system cross-references this with the DB to detect server-side tampering.

---

## 🚀 Key Features

*   **Secure Authentication**: Hashed credentials for User and Moderator login systems.
*   **Blockchain Integrity**: Custom implementation of Genesis blocks and Chain validation algorithms.
*   **Tamper Detection**: Automated tools that flag invalid blocks and repair the chain if authorized.
*   **Double-Entry Bookkeeping**: Votes are recorded in both the Candidate table (for counting) and the Blockchain table (for auditing).
*   **Anonymity**: Voter IDs are hashed into the transaction data, ensuring privacy.

---

## 🛠️ Installation & Setup

Follow these steps to get the system running on your local machine.

### Prerequisites
*   Python 3.8+
*   MySQL Server 8.0
*   MySQL Workbench (Recommended for setup)

### Step 1: Clone the Repository
```bash
git clone https://github.com/AASHPAW1015/Blockchain-Voting-System.git
cd Blockchain-Voting-System
```

### Step 2: Install Dependencies
You need the MySQL connector for Python.
```bash
pip install mysql-connector-python
```

### Step 3: Database Setup
1.  Open **MySQL Workbench**.
2.  Go to **Server > Data Import**.
3.  Select **Import from Self-Contained File** and choose `blckch_vt_sys.sql` included in this repository.
4.  Click **Start Import**.
5.  *(Optional)* If you want dummy data, import the CSV files located in the `data/` folder using the Table Data Import Wizard.

### Step 4: Configure Credentials
Open `blockchain_main.py`, `vote_recorder.py`, and `main menu.py`. Update the database connection settings to match your local MySQL setup:

```python
# Look for this block in the code:
connection = mysql.connector.connect(
    host="localhost",          # Change to your host IP
    user="root",               # Change to your MySQL username
    password="your_password",  # Change to your MySQL password
    database="login_data"
)
```

### Step 5: Run the System
```bash
python "main menu.py"
```

---

## 📖 User Manual (Terminal Walkthrough)

Once the system is running, follow these workflows to simulate an election.

### 1. Casting a Vote (Voter Flow)
Use this workflow to register a new user and cast a vote that gets added to the blockchain.

```text
> Main Menu:
  1. Voter
  2. Moderator
  3. Show Blockchain
  4. Exit
Enter your choice: 1

> Voter Menu:
  1. Log In
  2. Sign Up
Enter your choice: 2 (If new user)
  > Enter your full name: [Your Name]
  > Enter your age: [18+]
  > Enter your Aadhar: [Valid ID]
  > System generates User ID: 123456 (Save this!)

> Voter Menu:
Enter your choice: 1 (Log In)
  > User ID: 123456
  > Password: [Your Password]
  
> Logged In:
  1. Vote
Enter your choice: 1
  > Select Candidate: [1-5]
  > Success! Block mined and added to chain.
```

### 2. Administering the Election (Moderator Flow)
Use this workflow to validate the integrity of the election and check for hackers.

```text
> Main Menu:
Enter your choice: 2

> Moderator Menu:
Enter your choice: 1 (Log In)
  > User ID: [Mod ID]
  > Password: [Mod Pass]

> Logged In as Moderator:
  1. Validate Blockchain       (Checks all hashes for consistency)
  2. Flag and Fix Invalid      (Removes corrupted blocks)
  3. Check Vote Tampering      (Compares DB vs Local Snapshot)
  4. Stop Server               (Safely closes DB connections)
  5. Show Votes                (Displays current tally)
```

---

## 🛣️ The Development Journey

This project started as a simple script to understand how lists work in Python. Over time, it evolved into a complex system handling data persistence and cryptography.

*   **Phase 1**: Basic CLI to accept inputs.
*   **Phase 2**: Integrated MySQL to stop losing data when the script closed.
*   **Phase 3**: Realized SQL data is mutable (editable), so I implemented a Blockchain Class to secure it.
*   **Phase 4**: Added "Moderator Tools" to automate the validation process using pickle for state snapshots.
*   **Phase 5 (Current)**: Designed the full GUI architecture using Qt Designer.

---

## 🔮 Future Scope: UI Integration

The graphical user interface (GUI) has been fully designed and prototyped using **Qt Designer**. The backend logic is already separated from the frontend to facilitate this transition.

*   **Status**: Prototypes Complete. Ready for Integration.
*   **Files**:
    *   `loginuser.ui` / `signupuser.ui`: Modern authentication screens.
    *   `vote.ui`: Intuitive voting dashboard.
    *   `modtools.ui` / `validate.ui`: Admin control panel for blockchain validation.

---

## 👨‍💻 Maker's Note

> "I built this project to prove that secure voting doesn't need to be complicated—it just needs to be transparent. The hardest part was syncing the local Python objects with the SQL database without breaking the hash chain, but solving that race condition taught me more about backend engineering than any tutorial could. This project represents my first step into full-stack development."

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0** - see the `LICENSE` file for details.
