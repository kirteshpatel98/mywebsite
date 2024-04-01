import streamlit as st
import streamlit.components.v1 as components
from constant import *
import base64

st.set_page_config(page_title="Education", page_icon="🏫", layout="wide")
st.header("🏫 Education",divider='rainbow')
st.write("")

# fs
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    col11, col12 = st.columns([1,10])
    with col11:
        st.markdown("""<a href="https://www.frankfurt-school.de/home"><img src="data:image/png;base64,{}" width="50"></a>""".format(base64.b64encode(open("./icons/fs.png", "rb").read()).decode()),unsafe_allow_html=True,)
    with col12:
        st.subheader("Frankfurt School of Finance and Management")
with col3:
    st.write("")
    st.markdown("######   " + "August 2022 - August 2024")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Masters of Applied Data Science")
with col3:
    st.markdown("######   " + "Frankfurt, Germany")
st.write('Grade: 84%')
st.write('Key Courses: NLP, Deep Learning, AI Frontiers, Database and Cloud, Strategic Management, Machine Learning I, Machine Learning II')
st.divider()

# pdpu
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    col11, col12 = st.columns([1,10])
    with col11:
        st.markdown("""<a href="https://pdeu.ac.in/"><img src="data:image/png;base64,{}" width="50"></a>""".format(base64.b64encode(open("./icons/pdeu.png", "rb").read()).decode()),unsafe_allow_html=True,)
    with col12:
        st.subheader("Pandit Deendayal Energy University")
with col3:
    st.write("")
    st.markdown("######   " + "July 2016 - October 2020")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Bachelors in Technology Mechanical Engineering")
with col3:
    st.markdown("######   " + "Gandhinagar, India")
st.write("Grade: 76%")
st.write("Co-curricular: BAJA SAE India, Techgium by L&T, Gujarat Industrial Hackathon")
st.divider()


# kdav
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    col11, col12 = st.columns([1,10])
    with col11:
        st.markdown("""<a href="https://www.rfs.edu.in/jamnagar/"><img src="data:image/png;base64,{}" width="50"></a>""".format(base64.b64encode(open("./icons/reliance.png", "rb").read()).decode()),unsafe_allow_html=True,)
    with col12:
        st.subheader("K.D. Ambani Reliance Foundation School")
with col3:
    st.write("")
    st.markdown("######   " + " - March 2020")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "High School (Physics Chemistry Mathematics majors)")
with col3:
    st.markdown("######   " + "Jamnagar, India")
st.write("Grade: 82%")
st.write("Engineering Entrance Exam: 95 percentile")
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