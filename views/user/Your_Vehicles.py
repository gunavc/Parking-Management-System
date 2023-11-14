import streamlit as st
import mysql.connector

def parked_vehicles(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        query = "SELECT reg_no, vehicle_type FROM parking_system.vehicles WHERE driver_id=%s and isparked=1;"
        cursor.execute(query, (id, ))
        p_vehicles = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()
        return p_vehicles
    except Exception as e:
        st.error(e)


def notparked_vehicles(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        query = "SELECT reg_no, vehicle_type FROM parking_system.vehicles WHERE driver_id=%s and isparked=0;"
        cursor.execute(query, (id, ))
        np_vehicles = cursor.fetchall()

        conn.commit()
        cursor.close()
        conn.close()
        return np_vehicles
    except Exception as e:
        st.error(e)

def create_page(id):
    st.title("Your Vehicles")

    # st.write(
    # """
    # There is to be two sections: 
    # 1. A section having vehicles currently parked in the campus
    # 2. A section having all other vehicles

    # The user must also have the ability to make edits to the details of their vehicles.
    # This should be done by means of a data editor
    # dataframe can be loaded as a data_editor, and then saved back as the dataframe, and the dataframe gets loaded into the sql database
    # """
    # )

    # st.write(
    # """
    # Here the vehicles which are currently parked 
    # """
    # )
    p_vehicles = parked_vehicles(id)
    np_vehicles = notparked_vehicles(id)

    if len(p_vehicles)==0 and len(np_vehicles)==0:
        st.error("You have no vehicles currently registered")
    else:
        st.header("Currently Parked")
        if len(p_vehicles)!=0:
            for car_data in p_vehicles:
                st.write(f"Registration Number : {car_data[0]}")
                st.write(f"Vehicle Type : {car_data[1]}")
        else:
            st.error("None of your vehicles are parked")

        st.divider()

        st.header("Unparked Vehicles")
        if len(np_vehicles)!=0:
            for car_data in np_vehicles:
                st.write(f"Registration Number : {car_data[0]}")
                st.write(f"Vehicle Type : {car_data[1]}")
        else:
            st.error("All of your vehicles are parked")
