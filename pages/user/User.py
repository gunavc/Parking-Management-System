import streamlit as st
import pandas as pd

st.title("Your Cars")

"""
There is to be two sections: 
1. A section having cars currently parked in the campus
2. A section having all other cars

The user must also have the ability to make edits to the details of their cars.
This should be done by means of a data editor
dataframe can be loaded as a data_editor, and then saved back as the dataframe, and the dataframe gets loaded into the sql database
"""
all_cars = pd.DataFrame(
  [
    {"license_plate_no":"KA01LJ5275", "type":"Bike", "last_lot_no": 1, "last_slot_no": 15, "last_entry_time":"0830", "is_parked":True},
    {"license_plate_no":"KA05MH1813", "type":"Car", "last_lot_no": 1, "last_slot_no": 15, "last_entry_time":"0830", "is_parked":False},
    {"license_plate_no":"KA03NG8338", "type":"Car", "last_lot_no": 1, "last_slot_no": 15, "last_entry_time":"0830", "is_parked":False},
    {"license_plate_no":"KA03HU0739", "type":"Bike", "last_lot_no": 1, "last_slot_no": 15, "last_entry_time":"0830", "is_parked":False}
  ]
)
st.header("Currently Parked")
"""
Here the cars which are currently parked 
"""
"Temporarily defining a dataframe. This dataframe should be obtained from the database using SQL"
currently_parked = pd.DataFrame

st.divider()
st.header("Unparked Cars")
"""
Here the other cars which belong to the user, but are not parked
"""
not_parked = pd.DataFrame
