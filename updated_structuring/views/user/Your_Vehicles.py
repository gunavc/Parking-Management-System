import streamlit as st

def create_page():
    st.title("Your Vehicles")

    st.write(
    """
    There is to be two sections: 
    1. A section having vehicles currently parked in the campus
    2. A section having all other vehicles

    The user must also have the ability to make edits to the details of their vehicles.
    This should be done by means of a data editor
    dataframe can be loaded as a data_editor, and then saved back as the dataframe, and the dataframe gets loaded into the sql database
    """
    )

    st.header("Currently Parked")
    st.write(
    """
    Here the vehicles which are currently parked 
    """
    )


    st.divider()

    st.header("Unparked Vehicles")
    st.write(
    """
    Here the other vehicles which belong to the user
    """
    )
