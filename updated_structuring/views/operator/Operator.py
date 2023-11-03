import streamlit as st
import Lot_View, User_Profile, Vehicle_Entry, Vehicle_Exit

def create_page():
    lot_view, v_ent, v_exit, user_prof = st.tabs(["Lot View","Vehicle Entry","Vehicle Exit","User Profile"])

    with lot_view:
        Lot_View.create_page()

    with v_ent:
        Vehicle_Entry.create_page()

    with v_exit:
        Vehicle_Exit.create_page()

    with user_prof:
        User_Profile.create_page()