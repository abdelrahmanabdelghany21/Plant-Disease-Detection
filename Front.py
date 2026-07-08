import streamlit as st
import requests
from PIL import Image


st.set_page_config(page_title="Plant Disease Detection System", page_icon="🌿", layout="wide")

st.title("🌿 AI Plant Disease Detection System")
st.write("Upload plant leaf images, and the system will instantly analyze and diagnose the disease.")


if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0

col1, col2 = st.columns([4, 1])

with col2:
    st.write("") 
    st.write("")
    if st.button("🗑️ Clear Photos ", use_container_width=True):
        st.session_state.uploader_key += 1 
        st.rerun() 

with col1:
    uploaded_files = st.file_uploader(
        "Upload plant images", 
        type=["jpg", "jpeg", "png"], 
        accept_multiple_files=True,
        key=f"uploader_{st.session_state.uploader_key}" 
    )

if uploaded_files:
    if st.button("Analyze Photos 🔍", use_container_width=True):
        st.write(f"Analyzing {len(uploaded_files)} photos...")
        st.markdown("---")
        
        cols = st.columns(3)
        
        for index, uploaded_file in enumerate(uploaded_files):
            with cols[index % 3]:
                image = Image.open(uploaded_file)
                st.image(image, caption=uploaded_file.name, use_container_width=True)
                
                with st.spinner('Checking...'): 
                    try:
                        files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                        response = requests.post("http://127.0.0.1:8000/predict/", files=files)
                        
                        if response.status_code == 200:
                            result = response.json()
                            disease = result['disease']
                            confidence = result['confidence']
                            
                            st.success(f"**{disease}**")
                            st.info(f"Confidence: **{confidence}%**")
                        else:
                            st.error("An error occurred on the server (API).")
                    
                    except requests.exceptions.ConnectionError:
                        st.error("⚠️ Cannot connect to the API. Make sure the server is running.")