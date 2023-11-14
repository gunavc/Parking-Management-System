# Main Page Container for Admin View
import streamlit as st


def create_page():
    from views.admin import Parking_Analytics, Employee_Creation, Employee_Updation, Parked_Cars, User_Creation, CostMatrix_Updation
    parking_anal, emp_create, emp_update, user_create, costmatrix = st.tabs(["Parking Analytics", "Employee Creation", "Employee Updation", "Create User Login", "Cost Matrix"])

    with parking_anal:
        Parking_Analytics.create_page()

    with emp_create:
        Employee_Creation.create_page()

    with emp_update:
        Employee_Updation.create_page()

    # with parked_cars:
    #     Parked_Cars.create_page()
    with user_create:
        User_Creation.create_page()
    with costmatrix:
        CostMatrix_Updation.create_page()

create_page()