import streamlit as st

st.title('การวิเคราะห์ยกเลิกใช้บริการธุรกิจท่องเที่ยว')
st.header('นางสาว วาศิการ์ จิตติศักดิ์')
st.subheader('สาขาวิชาวิทยาการข้อมูล')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/pic1.jpg')
#with col2:
    #st.image('./pic/pic2.jpg')

html_1 = """
<div style="background-color:#52BE80;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ข้อมูลของลูกค้าทัวร์</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

raw_data=pd.read_csv('./data/Tour_Travel.csv')
st.write(raw_data.head(10))