
import streamlit as st

st.set_page_config(page_title="AI Mammogram Analysis", layout="wide")

st.markdown("""
<style>
.stApp {background:#eef1f5;}
.nav {background:#243b6b;padding:12px;border-radius:10px;color:white;font-size:18px;font-weight:bold;}
.hero{padding:70px 10px;text-align:center;}
.title{font-size:40px;font-weight:700;color:#243b6b;}
.desc{font-size:20px;color:#444;max-width:800px;margin:auto;}
div.stButton>button{
background:#243b6b;color:white;border-radius:30px;
padding:12px 40px;font-size:20px;border:none;}
</style>
""",unsafe_allow_html=True)

page=st.sidebar.radio("Navigation",["Home","Help / Instructions"])

if page=="Home":
    st.markdown('<div class="nav">🏠 Home</div>',unsafe_allow_html=True)
    st.markdown('<div class="hero">',unsafe_allow_html=True)
    st.markdown('<div class="title">AI-Powered Mammogram Analysis System<br>for Early Breast Cancer Classification</div>',unsafe_allow_html=True)
    st.markdown('<br>',unsafe_allow_html=True)
    st.markdown('<div class="desc">An AI-powered assistant designed to support healthcare professionals by analyzing mammogram images and assisting in the early classification of breast cancer. This system is intended to support, not replace, clinical decision-making.</div>',unsafe_allow_html=True)
    st.markdown("<br><br>",unsafe_allow_html=True)
    if st.button("▶ START ANALYSIS"):
        st.success("Later, connect this button to the diagnosis page.")
    st.markdown('</div>',unsafe_allow_html=True)
else:
    st.markdown('<div class="nav">❓ Help / Instructions</div>',unsafe_allow_html=True)
    st.header("Project Overview")
    st.write("""
This project is an AI-powered decision support system for early breast cancer classification using mammogram images.

### Objectives
- Support doctors with AI.
- Detect suspicious findings early.
- Reduce diagnosis time.

### Technologies Used
- Python
- Streamlit
- TensorFlow / Keras
- CNN-based deep learning
- Mammogram dataset

### Workflow
1. Upload a mammogram image.
2. Image preprocessing.
3. AI model prediction.
4. Display the classification result.

### Disclaimer
This system is intended to assist healthcare professionals and should not replace medical diagnosis. Final decisions must be made by qualified physicians.
""")
