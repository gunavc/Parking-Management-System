import streamlit as st
import mysql.connector

def vehicle_entry(license_plate_no, vehicle_type, slot_no):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        query = "INSERT INTO parking_system.parked_vehicles (reg_no, vehicle_type, entry_time, lot_no) VALUES (%s, %s, curdate(), %s);"
        vals = (license_plate_no, vehicle_type, slot_no)
        cursor.execute(query, vals)

        conn.commit()
        cursor.close()
        conn.close()

        return True

    except Exception as e:
        st.error(e)
        return False

def create_page():
    st.title("Vehicle Entry")

    with st.form("Vehicle Entry"):
        license_plate_no = st.text_input("License Plate Number")
        vehicle_type = st.text_input("Vehicle Type")
        slot_no = st.text_input("Slot Number")
        enter_vehicle = st.form_submit_button("Enter Vehicle")
        if enter_vehicle:
            if license_plate_no == '' or slot_no == '' or vehicle_type == '':
                st.error(f"Please Enter All Fields!")
            else:
                success = vehicle_entry(license_plate_no, vehicle_type, slot_no)
                if success:
                    st.success("Vehicle Successfully Entered")
                else:
                    st.error("Error adding the vehicle")
