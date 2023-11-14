import streamlit as st

def create_page(id):
    
    from views.user import Your_Vehicles, Add_Vehicles, Update_Vehicle
    your_v, add_v, update_v = st.tabs(["Your Vehicles", "Add Vehicle", "Update Vehicle"])

    with your_v:
        Your_Vehicles.create_page(id)

    with add_v:
        Add_Vehicles.create_page(id)

    with update_v:
        Update_Vehicle.create_page(id)
