import streamlit as st

st.title("Add Vehicle")

"The user should be able to add new vehicles to his list of currenlty owned vehicles."

"There should be a form here, which I am making here"

with st.form("Add Vehicle"):
    license_plate_no = st.text_input("Licence Plate Number")
    vehicle_type = st.selectbox("Hello", ["Car","Bike"])
    vehicle_added = st.form_submit_button("Add Vehicle")
    if vehicle_added:
        if license_plate_no == '':
            st.error("Please fill all fields.")
        else:
            st.success("Vehicle Successfully Added")

    
    