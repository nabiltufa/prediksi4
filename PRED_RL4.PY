import pickle
import streamlit as st
import datetime

model = pickle.load(open('kernel_mantap_linear.pkl', 'rb'))

st.title('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii di Desa Lontar')

masa_panen = st.date_input('Input Waktu Panen', value=None)
arus = st.number_input('Input Kecepatan Arus')
Salinitas = st.number_input('Input Salinitas')
suhu = st.text_input('Input Suhu')
modal = st.text_input('Input Modal')

predict = ''

if st.button ('Prediksi'):
    predict = model.predict(
        [[masa_panen,arus,Salinitas,suhu,modal]]
    )
    st.write('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii : ', predict)
    st.write ('Nilai Kesalahan : 3,18%')
