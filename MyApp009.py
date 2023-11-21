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
with col2:
    st.image('./pic/pic2.jpg')