import streamlit as st
import mysql.connector

def create_emp(fname, lname, empid, role, lnum):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        cursor.execute("INSERT INTO parking_system.employees (fname, lname, empid, role, lot_no) VALUES (%s,%s,%s,%s,%s);", (fname, lname, empid, role, lnum))
        conn.commit()

        cursor.close()
        conn.close()

        return True
    except Exception as e:
        st.error(e)
        return False

def create_page():
    st.title("Create Employee Account")
    # Add input fields for employee details
    with st.form("Employee Creation"):
        lot_no = ''
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        employee_id = st.text_input("Employee ID")
        role = st.text_input("Role")
        lot_no = st.text_input("Lot Number")

        account_created = st.form_submit_button("Create Acccount")
        if account_created:
            # Temporary success message
            if first_name == '' or last_name == '' or employee_id == '' or role == '':
                st.error("Please Fill All Fields")
            else:
                success = create_emp(first_name, last_name, employee_id, role, lot_no)
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