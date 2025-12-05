#Sign-in setup
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
    
    

