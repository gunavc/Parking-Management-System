import streamlit as st
import mysql.connector
import pandas as pd 

def get_costmatrix():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM parking_system.cost_matrix;")

        df = pd.DataFrame(cursor.fetchall(), columns=["Vehicle Type", "Price"])

        conn.commit()
        cursor.close()
        conn.close()

        return df
    except Exception as e:
        st.error(e)

def update_costmatrix(df):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        for index, row in df.iterrows():
            query = "UPDATE parking_system.cost_matrix SET price=%s WHERE vehicle_type=%s;"
            vals = (row["Price"], row["Vehicle Type"])
            cursor.execute(query, vals)

        conn.commit()
        cursor.close()
        conn.close()

        return True
    except Exception as e:
        st.error(e)
        return False

def create_page():
    st.title("Cost Matrix")

    df = get_costmatrix()

    edited_df = st.data_editor(df)
    if st.button("Save"):
        success = update_costmatrix(edited_df)
        if success:
            st.success("Updated successfully")
        else:
            st.error("Could not update the database")