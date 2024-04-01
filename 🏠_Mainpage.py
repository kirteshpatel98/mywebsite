import streamlit as st
import streamlit.components.v1 as components
from constant import *
import base64

st.set_page_config(page_title="Main Page", page_icon="🏠", layout="wide") 

#sidebar --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
with st.sidebar:
    st.success("Select a page above.")
#main page --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
st.header("Hey there! I'm Kirtesh",divider='rainbow')

col1, col2, col3 = st.columns([1.3 ,0.2, 1])

with col1:
    st.write("I'm on a journey of exploration and growth, navigating the diverse landscapes of AI, data and technology. Skilled in developing, training, and deploying ML/Deep Learning models to solve complex business and technical problems. Seeking to leverage expertise in data-driven decision-making and datacentric project delivery in dynamic environments. Dedicated to staying at the forefront of emerging technologies, I continuously refine my skills in AI, data analysis, and technological innovation.  I thrive in environments that foster creativity and encourage experimentation. Passionate about harnessing the power of data to drive actionable insights, I am committed to delivering solutions that drive organizational success and foster positive impact. ")
    
    # st.markdown(f"#####  Kirtesh Patel")
    # Frankfurt school
    col1, col2 = st.columns([1, 20])
    with col1:
        st.image('./icons/fs.png', width=25)
    with col2:
        st.markdown(f"###### Frankfurt School of Finance and Management - M.Sc. Data Science")

    # Location
    col1, col2 = st.columns([1, 20])
    with col1:
        st.image('./icons/ger.png', width=25)
    with col2:
        st.markdown(f"###### Frankfurt am Main")
    

    st.markdown(f"###### 📚 Interests: ML, AI, Data Science, NLP, Cloud")
    st.markdown(f"###### ⚽ Hobbies: Cycling, Football, Adventure Sports")

    with open("src/resume.pdf", "rb") as file:
        pdf_file = file.read()

    st.download_button(
        label="Download my :blue[resume]",
        data=pdf_file,
        file_name="resume",
        mime="application/pdf")

with col3:
    st.image("src/kirtesh.png", width=300)


# skills --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
skills1=['Python','PyTorch','github','Paperspace','Pandas','AWS','PowerBI','Keras','TensorFlow','MATLAB','MySQL','Transformers (Hugging Face)','Streamlit','Django','shell','R-programming','Microsoft 365']
# skills1=['Python','PyTorch']

st.subheader("My :blue[skills] ⚒️",divider='rainbow') #,divider='rainbow'

def skill_tab(skills1):
    rows,cols = len(skills1)//skill_col_size, skill_col_size
    skills = iter(skills1)
    if len(skills1)%skill_col_size!=0:
        rows+=1
    for x in range(rows):
        columns = st.columns(skill_col_size)
        for index_ in range(skill_col_size):
            try:
                # columns[index_].button(next(skills))
                # columns[index_].markdown(f"{next(skills)}")
                sk=next(skills)
                columns[index_].image(f"./icons/{sk}.png", caption=f"{sk}",width=60)
                
            except:
                break
with st.spinner(text="Loading section..."):
    skill_tab(skills1)



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

