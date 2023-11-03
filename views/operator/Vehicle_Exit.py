import streamlit as st

def create_page():
    st.title("Vehicle Exit")

    with st.form("Vehicle Exit"):
        license_plate_no = st.text_input("License Plate Number")
        # Find vehicle from database and then exit it, and make the slot empty
        exit_vehicle = st.form_submit_button("Exit Vehicle")

        if exit_vehicle:
            if license_plate_no == '':
                st.error("Please Enter License Plate Number!")
            else:
                # temporary success message
                st.success(f"Vehicle {license_plate_no} Exited Successfully")


