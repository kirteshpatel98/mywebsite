
import streamlit as st
import streamlit.components.v1 as components
from constant import *
import base64
from PIL import Image
# page config ----------------------------------------------------------------
im = Image.open("icons/shark_git1.png")
st.set_page_config(page_title="Portofolio", page_icon=im, layout="wide")
st.header("🚀 Portfolio",divider='rainbow')




# page functions ----------------------------------------------------------------
def Portfolio_component(header, content):
   st.subheader(header, divider='grey')
   st.write(content)

# Transformers for Time Series
st.subheader("Transformers for Time Series Forecasting", divider='grey')
tab1, tab2 = st.tabs(["About", "Results"])
with tab1:
   st.markdown(
""" ###### Implemented and trained PatchTST and Informer multivariate time series models in PyTorch, utilizing transformer architectures for accurate predictions.
We reproduce results from the following papers that introduced two special state-of-the-art transformer architectures for forecasting long sequence time-series data:-
"""
)
   st.markdown(
"""
- PatchTST - "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers" (https://doi.org/10.48550/arXiv.2211.14730)
- Informer - "Expanding the prediction capacity in long sequence time-series forecasting" (https://doi.org/10.1016/j.artint.2023.103886) + (https://doi.org/10.48550/arXiv.2012.07436)
"""
)
with tab2:
   st.image('./icons/transformers_time_series.png', width=700)

st.link_button("GitHub", "https://github.com/neelblabla/transformers_for_time_series_forecasting")

# Email Classification 
st.subheader("Email Classification using LLM", divider='grey')
tab1, tab2 = st.tabs(["About", "Results"])
with tab1:
   st.markdown(
""" ###### Fine-tuned BERT and XLNet LLM models in PyTorch for text classification, utilizing various regularization techniques. Employed regular expressions, NLTK, and spaCy for email dataset preprocessing. Implemented LLAMA generative AI model for email category recommendation.
"""
)
   st.markdown(
"""
Following is the workflow:
- Enron email corpus is an open dataset of more than 500,000 raw emails. We work on a subest of ~1700 pre-labeled emails available here - https://data.world/brianray/enron-email-dataset and another subset of chat GPT3.5 labelled ~12000.
- We narrowed down to lables in one layer i.e. we only consider 'Cat_1_level_1'and 'Cat_1_level_2' exclusively for our purpose. After this we get around 10 distinct classes.
- 'Regular Expressions' methods are used to clean the heavily unstructured email bodies in the labeled dataset along with lemmatization of email subject and body. ( Dataset is split into training (~1400) and testing (~300) subsets.
- Several Large Language models were fine tuned and trained for classification with several regularization and parameter efficient training methodologies.
"""
)
with tab2:
   pass

st.link_button("GitHub", "https://github.com/neelblabla/large_language_models_for_processing_emails")


'''
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

components.iframe("https://1drv.ms/b/s!AoiE7xOoBAsngs875jVpU6OUw0fqKA?e=3YvUm6", width=1000, height=700, scrolling=True)



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
'''