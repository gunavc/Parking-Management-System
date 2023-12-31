import streamlit as st
import mysql.connector
import pandas as pd 

def get_vehicles(id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT reg_no, vehicle_type FROM parking_system.vehicles WHERE driver_id=%s;",(id, ))

        df = pd.DataFrame(cursor.fetchall(), columns=["Registration Number", "Vehicle Type"])
        df["Mark to Delete"] = False
        conn.commit()
        cursor.close()
        conn.close()

        return df
    except Exception as e:
        st.error(e)

def update_vehicles(df):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        for index, row in df.iterrows():
            if row["Mark to Delete"]==False:
                query = "UPDATE parking_system.vehicles SET vehicle_type=%s, WHERE reg_no=%s;"
                vals = (row["Vehicle Type"], row["Registration Number"])
                cursor.execute(query, vals)
            elif row["Mark to Delete"]==True:
                query = "DELETE FROM parking_system.vehicles WHERE reg_no=%s;"
                vals = (row["Registration Number"], )
                cursor.execute(query, vals)

        conn.commit()
        cursor.close()
        conn.close()

        return True
    except Exception as e:
        st.error(e)
        return False

def create_page(id):
    st.title("Update Employee Account")

    df = get_vehicles(id)

    edited_df = st.data_editor(df)
    if st.button("Save Changes"):
        success = update_vehicles(edited_df)
        if success:
            st.success("Updated successfully")
        else:
            st.success("Could not update the database")

    # st.write("Temporary placeholder for Updating Employee")
    # st.markdown("""
    # The process of updating an employee must include the following steps:
    # 1. Find the employee and first showcase it in a collapsed view
    # 2. There should be two buttons on the side of the collapsed view of the employee: **Update** and **Delete**
    # 3. If we want to update the employee details, we press update, which brings up an interface similar to that of creating an employee, only here, the text boxes have placeholders, which are the original values of the employee details.
    # 4. If we want to delete the employee, we press the delete button, which pops a warning, asking us we are sure that we want to delete the employee. If we are sure, press delete again.
    #     """)
