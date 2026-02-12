import streamlit as st
import os
import tempfile
import traceback
import time
from utils.pptx_handler import translate_pptx, convert_pptx_to_pdf
from utils.pdf_handler import translate_pdf
from utils.docx_handler import translate_docx
from utils.txt_handler import translate_txt
from utils.xlsx_handler import translate_xlsx

# --- Page Config ---
st.set_page_config(
    page_title="TranslateX | AI Powered Document Translator",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS (The Magic) ---
def add_custom_css():
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

        /* Base Styles */
        body {
            font-family: 'Inter', sans-serif;
            background-color: #0e1117;
            color: #ffffff;
        }
        
        /* Hiding Streamlit Components */
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        /* Main Container */
        .main-container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 4rem 0;
            background: radial-gradient(circle at center, rgba(0,210,255,0.15) 0%, rgba(0,0,0,0) 70%);
            margin-bottom: 2rem;
        }
        
        .hero h1 {
            font-size: 4rem;
            font-weight: 800;
            background: linear-gradient(120deg, #ffffff 0%, #00d2ff 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 1rem;
            letter-spacing: -1px;
            text-shadow: 0 10px 30px rgba(0, 210, 255, 0.3);
        }
        
        .hero p {
            font-size: 1.2rem;
            color: #a0a0ba;
            max-width: 600px;
            margin: 0 auto;
            line-height: 1.6;
        }

        /* Glassmorphism Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 2rem;
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .glass-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4);
            border-color: rgba(0, 210, 255, 0.3);
        }

        /* Styled File Uploader */
        .stFileUploader {
            padding: 1rem;
            border-radius: 12px;
            border: 2px dashed rgba(255, 255, 255, 0.1);
            transition: all 0.3s ease;
        }
        
        .stFileUploader:hover {
            border-color: #00d2ff;
            background: rgba(0, 210, 255, 0.05);
        }

        /* Custom Buttons */
        .stButton > button {
            width: 100%;
            padding: 0.8rem 1.5rem;
            font-size: 1rem;
            font-weight: 600;
            color: #fff;
            background: linear-gradient(135deg, #00d2ff 0%, #007bff 100%);
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 210, 255, 0.3);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 25px rgba(0, 210, 255, 0.5);
            background: linear-gradient(135deg, #00efff 0%, #0061ff 100%);
        }
        
        .stButton > button:active {
            transform: translateY(1px);
        }

        /* Download Button Variant */
        .stDownloadButton > button {
            width: 100%;
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            border-radius: 12px;
            color: white;
            padding: 0.8rem 1.5rem;
            font-weight: 600;
            border: none;
            box-shadow: 0 4px 15px rgba(106, 17, 203, 0.3);
        }
        
        .stDownloadButton > button:hover {
             background: linear-gradient(135deg, #8132e0 0%, #4facfe 100%);
             transform: translateY(-2px);
             box-shadow: 0 8px 25px rgba(106, 17, 203, 0.5);
        }

        /* Divider */
        hr {
            border: 0;
            height: 1px;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            margin: 3rem 0;
        }

        /* Selectbox Styling */
        .stSelectbox > div > div {
            background-color: rgba(255, 255, 255, 0.05) !important;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: white;
        }
        
        /* Success/Info/Error Boxes */
        .stSuccess, .stInfo, .stWarning, .stError {
            background-color: rgba(255, 255, 255, 0.05) !important; 
            backdrop-filter: blur(10px);
            border-radius: 12px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #eee !important;
        }

    </style>
    """, unsafe_allow_html=True)

def main():
    add_custom_css()
    
    # Hero Section
    st.markdown("""
        <div class="hero">
            <h1>TranslateX</h1>
            <p>AI-Powered Document Translation. Preserves Layout using Advanced Algorithms.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Workflow Container
    col1, col2, col3 = st.columns([1, 4, 1])
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📤 Upload Document")
        st.markdown("<p style='font-size: 0.9rem; color: #888; margin-bottom: 1rem;'>Supported Formats: PDF, PPTX, DOCX, XLSX, TXT</p>", unsafe_allow_html=True)
        
        uploaded_file = st.file_uploader("", type=["pdf", "pptx", "docx", "txt", "xlsx"], label_visibility="collapsed")
        
        st.markdown("</div>", unsafe_allow_html=True)

        if uploaded_file:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            cols = st.columns([2, 1])
            with cols[0]:
                st.markdown(f"**Selected File:** `{uploaded_file.name}`")
                file_ext = uploaded_file.name.split('.')[-1].lower()
                st.caption(f"File Type: {file_ext.upper()} | Size: {uploaded_file.size / 1024:.2f} KB")
            
            with cols[1]:
                target_language = st.selectbox(
                    "Target Language",
                    options=["tr", "en", "de", "fr", "es", "it", "ru", "ar", "ja", "ko"],
                    format_func=lambda x: {
                        "tr": "🇹🇷 Turkish", "en": "🇺🇸 English", "de": "🇩🇪 German", 
                        "fr": "🇫🇷 French", "es": "🇪🇸 Spanish", "it": "🇮🇹 Italian", 
                        "ru": "🇷🇺 Russian", "ar": "🇸🇦 Arabic", "ja": "🇯🇵 Japanese", "ko": "🇰🇷 Korean"
                    }.get(x, x),
                    label_visibility="collapsed"
                )

            # Advanced Options
            convert_to_pdf_opt = False
            if file_ext == "pptx":
                st.markdown("---")
                convert_to_pdf_opt = st.checkbox("Convert result to PDF (Best for sharing)", value=False)
                if convert_to_pdf_opt:
                    st.caption("ℹ️ Requires LibreOffice on the server.")

            st.markdown("</div>", unsafe_allow_html=True)

            # Action Button
            if st.button("✨ START TRANSLATION"):
                with st.spinner("Processing your document... please wait."):
                    try:
                        # Progress simulation for consistent UX
                        progress_bar = st.progress(0)
                        for i in range(10):
                            time.sleep(0.05)
                            progress_bar.progress((i + 1) * 5)
                            
                        # Save uploaded file
                        with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_ext}") as tmp_file:
                            tmp_file.write(uploaded_file.getvalue())
                            input_path = tmp_file.name
                        
                        output_path = input_path.replace(f".{file_ext}", f"_translated.{file_ext}")
                        
                        # Processing Logic
                        time.sleep(0.5) # Slight UX pause
                        if file_ext == "pptx":
                            result_path = translate_pptx(input_path, output_path, target_language)
                            progress_bar.progress(80)
                            if convert_to_pdf_opt:
                                 st.toast("Converting to PDF...", icon="🔄")
                                 pdf_path = output_path.replace('.pptx', '.pdf')
                                 converted_pdf = convert_pptx_to_pdf(result_path, pdf_path)
                                 if converted_pdf:
                                     result_path = converted_pdf
                                 else:
                                     st.warning("PDF conversion failed, providing PPTX instead.")
                        elif file_ext == "pdf":
                            result_path = translate_pdf(input_path, output_path, target_language)
                        elif file_ext == "docx":
                            result_path = translate_docx(input_path, output_path, target_language)
                        elif file_ext == "txt":
                            result_path = translate_txt(input_path, output_path, target_language)
                        elif file_ext == "xlsx":
                             result_path = translate_xlsx(input_path, output_path, target_language)
                        else:
                            st.error("Unsupported file format.")
                            return

                        progress_bar.progress(100)
                        
                        # Success Logic
                        st.balloons()
                        
                        # Check fallback for PDF
                        is_docx_fallback = result_path.endswith(".docx") and file_ext == "pdf"
                        
                        st.markdown('<div class="glass-card" style="text-align: center;">', unsafe_allow_html=True)
                        st.success("Translation Complete Successfully!")
                        
                        if is_docx_fallback:
                            st.warning("Note: PDF conversion was unavailable. Providing editable Word document.")

                        # Read file for download
                        with open(result_path, "rb") as f:
                            file_data = f.read()
                            
                        download_name = uploaded_file.name.replace(".", f"_{target_language}.")
                        
                        # Adjust extension if changed during process
                        final_ext = result_path.split('.')[-1]
                        if not download_name.endswith(f".{final_ext}"):
                             download_name = ".".join(download_name.split('.')[:-1]) + f".{final_ext}"

                        mime_type = "application/octet-stream"
                        if final_ext == "pptx": mime_type = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
                        elif final_ext == "pdf": mime_type = "application/pdf"
                        elif final_ext == "docx": mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                        elif final_ext == "xlsx": mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                        elif final_ext == "txt": mime_type = "text/plain"

                        st.download_button(
                            label="⬇️ DOWNLOAD TRANSLATED FILE",
                            data=file_data,
                            file_name=download_name,
                            mime=mime_type
                        )
                        st.markdown('</div>', unsafe_allow_html=True)
                        
                    except Exception as e:
                        st.error("An error occurred during processing.")
                        st.exception(e)
                    finally:
                        # Cleanup
                        if 'input_path' in locals() and os.path.exists(input_path):
                            os.remove(input_path)
                        if 'result_path' in locals() and os.path.exists(result_path):
                             os.remove(result_path)

if __name__ == "__main__":
    main()
