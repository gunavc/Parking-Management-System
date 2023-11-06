import streamlit as st

def add_vehicle(reg_no, vehicle_type, id):
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

def create_page(id):
    st.title("Add Vehicle")
    
    # st.write(
    # "The user should be able to add new vehicles to his list of currenlty owned vehicles."

    # "There should be a form here, which I am making here"
    # )

    with st.form("Add Vehicle"):
        license_plate_no = st.text_input("Licence Plate Number")
        vehicle_type = st.selectbox("Vehicle Type", ["Car","Bike"])
        vehicle_added = st.form_submit_button("Add Vehicle")
        if vehicle_added:
            if license_plate_no == '':
                st.error("Please fill all fields.")
            else:
                st.success(f"{vehicle_type} with Plate, {license_plate_no} Successfully Added")

        
        