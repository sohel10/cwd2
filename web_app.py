#!/usr/bin/env python
# coding: utf-8

# In[13]:


#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pickle
import streamlit as st
from PIL import Image

# Loading the saved model
with open("rf_model2.pkl", "rb") as file:
    loaded_model = pickle.load(file)

# Creating a function for Prediction
def cwd_prediction(input_data):
    # Changing the input_data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        st.image('deern.png')
        return 'County CWD is Negative'
    else:
        st.image('deerp.png')
        return 'County CWD is Positive'

def main():
    # Giving a title
    st.title('Welcome to the CWD County-based Prediction Web App')
    image = Image.open("CWD1.png")
    st.image(image, use_column_width=True)
    st.header("User Input:")
    
    # Getting the input data from the user
    Cervid = st.slider('Number of Cervid Facilities', min_value=0, max_value=9, step=1, value=5)
    Harvest = st.slider('Total Harvest', min_value=5, max_value=9950, step=10, value=2000)
    Hunting = st.selectbox('Hunting Enclosures', [0, 0.5, 1])
    Baiting = st.selectbox('Baiting', [0, 0.5, 1])
    Feeding = st.selectbox('Feeding', [0, 0.5, 1])
    Carcass = st.selectbox('Whole Carcass Import', [0, 0.5])
    Urine = st.selectbox('Urine Lures', [0.0, 0.5, 1.0])
    Captive = st.selectbox('Captive status', [0, 1])
    Forest = st.slider('Forest (Average Proportion)', min_value=0.007, max_value=0.89, step=0.01, value=0.4)
    Clay = st.slider('Clay (Average Percent)', min_value=4, max_value=31, step=1, value=15)  # Corrected step to float to match other float values
    Streams = st.slider('Streams (Average distance to the nearest water)', min_value=1125, max_value=41430, step=20, value=2000)
  
    # Code for Prediction
    diagnosis = ''

    # Creating a button for Prediction
    if st.button('CWD Test Result'):
        diagnosis = cwd_prediction([Cervid, Harvest, Hunting, Baiting, Feeding, Carcass, Urine, Captive, Forest, Clay, Streams])

    st.success(diagnosis)

if __name__ == '__main__':
    main()



# In[ ]:




