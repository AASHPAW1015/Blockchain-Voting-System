import random
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
