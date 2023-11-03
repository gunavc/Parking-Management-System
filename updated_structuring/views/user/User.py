import streamlit as st
import Your_Vehicles, Add_Vehicles

def create_page():
    your_v, add_v = st.tabs(["Your Vehicles", "Add Vehicle"])

    with your_v:
        Your_Vehicles.create_page()

    with add_v:
        Add_Vehicles.create_page()