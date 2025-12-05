import random

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

def login_main_mods(c):
    cursor=c
    print("Enter your user id")
    username=input(">")
    print("Enter your password")
    password=input(">")
    print("finding mod....")
    query = "SELECT * FROM mod_logs WHERE User_Id = %s AND pass = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    if result:
        print("Access Granted")
        return True
    else:
        print("Access Denied: Incorrect Username or Password")
