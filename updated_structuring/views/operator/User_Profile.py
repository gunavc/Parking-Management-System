import streamlit as st

def create_page():
    # Set of bools for attribute changes
    name_change = False
    addr_change = False

    # Sample User Profile generated, Have to retreive this from the database
    st.title("User Profile")
    st.divider()
    user_details = {
        "fname":"John",
        "lname":"Doe",
        "emp_no":"PES1UG21CS684",
        "lot_no":"0",
        "addr":"timbuktu"
    }










    # name
    st.header("Name")
    name_val, name_stopgap, name_edit = st.columns(3, gap="large")
    with name_val:
        st.subheader(user_details["fname"]+" "+user_details["lname"])
    with name_edit:
        if st.button(label="Edit Name", key=0):
            name_change = True
        if name_change:
            with name_val:
                new_name = str(st.text_input(
                    label="Enter Your New Name", 
                    value=user_details["fname"] + " " +user_details["lname"],
                    placeholder="First_Name Last_Name"))
                new__name = new_name.split(" ")

    st.divider()

    # emp num (not changable by employee)
    st.header("Employee Number")
    st.subheader(user_details["emp_no"])

    st.divider()

    # lot number (not changable by employee)
    st.header("Lot Number")
    st.subheader(user_details["lot_no"])

    st.divider()

    # address
    st.header("Address")
    addr_val, addr_stopgap, addr_edit = st.columns(3, gap="large")
    with addr_val:
        st.subheader(user_details["addr"])
    
    with addr_edit:
        if st.button(label="Edit Address", key=1):
            addr_change = True
        if addr_change:
            with addr_val:
                new_addr = str(st.text_input(
                    label="Enter Your New Address", 
                    value=user_details["addr"],
                    placeholder="Street, Locality, City, Pincode"))
        