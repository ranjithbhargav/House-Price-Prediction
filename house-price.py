import numpy as np
import pickle
import streamlit as st#create account in streamlit
#location,types,facingand property
location_mapping = {
    'AGIRIPALLI': 0,
    'Ajit Singh Nagar': 1,
    'Andhra Prabha Colony Road': 2,
    'Ashok Nagar': 3,
    'Auto Nagar': 4,
    'Ayyappa Nagar': 5,
    'Bandar Road': 6,
    'Benz Circle': 7,
    'Bharathi Nagar': 8,
    'Bhavanipuram': 9,
    'Chennai Vijayawada Highway': 10,
    'Currency Nagar': 11,
    'Devi Nagar': 12,
    'Edupugallu': 13,
    'Enikepadu': 14,
    'G Konduru': 15,
    'Gandhi Nagar': 16,
    'Gannavaram': 17,
    'Gollapudi': 18,
    'Gollapudi1': 19,
    'Gosala': 20,
    'Governor Peta': 21,
    'Gudavalli': 22,
    'Gunadala': 23,
    'Guntupalli': 24,
    'Guru Nanak Colony': 25,
    'Ibrahimpatnam': 26,
    'Jaggayyapet': 27,
    'Kanchikacherla': 28,
    'Kandrika': 29,
    'Kanigiri Gurunadham Street': 30,
    'Kankipadu': 31,
    'Kanuru': 32,
    'Kesarapalli': 33,
    'LIC Colony': 34,
    'Labbipet': 35,
    'Madhuranagar': 36,
    'Mangalagiri': 37,
    'Milk Factory Road': 38,
    'Moghalrajpuram': 39,
    'Murali Nagar 2nd Cross Road': 40,
    'Mylavaram': 41,
    'MylavaramKuntamukkalaVellaturuVijayawada Road': 42,
    'Nandigama': 43,
    'Nidamanuru': 44,
    'Nunna': 45,
    'Nuzividu': 46,
    'Nuzvid Road': 47,
    'Nuzvid To Vijayawada Road': 48,
    'PNT Colony': 49,
    'Pamarru': 50,
    'Patamata': 51,
    'Payakapuram': 52,
    'Pedapulipaka Tadigadapa Road': 53,
    'Penamaluru': 54,
    'Poranki': 55,
    'Punadipadu': 56,
    'Rajiv Bhargav Colony': 57,
    'Rama Krishna Puram': 58,
    'Ramalingeswara Nagar': 59,
    'Ramavarapadu': 60,
    'Ramavarapadu Ring': 61,
    'SURAMPALLI': 62,
    'Satyanarayanapuram Main Road': 63,
    'Satyaranayana Puram': 64,
    'Sri Ramachandra Nagar': 65,
    'Srinivasa Nagar Bank Colony': 66,
    'Subba Rao Colony 2nd Cross Road': 67,
    'Tadepalligudem': 68,
    'Tadigadapa': 69,
    'Tarapet': 70,
    'Telaprolu': 71,
    'Tulasi Nagar': 72,
    'Vaddeswaram': 73,
    'Vidhyadharpuram': 74,
    'Vijayawada Airport Road': 75,
    'Vijayawada Guntur Highway': 76,
    'Vijayawada Nuzvidu Road': 77,
    'Vijayawada Road': 78,
    'Vuyyuru': 79,
    'chinnakakani': 80,
    'currency nagar': 81,
    'krishnalanka': 82,
    'kunchanapalli': 83,
    'ramavarappadu': 84,
    'undavalli': 85
}
status_mapping={'New':0,
    'Ready to move':1,
    'Resale':2,
    'Under Construction':3
}
direction_mapping = {
    'East':0,
    'None':1,
    'North':2,
    'NorthEast':3,
    'NorthWest':4,
    'South':5,
    'SouthEast':6,
    'SouthWest':7,
    'West':8
}
property_type_mapping = {
    'Apartment':0,
    'Independent Floor':1,
    'Independent House':2,
    'Residential Plot':3,
    'Studio Apartment':4,
    'Villa':5
}
#reading pickle file
with open("House.pkl",'rb')as f:
    model=pickle.load(f)

#create a function to accept input and create an array
def predict(bed,bath,loc,size,status,facing,Type):
    """function to accept data"""
    select_location=location_mapping[loc]
    select_status=status_mapping[status]
    select_direction=direction_mapping[facing]
    select_property_type=property_type_mapping[Type]

    input_data=np.array([[bed,bath,
                          select_location,
                          size,
                          select_status,
                          select_direction,
                          select_property_type
                          ]])
    return model.predict(input_data)[0]

if __name__=="__main__":
    st.header("house price prediction")
    col1,col2=st.columns([2,1])
    bed=col1.slider("No.of Bedrooms",max_value=10,min_value=1,value=2)
    bath=col1.slider("No.of Bathrooms",max_value=10,min_value=1,value=2)
    loc=col1.selectbox("Select Location",list(location_mapping.keys()))
    size=col1.number_input("Area",max_value=10000,min_value=500,
                           value=1000,step=500)
    status=col1.selectbox("Select the status",list(status_mapping.keys()))
    facing=col1.selectbox("Select facing",list(direction_mapping.keys()))
    Type=col1.selectbox("Property type",list(property_type_mapping.keys()))
    
    result=predict(bed,bath,loc,size,status,facing,Type)
    submit_button=st.button("submit")
    if submit_button:
        larger_text=f"<h2 style='color:red'>The predicted House Price is:{result}Lakhs</h2>"
        st.markdown(larger_text,unsafe_allow_html=True)
