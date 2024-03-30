import streamlit as st 
from constant import *

st.set_page_config(page_title="Contacts", page_icon="🌏") #layout="wide"

st.markdown(f"##### 📞 Phone: +49 15734414237")   
st.markdown(f"##### ✉️ Email: kirteshpatel98@gmail.com")
'''

with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(linkedin_logo, unsafe_allow_html=True)
    with col2:
        st.markdown(f"#####  Linkedin: {linkedin_link}")
with st.container():
    col1, col2 = st.columns([0.1, 3])
    with col1:
        st.write(github_logo, unsafe_allow_html=True)
    with col2:
        st.markdown(f"#####  Github: {github_link}")

'''

