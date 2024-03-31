
import streamlit as st
import streamlit.components.v1 as components
from constant import *
import base64
# page config ----------------------------------------------------------------
st.set_page_config(page_title="Portofolio", page_icon="🚀", layout="wide")
st.header("🚀 Portfolio",divider='rainbow')

'''

# page functions ----------------------------------------------------------------
def Portfolio_component(header, content):
   st.subheader(header, divider='grey')
   st.write(content)

# Deis Evaluation ----------------------------------------------------------------
Portfolio_component(Portfolio[1][0], Portfolio[1][1])

tab1, tab2 = st.tabs(["UI/UX", "View Website"])
with tab1:
   components.iframe(figma_link, width=800, height=500, scrolling=True)
with tab2:
   st.link_button("Go to Website", "https://deis-evaluation.onrender.com")
   components.iframe("https://deis-evaluation.onrender.com", width=800, height=600, scrolling=True)

# Data VIS in D3.js --------------------------------------------------------------
Portfolio_component(Portfolio[2][0], Portfolio[2][1])

st.link_button("Go to Github", "https://github.com/Rsirp0c/D3-practice")
st.image("src/Screenshot-2.png", width=800)
with st.expander("See more"):
   st.image("src/Screenshot-1.png", width=800)
   st.image("src/Screenshot-3.png", width=800)
   st.image("src/Screenshot-4.png", width=800)

# Desktop ChatApp -------------------------------------------------------------- 
Portfolio_component(Portfolio[3][0], Portfolio[3][1])

st.link_button("Go to :blue[Source Code]", "https://github.com/Rsirp0c/desktop_chatapp")

# Anthropology Research Project -----------------------------------------------------------
Portfolio_component(Portfolio[4][0], Portfolio[4][1])

components.iframe(StoryMap_iframe, width=1000, height=700, scrolling=True)

'''

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