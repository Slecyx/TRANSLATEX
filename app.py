import streamlit as st
import os
import tempfile
import traceback
import time
import base64
from utils.pptx_handler import translate_pptx, convert_pptx_to_pdf
from utils.pdf_handler import translate_pdf
from utils.docx_handler import translate_docx
from utils.txt_handler import translate_txt
from utils.xlsx_handler import translate_xlsx

# --- Cloud Config ---
st.set_page_config(
    page_title="TranslateX Prime | AI Suite",
    page_icon="�",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Hyper-Premium CSS ---
def add_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Rajdhani:wght@300;500;700&display=swap');

        /* === ANIMATED BACKGROUND === */
        .stApp {
            background: #000000;
            background-image: 
                radial-gradient(circle at 50% 50%, rgba(76, 29, 149, 0.2) 0%, rgba(0, 0, 0, 0) 50%),
                linear-gradient(rgba(0, 0, 0, 0.9), rgba(0, 0, 0, 0.9)),
                url("https://www.transparenttextures.com/patterns/cubes.png");
            overflow-x: hidden;
        }

        /* Moving Grid Animation (Pseudo-element) */
        .stApp::before {
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 200vw;
            height: 200vh;
            background: 
                linear-gradient(transparent 0%, rgba(0, 255, 255, 0.05) 50%, transparent 100%),
                linear-gradient(90deg, transparent 0%, rgba(255, 0, 255, 0.05) 50%, transparent 100%);
            background-size: 100px 100px;
            animation: moveGrid 20s linear infinite;
            z-index: -1;
            transform: perspective(500px) rotateX(60deg) translateY(-100px) translateZ(-200px);
        }

        @keyframes moveGrid {
            0% { transform: perspective(500px) rotateX(60deg) translateY(0) translateZ(-200px); }
            100% { transform: perspective(500px) rotateX(60deg) translateY(100px) translateZ(-200px); }
        }

        /* === TYPOGRAPHY === */
        h1, h2, h3 {
            font-family: 'Orbitron', sans-serif !important;
            text-transform: uppercase;
            letter-spacing: 2px;
        }

        p, div, label, button {
            font-family: 'Rajdhani', sans-serif !important;
        }

        /* === HERO SECTION === */
        .hero-container {
            text-align: center;
            padding: 4rem 1rem;
            position: relative;
        }
        
        .hero-title {
            font-size: 5rem;
            background: linear-gradient(to right, #00c6ff, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0px 0px 20px rgba(0, 198, 255, 0.5);
            margin-bottom: 0.5rem;
            animation: glow 3s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { text-shadow: 0 0 10px rgba(0, 198, 255, 0.5); }
            to { text-shadow: 0 0 30px rgba(0, 114, 255, 0.8), 0 0 10px rgba(0, 255, 255, 0.8); }
        }

        .hero-subtitle {
            font-size: 1.5rem;
            color: #a0a0ba;
            letter-spacing: 1px;
            margin-top: -10px;
        }

        /* === GLASS CARD === */
        .glass-card {
            background: rgba(10, 10, 20, 0.6);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(0, 255, 255, 0.1);
            border-radius: 16px;
            padding: 2.5rem;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
            transition: all 0.4s ease;
        }

        .glass-card:hover {
            border-color: rgba(0, 255, 255, 0.4);
            box-shadow: 0 0 30px rgba(0, 255, 255, 0.15);
            transform: translateY(-5px);
        }

        /* === FILE UPLOADER === */
        .stFileUploader {
            border: 2px dashed rgba(0, 255, 255, 0.2);
            border-radius: 12px;
            padding: 20px;
            transition: all 0.3s;
        }
        .stFileUploader:hover {
            border-color: #00c6ff;
            background: rgba(0, 198, 255, 0.05);
        }

        /* === BUTTONS === */
        .stButton > button {
            background: transparent;
            border: 2px solid #00c6ff;
            color: #00c6ff;
            font-size: 1.2rem;
            font-weight: 700;
            padding: 0.8rem 2rem;
            border-radius: 0;
            transition: all 0.3s ease;
            text-transform: uppercase;
            position: relative;
            overflow: hidden;
            z-index: 1;
        }

        .stButton > button::before {
            content: "";
            position: absolute;
            top: 0; left: 0; width: 0; height: 100%;
            background: #00c6ff;
            transition: all 0.3s ease;
            z-index: -1;
        }

        .stButton > button:hover::before {
            width: 100%;
        }

        .stButton > button:hover {
            color: black;
            box-shadow: 0 0 20px rgba(0, 198, 255, 0.6);
        }

        /* === DOWNLOAD BUTTON === */
        .stDownloadButton > button {
            background: linear-gradient(45deg, #ff0099, #493240);
            border: none;
            color: white;
            font-size: 1.1rem;
            padding: 0.8rem 2rem;
            border-radius: 30px;
            box-shadow: 0 4px 15px rgba(255, 0, 153, 0.4);
            transition: transform 0.2s;
        }
        .stDownloadButton > button:hover {
            transform: scale(1.05);
            box-shadow: 0 6px 20px rgba(255, 0, 153, 0.6);
        }

        /* === STATUS & ALERTS === */
        .stSuccess, .stInfo, .stWarning, .stError {
            background: rgba(0, 0, 0, 0.8) !important;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        /* Hiding Default Elements */
        #MainMenu, footer, header { visibility: hidden; }
        
    </style>
    """, unsafe_allow_html=True)

def main():
    add_custom_css()

    st.markdown('<div class="hero-container"><div class="hero-title">TRANSLATEX</div><div class="hero-subtitle">NEXT-GEN AI DOCUMENT LOCALIZATION SYSTEM</div></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 6, 1])

    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🧬 INPUT SEQUENCE")
        
        uploaded_file = st.file_uploader("DROP DATA PACKET HERE", type=["pdf", "pptx", "docx", "txt", "xlsx"])
        
        cols = st.columns([2, 1])
        with cols[0]:
            if uploaded_file:
                st.info(f"💾 PACKET DETECTED: {uploaded_file.name}")
        
        with cols[1]:
            target_language = st.selectbox(
                "TARGET SYNTAX",
                options=["tr", "en", "de", "fr", "es", "it", "ru", "ar", "ja", "ko"],
                format_func=lambda x: x.upper()
            )

        # Advanced Toggle
        convert_to_pdf_opt = False
        if uploaded_file and uploaded_file.name.endswith(".pptx"):
            st.markdown("---")
            convert_to_pdf_opt = st.checkbox("💠 RENDER AS PDF ARTIFACT", value=False)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if uploaded_file:
            if st.button("INITIALIZE TRANSLATION PROTOCOL"):
                
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                try:
                    # Simulation of tech processes
                    status_text.text("⚡ ESTABLISHING NEURAL LINK...")
                    time.sleep(0.5)
                    progress_bar.progress(10)
                    
                    status_text.text("📂 PARSING MOLECULAR STRUCTURE...")
                    
                    # Save uploaded file
                    file_ext = uploaded_file.name.split('.')[-1].lower()
                    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        input_path = tmp_file.name
                    
                    output_path = input_path.replace(f".{file_ext}", f"_translated.{file_ext}")
                    
                    # Process
                    status_text.text("🔄 DECODING & RE-ENCODING SYNTAX...")
                    progress_bar.progress(30)
                    
                    if file_ext == "pptx":
                        result_path = translate_pptx(input_path, output_path, target_language)
                        if convert_to_pdf_opt:
                             status_text.text("📄 RENDERING VISUAL ARTIFACT (PDF)...")
                             pdf_path = output_path.replace('.pptx', '.pdf')
                             converted_pdf = convert_pptx_to_pdf(result_path, pdf_path)
                             if converted_pdf:
                                 result_path = converted_pdf
                    elif file_ext == "pdf":
                        result_path = translate_pdf(input_path, output_path, target_language)
                    elif file_ext == "docx":
                        result_path = translate_docx(input_path, output_path, target_language)
                    elif file_ext == "txt":
                        result_path = translate_txt(input_path, output_path, target_language)
                    elif file_ext == "xlsx":
                         result_path = translate_xlsx(input_path, output_path, target_language)
                    else:
                        st.error("❌ UNKNOWN DATA FORMAT")
                        return

                    progress_bar.progress(90)
                    status_text.text("✨ FINALIZING ARTIFACT...")
                    time.sleep(0.5)
                    progress_bar.progress(100)
                    status_text.text("✅ OPERATION COMPLETE")

                    # Download
                    with open(result_path, "rb") as f:
                        file_data = f.read()
                        
                    download_name = uploaded_file.name.replace(".", f"_{target_language}.")
                    final_ext = result_path.split('.')[-1]
                    if not download_name.endswith(f".{final_ext}"):
                         download_name = ".".join(download_name.split('.')[:-1]) + f".{final_ext}"

                    mime_type = "application/octet-stream"
                    if final_ext == "pptx": mime_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
                    elif final_ext == "pdf": mime_type = "application/pdf"
                    elif final_ext == "docx": mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    elif final_ext == "xlsx": mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    elif final_ext == "txt": mime_type = "text/plain"

                    st.markdown("---")
                    col_d1, col_d2, col_d3 = st.columns([1, 2, 1])
                    with col_d2:
                        st.download_button(
                            label="⬇️ ACQUIRE TRANSLATED ASSET",
                            data=file_data,
                            file_name=download_name,
                            mime=mime_type
                        )
                    
                    st.balloons()

                except Exception as e:
                    st.error("⚠ SYSTEM CRITICAL FAILURE")
                    st.code(traceback.format_exc())
                finally:
                    if 'input_path' in locals() and os.path.exists(input_path):
                        os.remove(input_path)
                    if 'result_path' in locals() and os.path.exists(result_path):
                         os.remove(result_path)

        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center; color: #555; font-size: 0.8rem; margin-top: 2rem;'>SYSTEM VERSION 4.0 // SECURE CONNECTION</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
