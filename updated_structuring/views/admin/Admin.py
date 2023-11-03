# Main Page Container for Admin View
import streamlit as st
import Parking_Analytics, Employee_Creation, Employee_Updation, Parked_Cars

def create_page():
    parking_anal, emp_create, emp_update, parked_cars = st.tabs(["Parking Analytics", "Employee Creation", "Employee Updation", "Parked Cars"])

    with parking_anal:
        Parking_Analytics.create_page()

    with emp_create:
        Employee_Creation.create_page()

    with emp_update:
        Employee_Updation.create_page()

    with parked_cars:
        Parked_Cars.create_page()