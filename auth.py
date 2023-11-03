import streamlit as st
import streamlit_authenticator as stauth
import mysql.connector

db_config = {
    "host": "localhost",
    "user": "proj",
    "password": "proj",
    "database": "parking_system",
}

def get_role(username, name):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()
        cursor.execute(f"SELECT role FROM parking_system.users WHERE name={name} AND username={username};")
        role = cursor.fetchone()

        return role
    except Exception as e:
        print(e)

def get_creds():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system")

        try:
            cursor = conn.cursor()
            cursor.execute("USE parking_system;")
            cursor.execute(f"SELECT name, username, password, role FROM parking_system.users;")
        except Exception as e:
            print(e)
        users = cursor.fetchall()
        cursor.close()
        conn.close()

        return users
    except Exception as e:
        st.error("User Not Present in the directory")

def authenticate():
    users = get_creds()
    usernames = []
    passwords = []
    roles = []
    names = []

    for name, username, password, role in users:
        names.append(name)
        usernames.append(username)
        passwords.append(password)
        roles.append(role)

    credentials = {"usernames":{}}

    for un, name, pw in zip(usernames, names, passwords):
        user_dict = {"name":name,"password":pw}
        credentials["usernames"].update({un:user_dict})
    print(credentials)
    authenticator = stauth.Authenticate(credentials, "cookie", "key", cookie_expiry_days=1)
    name, auth_status, username = authenticator.login("Login", "main")
    
    if auth_status:
        authenticator.logout('Logout', 'sidebar')
        st.success(f"Successfully logged in as {username}")
        role = get_role(username, name)
        if role=="admin":
            #TODO
            pass
        elif role=="operator":
            #TODO
            pass
    elif auth_status==False:
        st.error("Invalid username or password")
    else:
        st.error("Please enter username and password")

if __name__ == "__main__":
    authenticate()