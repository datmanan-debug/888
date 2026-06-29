
import streamlit as st
st.set_page_config(layout="wide",page_title="AI Mammogram")

if "help" not in st.session_state:
    st.session_state.help=False

st.markdown("""
<style>
.stApp{background:#eef1f5;}
.top{display:flex;justify-content:flex-end;}
.help{font-size:28px;text-decoration:none}
.title{text-align:center;color:#243b6b;font-size:42px;font-weight:700;margin-top:40px}
.sub{text-align:center;color:#555;font-size:20px;max-width:850px;margin:auto}
.card{background:white;padding:20px;border-radius:14px;margin:18px 0;border-left:6px solid #243b6b;box-shadow:0 2px 10px rgba(0,0,0,.08);}
div.stButton>button{display:block;margin:40px auto;background:#243b6b;color:white;border-radius:40px;font-size:24px;padding:14px 50px;}
</style>
""",unsafe_allow_html=True)

c1,c2=st.columns([10,1])
with c2:
    if st.button("❓"):
        st.session_state.help=not st.session_state.help

if not st.session_state.help:
    st.markdown('<div class="title">AI-Powered Mammogram Analysis System<br>for Early Breast Cancer Classification</div>',unsafe_allow_html=True)
    st.markdown('<p class="sub">An AI-powered assistant that supports healthcare professionals in analyzing mammogram images for early breast cancer classification. It is designed to assist doctors, not replace clinical judgment.</p>',unsafe_allow_html=True)
    st.button("START")
else:
    st.title("Help & Project Information")
    sections=[
("🩺 Project Overview","AI system for early breast cancer classification from mammograms to support physicians."),
("📊 Datasets","Training, testing and final evaluation used CBIS-DDSM together with hospital mammogram images."),
("🧠 AI Model","CNN built with TensorFlow and Keras using convolution, ReLU, max pooling, dense and softmax layers."),
("⚙️ Training","Image size: 50x50, Epochs:25, Batch Size:75, Adam optimizer, Binary Crossentropy."),
("💻 Technologies","Python, Streamlit, TensorFlow, Keras, OpenCV, NumPy, Pandas, Pillow, OpenPyXL."),
("🚀 Workflow","Upload image → Preprocessing → AI Prediction → Result → Doctor review."),
("⚠ Disclaimer","This tool assists healthcare professionals and does not replace medical diagnosis.")
]
    for t,b in sections:
        st.markdown(f"<div class='card'><h3>{t}</h3><p>{b}</p></div>",unsafe_allow_html=True)
