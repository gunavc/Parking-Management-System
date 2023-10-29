import streamlit as st

st.title("Your Cars")

"""
There is to be two sections: 
1. A section having cars currently parked in the campus
2. A section having all other cars

The user must also have the ability to make edits to the details of their cars.
This should be done by means of a data editor
dataframe can be loaded as a data_editor, and then saved back as the dataframe, and the dataframe gets loaded into the sql database
"""

st.header("Currently Parked")
"""
Here the cars which are currently parked 
"""


st.divider()

st.header("Unparked Cars")
"""
Here the other cars which belong to the user
"""
