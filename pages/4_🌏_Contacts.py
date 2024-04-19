import streamlit as st 
from constant import *
import base64
from PIL import Image
im = Image.open("icons/shark_git1.png")

st.set_page_config(page_title="Contact", page_icon=im) #layout="wide")
# st.set_page_config(page_title="Contacts", page_icon="🌏", layout="wide")
st.header("🌏 Contact",divider='rainbow')

st.markdown("#### Get In Touch With Me")

contact_form = """
<form action="https://formsubmit.co/kirteshpatel98@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="Name" placeholder="Your Name" required>
     <input type="email" name="Email" placeholder="Your Email" required>
     <textarea name="Message" placeholder="Type a message"></textarea>
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form,unsafe_allow_html=True)


def local_css(file_name):
  with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

local_css("style/style.css")



st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

col1, col2, col3= st.columns(3)
with col1:
    st.markdown("""<a href="https://www.linkedin.com/in/kirtesh-patel-09997a180/"><img src="data:image/png;base64,{}" width="100"></a>""".format(base64.b64encode(open("./icons/linkedin.png", "rb").read()).decode()),unsafe_allow_html=True,)
with col3:
    st.markdown("""<a href="https://github.com/kirteshpatel98"><img src="data:image/png;base64,{}" width="100" ></a>""".format(base64.b64encode(open("./icons/github.png", "rb").read()).decode()),unsafe_allow_html=True,)
with col2:
    # st.markdown("""<a href="mailto:""kirteshpatel98@gmail.com">"kirteshpatel98@gmail.com"<img src="data:image/png;base64,{}" width="50" ></a>""".format(base64.b64encode(open("./icons/github.png", "rb").read()).decode()),unsafe_allow_html=True,)
    st.markdown("""<a href="mailto:kirteshpatel98@gmail.com"><img src="data:image/png;base64,{}" width="100" ></a>""".format(base64.b64encode(open("./icons/gmail.png", "rb").read()).decode()),unsafe_allow_html=True,)


st.sidebar.markdown('Contact')

# Add columns to the sidebar
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