import streamlit as st
import pandas as pd
import mysql.connector
from datetime import datetime

def get_tickets():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
        cursor = conn.cursor()

        cursor.execute("""
        SELECT *
        FROM tickets
        WHERE MONTH(entry_time) = MONTH(NOW()) AND YEAR(entry_time) = YEAR(NOW())
        ORDER BY entry_time DESC
        """)
        data = pd.DataFrame(cursor.fetchall(), columns=["Registration Number", "Entry Time", "Exit Time", "Cost"])

        conn.commit()
        cursor.close()
        conn.close()

        return data
    except Exception as e:
        st.error(e)

def create_page():
    
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    st.title("Parking Analytics")
    
    # st.write("Placeholder for parking analytics.")
    # st.markdown("""
    #     # What needs to be achieved:
    #     The parking analytics must lead to the data regarding all the previously parked cars in the last fo





    # """)
    conn = mysql.connector.connect(
            host="localhost",
            user="proj",
            password="proj",
            database="parking_system"
        )
    cursor = conn.cursor()

    query = """
    SELECT DAY(entry_time) AS day, COUNT(*) AS num_cars
    FROM parking_system.parked_vehicles
    WHERE MONTH(entry_time) = %s AND YEAR(entry_time) = %s
    GROUP BY day;
    """
    # Execute the query
    cursor.execute(query, (current_month, current_year))

    # Fetch the results
    results = cursor.fetchall()

    # Create a DataFrame from the database results
    parked_cars = pd.DataFrame(results, columns=['Date', 'Parked Cars'])
    
    col1, col2 = st.columns([1,2])
    with col1:
        parked_cars_num = parked_cars["Parked Cars"].sum()
        st.subheader(f"Total Parked Cars for the month of {current_month}")
        st.header(parked_cars_num)
        st.divider()
    
    with col2:
        st.write("Number of cars parked each day of the month")
        st.area_chart(parked_cars)


    #Display parking tickets
    st.header("Parking Tickets")
    ticket_data = get_tickets()
    if len(ticket_data)>0:
        st.dataframe(ticket_data)
    else:
        st.error("No Vehicles have been parked this month")