import streamlit as st 
import pickle

# membaca model
diabetes_model = pickle.load(open('diabetes_model.sav','rb'))

#judul
st.title('Aplikasi Data Mining Prediksi Diabetes')

#membagi kolom
col1,col2 = st.columns(2)

#form
with col1:
    Pregnancies = st.text_input('Input Value of Pregnancies')
with col1:
    Glucose = st.text_input('Input Value of Glucose')
with col1:
    BloodPressure = st.text_input('Input Value of Blood Presure')
with col1:
    SkinThickness = st.text_input('Input Value of Skin Thickness')
with col2:
    Insulin = st.text_input('Input Value of Insulin')
with col2:
    BMI = st.text_input('Input Value of BMI')
with col2:
    DiabetesPedigreeFunction = st.text_input('Input Value of Diabetes Pedigree Function')
with col2:
    Age = st.text_input('Input Value of Age')

#Code untuk prediksi
diab_diagnosis = ''

#Button
if st.button('Predict Here!'):
    diab_prediction = diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])

    if(diab_prediction[0]==1):
        diab_diagnosis = 'Pasien Got Diabetes'
    else:
        diab_diagnosis = 'Patient Clear From Diabetes'

st.success(diab_diagnosis)