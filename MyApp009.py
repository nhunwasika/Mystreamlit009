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
<div style="background-color:#ccccff;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>ข้อมูลของลูกค้าทัวร์</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")

import pandas as pd

raw_data=pd.read_csv('./data/Tour_Travel.csv')
st.write(raw_data.head(10))

html_2 = """
<div style="background-color:#FF99CC;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>แปลงข้อมูล</h5></center>
</div>
"""
st.markdown(html_2, unsafe_allow_html=True)
st.markdown("")

from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
raw_data["FrequentFlyer"]= le.fit_transform(raw_data["FrequentFlyer"])
raw_data["AnnualIncomeClass"]=le.fit_transform(raw_data["AnnualIncomeClass"])
raw_data["AccountSyncedToSocialMedia"]=le.fit_transform(raw_data["AccountSyncedToSocialMedia"])
raw_data["BookedHotelOrNot"]=le.fit_transform(raw_data["BookedHotelOrNot"])

st.write(raw_data.head(10))

html_3 = """
<div style="background-color:#FF6666;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การจำแนกคลาสการยกเลิกใช้งาน</h5></center>
</div>
"""
st.markdown(html_3, unsafe_allow_html=True)
st.markdown("")

s1 = st.number_input("กรุณาเลือกข้อมูล Age", step=1, format="%d")
s2 = st.number_input("กรุณาเลือกข้อมูล FrequentFlyer", step=1, format="%d")
s3 = st.number_input("กรุณาเลือกข้อมูล AnnualIncomeClass", step=1, format="%d")
s4 = st.number_input("กรุณาเลือกข้อมูล ServicesOpted", step=1, format="%d")
s5 = st.number_input("กรุณาเลือกข้อมูล AccountSyncedToSocialMedia", step=1, format="%d")
s6 = st.number_input("กรุณาเลือกข้อมูล BookedHotelOrNot", step=1, format="%d")

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import numpy as np



    
