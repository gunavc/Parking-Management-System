import streamlit as st
import mysql.connector

def show_parked_vehicles():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM parking_system.parked_vehicles")
        data = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()

        return data

    except Exception as e:
        st.error(e)

def create_page():
    st.title("All Parked Cars")

    vehicles = show_parked_vehicles()
    if len(vehicles)!=0:
        for car_data in vehicles:
            st.write(f"Registration Number : {car_data[0]}")
            st.write(f"Vehicle Type : {car_data[1]}")
            st.write(f"Entry Time : {car_data[2]}")
            st.write(f"Lot Number : {car_data[3]}")
    else:
        st.error("There are currently no cars parked")

