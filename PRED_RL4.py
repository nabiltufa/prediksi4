import pickle
import streamlit as st
import datetime
import numpy as np

model = pickle.load(open('kernel_mantap4_rbf.pkl', 'rb'))

st.title('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii di Desa Lontar')

masa_panen = st.date_input('Input Waktu Panen', value=None)
arus = st.number_input('Input Kecepatan Arus')
Salinitas = st.number_input('Input Salinitas')
suhu = st.text_input('Input Suhu')
modal = st.text_input('Input Modal')

predict = ''

if st.button('Prediksi'):
    # Konversi input waktu panen menjadi nilai numerik (misalnya jumlah hari sejak tanggal tertentu)
    tanggal_referensi = datetime.date(1970, 1, 1)  # atau gunakan tanggal referensi lain jika diperlukan
    masa_panen_numerik = (masa_panen - tanggal_referensi).days if masa_panen else None

    if masa_panen_numerik is not None:
        # Menggunakan nilai datetime sebagai input untuk memprediksi total produksi
        predict = model.predict(
            [[masa_panen_numerik, arus, Salinitas, suhu, modal]]
        )
        st.write('Prediksi Total Produksi Rumput Laut Eucheuma Cottonii : ', predict)
        st.write('Nilai Kesalahan : 3,18%')
    else:
        st.write("Masukkan tanggal panen yang valid.")
