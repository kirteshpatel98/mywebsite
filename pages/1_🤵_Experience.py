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
    st.markdown("######   " + "Frankfurt, Germany")
st.markdown(
"""
- Fine Tuned LLMs for prompt recognisition and entity recognisition.
- Developed AI segmentation and optimization techniques using PyTorch, SciPy, and Keras for the detection and design generation of optimized hygiene products.
- Effectively oversaw code, versions, and Agile-Scrum practices on GitHub Enterprise, ensuring efficient collaboration and streamlining.
"""
)
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
    st.markdown("######   " + "Frankfurt, Germany")
st.markdown(
"""
Roche Incubation Project
- Developing LLM capabilities to conduct regulatory analysis and semantic search of regulatory changes, facilitating streamlined regulatory checks in pharmaceutical industry.
- Ensured scalability and efficiency through strategic utilization of cloud-based services, facilitating seamless workflow integration.
"""
)


col1, col2, col3 = st.columns([3, 1, 1])
with col3:
    st.write("")
    st.markdown("")

col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Co-Op Student - AI, ML, NLP, Data Science")
with col3:
    st.markdown("######   " + "October 2023 - Januray 2024")
st.code("pip install reghub-pack",language='python')
st.markdown(
"""
- Developed diverse NLP capabilities through the creation and finetuning of multiple models, encompassing tasks such as multi label classification, similarity analysis, and news mapping.
- Fine-tuned LLaMA model for extracting key information enhancing its generative recommender system capabilities through Causal Language Modeling.
"""
)
if st.button("GitHub Link"):
    # Redirect to the website when the button is clicked
    st.markdown("https://github.com/kirteshpatel98/RegHub_news_signal_analysis")
    st.markdown("https://pypi.org/project/reghub-pack/")
st.divider()

# worley
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    col11, col12 = st.columns([1,10])
    with col11:
        st.markdown("""<a href="https://www.worley.com/"><img src="data:image/png;base64,{}" width="50"></a>""".format(base64.b64encode(open("./icons/worley.png", "rb").read()).decode()),unsafe_allow_html=True,)
    with col12:
        st.subheader("Worley")
with col3:
    st.write("")
    st.markdown("######   " + "Feburary 2021 - July 2022")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Engineer Level 1")
with col3:
    st.markdown("######   " + "Mumbai, India")
st.markdown(
"""
Renewable energy, data center projects.
- Reduced a significant amount of manpower using automation, AI, bots related to design, analysis and technical documentation.
- Implemented data analysis, quantative calculations and visualization of technical parameters in Excel, Power BI and Python.
- Developed pipelines of Excel sheets and Python script to incorporate design changes automatically, reducing manual efforts.
"""
)

col1, col2, col3 = st.columns([3, 1, 1])
with col3:
    st.write("")
    st.markdown("")

col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Project Intern")
with col3:
    st.markdown("######   " + "Januray 2020 - May 2020")
st.markdown(
"""
- Developed, analyzed, evaluated technical data sheets for insights.
- Conducted in-depth technical bid data analysis of equipment, extracting valuable insights for decision-making.
- Explored data-centric project delivery methodologies, focusing on automation bots and AI applications within the engineering industry.
"""
)
st.divider()

# reliance
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    col11, col12 = st.columns([1,10])
    with col11:
        st.markdown("""<a href="https://www.ril.com/"><img src="data:image/png;base64,{}" width="50"></a>""".format(base64.b64encode(open("./icons/reliance.png", "rb").read()).decode()),unsafe_allow_html=True,)
    with col12:
        st.subheader("Reliance Industries Limited")
with col3:
    st.write("")
    st.markdown("######   " + "June 2019 - July 2019")
col1, col2, col3 = st.columns([3, 1, 1])
with col1:
    st.markdown("###### " + "Internship")
with col3:
    st.markdown("######   " + "Jamnagar, India")
st.markdown(
"""
Efficiency, Quantative Performance analysis, Maintenance of pumps.
- Carried out quantative performance calculations and visualization performance of • pump in MATLAB.
- Implemented predictive maintenance of pump using data analysis and statistical methods.
"""
)
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