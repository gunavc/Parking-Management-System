import streamlit as st

def create_page(id):
    
    from views.user import Your_Vehicles, Add_Vehicles
    your_v, add_v = st.tabs(["Your Vehicles", "Add Vehicle"])

    with your_v:
        Your_Vehicles.create_page(id)

    with add_v:
        Add_Vehicles.create_page(id)
