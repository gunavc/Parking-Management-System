import streamlit as st
import mysql.connector
import pandas as pd 

def get_users():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT name, username, role, userid FROM parking_system.users;")

        df = pd.DataFrame(cursor.fetchall(), columns=["Name", "Username", "Role", "User ID"])
        df["Mark to Delete"] = False

        conn.commit()
        cursor.close()
        conn.close()

        return df
    except Exception as e:
        st.error(e)

def update_users(df):
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
                query = "UPDATE parking_system.users SET name=%s, username=%s, role=%s WHERE userid=%s;"
                vals = (row["Name"], row["Username"], row["Role"], row["User ID"])
                cursor.execute(query, vals)
            elif row["Mark to Delete"]==True:
                query = "DELETE FROM parking_system.users WHERE userid=%s;"
                vals = (row["User ID"], )
                cursor.execute(query, vals)

        conn.commit()
        cursor.close()
        conn.close()

        return True
    except Exception as e:
        st.error(e)
        return False

def create_page():
    st.title("Update Employee Account")

    df = get_users()

    edited_df = st.data_editor(df)
    if st.button("Update"):
        success = update_users(edited_df)
        if success:
            st.success("Updated successfully")
        else:
            st.success("Could not update the database")