import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os


st.markdown("""
    <style>
        body {
            background-image: url("https://wallpapercave.com/wp/wp6817539.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        .stApp {
            background-color: rgba(255, 255, 255, 0.1);
        }
    </style>
""", unsafe_allow_html=True)



# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

MODEL_PATH=os.path.join(dir_of_interest,'data','model.pkl')



















st.title('LAPTOP PRICE PREDICTOR')

RAM=st.selectbox('Enter RAM',('4','8','16','32','128'))
SSD_GB=st.selectbox('Enter SSD in GB',('128','256','512','1000','2000'))
HDD_GB=st.selectbox('Enter HDD in GB',('1000','256','0'))
OS=st.selectbox('Select type of OS',('64 bit Windows 11','64 bit Windows 10','other'))
CPU=st.selectbox('Select type of CPU',('AMD Ryzen 5','AMD Ryzen 7','AMD Ryzen 9','Intel Core i3','Intel Core i5', 
'Intel Core i7','Intel Core i9','Other Intel Processor'))

pickle_in = open(MODEL_PATH, 'rb') 
r = pickle.load(pickle_in)


def prediction(RAM,SSD_GB,HDD_GB,OS,CPU):
    if OS=='64 bit Windows 11':
        OS_64_bit_Windows_11=1
        OS_other=0

    elif OS=='OS_other':
        OS_64_bit_Windows_11=0
        OS_other=1

    else:
        OS_64_bit_Windows_11=0
        OS_other=0

    if CPU=='CPU_AMD Ryzen 5':
        CPU_AMD_Ryzen_5=1
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=0

    elif CPU=='CPU_AMD Ryzen 7':
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=1
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=0

    elif CPU=='CPU_AMD Ryzen 9':
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=1
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=0

    elif CPU=='CPU_Intel Core i3':
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=1
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=0

    elif CPU=='CPU_Intel Core i5':
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=1 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=0

    elif CPU=='CPU_Intel Core i7':
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=1
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=0

    elif CPU=='CPU_Intel Core i9':
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=1
        CPU_Other_Intel_Processor=0

    elif CPU=='CPU_Other Intel Processor':
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=1

    else:
        CPU_AMD_Ryzen_5=0
        CPU_AMD_Ryzen_7=0 
        CPU_AMD_Ryzen_9=0
        CPU_Intel_Core_i3=0 
        CPU_Intel_Core_i5=0 
        CPU_Intel_Core_i7=0
        CPU_Intel_Core_i9=0
        CPU_Other_Intel_Processor=0

        prediction=r.predict([[RAM,SSD_GB,HDD_GB,OS_64_bit_Windows_11,OS_other,CPU_AMD_Ryzen_5,CPU_AMD_Ryzen_7,CPU_AMD_Ryzen_9,CPU_Intel_Core_i3, CPU_Intel_Core_i5, 
        CPU_Intel_Core_i7,CPU_Intel_Core_i9,CPU_Other_Intel_Processor]])

        return prediction

if st.button('predict'):
    result=prediction(RAM,SSD_GB,HDD_GB,OS,CPU)
    #st.success(f'The predicted price for the laptop is: ' +str(int(np.exp(result)[0])))
    st.markdown(f'<p style="font-size:50px; font-weight:bold; color:#333;">The predicted price for the laptop is: {int(np.exp(result)[0])}</p>', unsafe_allow_html=True)

#st.title("The predicted price of this configuration is " + str(int(np.exp(pipe.predict(query)[0]))))