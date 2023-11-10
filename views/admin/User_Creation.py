import streamlit as st
import mysql.connector

# SCHEMA FOR USER: name, username, password, role, userid
def create_user(fname, lname, username, password):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        cursor.execute("INSERT INTO parking_system.users (fname, lname, username, password) VALUES (%s,%s,%s,%s);", (fname, lname, username, password))
        conn.commit()

        cursor.close()
        conn.close()

        return True
    except Exception as e:
        st.error(e)
        return False





def create_page():
    st.title("Create User Account")
    # Add input fields for employee details
    with st.form("User Creation"):

        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        username = st.text_input("Username")
        password = st.text_input("Password", type=password)

        account_created = st.form_submit_button("Create Acccount")
        if account_created:
            # Temporary success message
            if first_name == '' or last_name == '' or username == '' or password == '':
                st.error("Please Fill All Fields")
            else:
                success = create_user(first_name, last_name, username, password)
                if success:
                    st.success("Account Created Successfully")
                else:
                    st.error("Account could not be Created")
                #st.success("Account Successfully Created")
        # if st.button("Create Account"):
        #     if first_name and last_name and employee_id:
        #     # Insert employee details into the database
        #         st.success("Employee account created successfully.")




    #cursor.execute("INSERT INTO employees (first_name, last_name, employee_id) VALUES (%s, %s, %s)",(first_name, last_name, employee_id))