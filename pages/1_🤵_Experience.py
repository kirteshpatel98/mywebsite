import streamlit as st
import streamlit.components.v1 as components
from constant import *
import base64

st.set_page_config(page_title="Experience", page_icon="📚", layout="wide")
st.header("🤵 Experience",divider='rainbow')
st.write("")

# p&g
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    col11, col12 = st.columns([1,10])
    with col11:
        st.markdown("""<a href="https://de.pg.com//"><img src="data:image/png;base64,{}" width="50"></a>""".format(base64.b64encode(open("./icons/pg.png", "rb").read()).decode()),unsafe_allow_html=True,)
    with col12:
        st.subheader("Procter and Gamble")
with col3:
    st.write("")
    st.markdown("######   " + "April 2023 - Present")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Working Student R&D - AI, ML, Modelling, Data Science")
with col3:
    st.markdown("######   " + "Frankfurt")
st.write("content")
st.link_button("button_name", "www.google.com")
st.divider()

# reghub
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    col11, col12 = st.columns([1,10])
    with col11:
        st.markdown("""<a href="https://www.reghub.io/"><img src="data:image/png;base64,{}" width="50"></a>""".format(base64.b64encode(open("./icons/reghub.jpeg", "rb").read()).decode()),unsafe_allow_html=True,)
    with col12:
        st.subheader("RegHub")
with col3:
    st.write("")
    st.markdown("######   " + "March 2024 - Present")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Intern - AI, ML, NLP, Data Science")
with col3:
    st.markdown("######   " + "Frankfurt")
st.write("content")


col1, col2, col3 = st.columns([3, 1, 1])
with col3:
    st.write("")
    st.markdown("")

col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Co-Op Student - AI, ML, NLP, Data Science")
with col3:
    st.markdown("######   " + "October 2023 - Januray 2024")
st.write("content")
st.link_button("button_name", "www.google.com")
st.divider()

st.sidebar.markdown('Contact')


col1, col2, col3= st.sidebar.columns(3)

# Add content to the first column
with col1:
    st.markdown("""<a href="https://www.linkedin.com/in/kirtesh-patel-09997a180/"><img src="data:image/png;base64,{}" width="35"></a>""".format(base64.b64encode(open("./icons/linkedin1.png", "rb").read()).decode()),unsafe_allow_html=True,)

# Add content to the second column
with col3:
    st.markdown("""<a href="https://github.com/kirteshpatel98"><img src="data:image/png;base64,{}" width="35" ></a>""".format(base64.b64encode(open("./icons/github.png", "rb").read()).decode()),unsafe_allow_html=True,)

with col2:
    st.markdown("""<a href="mailto:kirteshpatel98@gmail.com"><img src="data:image/png;base64,{}" width="35" ></a>""".format(base64.b64encode(open("./icons/gmail1.png", "rb").read()).decode()),unsafe_allow_html=True,)




st.sidebar.markdown("---")
st.sidebar.markdown("© 2024 Kirtesh Patel. All rights reserved.")