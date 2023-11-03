import streamlit as st

def create_page():
    
    from views.user import Your_Vehicles, Add_Vehicles
    your_v, add_v = st.tabs(["Your Vehicles", "Add Vehicle"])

    with your_v:
        Your_Vehicles.create_page()

    with add_v:
        Add_Vehicles.create_page()