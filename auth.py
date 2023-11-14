import streamlit as st
import streamlit_authenticator as stauth
import mysql.connector
from views.admin import Admin
from views.operator import Operator
from views.user import User

db_config = {
    "host": "localhost",
    "user": "proj",
    "password": "proj",
    "database": "parking_system",
}

def get_role(username1, name1):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT role FROM parking_system.users WHERE name=%s AND username=%s;", (name1, username1))
        role = cursor.fetchone()

        cursor.close()
        conn.close()

        return role
    except Exception as e:
        print(e)

def get_id(username1, name1):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT userid FROM parking_system.users WHERE name=%s AND username=%s;", (name1, username1))
        id = cursor.fetchone()

        cursor.close()
        conn.close()

        return id
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
            cursor.execute("SELECT name, username, password, role FROM parking_system.users;")
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

    authenticator = stauth.Authenticate(credentials, "cookie", "key", cookie_expiry_days=1)
    name, auth_status, username = authenticator.login("Login", "main")
    #print(name, auth_status, username)
    if auth_status:
        authenticator.logout('Logout', 'sidebar')
        st.success(f"Successfully logged in as {username}")
        role = get_role(username, name)
        if role[0]=="admin":
            id = get_id(name, username)
            Admin.create_page()
        elif role[0]=="operator":
            id = get_id(name, username)
            Operator.create_page(id)
        elif role[0]=="user":
            id = get_id(name, username)
            User.create_page(id)
            
    elif auth_status==False:
        st.error("Invalid username or password")
    else:
        st.error("Please enter username and password")

if __name__ == "__main__":
    authenticate()