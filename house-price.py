import numpy as np
import pickle
import streamlit #create account in Streamlit
#map the data
#location,status,property type and facing
location_mapping = {
    "Kesarapalli":10,
    "Auto Nagar":12,
    "Poranki": 8,
    "Kankipadu": 5,
    "Benz Circle": 0,
    "Gannavaram": 2,
    "Rajarajeswari Peta": 9,
    "Gunadala": 4,
    "Gollapudi": 3,
    "Enikepadu": 1,
    "Vidhyadharpuram": 11,
    "Penamaluru": 7,
    "Payakapuram": 6
}

#in smilar way we do for status,facing and property type
status_mapping = {'Ready to move':1,
                  'New':0,'Resale':2,'Under Construction':3}








