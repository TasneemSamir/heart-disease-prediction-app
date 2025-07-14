import streamlit as st
import pickle
import numpy as np
from pyngrok import ngrok
ngrok.set_auth_token("YOUR_AUTH_2zs4HBWzIdT9iRZcenujXPk0ePM_65paCYbjANmuyebBKeBdCTOKEN_HERE")

with open('heart_disease_model.pkl', 'rb') as file:
    model = pickle.load(file)


st.title(":sparkling_heart: Heart Disease Prediction App")
st.markdown("Enter your health data below:")


max_heart_rate = st.number_input('Max Heart Rate Achieved', min_value=40, max_value=250,value=70)

oldpeak = st.number_input('ST Depression (Oldpeak)', min_value=0.0, max_value=6.0, value=1.0, step=0.1)

cp_typical_angina = st.selectbox('Chest Pain: Typical Angina?', ['No', 'Yes'])
cp_typical_angina_val = 1 if cp_typical_angina == 'Yes' else 0

thal_reversible_defect = st.selectbox('Thalassemia: Reversible Defect?', ['No', 'Yes'])
thal_reversible_val = 1 if thal_reversible_defect == 'Yes' else 0

exang = st.selectbox('Exercise Induced Angina?', ['No', 'Yes'])
exang_val = 1 if exang == 'Yes' else 0

cholestoral = st.number_input('Cholesterol (mg/dL)', min_value=100, max_value=600, value=200)

input_data = np.array([[max_heart_rate, oldpeak, cp_typical_angina_val,
                        thal_reversible_val, exang_val, cholestoral]])

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error(":warning: The model predicts that you may have heart disease.")
    else:
        st.success(":white_check_mark: The model predicts you are unlikely to have heart disease.")

