import streamlit as st
import pandas as pd

def create_page():
    from datetime import datetime
    


    current_month = datetime.today().strftime("%B")
    current_month_num = datetime.today().month
    
    st.title("Parking Analytics")
    
    st.write("Placeholder for parking analytics.")
    st.markdown("""
        # What needs to be achieved:
        The parking analytics must lead to the data regarding all the previously parked cars in the last fo





    """)
    parked_cars = pd.DataFrame(
        {
            "Date": [1,2,3,4,5,6,7,8],
            "Parked Cars": [56,43,44,16,7,50,56,42]
        }
    )
    col1, col2 = st.columns([1,2])
    with col1:
        parked_cars_num = parked_cars["Parked Cars"].sum()
        st.subheader(f"Total Parked Cars for the month of {current_month}")
        st.header(parked_cars_num)
        st.divider()
    
    with col2:
        st.write("Have a graph of somesorts here showing number of cars parked for each day of the month")
        st.area_chart(parked_cars)

    st.header("display ticket database")


create_page()
        
    

