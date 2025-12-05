#Sign-in setup

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

import random
def login_main(c):
    cursor = c
    print("Enter your user id (alphanumeric code provided at signing up)")
    username = input(">")
    print("Enter your password (case sensitive)")
    password = input(">")
    print("finding user....")
    query = "SELECT user_accountno FROM data_main WHERE user_accountno = %s AND user_pass = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("Access Granted")
        return result[0]  # Return the user ID
    else:
        print("Access Denied: Incorrect Username or Password")
        return None  # Return None if login failed


#Sign-up setup
def signup_main(c,con):
    cursor=c
    print("Enter your full name (as written on the aadhar card)")
    name=input('>')
    print("Enter your age (must be more than or equal to 18)")
    age=input('>')
    print("Enter your valid aadhar card number")
    aadharno=input('>')
    print("Enter your state")
    state=input('>')
    print("Your username is....")
    user=random.randrange(100000,999999)
    print(">",user)
    print("Enter your password (the password cannot be changed)")
    passwd=input('>')
    cursor.execute("use login_data")
    query= "insert into data_main (user_name,user_age,user_aadhar,user_state,user_accountno,user_pass) values(%s,%s,%s,%s,%s,%s)"
    cursor.execute(query,(name,age,aadharno,state,user,passwd))
    con.commit()
    
    

