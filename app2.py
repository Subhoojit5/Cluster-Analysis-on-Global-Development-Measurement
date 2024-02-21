import streamlit as st 
import numpy as np
import pandas as pd
import pickle
import sklearn
from PIL import Image

#loading model
model = pickle.load(open(r'C:\Users\Narsing\Downloads\Assigments data science\Project P302 DS G4\model.sav','rb'))
#pickle_in =open ("RF_model.pkl","rb")
#RF_model = pickle.load(pickle_in)
#PAge setting
st.set_page_config(layout='wide')

#Title

#st.title('Prediction of Countries Development using their development measures')
html_temp="""
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center">Prediction of Countries Development using their development measures</h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)
#Image
#image = Image.open('image2.png')
#st.image(image, '',width=500)

#Sidebar
st.sidebar.header('Development Index')

# FUNCTION
def dev_index():
  population = st.sidebar.slider('Population', -3,11, 1 )
  birth_rate = st.sidebar.slider('Birth Rate', -2,3, 1 )
  start_buss = st.sidebar.slider('Days to Start Bussiness', -8,15, 1 )
  enery = st.sidebar.slider('Enery Usage', -3,3, 1 )
  gdp = st.sidebar.slider('GDP', -1,18, 1 )
  health_exp = st.sidebar.slider('Health Expenditure', -3,7, 1 )
  health_exp_capita = st.sidebar.slider('Health Expenditure per capita', -6,7, 1)
  internet = st.sidebar.slider('Internet Usage', -10,5, 1 )
  len_int = st.sidebar.slider('Lending Interest', -10,5, 1 )
  Fem_life_exp = st.sidebar.slider('Female Life Expectancy', -4,2, 1 )
  male_life_exp = st.sidebar.slider('Male Life Expectancy', -4,4, 1 )
  mob_usg = st.sidebar.slider('Mobile phone Usage', -2,6, 1 )
  pop_15to64 = st.sidebar.slider('Population from 15 to 64 years of Age', -3,4, 1 )
  pop_65 = st.sidebar.slider('Population above 65 years of Age', -2,4, 1 )
  pop_urban = st.sidebar.slider('Population of Urban areas', -2,2, 1 )
  Tou_in = st.sidebar.slider('Toursim Inbound', -1,16, 1 )


  dev_index_data = {
      'Population':population,
      'Birth_rate':birth_rate,
      'Days_to_start_bussiness':start_buss,
      'Energy_Usage':enery,
      'GDP':gdp,
      'Health_Exp':health_exp,
      'Health_Exp_capita':health_exp_capita,
      'Internet_usage':internet,
      'Lending_interest':len_int,
      'Female_life_exp':Fem_life_exp,
      'Male-life_exp':male_life_exp,
      'Mobile_Usage':mob_usg,
      'Population_15_to_64':pop_15to64,
      'Population_65+':pop_65,
      'Population_urban':pop_urban,
      'Toursim_Inbound':Tou_in
  }
  dev_data = pd.DataFrame(dev_index_data, index=[0])
  return dev_data

#Model
dev_data_print = dev_index()
st.header('Selected Development measures are:')
st.write(dev_data_print)


def result(dev_model):
    if dev_model==0:
        return '"Least Developed country"'
    elif dev_model==1:
        return '"Developed Country"'
    elif dev_model==2:
        return '"Developing Country"'
    elif dev_model==3:
        return '"Most Developed Country"'
    else:
        return '"Economies in transition"'

if st.button('Predict'):
    dev_model = model.predict(dev_data_print)[0]
    st.subheader('Development Status of the country is:')
    st.subheader(result(dev_model))