import streamlit as st
import mysql.connector

def get_name(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM parking_system.employees WHERE empid=%s", (id))
        data = cursor.fetchone()

        conn.commit()
        cursor.close()
        conn.close()

        return data
    except Exception as e:
        st.error(e)

def update_name(fname, lname, id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE employees SET fname=%s WHERE empid=%s", (fname, id))
        cursor.execute("UPDATE employees SET lname=%s WHERE empid=%s", (lname, id))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(e)

def update_address(addr, id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()
        cursor.execute("UPDATE employees SET address=%s WHERE empid=%s", (addr, id))

        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        st.error(e)


def create_page(id):
    # Set of bools for attribute changes
    name_change = False
    addr_change = False

    # Sample User Profile generated, Have to retreive this from the database
    st.title("User Profile")
    st.divider()
    user_details = get_name(id)

    # name
    st.header("Name")
    name_val, name_stopgap, name_edit = st.columns(3, gap="large")
    with name_val:
        st.subheader(user_details[0]+" "+user_details[1])
    with name_edit:
        if st.button(label="Edit Name", key=0):
            name_change = True
        if name_change:
            with name_val:
                new_name = str(st.text_input(
                    label="Enter Your New Name", 
                    value=user_details[0] + " " +user_details[1],
                    placeholder="First_Name Last_Name"))
                new__name = new_name.split(" ")
                update_name(new_name[0], new_name[1], id)

    st.divider()

    # role (not changable by employee)
    st.header("Role")
    st.subheader(user_details[3])

    st.divider()

    # emp num (not changable by employee)
    st.header("Employee Number")
    st.subheader(user_details[2])

    st.divider()

    # lot number (not changable by employee)
    st.header("Lot Number")
    st.subheader(user_details[4])

    # st.divider()

    # address
    st.header("Address")
    addr_val, addr_stopgap, addr_edit = st.columns(3, gap="large")
    with addr_val:
        st.subheader(user_details[5])
    
    with addr_edit:
        if st.button(label="Edit Address", key=1):
            addr_change = True
        if addr_change:
            with addr_val:
                new_addr = str(st.text_input(
                    label="Enter Your New Address", 
                    value=user_details[5],
                    placeholder="Street, Locality, City, Pincode"))
                update_address(new_addr, id)