import streamlit as st

def create_page():
    st.title("Add Vehicle")
    
    st.write(
    "The user should be able to add new vehicles to his list of currenlty owned vehicles."

    "There should be a form here, which I am making here"
    )

    with st.form("Add Vehicle"):
        license_plate_no = st.text_input("Licence Plate Number")
        vehicle_type = st.selectbox("Vehicle Type", ["Car","Bike"])
        vehicle_added = st.form_submit_button("Add Vehicle")
        if vehicle_added:
            if license_plate_no == '':
                st.error("Please fill all fields.")
            else:
                st.success(f"{vehicle_type} with Plate, {license_plate_no} Successfully Added")

        
        