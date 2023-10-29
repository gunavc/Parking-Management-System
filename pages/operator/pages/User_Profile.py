import streamlit as st

st.set_page_config(page_title="User Profile")

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
st.subheader("Name")
st.write(user_details["fname"]+" "+user_details["lname"])
if st.button(label="✏️", key=0):
    name_change = True
if name_change:
    new_name = str(st.text_input(
        label="Enter Your New Name", 
        value=user_details["fname"] + " " +user_details["lname"],
        placeholder="First_Name Last_Name"))
    new__name = new_name.split(" ")

st.divider()

# emp num (not changable by employee)
st.subheader("Employee Number")
st.write(user_details["emp_no"])

st.divider()

# lot number (not changable by employee)
st.subheader("Lot Number")
st.write(user_details["lot_no"])

st.divider()

# address
st.subheader("Address")
st.write(user_details["addr"])
if st.button(label="✏️", key=1):
    addr_change = True
if addr_change:
    new_addr = str(st.text_input(
        label="Enter Your New Address", 
        value=user_details["addr"],
        placeholder="Street, Locality, City, Pincode"))
    