
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

