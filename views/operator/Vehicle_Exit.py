import streamlit as st
import mysql.connector
from datetime import datetime

def vehicle_exit(license_plate_no):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        query = "SELECT vehicle_type, entry_time FROM parking_system.parked_vehicles WHERE reg_no=%s;"
        vals = (license_plate_no)
        cursor.execute(query, vals)
        data = cursor.fetchone()
        exit_time = datetime.now()

        duration = exit_time - data[1]

        cursor.execute("SELECT price FROM parking_system.cost_matrix WHERE vehicle_type=%s;",data[0])
        c = cursor.fetchone

        price = duration * c

        conn.commit()
        cursor.close()
        conn.close()

        return [price, data[1], exit_time]
    except Exception as e:
        st.error(e)

def store_ticket(reg_no, cost, entry_time, exit_time):
    #TODO
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        query = "INSERT INTO parking_system.tickets(reg_no, entry_time, exit_time, cost) VALUES(%s,%s,%s,%s);"
        vals = (reg_no, entry_time, exit_time, cost)
        cursor.execute(query, vals)

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        st.error(e)

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
                cost, entry_time, exit_time = vehicle_exit(license_plate_no)
                st.success(f"Payment due for Vehicle {license_plate_no} : {cost}")
                store_ticket(license_plate_no, cost, entry_time, exit_time)