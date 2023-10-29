import streamlit as st

st.set_page_config(page_title="Vehicle Entry")
st.title("Vehicle Entry")

with st.form("Vehicle Entry"):
    license_plate_no = st.text_input("License Plate Number")
    slot_no = st.text_input("Slot Number")
    enter_vehicle = st.form_submit_button("Enter Vehicle")
    if enter_vehicle:
        # temporary success message: we need to check if the vehicle already exists in the user database
        st.success(f"Vehicle {license_plate_no} Entered Successfully")