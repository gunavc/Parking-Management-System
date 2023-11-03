import streamlit as st

def create_page():
    st.title("Vehicle Entry")

    with st.form("Vehicle Entry"):
        license_plate_no = st.text_input("License Plate Number")
        slot_no = st.text_input("Slot Number")
        enter_vehicle = st.form_submit_button("Enter Vehicle")
        if enter_vehicle:
            if license_plate_no == '' or slot_no == '':
                st.error(f"Please Enter All Fields!")
            else:
                # temporary success message: we need to check if the vehicle already exists in the user database
                st.success(f"Vehicle {license_plate_no} Entered Successfully into {slot_no}")